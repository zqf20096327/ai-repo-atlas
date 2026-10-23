# aws-samples/serverless-pdf-chat

⭐ 296 · TypeScript · MIT-0 · 推送 2026-04-07 · [GitHub](https://github.com/aws-samples/serverless-pdf-chat) · [官网](https://aws.amazon.com/blogs/compute/building-a-serverless-document-chat-with-aws-lambda-and-amazon-bedrock/) · 组织维护

**基于 Amazon Bedrock 的 PDF 文档问答示例应用**

AWS 官方 samples 出品的 Serverless RAG 示例应用：用户上传 PDF 后以自然语言提问，系统在 Lambda 中用 LangChain 编排问答链，Bedrock 模型生成嵌入与回答，FAISS 做向量检索，DynamoDB 存储会话记忆，Cognito 负责认证，前端为 React/TypeScript/Vite。部署方式为 AWS SAM CLI 部署后端、Amplify Hosting 或本地 Vite 运行前端。README 声明仅供演示与教学，未准备好生产使用，且架构会产生 AWS 费用；默认使用 Titan Embeddings G1 与 Claude v3 Sonnet，需在 Bedrock 控制台申请模型访问。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT-0 |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- Bedrock 提供嵌入与推理，LangChain 编排 Q&A 链
- FAISS 向量检索 + DynamoDB 会话记忆的 Serverless 架构
- SAM 一键部署，Cognito 用户认证
- 前端可本地 Vite 运行或部署至 Amplify Hosting

## 适用场景

- 上传 PDF 并用自然语言提问获得基于文档内容的回答
- 学习 Bedrock + Lambda + FAISS 的 Serverless RAG 架构
- 作为 AWS 上的文档问答参考实现进行扩展

## 场景标签

`文档问答` `RAG` · 领域:知识与检索

## 证据(README 行号)

> L3: This sample application allows you to ask natural language questions of any PDF document you upload. It combines the
> L15: - Amazon Bedrock for serverless embedding and inference
> L31: 1. A LLM then uses the results of this vector search, previous messages in the conversation, and its general-purpos

## 星数曲线

```mermaid
xychart-beta
    title "aws-samples/serverless-pdf-chat 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-23"]
    y-axis "stars" 295 --> 297
    line [296, 296]
```

2026-10-18 296 → 2026-10-23 296（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `6994c9190368` · [字段定义](../../DATASET.md)*
