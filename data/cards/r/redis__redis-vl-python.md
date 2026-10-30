# redis/redis-vl-python

⭐ 432 · Python · MIT · 推送 2026-10-29 · [GitHub](https://github.com/redis/redis-vl-python) · [官网](https://docs.redisvl.com) · 组织维护

**面向 AI 应用的 Redis Python 客户端与向量检索库**

Redis 官方维护的 Python 客户端库（Python>=3.10），在 Redis 之上提供索引 Schema 管理、向量/过滤/混合检索、语义缓存、嵌入缓存、LLM 对话记忆、语义路由等模块，并内置 MCP Server 将已有 Redis 索引暴露给 MCP 客户端（stdio/Streamable HTTP/SSE）。集成 8 家嵌入与重排提供商（OpenAI、Cohere、HuggingFace、Mistral 等）。另提供 rvl 命令行管理索引。需搭配 Redis 实例运行（支持 Redis Cloud/Docker/Enterprise/Sentinel/Azure Managed Redis）。

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

- 向量、范围、过滤、全文(BM25)与混合检索的查询类型体系
- SemanticCache/EmbeddingsCache/MessageHistory/SemanticRouter 扩展模块
- 内置 MCP Server，支持多索引 search/upsert 与只读模式
- rvl CLI 从终端管理索引的创建/删除/统计

## 适用场景

- 用 Redis 搭建 RAG 检索与向量搜索管道
- 为 LLM 应用加语义缓存以降低调用成本
- 为 AI agent 提供对话记忆与查询路由
- 通过 MCP 客户端检索已有 Redis 索引数据

## 场景标签

`向量数据库` `RAG` `Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L18: Redis Vector Library (RedisVL) is the production-ready Python client for AI applications built on Redis. **Lightnin
> L233: **RedisVL Extensions** provide production-ready modules implementing best practices and design patterns for workin
> L342: RedisVL includes an MCP server that lets MCP-compatible clients search or upsert data in one or more existing Redi

## 星数曲线

```mermaid
xychart-beta
    title "redis/redis-vl-python 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 431 --> 433
    line [432, 432]
```

2026-10-18 432 → 2026-10-30 432（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 mid · 依据 README sha `e4f4c1242ea4` · [字段定义](../../DATASET.md)*
