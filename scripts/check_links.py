#!/usr/bin/env python3
"""Check external Markdown/catalog links with curl; preserve inconclusive results."""
import concurrent.futures
import datetime
import json
from pathlib import Path
import re
import subprocess
import sys
from urllib.parse import urldefrag

ROOT = Path(__file__).resolve().parents[1]

def check(url):
    try:
        result = subprocess.run([
            'curl', '--location', '--silent', '--output', '/dev/null',
            '--write-out', '%{http_code}', '--max-time', '25',
            '--retry', '1', '--retry-delay', '1', '--user-agent',
            'awesome-microduck-link-check/1.0', url,
        ], capture_output=True, text=True, timeout=60)
        code = int(result.stdout or 0)
        status = 'ok' if result.returncode == 0 and 200 <= code < 300 else 'broken' if code in (404, 410) else 'inconclusive'
        return {'url': url, 'http_status': code, 'status': status}
    except (subprocess.TimeoutExpired, ValueError, OSError) as exc:
        return {'url': url, 'http_status': 0, 'status': 'inconclusive', 'error': str(exc)}

def main():
    urls = set()
    for path in ROOT.rglob('*.md'):
        if '.git' not in path.parts:
            urls.update(re.findall(r'\]\((https://[^\s)]+)\)', path.read_text()))
    for row in json.loads((ROOT/'data/resources.json').read_text())['resources']:
        urls.update((row['url'], row['source_url']))
    urls = sorted({urldefrag(url)[0] for url in urls})
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as pool:
        results = list(pool.map(check, urls))
    (ROOT/'link-report.json').write_text(json.dumps({
        'checked_at': datetime.datetime.now(datetime.timezone.utc).isoformat(),
        'scope': 'HTTP reachability only; fragments and execution not verified',
        'results': results,
    }, indent=2)+'\n')
    counts = {key: sum(r['status'] == key for r in results) for key in ('ok', 'broken', 'inconclusive')}
    print(json.dumps(counts))
    for row in results:
        if row['status'] != 'ok':
            print(f"{row['status']}: {row['http_status']} {row['url']}")
    return 1 if counts['broken'] else 2 if counts['inconclusive'] else 0

if __name__ == '__main__':
    sys.exit(main())
