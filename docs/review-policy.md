# Review policy / 收录与核验规则

[Back to catalog](../README.md)

## Scope

Include public resources directly useful to Microduck users. Prefer primary repositories and official documentation. A resource needs a clear purpose, environment, limitation and evidence URL. Popularity is discovery context, not proof of correctness. No payment is required for inclusion.

收录直接服务 Microduck 学习、开发或装机的公开资源。优先一手来源，说明用途、条件、限制及证据。Star 不等于可靠性；付费不是收录条件。

## Evidence vocabulary

| Field / label | Meaning |
| --- | --- |
| `verification: source-reviewed` | Maintainer read the linked source; no independent execution implied / 已阅读来源，非独立实测 |
| `official` | Published by upstream; describes provenance, not a test result / 官方发布主体 |
| `simulation-reported` | Authors document simulation results / 作者报告仿真结果 |
| `hardware-demo-reported` | Authors publish physical-hardware demonstrations / 作者展示实物结果 |
| `hardware-unverified` | Real-device validation not established in reviewed evidence / 真机验证未确立 |
| `experimental` | Research, incomplete behavior, or integration constraints / 存在实验性或集成限制 |
| `reviewed_at` | Date the description and evidence were reviewed; not a runtime test date / 内容核验日期 |

The source URL is mutable unless pinned. If an important claim changes, cite a commit or release in the update notes. A working HTTP URL establishes reachability only. Link checks never upgrade evidence labels.

## Maintenance

Edit `data/resources.json`, then run `python3 scripts/catalog.py` to regenerate both READMEs. Run `python3 scripts/catalog.py --check` before submitting. Review major upstream changes and aging entries manually; do not advance review dates without reading the source again.

Broken links, withdrawn policies and incompatible changes should be reported with the affected URL and evidence. Correct or remove the entry promptly after review. Never treat this discovery catalog as an executable policy registry.
