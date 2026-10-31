# SAP/langchain-integration-for-sap-hana-cloud

⭐ 19 · Python · Apache-2.0 · 推送 2026-08-25 · [GitHub](https://github.com/SAP/langchain-integration-for-sap-hana-cloud) · 组织维护

**将 LangChain 接入 SAP HANA Cloud 的向量与知识图谱集成包**

SAP 维护的 LangChain 集成包（langchain-hana），使 LLM 应用使用 SAP HANA Cloud 数据库的向量检索、知识图谱等库内能力。提供 HanaDB 向量存储（支持任意 LangChain Embeddings，含 HanaInternalEmbeddings 内置嵌入函数）、HanaTranslator 自查询检索器、HanaRdfGraph 知识图谱访问、SPARQL 问答链与可迭代生成执行 SPARQL 查询并自我纠错的 Agent。要求 Python 3.10+ 与运行中的 SAP HANA Cloud 实例，pip 安装。当前主线为 LangChain 0.3.x 之后版本，0.3.x 兼容版在 0.3.x 分支维护。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- HanaDB 向量存储接入 SAP HANA Cloud Vector Engine
- HanaInternalEmbeddings 使用数据库内置 VECTOR_EMBEDDING() 函数
- HanaRdfGraph 知识图谱访问与 SparqlQAChain 问答链
- HanaSparqlQAAgent 迭代生成执行 SPARQL 查询并自我纠错

## 适用场景

- 在 LangChain 应用中使用 SAP HANA Cloud 的向量检索构建 RAG
- 基于 SAP HANA 知识图谱做 SPARQL 问答
- 企业已有 SAP HANA Cloud 数据库时统一存储向量与业务数据

## 场景标签

`RAG` `知识图谱` · 领域:知识与检索

## 证据(README 行号)

> L16: Integrates LangChain with SAP HANA Cloud to make use of vector search, knowledge graph, and further in-database cap
> L30: pip install -U langchain-hana

## 星数曲线

```mermaid
xychart-beta
    title "SAP/langchain-integration-for-sap-hana-cloud 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 18 --> 20
    line [19, 19]
```

2026-10-18 19 → 2026-10-31 19（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `144e203d7e52` · [字段定义](../../DATASET.md)*
