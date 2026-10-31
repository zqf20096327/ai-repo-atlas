# Hexecu/mcp-neuralmemory

⭐ 16 · Python · MIT · 推送 2026-09-04 · [GitHub](https://github.com/Hexecu/mcp-neuralmemory) · [官网](https://pypi.org/project/kg-mcp/) · 个人维护

**为 AI 编程助手提供本地持久知识图谱记忆的 MCP 记忆服务器**

本地优先的个人认知记忆助手与"第二大脑"：将用户选择共享的桌面上下文转化为可搜索的时序知识图谱，锚定承诺、决策与会议记录，并通过原生 MCP 服务器（stdio）把这些上下文暴露给 Claude Desktop、Cursor 等编码代理。提供双轨架构：普通用户可用零依赖的 macOS DMG 安装包（数据存本地 SQLite），开发者可用 Docker Compose + Neo4j 5.26 全栈。内置 PrivacyShield 脱敏（信用卡/API key 掩码）、Ebbinghaus 遗忘曲线回放、定期修剪低级事件并生成每日简报的 Dream Mode。提供 recall_decisions 等多个 MCP 工具供代理调用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 原生 MCP 服务器（stdio），提供 recall_decisions / recall_commitments / search 等工具
- 时序知识图谱：主题聚类、时间线流（5 条语义高度泳道）、带 Ebbinghaus 衰减的时间旅行回放
- PrivacyShield 内存脱敏：自动掩码信用卡、IBAN、API key，忽略密码库
- 双轨安装：零依赖 macOS DMG 安装包或 Docker Compose + Neo4j 开发栈

## 适用场景

- 让 Claude Desktop / Cursor 等编码代理回忆过去的决策、未完成承诺和会议要点
- 把桌面上下文组织为本地持久知识图谱并混合搜索
- 每天从记忆图谱生成执行摘要简报

## 场景标签

`Agent 记忆` `知识图谱` · 领域:Agent 开发

## 证据(README 行号)

> L10: **Neural Memory** is a local-first personal cognitive memory assistant and second brain. It turns the desktop conte
> L60: - 🤖 **Agent-Ready Memory (MCP)**: Native Model Context Protocol server over `stdio` lets Claude Desktop, Cursor, An
> L86: ### Available MCP Tools for Agents:

## 星数曲线

```mermaid
xychart-beta
    title "Hexecu/mcp-neuralmemory 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-31 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `719bbc37128f` · [字段定义](../../DATASET.md)*
