# aws-samples/sample-ai-agent-accelerator

⭐ 29 · HCL · MIT-0 · 推送 2025-11-03 · [GitHub](https://github.com/aws-samples/sample-ai-agent-accelerator) · [官网](https://builder.aws.com/content/31Z6LBVoHw6xLCzPnYDGUVjwVj1/exploring-bedrock-agentcore-building-an-ai-agent-accelerator-reference-implementation) · 组织维护

**在 AWS 上快速部署 Bedrock AgentCore AI Agent 的参考实现**

由 AWS 提供的示例参考实现：用 Strands Agent Python 库构建 AI Agent，托管于 AgentCore Runtime，通过 Bedrock Knowledge Bases 与 Amazon S3 Vectors 实现 Agentic RAG，会话状态由 AgentCore Memory 管理。用户通过运行在 ECS Fargate 上的 Flask+HTMX Web 应用（含 GUI 与 HTTP JSON API）与 Agent 对话。部署依赖 Terraform（约 15 分钟内完成），文档覆盖自动扩缩容与 OpenTelemetry 可观测性，面向在自有 AWS 账号中搭建文档问答 Agent 的开发者。

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

- Strands Agent + AgentCore Runtime 构建的 Agentic RAG Agent
- Bedrock Knowledge Bases + S3 Vectors 做语义检索，无需自管数据库
- Web GUI 与 HTTP JSON API，部署于 ECS Fargate 并默认启用自动扩缩容
- 内置 OpenTelemetry 端到端可观测性（CloudWatch GenAI Observability）

## 适用场景

- 在 AWS 账号中快速搭建基于自有文档的问答 Agent
- 作为 Bedrock AgentCore 服务组合的参考架构学习与二次开发
- 需要无服务器、自动扩缩容的企业知识库问答部署

## 场景标签

`文档问答` `RAG` · 领域:知识与检索

## 证据(README 行号)

> L5: A sample reference implementation that showcases how to quickly build an AI agent using the AWS AgentCore service bu
> L7: The agent is built using the Strands Agent Python library and hosted on the AgentCore Runtime. The agent has a `retr

## 星数曲线

```mermaid
xychart-beta
    title "aws-samples/sample-ai-agent-accelerator 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 28 --> 30
    line [29, 29]
```

2026-10-18 29 → 2026-10-26 29（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `b2a8585a84ac` · [字段定义](../../DATASET.md)*
