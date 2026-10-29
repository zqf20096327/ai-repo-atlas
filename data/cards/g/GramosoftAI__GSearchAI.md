# GramosoftAI/GSearchAI

⭐ 27 · TypeScript · 推送 2026-10-28 · [GitHub](https://github.com/GramosoftAI/GSearchAI) · [官网](https://gsearchai.com/) · 组织维护

**自托管企业 AI 搜索与 Graph RAG 平台，面向多租户场景**

MIT 许可的开源后端框架，把 PDF、Excel、网页等非结构化数据接入 Neo4j + pgvector 混合检索层，通过 Active Ontology 约束三元组抽取，提供多跳图推理、可归因检索、上下文 Token 预算与反馈加权，并用 PostgreSQL RLS 与 Neo4j 租户约束实现多租户隔离。面向企业架构师、AI/ML 开发者与 MSP/ISV。README 明示部分智能层（生产级嵌入、生成式 LLM 回答、LLM 级实体抽取）为脚手架状态、仍在路线图上。通过 Docker Compose 部署，支持 RDF/OWL/SKOS 本体加载。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | — |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- Neo4j 图遍历 + pgvector 向量检索的混合检索与多跳推理
- PostgreSQL RLS 与 Neo4j 租户约束实现多租户隔离
- 基于本体蓝图的三元组抽取与逐 chunk 归因的可解释检索
- rdflib 集成，支持 OWL/SKOS 标准本体直接加载入 Neo4j

## 适用场景

- 在企业内网把分散文档转为带权限隔离的 AI 搜索知识层
- 为多客户共部署的平台（MSP/ISV）提供租户级知识隔离
- 需要可归因、可解释检索结果而非纯向量匹配的问答场景

## 场景标签

`知识图谱` `RAG` `语义搜索` · 领域:知识与检索

## 证据(README 行号)

> L15: > **GRAG is an open-source enterprise AI search and Graph RAG platform.** It connects unstructured company data — P
> L23: GRAG (**Gr**aph **R**etrieval-**A**ugmented **G**eneration) is a state-of-the-art backend framework for **enterpris
> L25: Vanilla RAG pipelines hallucinate relationships and stumble on multi-hop queries; standard graph databases lack sem

## 星数曲线

```mermaid
xychart-beta
    title "GramosoftAI/GSearchAI 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 26 --> 28
    line [27, 27]
```

2026-10-18 27 → 2026-10-29 27（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `533567ebb5a6` · [字段定义](../../DATASET.md)*
