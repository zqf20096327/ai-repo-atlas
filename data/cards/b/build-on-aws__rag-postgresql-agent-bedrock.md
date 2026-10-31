# build-on-aws/rag-postgresql-agent-bedrock

⭐ 36 · Python · MIT-0 · 推送 2026-03-10 · [GitHub](https://github.com/build-on-aws/rag-postgresql-agent-bedrock) · 组织维护

**AWS CDK 部署的 WhatsApp RAG 旅行客服 Agent 示例应用**

由 build-on-aws（AWS）提供的示例工程，用 Python CDK 分四个阶段在 AWS 上部署一个 WhatsApp 旅行客服助手：Aurora PostgreSQL 向量库作为 Bedrock Knowledge Base、Agents for Amazon Bedrock 处理会话与回答、DynamoDB 存储乘客信息与工单，支持语音消息经 Transcribe 转文字后进入对话。未解决问题自动创建工单并可查询工单库。需自备 AWS 账号、开通 Titan Embeddings V2 与 Claude 3 模型访问，产生多项 AWS 与 WhatsApp 费用；README 为教程式文档，非即装即用产品。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT-0 |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 四阶段 CDK 基础设施即代码部署（数据库→知识库→Agent→WhatsApp 界面）
- Bedrock Agent 托管会话跟踪，无需自行实现对话管理逻辑
- 语音消息经 Amazon Transcribe 转文字后进入助手流程
- 未解决问题自动创建工单并支持自然语言查询工单库

## 适用场景

- 参考搭建基于 Bedrock 与 Aurora PostgreSQL 的 RAG 客服系统
- 学习 AWS 上生成式 AI 应用的 CDK 基础设施部署
- 为旅行行业搭建带工单系统的 WhatsApp 客服助手

## 场景标签

`RAG` `教程课程` · 领域:知识与检索

## 证据(README 行号)

> L3: In our previous blog post, "Elevating Customer Support With a Whatsapp Assistant," we explored how advanced technolo
> L13: This application is built in four stages using infrastructure as code with AWS Cloud Development Kit (CDK) for pyth
> L58: 3. **Assistant Response:**
> L87: The final part of a four-part series on building an advanced WhatsApp-powered RAG Travel Support Agent using Amazon

## 星数曲线

```mermaid
xychart-beta
    title "build-on-aws/rag-postgresql-agent-bedrock 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 35 --> 37
    line [36, 36]
```

2026-10-18 36 → 2026-10-31 36（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `3f65656dab7d` · [字段定义](../../DATASET.md)*
