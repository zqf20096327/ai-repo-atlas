# AdilShamim8/Production-grade-RAG

⭐ 14 · Python · 推送 2026-04-05 · [GitHub](https://github.com/AdilShamim8/Production-grade-RAG) · [官网](https://grade-rag.streamlit.app/) · 个人维护

**面向开发者的生产级 RAG 系统：PDF 摄入与有据问答**

基于 FastAPI、Streamlit、LangChain 与 Qdrant 的检索增强生成系统，覆盖 PDF 上传、分块、嵌入、Top-K 检索到 LLM 回答的完整管线，回答附带检索来源。支持 OpenAI/Gemini/Claude/Ollama 多提供方路由，可配 Inngest 步骤函数实现持久化工作流；远程依赖不可用时降级到本地嵌入存储与本地模型。提供根应用与打包版 rag-engine（含测试），Docker Compose 启动 Qdrant 与 API 服务。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- PDF 摄入→分块→嵌入→Qdrant 检索→LLM 回答的完整管线
- 多提供方 LLM/嵌入路由（OpenAI/Gemini/Claude/Ollama/本地）
- Inngest 步骤函数持久化工作流与幂等摄入 ID
- 远程依赖不可用时的本地降级模式与 UI 预检诊断

## 适用场景

- 搭建基于自有 PDF 文档的问答服务
- 在断网或依赖不可用时用本地模型与嵌入式 Qdrant 继续运行
- 以 Docker Compose 部署 API 与向量库

## 场景标签

`RAG` `文档问答` · 领域:知识与检索

## 证据(README 行号)

> L8: A production-focused Retrieval-Augmented Generation (RAG) system for PDF ingestion and grounded Q&A.
> L25: PDF Upload -> Chunking -> Embeddings -> Qdrant -> Top-K Retrieval -> LLM Answer

## 星数曲线

```mermaid
xychart-beta
    title "AdilShamim8/Production-grade-RAG 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `5b149f351635` · [字段定义](../../DATASET.md)*
