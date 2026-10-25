# aws-samples/foundational-llm-chat

⭐ 36 · Python · MIT-0 · 推送 2026-02-11 · [GitHub](https://github.com/aws-samples/foundational-llm-chat) · 组织维护

**部署在 AWS 上的 Chainlit 聊天应用：通过 Bedrock 对话各家 LLM**

基于 AWS CDK 构建的 Chainlit Web 应用，经 Amazon Bedrock Converse API 与多家厂商的语言模型（Anthropic Claude、Meta Llama、Mistral、Amazon Nova、DeepSeek、Qwen、OpenAI GPT OSS 等）对话，支持图片/文档上传的多模态响应、两种推理模式（Anthropic 式 token 预算与 OpenAI 式 effort 等级）、MCP 工具调用、跨区域推理与 Prompt Manager 版本管理。部署依赖 Cognito 认证、ECS/Fargate 容器化与 CloudFront 分发，通过 config.json 按模型配置 ID、区域、成本与能力开关。面向需要在 AWS 环境中部署企业级 LLM 对话界面的开发者与组织。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT-0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 通过 Bedrock Converse API 支持 Claude/Llama/Mistral/Nova/DeepSeek/Qwen 等多厂商模型
- 多模态：图片与文档上传、视觉模型响应
- 双推理模式：Anthropic 式 token 预算与 OpenAI 式 effort 等级（含 DeepSeek R1 模型级常开推理处理）
- Cognito 认证、ECS/Fargate 部署、CloudFront 分发、按模型用量成本跟踪

## 适用场景

- 在自有 AWS 账号内部署一个带登录认证的 LLM 对话界面
- 在同一界面切换多家 Bedrock 模型并跟踪调用成本
- 对上传的图片和文档进行多模态问答

## 场景标签

`聊天机器人` `多模态` · 领域:对话与助手

## 证据(README 行号)

> L5: Foundational LLM Chat is a Chainlit application built using AWS CDK and Converse API that allows you to interact wit
> L11: - 🌐 Support for all text generation models in Amazon Bedrock through Converse API, including:

## 星数曲线

```mermaid
xychart-beta
    title "aws-samples/foundational-llm-chat 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 35 --> 37
    line [36, 36]
```

2026-10-18 36 → 2026-10-25 36（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `eb4f7e4af459` · [字段定义](../../DATASET.md)*
