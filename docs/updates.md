# Review notes / 更新记录

[English](../README.md) · [中文](../README.zh-CN.md)

## 2026-09-21 — Runtime release and new community routes / 运行时发布与新社区路线

- Reviewed the official [daemon v0.14.0](https://github.com/pollen-robotics/microduck/releases/tag/daemon-v0.14.0) and [v0.14.1](https://github.com/pollen-robotics/microduck/releases/tag/daemon-v0.14.1) releases. The first replaces the fake simulator path with the real runtime daemons against MuJoCo and adds a browser policy playground; the second exposes phone stand-up and policy-start controls and fixes controller reconnection behavior.
- Added the official releases page as the stable-version and artifact trail; development builds remain a separate class.
- Added [Microduck Web](https://github.com/TonyRuan/microduck-web) as a community-reported local browser simulation route with touch controls and compatible ONNX policy import. Its own documentation explicitly limits the project to simulation rather than physical hardware control.
- Added [OpenMicroDuck](https://github.com/SaberOnGo/open-microduck) as a bilingual community guide. Its evidence labels and unresolved hardware questions remain part of the recommendation.
- Added [Fanduck](https://github.com/7757/fanduck) as `hardware-demo-reported`: the maintainer publishes physical-build photos and clips plus versioned BOM, print and board packages. This is author evidence, not an independent reproduction, and the upstream-derived model carries non-commercial terms.
- Deferred several same-week repositories that were empty, extremely new, tied to an external service, or based on simulation findings not yet independently cross-checked. Deferral is not a negative verdict; they can be reconsidered as reproducible evidence accumulates.

本次核心更新：官方 v0.14.0/0.14.1 将真实运行时守护进程与 MuJoCo 仿真、手机起立和策略启动串联起来；新收录浏览器仿真、双语指南与有作者实机证据的复刻项目。同期内容为空、刚创建或实验结论尚未复核的项目暂不收录。

## 2026-09-16 — Initial catalog / 首期整理

Published here as a local editorial record; no GitHub Release has been created yet.

- Added 18 source-reviewed resources and routes for browser, Mac, CUDA, AMD, ROS 2, agents and DIY builders.
- Checked the [official policy manifest on main](https://github.com/pollen-robotics/microduck/blob/main/docs/policy-manifest.md). Do not rely on old summaries that describe the policy channel solely as a future branch feature.
- Highlighted [isaaclab-microduck's stated locomotion limitation](https://github.com/kabilankb/isaaclab-microduck). It is a research option, not a ready walking-policy recommendation.
- Kept the [MCP project's real-hardware validation limit](https://github.com/joeynyc/microduck-mcp) visible.
- Separated author-published physical demonstrations from independent reproduction.

首期重点：能选路线、能找到证据、能看见限制。以上为来源核验，本仓库未执行训练或机器人实测。

For a future update, record the resource, upstream revision, changed claim and reader impact. Only create a dated entry after actual review; no fixed publishing cadence is promised.
