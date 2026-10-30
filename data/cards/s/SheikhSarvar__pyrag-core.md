# SheikhSarvar/pyrag-core

⭐ 20 · Python · MIT · 推送 2026-10-24 · [GitHub](https://github.com/SheikhSarvar/pyrag-core) · 个人维护

**生产级 RAG 平台：FastAPI API 与可插拔向量存储**

开源的检索增强生成（RAG）平台，以 Python 为主并采用 API 驱动方式。技术栈包含 FastAPI + Pydantic v2 的 API 层、LangGraph + LangChain 的 Agent 层、Celery + Redis 队列、PostgreSQL 数据库、默认 Qdrant 的可插拔向量层、MinIO 存储与 Langfuse 可观测性。向量存储支持 Qdrant/Weaviate/Milvus/pgvector/Elasticsearch，LLM 提供 OpenAI/Anthropic/Gemini/OpenRouter/Ollama/vLLM 多家接入。通过 git clone 与 docker compose 安装运行，另提供 Streamlit 开发者 UI。面向需要搭建 RAG 服务的开发者。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- LangGraph 原生 Agent 层与 FastAPI API 层
- 5 种可插拔向量存储（Qdrant 默认）
- 6 家 LLM 提供商接入（含 Ollama/vLLM 本地运行时）
- Docker compose 单文件部署与 Streamlit 开发者 UI

## 适用场景

- 搭建带 API 的检索增强生成服务
- 需要可插拔切换向量数据库与 LLM 提供商的 RAG 项目
- 本地用 Docker 快速启动并调试文档解析、切块与索引流水线

## 场景标签

`RAG` `Agent 框架` `文档解析` · 领域:Agent 开发

## 证据(README 行号)

> L3: > Open-source, production-ready Retrieval-Augmented Generation platform. Python-first. API-driven. LangGraph-native.
> L10: |Agent|LangGraph + LangChain|
> L13: |Vector|Qdrant (pluggable)|

## 星数曲线

```mermaid
xychart-beta
    title "SheikhSarvar/pyrag-core 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-30"]
    y-axis "stars" 18 --> 21
    line [19, 20, 20]
```

2026-10-18 19 → 2026-10-30 20（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `713fc9af78ba` · [字段定义](../../DATASET.md)*
