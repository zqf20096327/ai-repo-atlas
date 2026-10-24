# mfmezger/conversational-agent-langchain

⭐ 256 · Python · MIT · 推送 2026-10-24 · [GitHub](https://github.com/mfmezger/conversational-agent-langchain) · 个人维护

**对话式 RAG Agent 的 FastAPI 后端：文档嵌入、语义检索与问答**

基于 FastAPI 的 REST 后端，结合 LangChain/LangGraph 与 Qdrant 向量数据库，提供文档嵌入、语义检索（含 BM25 混合搜索）、基于文档的问答与 LLM 文档处理；通过 LiteLLM 支持多种模型提供商（Cohere/Ollama/Google 等），并提供 OpenAI 兼容 API 子集（/v1/chat/completions 与 /v1/responses）。附带 Streamlit 前端、Phoenix 可观测性追踪、Cohere 与 FlashRank 两种重排序后端。以 Docker Compose 或 uv 源码方式运行，需配置 GEMINI 与 COHERE 的 API Key。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- OpenAI 兼容 API 子集（/v1/chat/completions、/v1/responses，支持 SSE 流式）
- Qdrant 向量库 + BM25 FastEmbed 混合语义检索
- 可选重排序后端：Cohere Rerank API / 本地 FlashRank
- Phoenix 追踪与 Streamlit 前端

## 适用场景

- 为私有文档库搭建语义检索与问答后端
- 以 OpenAI 兼容客户端接入自建 RAG 服务
- 观察和调试 RAG 管线的检索与生成过程

## 场景标签

`RAG` `文档问答` · 领域:知识与检索

## 证据(README 行号)

> L8: This is a Rest-Backend for a Conversational Agent, that allows you to embed Documents, search for them using Semanti
> L53: This project is a conversational rag agent that uses Google Gemini Large Language Models to generate responses to u

## 星数曲线

```mermaid
xychart-beta
    title "mfmezger/conversational-agent-langchain 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 255 --> 257
    line [256, 256]
```

2026-10-18 256 → 2026-10-24 256（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `c503df9df0d4` · [字段定义](../../DATASET.md)*
