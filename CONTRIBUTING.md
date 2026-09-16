# Contributing / 贡献指南

Thanks for improving the guide. / 欢迎补充资源和纠正错误。

1. Read the [review policy](docs/review-policy.md). Include a public primary source, environment, concrete purpose and known limitations.
2. Open a **Resource submission** or **Correction** issue using the repository's Issues tab, or edit `data/resources.json` in a pull request.
3. Supply both `en` and `zh` descriptions. Use factual one-line summaries; disclose if you maintain the submitted project.
4. Record when the source was actually reviewed. Do not claim independent hardware validation from a simulation video.
5. Run the commands below and commit the JSON plus both generated README sections.

```bash
python3 scripts/catalog.py
python3 scripts/catalog.py --check
python3 scripts/check_links.py
```

Python 3.10+ and curl are sufficient. No third-party Python packages are required. The final command accesses the network, writes `link-report.json`, and reports temporary service failures separately from confirmed 404/410 responses. Inspect warnings before claiming a clean audit.

Resources are alphabetized within categories, not ranked by payment or Star count. Do not edit generated sections manually. Original contributions are dedicated under [CC0](LICENSE); do not copy third-party assets without permission.

中文：在 JSON 中补充中英简介、设备要求、状态和证据，运行生成与检查脚本即可。也可以通过 Issue 提交，不要求会写代码；请披露自己与所推荐项目的关系。
