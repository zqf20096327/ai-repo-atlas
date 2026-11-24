# qdrant/mcp-server-qdrant

⭐ 1,577 · Python · Apache-2.0 · 推送 2026-11-24 · [GitHub](https://github.com/qdrant/mcp-server-qdrant) · [官网](https://qdrant.tech) · 组织维护

**为 MCP 客户端提供 Qdrant 语义记忆存取的服务器**

Qdrant 官方的 Model Context Protocol 服务器实现，在 Qdrant 向量数据库之上提供语义记忆层：暴露 qdrant-store 与 qdrant-find 两个工具，供 LLM 应用存储和检索信息。通过环境变量配置 Qdrant URL/本地路径、默认集合、嵌入模型（目前仅支持 FastEmbed）、只读模式等；支持 stdio/SSE/streamable-http 传输，基于 FastMCP 构建。可经 uvx 直接运行、Docker 构建或 Smithery 安装，适配 Claude Desktop、Cursor、Windsurf、VS Code、Claude Code 等客户端。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 提供 qdrant-store / qdrant-find 两个 MCP 工具，实现信息的语义存取
- 支持 stdio、SSE、streamable-http 三种传输协议
- 嵌入默认使用 FastEmbed 的 all-MiniLM-L6-v2 模型，支持本地或远程 Qdrant
- 可定制工具描述，将服务器改造为代码语义搜索工具

## 适用场景

- 让 Claude Desktop / Cursor 等 MCP 客户端保存并检索长期记忆
- 为代码库搭建语义搜索：存储代码片段并用自然语言查询
- 团队通过 SSE 在远程/云环境中共享同一个 MCP 服务器

## 场景标签

`Agent 记忆` `语义搜索` `向量数据库` `编码 Agent` · 领域:Agent 开发

## 证据(README 行号)

> L10: This repository is an example of how to create a MCP server for Qdrant, a vector search engine.
> L14: An official Model Context Protocol server for keeping and retrieving memories in the Qdrant vector search engine.
> L15: It acts as a semantic memory layer on top of the Qdrant database.

## 星数曲线

```mermaid
xychart-beta
    title "qdrant/mcp-server-qdrant 星数(近 18 点)"
    x-axis ["2026-10-22", "2026-10-24", "2026-10-27", "2026-10-28", "2026-10-29", "2026-10-30", "2026-10-31", "2026-11-01", "2026-11-06", "2026-11-08", "2026-11-11", "2026-11-12", "2026-11-14", "2026-11-16", "2026-11-18", "2026-11-19", "2026-11-20", "2026-11-24"]
    y-axis "stars" 1550 --> 1577
    line [1552, 1553, 1554, 1556, 1558, 1560, 1561, 1562, 1553, 1565, 1567, 1568, 1570, 1571, 1572, 1573, 1575, 1575]
```

2026-10-22 1,552 → 2026-11-24 1,575（+23）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-23 · 置信度 high · 依据 README sha `cc493a4b51d9` · [字段定义](../../DATASET.md)*
