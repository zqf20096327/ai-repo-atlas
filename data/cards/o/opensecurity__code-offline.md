# opensecurity/code-offline

⭐ 15 · Makefile · 推送 2026-03-28 · [GitHub](https://github.com/opensecurity/code-offline) · 组织维护

**全本地容器化的 pi 编码 agent + llama.cpp 运行环境**

由 OpenSecurity 维护的容器化开发环境：以 Docker Compose 编排 llama.cpp 服务与 pi 编码 agent，在 CPU 或 NVIDIA GPU 上运行本地模型，不依赖外部 API。通过 Makefile 管理构建、启动、进入 agent 终端与清理；首次启动自动按 .env 配置从 Hugging Face 下载模型（默认 Qwen 3.5 系列 UD-Q4_K_XL 量化）。workspace、模型缓存与 agent 状态以卷形式持久化到宿主机。需自备 Docker、Docker Compose，GPU 模式另需 NVIDIA Container Toolkit。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Docker Compose 编排 llama.cpp 后端与 pi 编码 agent
- CPU / NVIDIA GPU 双模式（MODE=gpu 切换）
- 首次运行自动从 Hugging Face 下载指定模型
- workspace/models/agent_data 卷持久化到宿主机

## 适用场景

- 在离线或内网环境跑本地 LLM 编码助手
- 用私有模型处理代码且不让数据离开本机
- 在 CPU 或 NVIDIA GPU 服务器上一键搭建本地 agent 环境

## 场景标签

`编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L3: A localized, containerized development environment for running the pi coding agent backed by llama.cpp. This stack l
> L44: ```bash

## 星数曲线

```mermaid
xychart-beta
    title "opensecurity/code-offline 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-31 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `03f28898e93f` · [字段定义](../../DATASET.md)*
