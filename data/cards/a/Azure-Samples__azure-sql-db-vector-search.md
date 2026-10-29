# Azure-Samples/azure-sql-db-vector-search

⭐ 99 · Jupyter Notebook · MIT · 推送 2026-09-27 · [GitHub](https://github.com/Azure-Samples/azure-sql-db-vector-search) · [官网](https://learn.microsoft.com/en-us/sql/sql-server/artificial-intelligence-intelligent-applications) · 组织维护

**Azure SQL/SQL Server 原生向量搜索的官方示例集合**

Azure-Samples 官方仓库，演示 Azure SQL DB 与 SQL Server 2025 的原生向量支持：用 T-SQL 生成 OpenAI 嵌入、精确与近似向量搜索（DiskANN VECTOR_SEARCH）、全文+余弦相似度混合搜索、语义重排、RAG，以及 SqlClient/.NET、EF Core、Dapper、Semantic Kernel 集成示例。前提条件为 Azure 订阅、Azure SQL 或 SQL Server 2025、Azure OpenAI 资源；DiskANN 示例需 SQL Server 2025 或 Azure SQL。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- T-SQL 内直接获取 OpenAI 嵌入的示例
- DiskANN 近似最近邻搜索（VECTOR_SEARCH）示例
- BM25 + 余弦相似度混合搜索与 RRF 融合
- SqlClient/EF Core/Dapper/Semantic Kernel 集成示例

## 适用场景

- 在 Azure SQL 中实现语义搜索与 RAG
- 评估向量数据库功能在 SQL Server 2025 上的用法
- .NET 应用中接入原生向量查询

## 场景标签

`语义搜索` `RAG` · 领域:知识与检索

## 证据(README 行号)

> L3: This repo hosts samples meant to help use the new **Native Vector Support in Azure SQL DB** feature. We illustrate k
> L35: Learn how to get embeddings from OpenAI directly from Azure SQL using the sample available the Embeddings/T-SQL fol
> L60: The RAG pattern is a powerful way to generate text using a pre-trained language model and a retrieval mechanism. Th

## 星数曲线

```mermaid
xychart-beta
    title "Azure-Samples/azure-sql-db-vector-search 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-29"]
    y-axis "stars" 97 --> 100
    line [98, 99, 99]
```

2026-10-18 98 → 2026-10-29 99（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `144a4c448eee` · [字段定义](../../DATASET.md)*
