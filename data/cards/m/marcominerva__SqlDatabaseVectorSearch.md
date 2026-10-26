# marcominerva/SqlDatabaseVectorSearch

⭐ 145 · C# · MIT · 推送 2026-10-07 · [GitHub](https://github.com/marcominerva/SqlDatabaseVectorSearch) · 个人维护

**基于 Azure SQL VECTOR 类型的 RAG 与向量搜索示例应用**

Blazor Web App 与 Minimal API 示例：加载 PDF/DOCX/TXT/MD 文档，生成嵌入并以原生 VECTOR 类型存入 Azure SQL Database 或 SQL Server 2025，无需外部向量库。嵌入与对话由 Microsoft Agent Framework 编排：文档导入走工作流，追问改写与 RAG 问答由 agent 完成；支持流式回答、token 用量展示与 Markdown 内嵌来源引用。面向 .NET 10 开发者，需 Azure OpenAI 密钥；VECTOR 列上限 1998。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 原生 VECTOR 类型存储嵌入，无需外部向量存储
- Microsoft Agent Framework 编排嵌入工作流、改写 agent 与 RAG agent
- 支持 SSE 流式回答、token 用量与 Markdown 来源引用
- 同时提供 Blazor 界面与 Minimal API 两种使用方式

## 适用场景

- 在 Azure SQL/SQL Server 2025 上直接搭建文档问答
- 通过 API 导入文档并做语义搜索与 RAG 问答
- 参考 .NET + Semantic Kernel/Agent Framework 的 RAG 实现方式

## 场景标签

`文档问答` `RAG` `语义搜索` · 领域:知识与检索

## 证据(README 行号)

> L7: A Blazor Web App and Minimal API for performing RAG (Retrieval Augmented Generation) and vector search using the nat
> L15: - Perform semantic search and RAG using Azure OpenAI and Microsoft Agent Framework agents
> L18: The native `VECTOR` type is available in both Azure SQL Database and SQL Server 2025, so no external vector store i

## 星数曲线

```mermaid
xychart-beta
    title "marcominerva/SqlDatabaseVectorSearch 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-26"]
    y-axis "stars" 143 --> 146
    line [144, 145, 145]
```

2026-10-18 144 → 2026-10-26 145（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `6b7909b43361` · [字段定义](../../DATASET.md)*
