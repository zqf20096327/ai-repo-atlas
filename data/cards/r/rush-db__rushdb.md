# rush-db/rushdb

⭐ 325 · TypeScript · 推送 2026-10-13 · [GitHub](https://github.com/rush-db/rushdb) · [官网](https://rushdb.com) · 组织维护 · 中文 README

**面向 AI agent 的图+向量数据库与记忆层**

基于 Neo4j 构建的数据库服务，定位为 AI agent 与应用的记忆层：写入任意 JSON 后自动推断类型、标签与关系，属性提升为图节点（LMPG 模型），无需预设计 schema 或迁移。支持图遍历、语义向量检索（服务端自动嵌入）、聚合分组与 schema 自省，组合在同一查询 API 中。提供 JavaScript/Python SDK、REST API 与 MCP server，可接入 Claude Desktop、Cursor 等 MCP 客户端。支持托管云或 Docker 自托管（需 Neo4j 2026.01.4+ 与 APOC 插件）。README 明确列出不适用场景：极高写入吞吐、纯键值存储、强关系型 schema 需求。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 零 schema：JSON 写入自动推断标签、类型与关系
- 图遍历、语义检索与聚合组合在单一查询中
- 内置 MCP server 与可安装的 Agent Skills 包
- 服务端自动嵌入与 ACID 事务（Neo4j 底层）

## 适用场景

- 为 AI agent 提供持久化、可自省的结构化记忆
- 带关系遍历的 RAG 上下文检索
- 无 schema 约束的快速应用后端数据存储

## 场景标签

`向量数据库` `Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L5: ### The memory layer for AI agents and apps.
> L124: RushDB ships an MCP server. Your agent gets persistent, structured memory — out of the box.
> L143: |**ACID transactions**|Concurrent agents don't corrupt shared memory. Neo4j under the hood|

## 星数曲线

```mermaid
xychart-beta
    title "rush-db/rushdb 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 324 --> 326
    line [325, 325]
```

2026-10-18 325 → 2026-10-24 325（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `8d93bb01ddb4` · [字段定义](../../DATASET.md)*
