# hive-agi/hive-mcp

⭐ 29 · Clojure · NOASSERTION · 推送 2026-10-26 · [GitHub](https://github.com/hive-agi/hive-mcp) · [官网](https://hive-mcp.com) · 组织维护

**带持久记忆与多 Agent 协调的 Clojure MCP server**

面向 hive-framework 开发的 MCP server，定位为 addon host 兼 agent harness：核心提供跨会话持久记忆（语义搜索、TTL 衰减、项目作用域）、知识图谱（结构化边）、ling 子 Agent 生成与 hivemind 协调、kanban 任务管理、workflow 生产带等约 20 个工具根。通过 catchup/wrap 两个会话仪式在 MCP 客户端（如 Claude Code）间延续上下文。采用 IAddon 插件架构，CLOSED for modification、OPEN for extension；后端为 JVM 进程（nREPL 7910），客户端经 bb-mcp（需 Babashka）接入。AGPL-3.0 许可，含 Chroma/Emacs 等可选组件与部分待发布 addon。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `viral` | NOASSERTION |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 跨会话持久记忆：语义搜索、TTL 衰减、项目作用域分层检索（HCR）
- 知识图谱结构化边 + catchup/wrap 会话延续仪式
- 多 Agent 协调：ling 生成、文件声明、hivemind 通信、workflow FSM 生产带
- IAddon 插件架构，新 addon 工具根自动注册为顶层工具

## 适用场景

- 让 Claude Code 等 MCP 客户端在跨会话间记住项目约定与决策
- 编排多个子 Agent 协同完成开发任务并管理看板
- 为 Clojure 项目接入 nREPL/LSP/Kondo 代码智能工具

## 场景标签

`多智能体` `知识图谱` `语义搜索` `Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L205: hive-mcp is a **host**: a runtime that other things mount into. It is not a library you
> L217: In one sentence: **hive-mcp is an addon host that doubles as an agent harness.** Your MCP
> L224: Core owns protocols, registries, orchestrators, the server, memory CRUD, KG edges, swarm

## 星数曲线

```mermaid
xychart-beta
    title "hive-agi/hive-mcp 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 28 --> 30
    line [29, 29]
```

2026-10-18 29 → 2026-10-28 29（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `6503a5b0372f` · [字段定义](../../DATASET.md)*
