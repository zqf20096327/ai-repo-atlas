# Aquiles-ai/Aquiles-RAG

⭐ 30 · Python · Apache-2.0 · 推送 2026-01-06 · [GitHub](https://github.com/Aquiles-ai/Aquiles-RAG) · [官网](https://aquiles-ai.vercel.app) · 个人维护

**自托管 RAG API 服务器：Redis/Qdrant/PostgreSQL 向量检索**

基于 FastAPI 的生产就绪 RAG API 服务器，支持 Redis HNSW、Qdrant、PostgreSQL pgvector 三种向量存储后端，切换后端无需改代码。提供交互式 CLI 配置向导、异步与同步的 Python 及 TypeScript SDK、内置 MCP Server 供 AI 助手接入，支持向量相似度搜索、元数据过滤、批量操作与可选重排序。要求 Python 3.9+ 及三种后端之一；PostgreSQL 需手动创建 pgvector 扩展和表，不执行自动迁移。

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

- 三种可切换向量后端（Redis HNSW / Qdrant / PostgreSQL pgvector）
- 内置 MCP Server，提供索引管理、文档摄取、语义搜索等工具
- Python 与 TypeScript SDK，含异步客户端
- CLI 配置向导与 Web UI Playground

## 适用场景

- 在自有基础设施上搭建 RAG 语义搜索服务
- 复用已有的 Redis/Qdrant/PostgreSQL 做向量检索
- 通过 MCP 让 AI 助手直接查询知识库

## 场景标签

`RAG` · 领域:知识与检索

## 证据(README 行号)

> L15: **Aquiles-RAG** is a production-ready RAG (Retrieval-Augmented Generation) API server that brings high-performance 
> L91: Aquiles-RAG includes a built-in Model Context Protocol server for seamless AI assistant integration.

## 星数曲线

```mermaid
xychart-beta
    title "Aquiles-ai/Aquiles-RAG 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 29 --> 31
    line [30, 30]
```

2026-10-18 30 → 2026-10-28 30（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 mid · 依据 README sha `f0ef560a104b` · [字段定义](../../DATASET.md)*
