# langchain-ai/langchain-postgres

⭐ 282 · Python · MIT · 推送 2026-10-22 · [GitHub](https://github.com/langchain-ai/langchain-postgres) · 组织维护

**基于 Postgres 实现 LangChain 核心抽象的 Python 集成包**

langchain-ai 组织维护的集成库，用 Postgres 后端实现 LangChain 核心抽象：PGVectorStore 向量存储（支持混合检索、异步）、PostgresChatMessageHistory 聊天历史持久化，通过 PGEngine 建立连接。支持 asyncpg 与 psycopg3 两种驱动。面向使用 LangChain 构建 LLM 应用的开发者，以 pip 包分发，MIT 许可。v0.0.14+ 中 PGVector 类已弃用，需迁移到 PGVectorStore。README 另列出 Google Cloud 的 AlloyDB/Cloud SQL 对应集成包。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- PGVectorStore 向量存储，支持混合检索与异步接口
- PostgresChatMessageHistory 按 table_name + session_id 持久化聊天记录
- 支持 asyncpg 与 psycopg3 两种驱动
- 同步函数均有对应异步版本

## 适用场景

- 为 LangChain 应用提供 Postgres 向量存储做 RAG 检索
- 把聊天消息历史持久化到 Postgres 表
- 用混合检索（向量+关键词）提升检索覆盖

## 场景标签

`向量数据库` · 领域:知识与检索

## 证据(README 行号)

> L10: The `langchain-postgres` package implementations of core LangChain abstractions using `Postgres`.
> L26: ## Vectorstore

## 星数曲线

```mermaid
xychart-beta
    title "langchain-ai/langchain-postgres 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 281 --> 283
    line [282, 282]
```

2026-10-18 282 → 2026-10-24 282（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `8d0c12b7b80c` · [字段定义](../../DATASET.md)*
