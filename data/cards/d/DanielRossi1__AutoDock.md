# DanielRossi1/AutoDock

⭐ 36 · Shell · 推送 2026-04-16 · [GitHub](https://github.com/DanielRossi1/AutoDock) · [官网](https://danielrossi1.github.io/AutoDock/) · 个人维护

**面向 AI 科研项目的 Docker 化环境与复现框架**

以 Docker 容器封装 AI 研究项目的运行环境，提供 build.sh/run.sh 脚本构建与启动镜像，封装 Ubuntu + CUDA + 依赖安装，支持多套 requirements 按目标设备（工作站、Jetson Nano/Orin、树莓派）切换。run.sh 提供目录挂载、SSH、AI 缓存（pip/huggingface/torch/uv）、GPU、摄像头/音频/外设等选项；另支持 autodock.config.json 结构化配置、Conda 环境生成、VSCode 容器内开发与远程主机连接，可自动安装 ROS Noetic。给需要在多台机器间共享与复现实验环境的研究者使用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- build.sh/run.sh 构建并运行含 Ubuntu+CUDA+依赖的容器
- 按设备分设 requirements（Jetson Nano/Orin、树莓派等）
- run.sh 支持挂载、AI 缓存、SSH/GPU/摄像头/音频/外设选项
- remote.sh 配置远程主机容器连接与 VSCode 远程开发

## 适用场景

- 把 AI 科研项目打包成可复现的容器环境
- 在 Jetson、树莓派等边缘设备上复用同一套环境配置
- 本地 VSCode 直接附加到远程机器上的容器开发调试

## 场景标签

 · 领域:AI 开发环境/容器化

## 证据(README 行号)

> L15: This Docker-based framework is designed to facilitate research by enabling projects to run seamlessly across differ
> L17: Its primary objective is to minimize the setup and execution times of AI projects by providing a streamlined and st

## 星数曲线

```mermaid
xychart-beta
    title "DanielRossi1/AutoDock 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 35 --> 37
    line [36, 36]
```

2026-10-18 36 → 2026-10-31 36（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `9261f3e65610` · [字段定义](../../DATASET.md)*
