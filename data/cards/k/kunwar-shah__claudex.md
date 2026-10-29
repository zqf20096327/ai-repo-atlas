# kunwar-shah/claudex

⭐ 97 · JavaScript · MIT · 推送 2026-06-20 · [GitHub](https://github.com/kunwar-shah/claudex) · [官网](https://kunwar-shah.github.io/claudex/) · 个人维护

**Claude Code 对话历史查看器与持久记忆 MCP 服务器**

面向开发者、QA 与研究者的全栈 Web 应用：自动扫描 ~/.claude/projects 目录发现 Claude Code 会话，用 SQLite FTS5 提供全文检索（支持项目/会话/角色/日期过滤与高亮），带基于 Tremor 的分析仪表盘与 JSON/HTML/TXT 导出，兼容 V1/V2/V3 全部对话格式。1.3.0 起内置 MCP 服务器，提供 10 个工具与结构化记忆系统（优先级、置信度、TTL），使 Claude Code 跨会话保留编码知识。支持 npm 全局安装或源码运行，前端 3000 端口、后端 Fastify 3400 端口。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- SQLite FTS5 全文检索，支持多维度过滤与内容高亮
- MCP 服务器 10 个工具 + 结构化记忆（优先级/置信度/TTL）
- V1/V2/V3 全部 Claude Code 会话格式自动检测解析
- 对话分析仪表盘与 JSON/HTML/TXT 导出

## 适用场景

- 浏览和检索我在多个项目里的 Claude Code 会话历史
- 让 Claude Code 跨会话记住编码约定与架构决策
- 导出和分析会话数据用于回顾或研究

## 场景标签

`Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L19:  Claudex — browse, search, and give Claude Code persistent memory. SQLite FTS5 full-text search across all sessions
> L71: - **MCP Server**: Give Claude Code persistent memory — conventions, architecture, decisions, and error patterns sur
> L73: - **Auto Project Discovery**: Automatically scans `~/.claude/projects` directory to discover all conversations acro

## 星数曲线

```mermaid
xychart-beta
    title "kunwar-shah/claudex 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 96 --> 98
    line [97, 97]
```

2026-10-18 97 → 2026-10-29 97（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 mid · 依据 README sha `096380b69718` · [字段定义](../../DATASET.md)*
