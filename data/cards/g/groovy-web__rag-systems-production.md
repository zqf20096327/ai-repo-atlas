# groovy-web/rag-systems-production

⭐ 16 · Apache-2.0 · 推送 2026-03-24 · [GitHub](https://github.com/groovy-web/rag-systems-production) · [官网](https://www.groovyweb.co) · 组织维护

**面向生产环境的企业级 RAG 系统实现模板**

由 Groovy Web 维护的生产级 RAG 系统代码库：提供多格式文档摄取（PDF/DOCX/TXT/Markdown）、Pinecone/Weaviate/ChromaDB/pgvector 向量库接入、语义/混合检索与重排，以及 LLM 提供商集成。生产特性含分布式处理与缓存、Prometheus/Grafana 监控、OpenTelemetry 追踪、API key 管理与限流。提供 Docker Compose 与 Kubernetes 部署方式，面向构建 AI 应用后端的开发者。注意 README 中 License 声明存在 MIT 与 Apache 2.0 前后不一致。

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

- 4 种向量库（Pinecone/Weaviate/ChromaDB/pgvector）与多提供商 embedding 接入
- 语义/混合检索与重排策略
- Prometheus 指标、Grafana 面板与 OpenTelemetry 分布式追踪
- Docker Compose 与 Kubernetes 部署配置

## 适用场景

- 搭建可监控、可扩展的生产级 RAG 服务
- 企业知识库问答系统的检索后端参考实现
- 按模板快速切换向量库与 LLM 提供商

## 场景标签

`RAG` · 领域:知识与检索

## 证据(README 行号)

> L10: This repository provides a complete, production-ready implementation of RAG systems for building AI-powered applica
> L16: - **Vector Stores**: Support for Pinecone, Weaviate, ChromaDB, and pgvector

## 星数曲线

```mermaid
xychart-beta
    title "groovy-web/rag-systems-production 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-30 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `bc29a8342828` · [字段定义](../../DATASET.md)*
