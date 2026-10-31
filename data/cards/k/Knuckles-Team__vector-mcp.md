# Knuckles-Team/vector-mcp

⭐ 16 · Python · MIT · 推送 2026-10-30 · [GitHub](https://github.com/Knuckles-Team/vector-mcp) · 组织维护

**面向 AI agent 的向量数据库 MCP 服务器，支持多后端**

以 MCP 服务器形式向 AI agent 提供向量集合管理与检索两个工具，默认使用本地零依赖的 epistemic-graph 引擎，可选接入 PostgreSQL/pgvector、Qdrant、MongoDB 等后端（描述另提及 ChromaDB、Couchbase）。通过 Action-Routed 动态工具选择降低 token 开销，支持 CLI 参数、环境变量、HTTP 头与查询参数多种工具过滤通道，内置 LLM-free 的意图匹配层。凭据通过 secret:// 引用解析，README 不落盘任何端点或主机路径。支持 stdio、streamable-http、SSE 传输及 Docker/Podman 容器部署。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 两个 MCP 工具：vector_collection_management 与 vector_search
- 默认本地 epistemic-graph 引擎，可选 postgres/qdrant/mongodb 后端
- 运行时动态工具选择与可见性过滤（CLI/环境变量/HTTP 头/查询参数）
- 凭据经 secret:// 引用注入，README 不含端点与身份信息

## 适用场景

- 为 IDE 中的 AI agent 接入向量检索能力
- 在受治理环境下管理向量集合并执行搜索
- 以最小权限容器方式部署 MCP 向量服务

## 场景标签

`向量数据库` · 领域:知识与检索

## 证据(README 行号)

> L3: Action-routed MCP and agent interfaces for governed vector collection management and retrieval.
> L9: - MCP tools: `vector_collection_management` and `vector_search`
> L163: |`DATABASE_TYPE`|`epistemic_graph`|Backend used when db_type is unspecified. Default is the native epistemic-graph

## 星数曲线

```mermaid
xychart-beta
    title "Knuckles-Team/vector-mcp 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-31"]
    y-axis "stars" 14 --> 17
    line [15, 16, 16]
```

2026-10-18 15 → 2026-10-31 16（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `bda40a91fa89` · [字段定义](../../DATASET.md)*
