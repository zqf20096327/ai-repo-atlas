# pgEdge/pgedge-vectorizer

⭐ 41 · PLpgSQL · NOASSERTION · 推送 2026-10-29 · [GitHub](https://github.com/pgEdge/pgedge-vectorizer) · [官网](https://docs.pgedge.com/pgedge-vectorizer/) · 组织维护

**给开发者的 PostgreSQL 扩展：自动分块并生成向量嵌入**

PostgreSQL 扩展，通过触发器与后台 worker 对已有表的文本列做异步分块和向量嵌入生成，提供 enable_vectorization 等 SQL 接口。支持 OpenAI、Voyage AI、Ollama、Gemini 四种嵌入提供方，Ollama 本地运行无需 API key；可覆盖 api_url 接入 OpenAI 兼容本地推理服务。支持 BM25 稀疏向量与 RRF 融合的混合搜索，含队列监控视图、重试与自动清理。需 PostgreSQL 14+、pgvector 与 libcurl 开发文件，从源码编译安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 后台 worker 异步分块与嵌入生成，不阻塞应用
- 支持 OpenAI/Voyage/Ollama/Gemini 四种嵌入提供方
- BM25 稀疏向量 + RRF 混合搜索
- 队列监控视图与指数退避自动重试

## 适用场景

- 为已有业务表开启文本列的自动向量化
- 在 PostgreSQL 内构建稠密+BM25 混合检索
- 用本地 Ollama 生成嵌入，避免外部 API key

## 场景标签

`向量数据库` `语义搜索` · 领域:知识与检索

## 证据(README 行号)

> L7: A PostgreSQL extension for asynchronous text chunking and vector embedding generation.
> L11: pgEdge Vectorizer automatically chunks text content and generates vector embeddings using background workers. It su

## 星数曲线

```mermaid
xychart-beta
    title "pgEdge/pgedge-vectorizer 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 40 --> 42
    line [41, 41]
```

2026-10-18 41 → 2026-10-31 41（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `64ec3e9d3a32` · [字段定义](../../DATASET.md)*
