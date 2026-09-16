#!/usr/bin/env python3
"""Validate catalog and local Markdown links; generate bilingual resource sections."""
import argparse
import datetime
import json
import re
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
CATEGORIES = {
    'official': ('Official', '官方入口'),
    'docs': ('Documentation', '文档'),
    'simulation': ('Simulation and training', '仿真与训练'),
    'policies': ('Policy experiments', '策略实验'),
    'tools': ('Developer and agent tools', '开发与 Agent 工具'),
    'hardware': ('Hardware and DIY', '硬件与复刻'),
}
STATUSES = {'official', 'simulation-reported', 'hardware-demo-reported', 'experimental', 'hardware-unverified'}
START, END = '<!-- RESOURCES:START -->', '<!-- RESOURCES:END -->'

def slug(text):
    return re.sub(r'[^\w\- ]', '', text.lower()).replace(' ', '-')

def anchors(text):
    result = set(re.findall(r'<a id="([^"]+)"', text))
    counts = {}
    for title in re.findall(r'^#{1,6} (.+)$', text, re.M):
        key = slug(title)
        count = counts.get(key, 0)
        result.add(key if count == 0 else f'{key}-{count}')
        counts[key] = count + 1
    return result

def validate(data):
    assert data['schema_version'] == 1, 'unsupported schema version'
    assert data['resources'], 'empty resource list'
    ids, urls = set(), set()
    required = {'id', 'name', 'url', 'category', 'environment', 'status', 'description', 'source_url', 'reviewed_at', 'verification'}
    for row in data['resources']:
        assert required == set(row), f"invalid fields: {row.get('id')}"
        assert re.fullmatch(r'[a-z0-9-]+', row['id']), 'invalid ID'
        assert row['id'] not in ids, f"duplicate ID: {row['id']}"
        assert row['url'].rstrip('/').casefold() not in urls, f"duplicate URL: {row['url']}"
        ids.add(row['id']); urls.add(row['url'].rstrip('/').casefold())
        for field in ('url', 'source_url'):
            parsed = urlsplit(row[field])
            assert parsed.scheme == 'https' and parsed.netloc, f'invalid {field}'
        assert row['category'] in CATEGORIES, 'unknown category'
        assert row['status'] in STATUSES, 'unknown status'
        assert row['verification'] == 'source-reviewed', 'unsupported verification claim'
        assert datetime.date.fromisoformat(row['reviewed_at']) <= datetime.date.today(), 'future review date'
        assert set(row['description']) == {'en', 'zh'}, 'missing translation'
        for value in [row['name'], row['environment'], *row['description'].values()]:
            assert isinstance(value, str) and value.strip(), 'empty text'
            assert not any(c in value for c in '\n\r|[]<>'), 'unsupported Markdown in catalog text'

def render(rows, lang):
    output = []
    for category, (en, zh) in CATEGORIES.items():
        title = en if lang == 'en' else zh
        output.extend([f'<a id="{slug(en)}"></a>', f'### {title}', ''])
        for r in sorted((r for r in rows if r['category'] == category), key=lambda r: r['name'].casefold()):
            suffix = 'Source' if lang == 'en' else '来源'
            output.append(f"- [{r['name']}]({r['url']}) — {r['description'][lang]} **{r['environment']}** · `{r['status']}` · [{suffix}]({r['source_url']}) · {r['reviewed_at']}.")
        output.append('')
    return '\n'.join(output).rstrip()

def check_local_links():
    errors = []
    for path in ROOT.rglob('*.md'):
        if '.git' in path.parts:
            continue
        text = re.sub(r'```.*?```', '', path.read_text(), flags=re.S)
        for target in re.findall(r'!?\[[^\]]*\]\(([^\s)]+)\)', text):
            if urlsplit(target).scheme or target.startswith('//'):
                continue
            file, _, fragment = unquote(target).partition('#')
            dest = (path.parent / file).resolve() if file else path
            if not dest.exists():
                errors.append(f'{path.relative_to(ROOT)}: missing {target}')
            elif fragment and dest.suffix == '.md' and fragment not in anchors(dest.read_text()):
                errors.append(f'{path.relative_to(ROOT)}: missing anchor {target}')
    assert not errors, '\n'.join(errors)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--check', action='store_true')
    args = parser.parse_args()
    data = json.loads((ROOT / 'data/resources.json').read_text())
    validate(data)
    for name, lang in [('README.md', 'en'), ('README.zh-CN.md', 'zh')]:
        path = ROOT / name
        text = path.read_text()
        assert text.count(START) == text.count(END) == 1, f'{name}: invalid markers'
        before, rest = text.split(START)
        _, after = rest.split(END)
        expected = before + START + '\n' + render(data['resources'], lang) + '\n' + END + after
        if args.check:
            assert text == expected, f'{name} is stale; run python3 scripts/catalog.py'
        else:
            path.write_text(expected)
    check_local_links()
    print(f"PASS: {len(data['resources'])} resources, bilingual catalog and local Markdown links")

if __name__ == '__main__':
    main()
