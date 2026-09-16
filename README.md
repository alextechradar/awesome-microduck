# Awesome Microduck

![Awesome Microduck — discover, simulate, train, build](assets/banner.svg)

**A curated and continuously reviewed map of the Microduck ecosystem.**

Discover simulators, policies, agent tools, hardware builds and experiments — with practical notes on what works today and what remains unproven.

⭐ **Star this repository to follow the Microduck ecosystem.**

English · [简体中文](README.zh-CN.md) · [Start here](docs/getting-started.md) · [Contribute](CONTRIBUTING.md)

## 🆕 What's new

### 2026-09-16

- 🧠 Added **[microduck-mcp](https://github.com/joeynyc/microduck-mcp)** — an agent interface with mock and simulation support; real-device transports remain hardware-unverified.
- 🍎 Added **[Microduck Lab](https://github.com/jonathanhawkins/microduck-lab)** — local Microduck experiments for Apple Silicon, with a browser viewer.
- 🔧 Added **[Microduck replica](https://github.com/fanhao375/microduck-replica)** — reconstruction notes, CAD and build logs; check the actuator variant and completion status.
- ⚠️ Reviewed **[isaaclab-microduck](https://github.com/kabilankb/isaaclab-microduck)** — its README reports unsuccessful locomotion; treat it as task-port research, not a ready walking policy.

→ [See all review notes](docs/updates.md)

## Choose your route

| What you have | Start here | First milestone |
| --- | --- | --- |
| A browser | [Official sandbox](https://huggingface.co/spaces/pollen-robotics/microduck-simulator) | Observe and control a simulated duck |
| An Apple Silicon Mac | [Microduck Lab](https://github.com/jonathanhawkins/microduck-lab) | Reproduce a local simulation |
| An NVIDIA CUDA setup | [Official RL stack](https://github.com/pollen-robotics/microduck_rl) | Confirm dependencies and list training tasks |
| An AMD Linux workstation | [Genesis port](https://github.com/Macmachi/microduck-rl-genesis) | Check the project's tested ROCm setup |
| ROS 2 experience | [ROS 2 tutorial](https://github.com/osrbot/microduck-ros2-isaac) | Inspect the model in RViz |
| A DIY workbench | [Build tutorial](https://github.com/AI-FanGe/Microduck-build-tutorial) | Match one complete hardware configuration |
| An agent integration idea | [MCP project](https://github.com/joeynyc/microduck-mcp) | Exercise the mock path before simulation |

Read the [step-by-step routes and common traps](docs/getting-started.md).

## Browse the ecosystem

[Official](#official) · [Documentation](#documentation) · [Simulation](#simulation-and-training) · [Policies](#policy-experiments) · [Tools](#developer-and-agent-tools) · [Hardware](#hardware-and-diy)

Each entry includes its environment, evidence status and review date. [How to read the labels](#how-resources-are-reviewed).

<!-- Future categories: Examples & Demos; Community Projects; Hardware Mods;
CAD / 3D Printing; Sensors & Accessories; Vision / VLA / Agents;
Training Recipes; Videos & Tutorials; Research & Experiments.
Introduce a category only when reviewed resources justify it; never publish empty sections.
Keep catalog generation in sync when introducing a category. -->

<!-- RESOURCES:START -->
<a id="official"></a>
### Official

- [Microduck RL](https://github.com/pollen-robotics/microduck_rl) — Official training workspace; begin with its requirements and live task registry. **CUDA** · `official` · [Source](https://github.com/pollen-robotics/microduck_rl) · 2026-09-16.
- [Microduck runtime](https://github.com/pollen-robotics/microduck) — Start here for robot software and operator documentation. **Robot / simulation** · `official` · [Source](https://github.com/pollen-robotics/microduck) · 2026-09-16.
- [Microduck Sandbox](https://huggingface.co/spaces/pollen-robotics/microduck-simulator) — Try the hosted simulator before choosing a local setup. **Browser** · `official` · [Source](https://huggingface.co/spaces/pollen-robotics/microduck-simulator) · 2026-09-16.
- [Official policy files](https://huggingface.co/pollen-robotics/microduck-policies) — Find published weights; check the runtime manifest contract before integration. **ONNX** · `official` · [Source](https://github.com/pollen-robotics/microduck/blob/main/docs/policy-manifest.md) · 2026-09-16.

<a id="documentation"></a>
### Documentation

- [Documentation index](https://github.com/pollen-robotics/microduck/blob/main/docs/README.md) — Find the relevant operator or developer guide. **Reading** · `official` · [Source](https://github.com/pollen-robotics/microduck/blob/main/docs/README.md) · 2026-09-16.
- [Policy manifest reference](https://github.com/pollen-robotics/microduck/blob/main/docs/policy-manifest.md) — Check policy metadata and compatibility requirements. **Reading** · `official` · [Source](https://github.com/pollen-robotics/microduck/blob/main/docs/policy-manifest.md) · 2026-09-16.
- [Robot command reference](https://github.com/pollen-robotics/microduck/blob/main/docs/robot/cheatsheet.md) — Look up commands for the installed runtime version. **Reading** · `official` · [Source](https://github.com/pollen-robotics/microduck/blob/main/docs/robot/cheatsheet.md) · 2026-09-16.
- [Runtime simulation guide](https://github.com/pollen-robotics/microduck/blob/main/docs/robot/simulation.md) — Follow the upstream setup for testing the runtime in simulation. **Reading** · `official` · [Source](https://github.com/pollen-robotics/microduck/blob/main/docs/robot/simulation.md) · 2026-09-16.

<a id="simulation-and-training"></a>
### Simulation and training

- [isaaclab-microduck](https://github.com/kabilankb/isaaclab-microduck) — Task-port research. The reviewed README reports unsuccessful locomotion; do not select it as a ready walking policy. **Isaac Lab / CUDA** · `experimental` · [Source](https://github.com/kabilankb/isaaclab-microduck) · 2026-09-16.
- [Microduck Lab](https://github.com/jonathanhawkins/microduck-lab) — Mac-oriented reward experiments with a browser viewer; community implementation. **Apple Silicon / CPU** · `simulation-reported` · [Source](https://github.com/jonathanhawkins/microduck-lab) · 2026-09-16.
- [Microduck RL on Genesis](https://github.com/Macmachi/microduck-rl-genesis) — An AMD-oriented training alternative; follow its tested configuration. **Linux / AMD ROCm** · `simulation-reported` · [Source](https://github.com/Macmachi/microduck-rl-genesis) · 2026-09-16.
- [MicroDuck ROS 2 + Isaac Sim](https://github.com/osrbot/microduck-ros2-isaac) — Start with the RViz path; use the separate Isaac tutorials when needed. **ROS 2 Jazzy / optional Isaac Sim** · `simulation-reported` · [Source](https://github.com/osrbot/microduck-ros2-isaac) · 2026-09-16.
- [microduck-rl-torch](https://github.com/bsprenger/microduck-rl-torch) — Explore a portable PyTorch implementation; check backend limitations first. **PyTorch / CPU / GPU** · `experimental` · [Source](https://github.com/bsprenger/microduck-rl-torch) · 2026-09-16.

<a id="policy-experiments"></a>
### Policy experiments

- [Microduck Playground](https://github.com/Vottivott/microduck-playground) — Browse experiment write-ups and their associated policy demonstrations. **Simulation** · `simulation-reported` · [Source](https://github.com/Vottivott/microduck-playground) · 2026-09-16.

<a id="developer-and-agent-tools"></a>
### Developer and agent tools

- [Microduck Studio](https://github.com/microai-lab/microduck-studio) — A development interface joining runtime and simulation; requires sibling repositories. **Local / Docker launcher** · `experimental` · [Source](https://github.com/microai-lab/microduck-studio) · 2026-09-16.
- [microduck-mcp](https://github.com/joeynyc/microduck-mcp) — Agent interface with mock and simulation paths. Its README states real-device transports have only fake-daemon validation. **Node.js / mock / simulation** · `hardware-unverified` · [Source](https://github.com/joeynyc/microduck-mcp) · 2026-09-16.

<a id="hardware-and-diy"></a>
### Hardware and DIY

- [Microduck build tutorial](https://github.com/AI-FanGe/Microduck-build-tutorial) — Chinese assembly and setup guide with author-published hardware clips; its configuration differs from the official product. **DIY / Raspberry Pi** · `hardware-demo-reported` · [Source](https://github.com/AI-FanGe/Microduck-build-tutorial) · 2026-09-16.
- [Microduck replica](https://github.com/fanhao375/microduck-replica) — Reconstruction notes and build logs; check the specific actuator variant and current completion status. **CAD / electronics / DIY** · `experimental` · [Source](https://github.com/fanhao375/microduck-replica) · 2026-09-16.
<!-- RESOURCES:END -->

## How resources are reviewed

Resources are reviewed against upstream documentation, demos and published evidence. Status labels distinguish the publisher and what is currently demonstrated, rather than planned support. Source review does not imply independent testing.

| Label | What it tells you |
| --- | --- |
| `official` | Published by upstream; identifies provenance, not a test result |
| `simulation-reported` | Authors report simulation results |
| `hardware-demo-reported` | Authors publish physical-hardware demonstrations |
| `experimental` | Research or integration work with current limitations |
| `hardware-unverified` | Real-device validation is not established |

The current catalog and route requirements were source-reviewed on **2026-09-16**; this list has not independently run the projects.

[Read the full review policy](docs/review-policy.md)

## Keep exploring

- [Getting started / 入门路线](docs/getting-started.md): choose a setup and define a reproducible first result.
- [Review notes / 更新记录](docs/updates.md): new projects, tools, hardware and important progress.
- [Machine-readable catalog](data/resources.json): bilingual descriptions, evidence links and review dates.
- For curated release notifications, use GitHub **Watch → Custom → Releases**. Review notes will accompany releases when published.

## Contributing

Found a new project, hardware mod, sensor, accessory or training recipe? [Contribute a resource or correction](CONTRIBUTING.md) with its requirements, demonstrated results and limitations.

We also welcome charging docks, grippers, additional actuators and vision / VLA / multimodal control experiments. Include evidence of what works today; new categories will appear as reviewed resources arrive.

## Credits and license

Independent community resource; not affiliated with Pollen Robotics or Hugging Face.


Inspired by [joeynyc/awesome-microduck](https://github.com/joeynyc/awesome-microduck), particularly its ecosystem-navigation approach and resource organization. Thanks to the project for helping map the early Microduck community.

Original catalog text, documentation and banner: [CC0](LICENSE). Linked code, model weights, CAD and media retain their own licenses; inclusion grants no additional rights.
