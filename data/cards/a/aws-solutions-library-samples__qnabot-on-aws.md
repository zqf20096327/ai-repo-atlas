# aws-solutions-library-samples/qnabot-on-aws

⭐ 448 · JavaScript · Apache-2.0 · 推送 2026-09-09 · [GitHub](https://github.com/aws-solutions-library-samples/qnabot-on-aws) · [官网](https://aws.amazon.com/solutions/implementations/aws-qnabot) · 组织维护

**AWS 上的多渠道多语言问答聊天机器人部署方案**

QnABot on AWS 是部署在 AWS 账户内的对话式问答方案：通过 CloudFormation 模板部署 Lex、Lambda、OpenSearch、DynamoDB 等组件，支持网页客户端、语音、SMS 与 Amazon Alexa 多渠道；提供 Content Designer UI 供管理员配置问答库。文本生成与向量嵌入经 Amazon Bedrock 基础模型处理，可配置 Kendra 或 Bedrock Knowledge Base 作为无匹配时的回退，并支持前后置 guardrails 与 RAG 流式响应。自定义部署需 Linux、npm/node、Python、Poetry 与 AWS CLI。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 多渠道部署：网页客户端、语音、SMS、Amazon Alexa
- 经 Amazon Bedrock 基础模型实现文本生成与文本嵌入
- Kendra 或 Bedrock Knowledge Base 回退与 RAG 流式响应
- OpenSearch Dashboards 查看使用记录与用户反馈

## 适用场景

- 搭建客服问答机器人以减少人工坐席等待时间
- 在多渠道（聊天/语音/SMS/Alexa）提供一致的问答服务
- 通过 Content Designer 管理问答知识库并分析使用数据

## 场景标签

`聊天机器人` · 领域:对话与助手

## 证据(README 行号)

> L5: QnABot on AWS is a multi-channel, multi-language conversational interface (chatbot) that responds to your customer’s
> L29: 4. The `Content Designer` AWS Lambda function saves the input in Amazon OpenSearch Service in a questions bank inde
> L39: 9. If using LLM features such as text generation and text embeddings, these requests will first pass through variou

## 星数曲线

```mermaid
xychart-beta
    title "aws-solutions-library-samples/qnabot-on-aws 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 447 --> 449
    line [448, 448]
```

2026-10-18 448 → 2026-10-29 448（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 mid · 依据 README sha `d694483fb62f` · [字段定义](../../DATASET.md)*
