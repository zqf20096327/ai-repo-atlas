# awskrug/lambda-gurumi-bot

⭐ 33 · Python · 推送 2026-04-13 · [GitHub](https://github.com/awskrug/lambda-gurumi-bot) · 组织维护

**基于 AWS Lambda 与 Bedrock 的 Slack RAG 聊天机器人**

面向 Slack 用户的问答机器人：用户在频道提及或私信时，通过 Amazon Bedrock Knowledge Bases 与 S3 Vectors 检索文档（RAG）生成回答。架构为 AWS Lambda + API Gateway + DynamoDB（保存线程上下文，1 小时 TTL），支持频道白名单、用户级请求限流、长消息分段发送。文档可从 S3 上传（PDF/TXT/MD/HTML/DOCX/CSV），并有 Notion 与 AWS 官方 PDF 的自动同步工作流，经 Serverless Framework 部署。运行依赖 AWS 账号与 Slack 应用配置。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Bedrock Knowledge Bases + S3 Vectors 的 RAG 文档检索回答
- DynamoDB 维护线程对话上下文（1 小时 TTL）
- Notion 页面与 AWS 官方 PDF 的自动同步入库工作流
- 频道白名单与用户级请求限流

## 适用场景

- 在 Slack 中搭建基于自有文档的知识问答机器人
- 团队把 Notion 页面与 AWS 官方文档接入 Slack 即时查询
- 以 Serverless 方式低运维运行 RAG 聊天服务

## 场景标签

`文档问答` · 领域:知识与检索

## 证据(README 行号)

> L3: AWS Lambda, Amazon Bedrock, S3 Vectors를 활용한 서버리스 AI 챗봇입니다. RAG(Retrieval-Augmented Generation) 기반으로 문서를 검색하여 답변합니다.
> L9: - **RAG 지원**: S3 Vectors + Bedrock Knowledge Base 기반 문서 검색 및 답변

## 星数曲线

```mermaid
xychart-beta
    title "awskrug/lambda-gurumi-bot 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 32 --> 34
    line [33, 33]
```

2026-10-18 33 → 2026-10-25 33（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `60ce05c9e416` · [字段定义](../../DATASET.md)*
