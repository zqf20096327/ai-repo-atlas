# UpayanGhosh/Synapse-OSS

⭐ 15 · Python · MIT · 推送 2026-09-25 · [GitHub](https://github.com/UpayanGhosh/Synapse-OSS) · 个人维护

**自托管的个人 AI 助手：跨渠道对话并带持久记忆**

面向个人用户的自托管 AI 助手：将 WhatsApp、Telegram、Discord、Slack、CLI 与浏览器统一为一个对话入口，消息经异步网关进入混合 RAG 记忆（FastEmbed/Gemini-embed 嵌入 + LanceDB ANN/FTS + FlashRank 重排），并由 SBS 八层行为画像每 50 条消息重建一次用户画像；敏感话题按隐私路由转发到本地 Ollama 模型。模型可切换（云或本地），当前单用户单实例、个人独立维护。提供 npm 全局命令、Docker 演示与源码三种安装路径。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 多渠道统一入口：WhatsApp/Telegram/Discord/Slack/CLI/浏览器
- 混合 RAG 记忆：LanceDB ANN+FTS 检索加 FlashRank 重排
- SBS 行为画像每 50 条消息从对话历史重建
- 隐私感知路由：敏感话题转发到本地 Ollama 模型，不出本机

## 适用场景

- 在多个聊天平台上拥有记忆连续的私人 AI 助手
- 让 AI 记住偏好与长期上下文，随时间更了解自己
- 敏感话题本地处理，自行托管掌控数据

## 场景标签

`AI 助手` `聊天机器人` · 领域:对话与助手

## 证据(README 行号)

> L10: > **Personal AI with continuity** — multi-channel, hybrid-RAG memory, evolving behavioral profile, privacy-aware ro
> L51: - **Multi-channel** — WhatsApp, Telegram, Discord, Slack, CLI, browser playground.
> L55: - **Privacy-aware routing** — sensitive topics route to a local Ollama "Vault" model; nothing about them leaves you

## 星数曲线

```mermaid
xychart-beta
    title "UpayanGhosh/Synapse-OSS 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-31 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 mid · 依据 README sha `9cc5bb8f07a4` · [字段定义](../../DATASET.md)*
