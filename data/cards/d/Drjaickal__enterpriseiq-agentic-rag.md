# Drjaickal/enterpriseiq-agentic-rag

⭐ 3 · Python · MIT · 推送 2026-11-20 · [GitHub](https://github.com/Drjaickal/enterpriseiq-agentic-rag) · [官网](https://enterpriseiq-agentic-rag.vercel.app) · 个人维护

**面向企业文档的 RAG 问答平台：上传文档、检索证据并生成答案**

以 FastAPI 后端 + PostgreSQL/pgvector 构建的文档问答应用：上传 PDF/DOCX/TXT（限 20MB），经文本抽取、递归分块、768 维向量嵌入、余弦距离检索，再由 LLM 基于检索上下文生成答案并返回来源 ID、块索引与相似度。嵌入与生成模型均可通过环境变量在 Gemini 与 Ollama 间切换；含 SHA-256 内容去重、引用编号校验、FastAPI 路由（健康检查/上传/问答）。README 自述为研究导向的可学习基础，未包含多租户授权与评测层的完整实现，生产使用需补充安全与可靠性工作。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- PDF/DOCX/TXT 摄取，SHA-256 内容哈希去重
- 嵌入与生成后端可经环境变量在 Gemini 与 Ollama 间切换
- 答案返回来源元数据，并校验引用编号超出检索范围的情况
- 本地通过 Docker Compose 启动 pgvector PostgreSQL

## 适用场景

- 把合同、信函等业务文档建成可自然语言提问的知识库
- 学习 RAG 流水线各阶段（分块、嵌入、检索、生成）的可替换实现
- 在内网用 Ollama 本地模型搭建文档问答服务

## 场景标签

`文档问答` `RAG` · 领域:知识与检索

## 证据(README 行号)

> L23: EnterpriseIQ is a document-grounded question-answering application built around a Retrieval-Augmented Generation (R
> L42: It is valuable for learning because each stage is visible and replaceable. It is a production-minded foundation bec
> L53: |Embeddings|Gemini or Ollama, selected through environment variables|

## 星数曲线

```mermaid
xychart-beta
    title "Drjaickal/enterpriseiq-agentic-rag 星数(近 2 点)"
    x-axis ["2026-11-21", "2026-11-23"]
    y-axis "stars" 2 --> 4
    line [3, 3]
```

2026-11-21 3 → 2026-11-23 3（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-22 · 置信度 high · 依据 README sha `1da6a276a4aa` · [字段定义](../../DATASET.md)*
