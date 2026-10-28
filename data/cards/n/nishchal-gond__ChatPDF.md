# nishchal-gond/ChatPDF

⭐ 20 · Python · MIT · 推送 2026-09-02 · [GitHub](https://github.com/nishchal-gond/ChatPDF) · 个人维护

**基于 Amazon Bedrock 的 PDF 对话问答应用（RAG）**

一个使用 Python、LangChain、Docker 与 Amazon S3 构建的 PDF 问答演示应用，分 Admin 与 User 两个 Web 应用：Admin 端上传 PDF、切分文本、用 Amazon Titan Embedding 生成向量并以 FAISS 建索引上传到 S3；User 端下载索引构建本地 FAISS，通过 RetrievalQA 做相似度检索取 5 个相关片段，交给 Claude 模型生成回答。文档提及可选 OpenSearch/Pinecone/PgVector 等向量库，提供 Docker 构建与运行命令。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Titan Embeddings 生成向量，FAISS 建索引并存储到 S3
- LangChain RetrievalQA 检索 5 个相关片段交给 Claude 回答
- Admin 上传建库 / User 查询问答的双应用架构
- 提供 Docker 构建与运行命令

## 适用场景

- 上传自有 PDF 并对其内容进行问答
- 学习 Bedrock+LangChain+S3 的 RAG 应用搭建方式

## 场景标签

`文档问答` · 领域:知识与检索

## 证据(README 行号)

> L2: ## Built Using Amazon Bedrock, Langchain, Python, Docker, Amazon S3
> L28:  - Langchain's RetrievalQA, does the following:
> L31:  - Using Prompt template, provide the question and context to the Large Language Model. We are using Claude model f

## 星数曲线

```mermaid
xychart-beta
    title "nishchal-gond/ChatPDF 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 19 --> 21
    line [20, 20]
```

2026-10-18 20 → 2026-10-28 20（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `f80ffaa04725` · [字段定义](../../DATASET.md)*
