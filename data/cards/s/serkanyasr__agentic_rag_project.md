# serkanyasr/agentic_rag_project

⭐ 29 · Python · MIT · 推送 2025-11-03 · [GitHub](https://github.com/serkanyasr/agentic_rag_project) · 个人维护

**基于 Pydantic AI/FastAPI/pgvector 的 Agentic RAG 问答系统**

面向文档问答场景的检索增强生成系统：用 Docling 抽取 PDF 文本、表格与图片，经分块后以 PostgreSQL + pgvector 存储，agent 通过向量检索与混合检索工具生成回答；提供 FastAPI 后端（SSE 流式接口、会话管理）与 Streamlit 网页界面。LLM 默认调用 OpenAI gpt-4（需配置 API key），部署方式为 Docker Compose 多容器。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 向量检索与混合检索两种检索策略
- Docling 抽取 PDF 文本、表格与图片
- FastAPI 提供 /chat 与 SSE 流式接口，含会话历史
- Docker Compose 一键部署 PostgreSQL 17 + API + Streamlit

## 适用场景

- 上传 PDF 后直接提问获取带检索依据的回答
- 作为文档类 AI 应用的基础工程搭建起点
- 通过 API 将 RAG 问答嵌入自己的系统

## 场景标签

`文档问答` `RAG` · 领域:知识与检索

## 证据(README 行号)

> L3: A modern Agentic RAG (Retrieval-Augmented Generation) system built with Pydantic AI, FastAPI, and PostgreSQL (pgvect
> L10: - 🧠 Pydantic AI-based intelligent agent system
> L127: - `POST /chat/stream` - Streaming chat

## 星数曲线

```mermaid
xychart-beta
    title "serkanyasr/agentic_rag_project 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 28 --> 30
    line [29, 29]
```

2026-10-18 29 → 2026-10-28 29（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 mid · 依据 README sha `f66aafee96ea` · [字段定义](../../DATASET.md)*
