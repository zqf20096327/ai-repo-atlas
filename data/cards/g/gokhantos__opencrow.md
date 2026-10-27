# gokhantos/opencrow

⭐ 24 · TypeScript · MIT · 推送 2026-07-26 · [GitHub](https://github.com/gokhantos/opencrow) · 个人维护

**自托管多 agent 平台：在 Telegram/WhatsApp/Web 运行专属 AI agent**

OpenCrow 是自托管的多 agent AI 平台，核心编排器以隔离子进程运行各子系统（agent、爬虫、cron、web），带崩溃恢复与状态调和。每个 agent 拥有独立 persona、模型、工具与记忆，基于 Claude Agent SDK 经 MCP 桥接驱动，内置 31 个专职子 agent、100+ 工具与 15 个自治爬虫（HackerNews、Reddit、X/Twitter 等），数据存入 PostgreSQL 并索引到 Qdrant 供混合检索。技术栈为 Bun、Hono、React，需自建部署。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Telegram/WhatsApp/Web 三渠道运行独立 persona 的 agent
- 31 个内置子 agent 与 planner→实现→审查的编排工作流
- 15 个自治爬虫覆盖 HackerNews/Reddit/X/App Store 等数据源，索引入 Qdrant
- 向量+全文混合检索的跨会话长期记忆与 cron 定时调度

## 适用场景

- 在 Telegram/WhatsApp 上运行自己的多角色 AI agent 群
- 定时自动抓取与研究多源数据并生成想法/摘要
- 通过 agent 自管理进程、部署代码与系统监控

## 场景标签

`多智能体` `Agent 框架` `网页抓取` `聊天机器人` · 领域:Agent 开发

## 证据(README 行号)

> L10: A self-hosted multi-agent AI platform that orchestrates specialized agents across Telegram, WhatsApp, and a web das
> L14: - **Run AI agents** on Telegram, WhatsApp, and web — each with its own persona, model, tools, and memory

## 星数曲线

```mermaid
xychart-beta
    title "gokhantos/opencrow 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 23 --> 25
    line [24, 24]
```

2026-10-18 24 → 2026-10-27 24（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 mid · 依据 README sha `55c39cb96679` · [字段定义](../../DATASET.md)*
