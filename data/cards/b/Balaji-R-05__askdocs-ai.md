# Balaji-R-05/askdocs-ai

⭐ 42 · Python · 推送 2026-04-12 · [GitHub](https://github.com/Balaji-R-05/askdocs-ai) · [官网](https://askdocs-ai.streamlit.app) · 个人维护

**基于混合 RAG 的 PDF 问答聊天机器人**

面向终端用户的 PDF 问答应用：用户上传 PDF 后，系统结合 ChromaDB 语义向量检索与 BM25 关键词检索（权重可在配置中调节），调用 Groq Cloud 上的 LLM 生成基于文档内容的回答。后端为 FastAPI，前端为 Streamlit；PDF 摄取与索引在后台线程异步处理。需要 GROQ_API_KEY 才能运行，提供 Docker Compose 部署与本地虚拟环境两种方式，服务器镜像针对 CPU 环境优化。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | locked-api |  |
| 硬件要求 | `cpu-ok` | |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- ChromaDB 语义检索与 BM25 关键词检索加权融合
- 通过 Groq Cloud 调用 LLM 生成回答
- PDF 摄取与索引异步后台处理
- Docker 卷持久化向量库与上传文件

## 适用场景

- 上传 PDF 文档并针对内容提问
- 通过调整检索权重适配不同文档的问答效果
- 本地或 Docker 环境部署私有文档问答服务

## 场景标签

`文档问答` · 领域:知识与检索

## 证据(README 行号)

> L3: **AskDocs AI** is an AI-powered chatbot that leverages **Hybrid RAG (Retrieval-Augmented Generation)** to answer you
> L11: - **LLM Powered**: High-performance LLM via Groq Cloud.

## 星数曲线

```mermaid
xychart-beta
    title "Balaji-R-05/askdocs-ai 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 41 --> 43
    line [42, 42]
```

2026-10-18 42 → 2026-10-25 42（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `d16f8e6d3a73` · [字段定义](../../DATASET.md)*
