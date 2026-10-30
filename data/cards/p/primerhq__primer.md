# primerhq/primer

⭐ 16 · Python · Apache-2.0 · 推送 2026-10-29 · [GitHub](https://github.com/primerhq/primer) · [官网](https://primerhq.github.io) · 组织维护

**自托管的小型上下文优化 agent 舰队编排平台**

面向自托管部署的 AI agent 编排平台：以小型本地开源权重模型加紧凑上下文为核心设定，提供有向循环 agent 图（Pregel 风格执行器、max_iterations 约束）、共享工作区、yielding 工具、语义工具检索（每个 agent 仅携带 search/call 两个元工具）与 MCP 服务端/客户端等原语。内置知识集合（RAG）、Slack/Telegram/Discord 通道、cron/webhook 触发器、人工审批门与 web 搜索。安装支持 pipx、Docker 镜像或源码，默认零配置 SQLite，生产可切 Postgres+pgvector。README 声明项目正处于 mid-revamp，v0.6.x 为最后稳定版，下一标签为 v2.0.0。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- Pregel 风格有向循环 agent 图，支持分支/扇出/汇合与条件路由
- 每个 agent 仅携带 search/call 两个元工具的语义工具检索
- 全能力经 MCP 暴露，可由 Claude、opencode 等 MCP 客户端驱动
- 触发器、人工审批门、park-and-resume 与 Slack/Telegram/Discord 通道内置

## 适用场景

- 自托管编排多个小模型 agent 完成分支与汇合的多步工作流
- 把 agent 接入 Slack/Telegram/Discord，通过消息发起与审批工作
- 用 MCP 客户端从外部驱动和运维整个 agent 平台

## 场景标签

`Agent 框架` `多智能体` · 领域:Agent 开发

## 证据(README 行号)

> L27: So instead of one giant agent with everything crammed into its prompt, Primer lets you orchestrate **fleets of smal
> L174: At runtime, requests arrive from many edges (REST/shell, MCP clients, messaging channels, triggers), become **sess

## 星数曲线

```mermaid
xychart-beta
    title "primerhq/primer 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-30 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `60541a0949cf` · [字段定义](../../DATASET.md)*
