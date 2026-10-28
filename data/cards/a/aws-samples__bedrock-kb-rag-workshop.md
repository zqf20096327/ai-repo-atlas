# aws-samples/bedrock-kb-rag-workshop

⭐ 66 · HTML · MIT-0 · 推送 2026-07-14 · [GitHub](https://github.com/aws-samples/bedrock-kb-rag-workshop) · 组织维护

**基于 Amazon Bedrock 构建 RAG 问答应用的示例代码/Workshop**

AWS 官方 samples 仓库，提供用 Amazon Bedrock 实现 RAG 问答的两部分示例：数据管道（Bedrock Agent 读取 S3 文档、分块、用 Amazon Titan Embeddings 生成向量并存入 OpenSearch Serverless）与问答应用（检索上下文拼接提示词交 LLM 生成回答）。通过 CloudFormation 模板一键创建 AOSS、S3、IAM 与 SageMaker Notebook；另提供 Managed Knowledge Bases 模板，省去独立向量库，支持托管重排（含 Cohere 自定义选项）。面向在 AWS 上搭建 RAG 的开发者。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT-0 |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- CloudFormation 模板创建 AOSS/S3/IAM/SageMaker Notebook 全套资源
- Bedrock Agent 自动完成文档摄取、分块与 Titan Embeddings 向量化
- Managed Knowledge Bases 模板免独立向量库，支持 agentic retrieval 与托管/自定义重排

## 适用场景

- 在 AWS 账号内快速搭建 Bedrock 知识库 RAG 问答方案
- 对比向量库方案与 Managed Knowledge Bases 托管方案
- 在 SageMaker Notebook 中按步骤复现与修改 RAG 流程

## 场景标签

`RAG` · 领域:知识与检索

## 证据(README 行号)

> L3: This repository provides sample code for implementing a question answering application using the Retrieval Augmented
> L9: The data pipeline represents an undifferentiated heavy lifting and can be implemented using Amazon Bedrock Agents fo

## 星数曲线

```mermaid
xychart-beta
    title "aws-samples/bedrock-kb-rag-workshop 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 65 --> 67
    line [66, 66]
```

2026-10-18 66 → 2026-10-28 66（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `4ec091052794` · [字段定义](../../DATASET.md)*
