# Azure-Samples/SQL-AI-samples

⭐ 331 · HTML · MIT · 推送 2026-06-03 · [GitHub](https://github.com/Azure-Samples/SQL-AI-samples) · [官网](https://aka.ms/sql-ai) · 组织维护

**Azure SQL 数据库与 AI 结合的官方示例集合**

微软 Azure-Samples 维护的示例仓库，演示如何在 Azure SQL Database 数据之上构建 AI 应用：包括认知搜索集成向量化、Prompt Flow 端到端流程、从数据库调用 Azure OpenAI 生成向量嵌入并做相似度检索、Vanna.AI 生成 SQL、T-SQL 实现 RAG、内容安全与 PII 检测脚本、LangChain NL2SQL agent、MSSQL MCP Server、FAISS 相似搜索、IVFFlat 向量索引，以及两个动手实验（workshop）。每个示例在各自目录内附 README 或 notebook 说明，无统一安装入口。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 覆盖向量嵌入、RAG、NL2SQL、内容审核、MCP Server 等 20 余个示例
- 提供 T-SQL 层面直接调用 OpenAI 的 RAG 与内容安全脚本
- 含 LangChain NL2SQL agent 与 MSSQL MCP Server（C# SDK）
- 附两个动手实验：嵌入 Lab 与 Fabric GraphQL RAG

## 适用场景

- 参考示例在自有 Azure SQL 数据上构建 RAG 问答或推荐系统
- 学习从数据库层直接调用 OpenAI 嵌入与相似度计算
- 为 MSSQL 数据库搭建 MCP Server 或 NL2SQL agent

## 场景标签

`RAG` `数据分析` · 领域:效率与自动化

## 证据(README 行号)

> L5: This repo hosts samples meant to help design AI applications built on data from an Azure SQL Database. We illustrate
> L135: See the description in each sample for instructions (projects will have either a README file or instructions in th

## 星数曲线

```mermaid
xychart-beta
    title "Azure-Samples/SQL-AI-samples 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 330 --> 332
    line [331, 331]
```

2026-10-18 331 → 2026-10-26 331（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `a9fd50b609e6` · [字段定义](../../DATASET.md)*
