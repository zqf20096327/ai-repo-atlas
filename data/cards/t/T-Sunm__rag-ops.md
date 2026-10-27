# T-Sunm/rag-ops

⭐ 74 · Python · 推送 2026-09-29 · [GitHub](https://github.com/T-Sunm/rag-ops) · 个人维护

**面向开发者的端到端 RAG 聊天机器人系统，覆盖摄取到防护全链路**

基于 LangChain 实现的完整 RAG 聊天机器人系统，按 LLMOps 实践组织为多个层次：FastAPI 的阻塞与流式（SSE/WebSocket）API 层、基于 Airflow/MinIO 的数据摄取与向量化管道（存入 ChromaDB）、可切换推理后端（LM Studio/Groq Cloud/vLLM）、Langfuse 可观测性、Redis 确定性缓存与语义缓存、内容过滤与 PII 防护（Guardrails）、路由与网关层。面向开发者、MLOps 工程师与研究人员学习或部署生产级 RAG 系统。需 Python 3.10+、Docker/Conda，通过源码 clone 并用 pip 安装依赖运行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 分层模块化架构：API/摄取/推理/可观测/缓存/防护/路由/网关
- 推理层支持 LM Studio、Groq Cloud、vLLM 之间切换（--provider 启动参数）
- Langfuse 集成：prompt 追踪、评估、成本追踪，本地 Docker 自托管
- Airflow DAG 编排文档加载→分块→嵌入→ChromaDB 存储

## 适用场景

- 学习并搭建覆盖摄取到防护全流程的生产级 RAG 系统
- 在本地用 Docker 部署带可观测性与缓存的聊天机器人 API
- 对比切换不同推理后端（本地 LM Studio 与云端 Groq/vLLM）

## 场景标签

`RAG` `MLOps` · 领域:知识与检索

## 证据(README 行号)

> L1: # End-to-End RAG Chatbot System with Langchain: From Ingestion to Guardrails
> L4: This project implements a complete Retrieval-Augmented Generation (RAG) chatbot system using Langchain and modern LL

## 星数曲线

```mermaid
xychart-beta
    title "T-Sunm/rag-ops 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-24", "2026-10-27"]
    y-axis "stars" 72 --> 75
    line [73, 74, 74]
```

2026-10-18 73 → 2026-10-27 74（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `d57a7c99a6d5` · [字段定义](../../DATASET.md)*
