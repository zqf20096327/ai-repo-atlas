# kaivyy/kabot

⭐ 20 · Python · MIT · 推送 2026-03-17 · [GitHub](https://github.com/kaivyy/kabot) · [官网](https://kaivyy.github.io/kabot/) · 个人维护

**运行在本地硬件上的个人自主 AI 助手，带持久记忆**

面向单用户的个人 AI 助手，以 pip 包安装并在本地启动 gateway 运行。核心机制包括：Hybrid Memory 架构（SQLite 关系库 + ChromaDB 向量库 + BM25 词法检索 + 重排与 token 限额过滤）、Brainstorm→Plan→Execute 的执行流程、Python 原生 MCP 运行时、可跨重启持久化的后台子代理，以及 boros/hemat 两种 token 模式。接入层支持 Telegram、Discord、Slack、WhatsApp（Beta，经本地桥接，需 Node.js）与 CLI；通过 setup wizard 选择 AI 提供商并配置 API key，支持 OpenRouter 等多提供商路由与回退链。提供 Web 仪表盘（SSR+HTMX）与 JSON API。

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

- SQLite + ChromaDB + BM25 + 重排的混合记忆架构，状态跨重启持久
- Python 原生 MCP 运行时，按会话挂载真实 MCP 服务器
- 持久化后台子代理（状态落盘，重启后可继续查询）
- Telegram/Discord/Slack/WhatsApp/CLI 多渠道接入，含 Web 仪表盘

## 适用场景

- 在本地跑一个长期记住上下文的个人 AI 助手
- 通过 Telegram/Discord 等聊天渠道随时调用自主代理执行任务
- 需要长期项目记忆与工具调用能力的单用户运维/编码助手

## 场景标签

`AI 助手` `聊天机器人` · 领域:对话与助手

## 证据(README 行号)

> L13: > **Kabot** is a _personal AI assistant_ engineered for **resilience**, **complex task execution**, and **long-term
> L105: - choose your AI provider,
> L272: * **Telegram**: DM your bot.

## 星数曲线

```mermaid
xychart-beta
    title "kaivyy/kabot 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 19 --> 21
    line [20, 20]
```

2026-10-18 20 → 2026-10-31 20（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 mid · 依据 README sha `c7414f99883f` · [字段定义](../../DATASET.md)*
