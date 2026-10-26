# rineshpk/dotnet-rag-pgvector

⭐ 25 · C# · MIT · 推送 2026-03-22 · [GitHub](https://github.com/rineshpk/dotnet-rag-pgvector) · 个人维护

**.NET RAG 语义搜索参考实现：pgvector+Aspire+可插拔 LLM**

演示如何在 .NET 10 中构建语义搜索 + RAG 管线的参考项目：用 PostgreSQL pgvector 存储向量并以余弦相似度检索，通过 Ollama 或 OpenAI 生成嵌入与回答，经 POST /ask 端点对外提供问答。采用 Clean Architecture（Domain/Application/Infrastructure 分层），.NET Aspire 编排 Postgres、Ollama 与 API 容器，切换 LLM 提供商仅需改配置无需改代码。启动时自动用架构模式数据集做种子并向量化。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- pgvector 向量列存储与余弦相似度检索
- 可插拔 LLM 提供商（Ollama/OpenAI），配置切换无需改代码
- .NET Aspire 一键编排 Postgres + Ollama + API
- Clean Architecture 分层与 Scalar API 测试界面

## 适用场景

- 学习在 .NET 中实现 RAG 与 pgvector 语义搜索的完整流程
- 以此为模板搭建可切换本地/云端 LLM 的问答服务
- 体验 Aspire 编排多容器的 .NET AI 应用开发方式

## 场景标签

`RAG` `语义搜索` · 领域:知识与检索

## 证据(README 行号)

> L3: A production-style **Retrieval-Augmented Generation (RAG)** implementation in .NET using PostgreSQL `pgvector`, .NET
> L10: * LLM-based answer generation (Ollama / OpenAI)
> L36: * ✅ Retrieval-Augmented Generation (RAG)

## 星数曲线

```mermaid
xychart-beta
    title "rineshpk/dotnet-rag-pgvector 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 24 --> 26
    line [25, 25]
```

2026-10-18 25 → 2026-10-26 25（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `0ba5e76d95b9` · [字段定义](../../DATASET.md)*
