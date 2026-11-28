# TrebuchetDynamics/gormes-agent

⭐ 10 · Go · 推送 2026-11-05 · [GitHub](https://github.com/TrebuchetDynamics/gormes-agent) · [官网](https://gormes.ai) · 组织维护

**Go 单二进制 agent 运行时，便携运行 Hermes 兼容代理**

以 Go 语言实现的 agent 运行时，将 provider 调用、工具/技能注册、SQLite 本地记忆、会话、仪表盘与 Telegram/Discord/Slack 网关打包为单个静态二进制。目标是让 Hermes 形态的 agent 在无 Python/Node/Docker 环境下运行（Termux、WSL2、受限 Linux 主机），提供离线诊断、引导式配置，并支持从 Hermes/OpenClaw 迁移配置。语音/TTS、发布签名、MCP parity 等仍在路线图，Navivox 应用通道为实验性。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 单 Go 静态二进制，无需 pip/venv/Docker daemon/Redis/向量库
- 内置 30 个 Hermes 技能（编码、GitHub、浏览器、研究等）
- 本地 SQLite 记忆与会话，数据位于 ~/.gormes
- 支持 Hermes/OpenClaw 带干跑的迁移与离线自检

## 适用场景

- 在没有 Python 环境的服务器或 Termux 上运行持久化 agent
- 通过 Telegram/Discord/Slack 网关与自己的 agent 对话
- 从 Hermes 或 OpenClaw 迁移现有 agent 配置与记忆

## 场景标签

`Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L3:  Run Hermes-compatible agents from one Go binary.
> L14: Gormes is not a micro-agent or a prompt-wrapper app. It is runtime plumbing for agents that need to keep useful str

## 星数曲线

```mermaid
xychart-beta
    title "TrebuchetDynamics/gormes-agent 星数(近 2 点)"
    x-axis ["2026-10-26", "2026-11-28"]
    y-axis "stars" 9 --> 11
    line [10, 10]
```

2026-10-26 10 → 2026-11-28 10（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-20 · 置信度 high · 依据 README sha `c927cdceaf8e` · [字段定义](../../DATASET.md)*
