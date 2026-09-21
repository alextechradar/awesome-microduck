# Verification / 交付检查

- Catalog: 22 resources; all required fields and bilingual descriptions present.
- Generated README sections: match the source JSON.
- Local Markdown files and anchors: passed.
- External links: 28 returned HTTP 2xx; 0 broken; 0 inconclusive.
- Negative checks: duplicate URL, stale README, missing local file and missing anchor were each rejected in an isolated temporary copy.
- Scripts: Python compilation passed. Banner SVG parsed. Full CC0 legal text included.

External check timestamp: `2026-09-21T06:52:05.414939+00:00`.

Reproduce:

```bash
python3 scripts/catalog.py --check
python3 scripts/check_links.py
```

The link script writes an ignored `link-report.json` locally. HTTP success does not validate resource behavior, remote page fragments or hardware compatibility. Robot software, policies and training have not been executed during catalog preparation. GitHub Actions configuration is included but has not run on GitHub yet.

检查范围为资源清单和链接质量；不是机器人运行或训练验收。此文档是一次检查快照，不会随脚本自动更新。
