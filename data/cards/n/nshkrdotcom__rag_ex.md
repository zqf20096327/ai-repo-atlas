# nshkrdotcom/rag_ex

⭐ 13 · Elixir · MIT · 推送 2026-04-09 · [GitHub](https://github.com/nshkrdotcom/rag_ex) · 组织维护

**Elixir RAG 构建库：多 LLM 路由、GraphRAG 与工具 Agent**

bitcrowd/rag 的分支，为 Elixir 开发者提供构建 RAG 系统的库：支持 Gemini、Claude、Codex（OpenAI 兼容）与 Ollama 多提供商接入，路由策略含 fallback、round-robin 与 specialist；提供可插拔的 Retriever（语义/全文/混合/图）、VectorStore（pgvector、RocksDB 三元组库）与 Reranker 行为，含 7 种分块策略、可组合 Pipeline（并行执行、ETS 缓存、重试、telemetry）、GraphRAG（实体抽取、标签传播社区发现）及带会话记忆的工具型 Agent 框架。本库不含 Ecto Repo，向量库功能需宿主应用自带 Repo 并跑迁移；LLM 功能无需数据库。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 多提供商路由：fallback / round-robin / specialist 策略
- 可插拔 Retriever / VectorStore / Reranker 行为与可组合 Pipeline
- GraphRAG：LLM 实体抽取、社区发现、局部/全局/混合图检索
- 7 种分块策略（字符/句子/段落/递归/语义/格式感知等）

## 适用场景

- 在 Elixir 应用中接入多个 LLM 提供商并做故障切换路由
- 构建带知识图谱的 GraphRAG 检索流程
- 搭建带工具调用与会话记忆的 Agent

## 场景标签

`RAG` `知识图谱` `Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L11: A library to build RAG (Retrieval Augmented Generation) systems in Elixir with multi-LLM support and agentic capabi
> L16: - **Multi-LLM Provider Support**: Gemini, Claude, Codex (OpenAI-compatible), and Ollama

## 星数曲线

```mermaid
xychart-beta
    title "nshkrdotcom/rag_ex 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 12 --> 14
    line [13, 13]
```

2026-10-18 13 → 2026-10-31 13（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `254d3c717e19` · [字段定义](../../DATASET.md)*
