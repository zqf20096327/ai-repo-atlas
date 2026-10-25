# build-on-aws/langchain-embeddings

⭐ 58 · Jupyter Notebook · MIT-0 · 推送 2026-04-14 · [GitHub](https://github.com/build-on-aws/langchain-embeddings) · 组织维护

**面向开发者的 AWS 多模态搜索与 RAG 教学仓库：Bedrock 嵌入+向量库**

AWS build-on-aws 维护的学习型仓库，用 Python 演示基于 Amazon Bedrock（Nova 多模态嵌入模型）、LangChain、FAISS、Aurora PostgreSQL/pgvector 构建文本/图像/视频的自然语言多模态搜索。内容含 7 个 Jupyter 教学笔记本（从语义检索入门到 Strands Agents 视频代理 RAG）与 3 个 CDK 示例部署（Aurora 向量库、Lambda 无服务器系统、ECS 视频流水线）。附 Bedrock/Lambda/Aurora 等服务成本估算。限制：需 AWS 账号并开启 Bedrock 访问；LangChain 的 BedrockEmbeddings 与 Nova 嵌入不兼容，需直接用 boto3 请求格式。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | MIT-0 |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 7 个分级笔记本覆盖文本/图像/视频嵌入到 Agentic 视频 RAG
- 3 个可 CDK 部署的示例架构（Aurora pgvector、Lambda、ECS）
- 指明 Nova 嵌入与 LangChain BedrockEmbeddings 的兼容性问题及 boto3 正确格式
- 各 AWS 服务的用量成本估算表

## 适用场景

- 学习用 Bedrock 嵌入和 pgvector 搭建多模态搜索
- 参考无服务器 Lambda 文档处理与 ECS 视频分析架构
- 了解 LangChain 与 Nova 嵌入模型配合时的 API 格式差异

## 场景标签

`教程课程` `语义搜索` `RAG` `多模态` · 领域:知识与检索

## 证据(README 行号)

> L1: ## 🚀 Multimodal Search Learning Experience
> L20: |**📓 Jupyter Notebooks**|Multimodal AI fundamentals with interactive tutorials|30-120 min|Beginner|
> L29: |**01 - Semantic Search with LangChain, Amazon Titan Embeddings, and FAISS**|Text embeddings and PDF processing - D

## 星数曲线

```mermaid
xychart-beta
    title "build-on-aws/langchain-embeddings 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 57 --> 59
    line [58, 58]
```

2026-10-18 58 → 2026-10-25 58（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `368da90dfaaa` · [字段定义](../../DATASET.md)*
