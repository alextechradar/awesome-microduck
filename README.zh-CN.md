# Awesome Microduck

![Awesome Microduck：发现、仿真、训练与构建](assets/banner.svg)

**一份持续追踪、精选并核验的 Microduck 生态地图。**

发现仿真器、运动策略、Agent 工具、硬件构建与实验项目，了解它们适合谁、当前能做什么，以及哪些能力仍待验证。

⭐ **Star 本仓库，持续关注 Microduck 生态进展。**

[English](README.md) · 简体中文 · [入门路线](docs/getting-started.md) · [贡献资源](CONTRIBUTING.md)

## 🆕 最新动态

### 2026-11-02

- 📦 核验官方稳定版 **[daemon v0.18.3](https://github.com/pollen-robotics/microduck/releases/tag/daemon-v0.18.3)**——v0.17.7–v0.18.3 连续更新改进配网、跌倒安全、摄像头行为、手柄重连与启动检查，并加入可选健康档案分享及可退出的匿名遥测。
- 💾 新增官方 **[Microduck OS v1.1.0](https://github.com/pollen-robotics/microduck_yocto/releases/tag/microduck-os-v1.1.0)**——生产镜像现随附手柄与 NFC 守护进程，更新后保留蓝牙配对并验证 V1.0 面板 LED；工厂刷写指南尚未在板卡上完整走通。
- 🧠 更新 **[Microduck RL](https://github.com/pollen-robotics/microduck_rl/commit/3b8759e9dad2bd12dae03129bc4a07fe24a48026)**——现可选择性发布包含完整检查点、来源记录和蒸馏教师的 Hub 训练包，用于可复现续训或热启动。
- 🏁 更新 **[Arena v0.7.0](https://github.com/pollen-robotics/microduck-arena/releases/tag/v0.7.0)** 与 **[Microduck challenges](https://github.com/pollen-robotics/microduck-challenges/commit/5cee942d8b434aafd395070facb659034aac3b5e)**——新增拔河和 Sock Heist，公开训练工作坊现覆盖六项仿真赛事。
- 🦆 新增 **[DuckBuddy](https://github.com/Animan-AI/DuckBuddy/commit/933c6d9547cfd0e5cd06c805bc406bf394ba6ca3)**——已核验开放板卡、固件、训练栈及作者实机离线语音连续动作演示；HD-1910、端侧 VLM 与定位仍未完成。
- 🔧 更新 **[Microduck replica](https://github.com/fanhao375/microduck-replica/releases/tag/microduck-software-v2026.10.31)** 与 **[XGO Duck V1.1](https://github.com/LuwuDynamics/xgoduck_hardware/commit/7dd33c603cbff92bc4afbc7f318abd4ccd9127b6)**——补充签名软件交付、本地语音、诊断与新版板卡证据，同时保留手柄驱动、镜像、IMU、PCB 源文件和兼容性缺口。
- 🧰 更新 **[quackd v0.29.1](https://github.com/rokbenko/quackd/releases/tag/v0.29.1)**——加入浏览器界面、视觉、头部跟踪与仿真探索；因尚无实体鸭运行，Microduck 路径继续标记为 `hardware-unverified`。

### 2026-10-19

- 📦 核验官方稳定版 **[daemon v0.17.6](https://github.com/pollen-robotics/microduck/releases/tag/daemon-v0.17.6)**：v0.16.2–v0.17.6 连续更新加入 v8 默认策略、网络手柄安全处理、健康档案和更新器修复；v0.17.5–v0.17.6 仅通过 CI 更新验证，明确未经真机验证。
- 🧠 核验官方 **[v8 策略集](https://huggingface.co/pollen-robotics/microduck-policies/tree/v8)** 及其 **[训练谱系](https://github.com/pollen-robotics/microduck_rl/commit/b02fdea4902c2b93b7d34a83a6f05da4ececb7d3)**：作者报告已在真机验证更平顺的跌倒恢复、偏航跟踪与行走。
- 🏁 收录官方 **[Microduck Arena](https://github.com/pollen-robotics/microduck-arena/releases/tag/v0.5.0)** 和公开的 **[挑战训练仓库](https://github.com/pollen-robotics/microduck-challenges/commit/6ff40704a1b086618b52173c4ea3851bb21ee4f6)**：包含四项可复现仿真赛事及最多八只鸭的才艺编队；竞赛成绩不是真机证据。
- 🔧 更新 **[Microduck replica](https://github.com/fanhao375/microduck-replica/commit/06822f1231f2f6a849b499708037c18b50c8ea97)**：修复 BNO085 陀螺融合后，作者报告推摇杆行走 60 秒未摔；转向、偶发重启及缺少交错 A/B 测试仍待解决。
- 🧪 收录 **[my-microduck-journal v0.2](https://github.com/xinhuagu/my-microduck-journal/releases/tag/v0.2)** 的 ONNX 策略与多随机种子仿真原始数据，以及 **[Microduck-kissqy](https://github.com/kissqy/Microduck-kissqy/commit/f02e875e73b88bf8ec7d5bbb34d0b461ac83b010)** 已测试镜像、公开构建栈和作者实机演示。
- 🧰 更新 **[quackd v0.18.1](https://github.com/rokbenko/quackd/releases/tag/v0.18.1)** 的当前 robotd 兼容状态，同时保留 `hardware-unverified`：维护者明确说明尚未在 Microduck 真机运行。

### 2026-10-12

- 📦 核验官方稳定版 **[daemon v0.16.1](https://github.com/pollen-robotics/microduck/releases/tag/daemon-v0.16.1)**：v0.15.3–v0.16.1 连续更新带来 beta 板支持、手柄断连后的安全坐下、电池显示和 Rustls 安全更新；v0.15.3 明确未经过真机验证。
- ⚖️ 记录官方 **[Microduck RL 许可范围修订](https://github.com/pollen-robotics/microduck_rl/commit/7cc1961674f78d4fca7064fde715e0c9bcd7b9c4)**：仓库内 STL 网格采用 CC BY-NC-SA 4.0，代码、MJCF 与其他列明文件仍为 Apache-2.0。
- 🔧 更新 **[Microduck replica](https://github.com/fanhao375/microduck-replica/commit/75c2b4b3249a8a4a17e29dabb872ebb465c393f9)**：已在真机跑通 BNO085、15 舵机控制环、HOME 与 10 秒策略保持；连续行走仍受主板过热降频阻塞，尚未验证。
- 🤖 重新核验 **[MicroDuck ROS 2 + Isaac Sim](https://github.com/osrbot/microduck-ros2-isaac/commit/2adc4b157fc732d4751ad97577e4ea39bd727abd)**：已固定 v7 策略并同步双语上游说明；转换后的 USD/GPU 回放仍待复验，且不含真机驱动。
- 🧱 收录 **[MicroDuck Jetson Orin Nano mount](https://github.com/adammong/microduck-jetson-mount)**：提供可打印参数化 CAD 与有测量记录的 MuJoCo 载荷策略研究，但真机适配、强度和控制尚未测试。

### 2026-10-08

- 📦 核验官方 **[daemon v0.15.2](https://github.com/pollen-robotics/microduck/releases/tag/daemon-v0.15.2)**：运动上限可配置，关机前会平缓进入记录的归位姿态，被抱起时会暂停当前策略；v0.15.1 还加强了装机与更新校验。
- 🧠 核验官方 **[v7 策略集](https://huggingface.co/pollen-robotics/microduck-policies/tree/v7)**：v6 降低坐姿下突然转头导致后仰的风险，v7 恢复站立时的横滚/俯仰控制；两者均由作者报告已通过真机验证，但 v7 仍未学会下蹲。
- 🧪 更新 **[Microduck Playground](https://github.com/Vottivott/microduck-playground)** 与 **[Microduck Lab](https://github.com/jonathanhawkins/microduck-lab)**：新增长跳/后空翻实验和更丰富的多机器人浏览器世界；这些仍是仿真结果。
- ⚠️ 标注 **[XGO Duck 接口修订](https://github.com/LuwuDynamics/xgoduck_hardware/blob/63b1c45/PCBA/README.md)**：旧板 U3、U4、U5 可能将 GND 与信号线接反，上电前必须核对。
- 🧰 收录 **[DuckKit](https://github.com/craigm26/duckkit)** 与 **[quackd](https://github.com/rokbenko/quackd)**，分别用于 Swift 原生集成和目标驱动/MCP 实验；两者都尚未验证 Microduck 真机控制。

### 2026-09-29

- 📡 核验官方 **[daemon v0.15.0](https://github.com/pollen-robotics/microduck/releases/tag/daemon-v0.15.0)**：稳定版遥测已加入关节速度与负载，文档也补充服务端 Agent 控制路径；后续 `daemon-dev-*` 仍属预发布。
- 🧩 更新 **[Microduck Playground](https://github.com/Vottivott/microduck-playground)**：已发布烟囱式攀爬仿真演示与策略产物；真机表现尚未测试。
- 🔧 重新核验 **[Microduck replica](https://github.com/fanhao375/microduck-replica)**：HD-1910 版已完成装机，并报告了姿态控制与关节回读，但尚未验证完整 IMU—策略环路和行走。
- 🦆 收录 **[XGO Duck](https://github.com/LuwuDynamics/xgoduck_hardware)**：基于 Arduino Uno Q 与飞特舵机的适配版，开放了制作文件、运行时和训练代码，并有作者发布的实机演示。

### 2026-09-21

- 📱 核验官方 **[daemon v0.14.1](https://github.com/pollen-robotics/microduck/releases/tag/daemon-v0.14.1)**：手机端已可让机器人起立并启动策略；v0.14.0 还将 MuJoCo 数字体切换为真实运行时守护进程驱动。
- 🌐 收录 **[Microduck Web](https://github.com/TonyRuan/microduck-web)**：支持触控与 ONNX 策略导入的社区浏览器仿真器；不控制实体硬件。
- 📚 收录 **[OpenMicroDuck](https://github.com/SaberOnGo/open-microduck)**：双语学习与研究指南，区分官方事实、社区重建和待确认问题。
- 🧰 收录 **[Fanduck](https://github.com/7757/fanduck)**：已完成的社区复刻，提供作者实机演示与制作资料；使用前需核对模型的非商业条款。

### 2026-09-16

- 🧠 收录 **[microduck-mcp](https://github.com/joeynyc/microduck-mcp)**：支持 mock 与仿真的 Agent 接口；真机传输仍未经过硬件验证。
- 🍎 收录 **[Microduck Lab](https://github.com/jonathanhawkins/microduck-lab)**：面向 Apple Silicon 的本地 Microduck 实验，配有浏览器可视化。
- 🔧 收录 **[Microduck replica](https://github.com/fanhao375/microduck-replica)**：逆向结构、CAD 与装机记录；需区分舵机版本和当前完成状态。
- ⚠️ 核验 **[isaaclab-microduck](https://github.com/kabilankb/isaaclab-microduck)**：README 明示行走尚未成功，应作为任务移植研究，而非现成行走策略。

→ [查看全部更新记录](docs/updates.md)

## 按你的设备开始

| 你现在有什么 | 建议入口 | 第一个目标 |
| --- | --- | --- |
| 只有浏览器 | [官方在线仿真](https://huggingface.co/spaces/pollen-robotics/microduck-simulator) | 观察并控制仿真小鸭 |
| Apple Silicon Mac | [Microduck Lab](https://github.com/jonathanhawkins/microduck-lab) | 复现本地仿真 |
| NVIDIA CUDA 环境 | [官方 RL 工程](https://github.com/pollen-robotics/microduck_rl) | 核对依赖、列出可训练任务 |
| 策略基准目标 | [官方 Arena 挑战](https://github.com/pollen-robotics/microduck-challenges) | 训练、评分并发布一项仿真参赛策略 |
| AMD Linux 工作站 | [Genesis 移植](https://github.com/Macmachi/microduck-rl-genesis) | 对照作者已测试的 ROCm 环境 |
| ROS 2 基础 | [ROS 2 教程](https://github.com/osrbot/microduck-ros2-isaac) | 在 RViz 查看模型 |
| 动手装机条件 | [中文装机教程](https://github.com/AI-FanGe/Microduck-build-tutorial) | 确认一套完整硬件配置 |
| Agent 接入想法 | [MCP 项目](https://github.com/joeynyc/microduck-mcp) | 先验证 mock，再进入仿真 |

查看[详细路线与常见问题](docs/getting-started.md)。

## 浏览 Microduck 生态

[官方入口](#official) · [文档](#documentation) · [仿真训练](#simulation-and-training) · [策略实验](#policy-experiments) · [开发工具](#developer-and-agent-tools) · [硬件复刻](#hardware-and-diy)

每项资源附有运行环境、证据状态与核验日期。[了解状态标签](#资源如何核验)。

<!-- 后续按资源积累扩展：Examples & Demos；Community Projects；Hardware Mods；
CAD / 3D Printing；Sensors & Accessories；Vision / VLA / Agents；
Training Recipes；Videos & Tutorials；Research & Experiments。
有已核验资源后再引入分类，不发布空章节；新增分类时同步目录生成脚本。 -->

<!-- RESOURCES:START -->
<a id="official"></a>
### 官方入口

- [Microduck OS](https://github.com/pollen-robotics/microduck_yocto) — 官方生产镜像；v1.1.0 随镜像提供手柄与 NFC 守护进程，在分区切换更新后保留蓝牙配对，改进可安装版本筛选，并逐灯验证 V1.0 面板映射；新工厂刷写指南尚未在板卡上完整走通。 **Radxa Zero 3W / Yocto / RK3566** · `official` · [来源](https://github.com/pollen-robotics/microduck_yocto/releases/tag/microduck-os-v1.1.0) · 2026-11-02.
- [Microduck RL](https://github.com/pollen-robotics/microduck_rl) — 官方 CUDA 训练工程，含 v8 谱系与作者报告的真机验证；现支持选择性发布 Hub 训练包，包含完整检查点、来源记录和蒸馏教师，可用于续训或热启动。 **CUDA** · `official` · [来源](https://github.com/pollen-robotics/microduck_rl/commit/3b8759e9dad2bd12dae03129bc4a07fe24a48026) · 2026-11-02.
- [Microduck runtime](https://github.com/pollen-robotics/microduck) — 官方运行时与操作文档；稳定版 v0.17.7–v0.18.3 新增更安全的跌倒处理、弱网摄像头自适应、beta 摄像头标定、手柄重连、加快启动检查、可选健康档案分享，以及可退出的匿名遥测。 **Robot / simulation** · `official` · [来源](https://github.com/pollen-robotics/microduck/releases/tag/daemon-v0.18.3) · 2026-11-02.
- [Microduck Sandbox](https://huggingface.co/spaces/pollen-robotics/microduck-simulator) — 先在线体验仿真，再决定是否搭建本地环境。 **Browser** · `official` · [来源](https://huggingface.co/spaces/pollen-robotics/microduck-simulator) · 2026-09-16.
- [Official policy files](https://huggingface.co/pollen-robotics/microduck-policies) — 官方 v8 ONNX 策略集；作者报告已在真机验证更平顺可靠的起身和偏航指令跟踪，并延续 v7 的站立横滚与俯仰控制。 **ONNX** · `official` · [来源](https://huggingface.co/pollen-robotics/microduck-policies/tree/v8) · 2026-10-19.

<a id="documentation"></a>
### 文档

- [Documentation index](https://github.com/pollen-robotics/microduck/blob/main/docs/README.md) — 按操作与开发需求查找上游文档。 **Reading** · `official` · [来源](https://github.com/pollen-robotics/microduck/blob/main/docs/README.md) · 2026-09-16.
- [Official daemon releases](https://github.com/pollen-robotics/microduck/releases) — 跟踪稳定版 daemon，并与签名开发构建区分。 **Reading / release artifacts** · `official` · [来源](https://github.com/pollen-robotics/microduck/releases/tag/daemon-v0.18.3) · 2026-11-02.
- [OpenMicroDuck](https://github.com/SaberOnGo/open-microduck) — 覆盖仿真、训练与复刻研究的双语社区指南；阅读时保留对来源标签和未决硬件问题的关注。 **Bilingual guide** · `experimental` · [来源](https://github.com/SaberOnGo/open-microduck) · 2026-09-21.
- [Policy manifest reference](https://github.com/pollen-robotics/microduck/blob/main/docs/policy-manifest.md) — 核对策略元数据与兼容性要求。 **Reading** · `official` · [来源](https://github.com/pollen-robotics/microduck/blob/main/docs/policy-manifest.md) · 2026-09-16.
- [Robot command reference](https://github.com/pollen-robotics/microduck/blob/main/docs/robot/cheatsheet.md) — 查阅对应运行时版本的操作命令。 **Reading** · `official` · [来源](https://github.com/pollen-robotics/microduck/blob/main/docs/robot/cheatsheet.md) · 2026-09-16.
- [Runtime simulation guide](https://github.com/pollen-robotics/microduck/blob/main/docs/robot/simulation.md) — 用真实运行时守护进程驱动 MuJoCo 机体；物理总线和设备驱动不在仿真范围内。 **Reading** · `official` · [来源](https://github.com/pollen-robotics/microduck/blob/main/docs/robot/simulation.md) · 2026-09-21.

<a id="simulation-and-training"></a>
### 仿真与训练

- [isaaclab-microduck](https://github.com/kabilankb/isaaclab-microduck) — 任务移植研究。核验时 README 明示行走尚未成功，不应作为现成行走策略。 **Isaac Lab / CUDA** · `experimental` · [来源](https://github.com/kabilankb/isaaclab-microduck) · 2026-09-16.
- [Microduck Arena](https://huggingface.co/spaces/pollen-robotics/microduck-arena) — 官方可复现策略竞赛平台，使用固定服务端赛道并支持下载参赛策略；v0.7.0 新增拔河与六米红绿灯玩法 Sock Heist。 **Browser / local / ONNX** · `official` · [来源](https://github.com/pollen-robotics/microduck-arena/releases/tag/v0.7.0) · 2026-11-02.
- [Microduck challenges](https://github.com/pollen-robotics/microduck-challenges) — 官方公开的六项 Arena 赛事训练目录与工作坊，新增拔河与 Sock Heist，支持检查点评测及发布到 Arena；成绩仅属于仿真证据。 **Python 3.12 / CUDA or Hugging Face Jobs** · `official` · [来源](https://github.com/pollen-robotics/microduck-challenges/commit/5cee942d8b434aafd395070facb659034aac3b5e) · 2026-11-02.
- [Microduck Lab](https://github.com/jonathanhawkins/microduck-lab) — 面向 Apple Silicon 与 CPU 的训练实验室，含浏览器世界、多鸭足球和整理行为；本次核验结果仍仅限仿真。 **Apple Silicon / CPU** · `simulation-reported` · [来源](https://github.com/jonathanhawkins/microduck-lab/commit/bbf0326) · 2026-10-08.
- [Microduck RL on Genesis](https://github.com/Macmachi/microduck-rl-genesis) — 面向 AMD 的训练替代方案；使用项目列出的已测试配置。 **Linux / AMD ROCm** · `simulation-reported` · [来源](https://github.com/Macmachi/microduck-rl-genesis) · 2026-09-16.
- [MicroDuck ROS 2 + Isaac Sim](https://github.com/osrbot/microduck-ros2-isaac) — ROS 2 Jazzy 查看器与 Isaac Sim/Lab 教程现已固定官方 v7 策略；转换后的 USD 与 GPU 回放仍待复验，且不含真机驱动。 **ROS 2 Jazzy / optional Isaac Sim** · `simulation-reported` · [来源](https://github.com/osrbot/microduck-ros2-isaac/commit/2adc4b157fc732d4751ad97577e4ea39bd727abd) · 2026-10-12.
- [Microduck Web](https://github.com/TonyRuan/microduck-web) — 支持触控与策略导入的社区 MuJoCo 和 ONNX 仿真器；不控制实体硬件。 **Browser / mobile / offline cache** · `simulation-reported` · [来源](https://github.com/TonyRuan/microduck-web) · 2026-09-21.
- [microduck-rl-torch](https://github.com/bsprenger/microduck-rl-torch) — 探索 PyTorch 移植方案；先阅读各计算后端的限制。 **PyTorch / CPU / GPU** · `experimental` · [来源](https://github.com/bsprenger/microduck-rl-torch) · 2026-09-16.

<a id="policy-experiments"></a>
### 策略实验

- [Microduck Playground](https://github.com/Vottivott/microduck-playground) — 可复现仿真涵盖烟囱攀爬、高台长跳与后空翻并发布策略；真机仍未测试，后空翻明确提示可能损坏机器人。 **Simulation** · `simulation-reported` · [来源](https://github.com/Vottivott/microduck-playground/commit/f010ef1) · 2026-10-08.
- [my-microduck-journal](https://github.com/xinhuagu/my-microduck-journal) — 面向消费级 GPU 的训练记录，已发布 ONNX 策略、补丁、多随机种子原始评测数据与校验和；v0.2 的速度和恢复结果为作者报告的仿真数据，尚无真机验证。 **CUDA / WSL2 / ONNX** · `simulation-reported` · [来源](https://github.com/xinhuagu/my-microduck-journal/releases/tag/v0.2) · 2026-10-19.

<a id="developer-and-agent-tools"></a>
### 开发与 Agent 工具

- [DuckKit](https://github.com/craigm26/duckkit) — 以零依赖 Swift 实现策略、观测、运动学与 RPC 契约；作者报告 347 项离线测试，但尚无真机验证。 **Swift / Linux / Apple** · `experimental` · [来源](https://github.com/craigm26/duckkit/releases/tag/v1.37.0) · 2026-10-08.
- [Microduck Studio](https://github.com/microai-lab/microduck-studio) — 连接运行时与仿真的开发界面；需配套同级仓库。 **Local / Docker launcher** · `experimental` · [来源](https://github.com/microai-lab/microduck-studio) · 2026-09-16.
- [microduck-mcp](https://github.com/joeynyc/microduck-mcp) — 提供 mock 与仿真路径的 Agent 接口；README 说明真机传输仅经过伪守护进程验证。 **Node.js / mock / simulation** · `hardware-unverified` · [来源](https://github.com/joeynyc/microduck-mcp) · 2026-09-16.
- [quackd](https://github.com/rokbenko/quackd) — 面向目标任务的机器人 CLI、浏览器界面与 MCP 桥接，支持 mock 和 MuJoCo；v0.29.1 已加入视觉、头部跟踪与仿真房间探索，但维护者仍说明尚无 Microduck 真机运行。 **Python 3.12 / mock / MuJoCo / MCP** · `hardware-unverified` · [来源](https://github.com/rokbenko/quackd/releases/tag/v0.29.1) · 2026-11-02.

<a id="hardware-and-diy"></a>
### 硬件与复刻

- [DuckBuddy](https://github.com/Animan-AI/DuckBuddy) — 开放硬件与软件分支，公开板卡、固件、训练代码及作者实机离线语音连续动作演示；HL-2915 版本已日常使用，HD-1910、端侧 VLM 与定位仍未完成。 **DIY / Orange Pi Zero 3W / Feetech HL-2915** · `hardware-demo-reported` · [来源](https://github.com/Animan-AI/DuckBuddy/commit/933c6d9547cfd0e5cd06c805bc406bf394ba6ca3) · 2026-11-02.
- [Fanduck](https://github.com/7757/fanduck) — 已完成的社区复刻，提供作者实机演示、BOM、打印与板件资料；使用前核对模型的非商业条款。 **DIY / CAD / PCB** · `hardware-demo-reported` · [来源](https://github.com/7757/fanduck) · 2026-09-21.
- [Microduck build tutorial](https://github.com/AI-FanGe/Microduck-build-tutorial) — 中文装机与部署教程，作者提供实物视频；配置与官方产品不同。 **DIY / Raspberry Pi** · `hardware-demo-reported` · [来源](https://github.com/AI-FanGe/Microduck-build-tutorial) · 2026-09-16.
- [MicroDuck Jetson Orin Nano mount](https://github.com/adammong/microduck-jetson-mount) — 面向外置算力的参数化挂载方案，提供可打印 CAD 与可复现的载荷策略研究；适配、强度和控制结果仍仅限仿真。 **CAD / MuJoCo / Jetson Orin Nano** · `simulation-reported` · [来源](https://github.com/adammong/microduck-jetson-mount/commit/8d361ceae40c8474e43468bfbd2d311344387fa1) · 2026-10-12.
- [Microduck replica](https://github.com/fanhao375/microduck-replica) — HD-1910 复刻已报告持续行走，并提供签名网页更新、本地坐站语音、模型管理与诊断；2026-10-31 手柄驱动、新镜像组合及秦墨 IMU 路线仍有明确的实物验收缺口。 **CAD / electronics / DIY** · `hardware-demo-reported` · [来源](https://github.com/fanhao375/microduck-replica/releases/tag/microduck-software-v2026.10.31) · 2026-11-02.
- [Microduck-kissqy](https://github.com/kissqy/Microduck-kissqy) — HD-1910 构建栈，公开 HAT 与 IMU 文件、打印件、固件、机器人及训练中控、已刷卡测试的 R1 镜像和作者实机视频；仍需逐机标定，原创新增部分限非商业使用。 **DIY / Radxa Zero 3W / Feetech HD-1910** · `hardware-demo-reported` · [来源](https://github.com/kissqy/Microduck-kissqy/commit/f02e875e73b88bf8ec7d5bbb34d0b461ac83b010) · 2026-10-19.
- [XGO Duck](https://github.com/LuwuDynamics/xgoduck_hardware) — 基于 Arduino Uno Q 且有作者实机演示；V1.1 已公开生产文件及反接、堵转测试视频，但缺少 V1.1 PCB 源文件与兼容说明，旧板仍须按文档核对接线。 **DIY / Arduino Uno Q / Feetech 1910** · `hardware-demo-reported` · [来源](https://github.com/LuwuDynamics/xgoduck_hardware/commit/7dd33c603cbff92bc4afbc7f318abd4ccd9127b6) · 2026-11-02.
<!-- RESOURCES:END -->

## 资源如何核验

我们对照上游文档、演示与公开证据核验资源。状态标签区分发布主体与当前已展示的能力，未来计划不作为已实现功能。来源核验不等于独立实测。

| 标签 | 含义 |
| --- | --- |
| `official` | 上游官方发布，表示来源而非测试结果 |
| `simulation-reported` | 作者提供仿真结果 |
| `hardware-demo-reported` | 作者提供实物演示 |
| `experimental` | 仍有研究或集成限制 |
| `hardware-unverified` | 真机验证尚未确立 |

本次周更的来源核验日期为 **2026-11-02**；每项资源的日期表示其最近单独核验时间。本清单尚未逐项安装运行。

[阅读完整核验规则](docs/review-policy.md)

## 持续探索

- [入门路线](docs/getting-started.md)：选环境、定目标、记录可复现结果。
- [更新记录](docs/updates.md)：关注新项目、新工具、新硬件与重要进展。
- [JSON 资源索引](data/resources.json)：包含中英描述、证据链接和核验日期。
- 想接收精选版本通知，请使用 GitHub **Watch → Custom → Releases**；后续发布时会附上更新说明。

## 参与贡献

发现新项目、硬件改装、传感器、配件或训练方案？欢迎[贡献资源或纠正信息](CONTRIBUTING.md)，说明环境要求、已展示的结果与限制。

也欢迎充电底座、夹爪、额外执行器，以及视觉 / VLA / 多模态控制实验。请提供当前能力的证据；相关资源通过核验后，再扩展对应分类。

## 致谢与许可

独立社区项目，与 Pollen Robotics、Hugging Face 无隶属关系。


受到 [joeynyc/awesome-microduck](https://github.com/joeynyc/awesome-microduck) 的启发，尤其是其生态导航思路与资源组织方式。感谢该项目为梳理早期 Microduck 社区所做的贡献。

原创清单文字、文档与横幅采用 [CC0](LICENSE)。外链代码、权重、CAD 与媒体遵循各自许可，收录不改变其使用权限。
