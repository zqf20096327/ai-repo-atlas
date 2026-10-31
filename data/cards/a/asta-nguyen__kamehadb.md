# asta-nguyen/kamehadb

⭐ 14 · TypeScript · Apache-2.0 · 推送 2026-10-27 · [GitHub](https://github.com/asta-nguyen/kamehadb) · [官网](https://kamehadb.astalife.co) · 个人维护

**连接 10 种数据库的本地优先桌面 GUI，含 AI 对话与 MCP 服务**

基于 Wails（Go 内嵌后端 + React 19 前端）的跨平台数据库工作台，支持 PostgreSQL、MySQL、SQLite、MongoDB、Redis 等 10 种引擎的浏览、查询、图表与 ER 图。AI 功能包括读取真实 DDL 上下文的多供应商聊天（OpenAI/Ollama 本地与云端/DeepSeek/Gemini/9Router），生成 SQL 但不由聊天流程执行；另内置只读 MCP 服务器，供 Claude Code、Codex 等客户端经 bearer token 在 127.0.0.1 端点执行受限查询。元数据存本地 SQLite，无遥测。从源码用 pnpm 构建运行，无签名 macOS 构建需处理 Gatekeeper。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 单一 Go 二进制内嵌后端，本地 SQLite 存元数据、无遥测
- AI 聊天读取实际 DDL/索引/约束生成 SQL、Mongo 管道与 Redis 命令
- 只读 MCP 服务器（127.0.0.1 + bearer token），拒绝写语句与 $out/$merge
- Schema 快照时间线、diff 与自动生成迁移 DDL

## 适用场景

- 在一个桌面应用里同时管理多种 SQL/文档/缓存数据库
- 让 AI 基于真实 schema 生成并审阅 SQL，不自动执行
- 让 Claude Code 等 AI 客户端经 MCP 只读检查库结构
- 对比 schema 快照并生成迁移 DDL

## 场景标签

`数据分析` · 领域:效率与自动化

## 证据(README 行号)

> L7: **KamehaDB** is a local-first, cross-platform desktop database workspace that connects to PostgreSQL, MySQL, MariaDB
> L14: - **AI with real schema context** — multi-provider chat (OpenAI, Ollama local + cloud, 9Router, DeepSeek, Gemini) r
> L15: - **Read-only MCP server** — let Codex, Claude Code, Devin CLI, and OpenCode inspect schemas and run read-only SQL/

## 星数曲线

```mermaid
xychart-beta
    title "asta-nguyen/kamehadb 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `0566525e9e90` · [字段定义](../../DATASET.md)*
