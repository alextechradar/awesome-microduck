# Getting started / Microduck 入门路线

[English catalog](../README.md) · [中文目录](../README.zh-CN.md)

Pick one route, reproduce one result, and record the upstream commit and environment. These are navigation guides, not independently tested installation recipes.

先完成一个可复现的小目标，再扩展训练或装机。以下路线基于上游文档；不承诺完成时间，也不代表本仓库已实测。

## 1. Browser / 只用浏览器

Open the [official sandbox](https://huggingface.co/spaces/pollen-robotics/microduck-simulator). Wait for the Space to load, read its controls and observe one behavior. If the service is sleeping or unavailable, retry later or choose a local route.

打开官方仿真，按页面提示尝试控制并观察一个动作。在线服务可能休眠或暂时不可用。记录你观察到的行为与异常；能展示动作不等于能部署到实物。

## 2. Mac or CPU / Mac 与无 CUDA 路线

Read [Microduck Lab](https://github.com/jonathanhawkins/microduck-lab), especially prerequisites and setup. Reproduce its viewer before changing rewards. Compare [microduck-rl-torch](https://github.com/bsprenger/microduck-rl-torch) only if you need its PyTorch backend; inspect its known limitations.

先按 Microduck Lab 的前置条件启动已有策略的可视化，再尝试奖励设计。不要把社区训练方案的输出自动视为官方硬件兼容结果。PyTorch 移植可作为另一条研究路线，需单独核对后端限制。

## 3. CUDA / 官方训练路线

Use the [official training instructions](https://github.com/pollen-robotics/microduck_rl). Confirm CUDA and uv prerequisites; start with the task registry. Training consumes compute, so select the task and environment count deliberately.

核对 CUDA 与 uv 环境后，可先下载工程并查看任务；这一步不会主动开始训练：

```bash
git clone https://github.com/pollen-robotics/microduck_rl
cd microduck_rl
uv run list-envs
```

`uv run` may download dependencies. For training, evaluation and export, use the commands from your checked-out upstream version. Save the commit, configuration, seed and evaluation result together.

训练、评估和导出命令以实际 checkout 版本为准。至少保存 commit、配置、随机种子与评估结果；奖励升高并不直接说明目标动作完成。

## 4. AMD or ROS / 替代仿真路线

For AMD Linux, review the [Genesis port](https://github.com/Macmachi/microduck-rl-genesis) and its tested configuration. For ROS 2, start with [RViz](https://github.com/osrbot/microduck-ros2-isaac); the project's initial ROS path does not require Isaac Sim.

AMD 用户按 Genesis 项目已测试配置选择环境；ROS 2 用户可先查看关节模型。不要将不同项目的依赖环境与命令混用。Isaac Lab 移植项目之间也不能仅凭相似名称判断成熟度。

## 5. Hardware / 硬件路线

Separate the [official operator docs](https://github.com/pollen-robotics/microduck/blob/main/docs/README.md) from the [community build tutorial](https://github.com/AI-FanGe/Microduck-build-tutorial) and [replica research](https://github.com/fanhao375/microduck-replica). Pick one documented configuration before sourcing parts.

区分官方产品与社区复刻的板卡、舵机及固件。先检查 BOM、装配记录、适配策略及文件许可，再采购。模型能在仿真中加载，不代表结构件可直接打印装机。

## Common questions / 常见问题

**Do I need a robot? / 必须买机器鸭吗？** No for the simulation routes. 仿真路线不需要实物。

**Does official training work on a plain Mac? / 官方训练能直接在普通 Mac 跑吗？** Its documented local training path requires CUDA; use a separately documented alternative. 官方本地训练要求 CUDA，社区路线需要独立环境。

**Can I run any ONNX file? / ONNX 都能直接上机吗？** Check the [manifest contract](https://github.com/pollen-robotics/microduck/blob/main/docs/policy-manifest.md), model assumptions and runtime version. 文件格式相同不代表观测、动作或硬件兼容。

**Are all assets freely usable commercially? / 全部都可商用吗？** No. The [RL repository](https://github.com/pollen-robotics/microduck_rl) distinguishes software and hardware-design licenses. 需逐项查看实际文件许可。

## Record your first result / 记录第一次复现

Use this in a resource contribution:

```text
Project URL / 项目链接:
Commit or release / 版本:
OS and hardware / 环境:
Route / browser, mock, simulation, hardware:
What ran / 完成了什么:
Evidence / 日志或视频:
Limitations / 未完成与已知限制:
```

Return to the [catalog](../README.md) or [contribute your finding](../CONTRIBUTING.md).
