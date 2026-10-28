# awslabs/unified-kg-rag-on-aws

⭐ 37 · Python · Apache-2.0 · 推送 2026-10-27 · [GitHub](https://github.com/awslabs/unified-kg-rag-on-aws) · 组织维护 · 中文 README

**AWS 原生知识图谱 RAG 框架，统一 GraphRAG 与 LightRAG 两种检索方法**

将大规模多语文档语料摄取为知识图谱，存储于 Amazon Neptune 与 OpenSearch，通过 Amazon Bedrock 模型以多跳图遍历回答跨文档问题。框架在同一技术栈上重新实现 Microsoft GraphRAG（社区摘要）与 LightRAG（双级关键词）两种检索方法，可按查询选择策略而非按部署绑定。提供 BM25+向量+图遍历的三重混合检索、增量索引、多语言处理、提示调优与评估 CLI、可视化，以及可插拔的存储与模型后端。支持本地模式（嵌入式 SQLite 或容器，配 Ollama）、接入已有 AWS 资源、或部署内置 CDK 全套栈。定位为教育性参考框架，不建议未经加固直接用于生产。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- GraphRAG 与 LightRAG 两种检索方法共用摄取/索引/缓存/搜索栈，按查询选择策略
- BM25+向量+Neptune 图遍历三重混合检索，RRF 融合并用 Bedrock 模型重排
- 基于 doc-status 注册表的增量索引，仅重索引新增/变更文档
- 7 种检索策略（auto/simple/local/global/drift/mix/hybrid/naive）与提示调优、评估、可视化 CLI

## 适用场景

- 在 AWS 上对大规模文档语料做多跳知识图谱问答
- 同一部署内按查询类型切换 GraphRAG 或 LightRAG 检索方法
- 本地用 Ollama 做开发评估后再迁移到 Neptune/OpenSearch/Bedrock
- 对 RAG 语料做增量索引与检索质量评估

## 场景标签

`RAG` `知识图谱` · 领域:知识与检索

## 证据(README 行号)

> L10: An AWS-native knowledge graph RAG (Retrieval-Augmented Generation) framework that turns large, multilingual documen
> L16: - **Two methodologies on one AWS stack.** GraphRAG (community summaries) and LightRAG (dual-level keywords) share i

## 星数曲线

```mermaid
xychart-beta
    title "awslabs/unified-kg-rag-on-aws 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-27", "2026-10-28"]
    y-axis "stars" 35 --> 38
    line [36, 37, 37]
```

2026-10-18 36 → 2026-10-28 37（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `e5a09c1a334a` · [字段定义](../../DATASET.md)*
