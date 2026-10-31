# moorcheh-ai/moorcheh-python-sdk

⭐ 52 · Python · MIT · 推送 2026-05-28 · [GitHub](https://github.com/moorcheh-ai/moorcheh-python-sdk) · [官网](https://www.moorcheh.ai/) · 组织维护

**面向 Moorcheh 语义搜索 API 的 Python SDK**

Moorcheh 官方 Python SDK，封装 Moorcheh 语义搜索 API v1：提供同步与异步客户端（MoorchehClient / AsyncMoorchehClient），支持命名空间管理、文本/文件/向量摄取、语义相似度查询与从命名空间生成有据回答（One-shot RAG）。面向构建 RAG、agentic memory 与语义分析的开发者；依赖 Moorcheh 托管平台 API key，也提供自托管 IaC 模板路线。通过 pip 安装，MIT 许可。LlamaIndex、LangChain、n8n、MCP 集成为对接生态。API 方法含文档与向量增删、查询与答案生成；eigenvectors、graph、UMAP 为路线图未实现项。

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

- 同步/异步双客户端，方法签名一致
- 统一 API 摄取原始文本、文件或向量
- similarity_search.query 语义查询与 answer.generate 有据回答生成
- 提供 LlamaIndex / LangChain / n8n / MCP 集成入口

## 适用场景

- 在 RAG 流程中用 Moorcheh 做向量存储与语义检索
- 为助手和长期运行的 agent 提供有状态记忆层
- 通过 SDK 自动化 Moorcheh 的数据摄取与查询工作流

## 场景标签

`RAG` `语义搜索` `向量数据库` `Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L7:  The Information-Theoretic Search Engine for RAG & Agentic Memory
> L27: Moorcheh is the universal memory layer for agentic AI, providing fast deterministic semantic search with zero‑ops s
> L68: ## API Client Methods

## 星数曲线

```mermaid
xychart-beta
    title "moorcheh-ai/moorcheh-python-sdk 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 51 --> 53
    line [52, 52]
```

2026-10-18 52 → 2026-10-31 52（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `4f726719c2bf` · [字段定义](../../DATASET.md)*
