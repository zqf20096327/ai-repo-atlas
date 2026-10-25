# oracle/ai-optimizer

⭐ 102 · Python · UPL-1.0 · 推送 2026-10-24 · [GitHub](https://github.com/oracle/ai-optimizer) · [官网](https://www.oracle.com/database/ai-optimizer-toolkit/?source=:ex:tb:::::Githubrepo&SC=:ex:tb:::::Githubrepo&pcode=) · 组织维护

**面向开发者的 GenAI 实验工具：在 Oracle AI 数据库上做 RAG 与 NL2SQL**

Oracle 维护的 Agentic 优化与实验工具包：集成 Oracle AI Database Vector Search 与 SQLcl MCP，让开发者和数据科学家配置嵌入/聊天模型、切分并嵌入文档、从 OCI Object Storage 自动刷新向量库、调整系统提示词与 LLM 参数，并在自动生成或已有的 Q&A 数据集上运行 Giskard 测试。技术栈含 Python/Streamlit/FastAPI、LangChain/LangGraph/LiteLLM/MCP，支持多种模型提供方与本地运行时。可在裸机、容器或 Kubernetes 集群部署，也可经 IaC 部署到 OCI。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `viral` | UPL-1.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- RAG 与 NL2SQL 实验环境，集成 Oracle AI Database Vector Search 与 SQLcl MCP
- 配置嵌入/聊天模型、提示词工程与 LLM 参数实验
- Giskard v3 测试床：基于自动生成或已有 Q&A 数据集做评测
- 支持 OCI GenAI、OpenAI 兼容 API、Ollama、vLLM 等多种模型提供方与运行时

## 适用场景

- 在自有数据库上搭建并实验 RAG 问答系统
- 通过自然语言查询数据库（NL2SQL）
- 用 Q&A 数据集评测 LLM 配置与提示词方案

## 场景标签

`RAG` `数据分析` `提示工程` `模型评测` · 领域:Agent 开发

## 证据(README 行号)

> L9: The **Oracle AI Optimizer and Toolkit** (the **AI Optimizer**) provides a streamlined environment where developers a
> L14: - **AI orchestration:** LangChain, LangGraph, LiteLLM, AgentSpec/pyagentspec, and Model Context Protocol (MCP).
> L17: - **Model providers and runtimes:** OCI GenAI, OpenAI-compatible APIs, OpenAI, Cohere, Perplexity, Ollama, Hugging 

## 星数曲线

```mermaid
xychart-beta
    title "oracle/ai-optimizer 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 101 --> 103
    line [102, 102]
```

2026-10-18 102 → 2026-10-25 102（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `1151132e6411` · [字段定义](../../DATASET.md)*
