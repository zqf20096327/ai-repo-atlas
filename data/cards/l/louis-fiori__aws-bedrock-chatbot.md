# louis-fiori/aws-bedrock-chatbot

⭐ 19 · HCL · GPL-2.0 · 推送 2026-09-14 · [GitHub](https://github.com/louis-fiori/aws-bedrock-chatbot) · [官网](https://aws.plainenglish.io/deploying-your-own-chatgpt-on-aws-with-amazon-bedrock-and-open-webui-eb4ae62bfc74) · 个人维护

**自托管生成式 AI 聊天助手：Terraform 一键部署 Bedrock 到 AWS**

用 Terraform 将 Open WebUI、Bedrock Access Gateway 与 MCPO 打包为容器部署到 AWS ECS Fargate，构成一个部署在自己 AWS 账号内的私有聊天应用：通过 OpenAI 兼容网关调用 Amazon Bedrock 的 Claude、Titan 等模型，并通过 MCPO 暴露 time、GitLab、Linear 等 MCP 工具。附带 VPC、ALB、EFS、S3、Secrets Manager 等基础设施。作者声明其为 proof of concept：默认无 TLS、开放注册、IAM 权限较宽。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | GPL-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- Terraform 全量定义，Makefile/deploy.sh 一键部署到 ECS Fargate（ARM64）
- Bedrock Access Gateway 提供 OpenAI 兼容 API 接入 Bedrock 模型
- MCPO 将 MCP 服务器（time、GitLab、Linear 等）暴露为 UI 工具
- 附带 VPC/ALB/EFS/S3/Secrets Manager 及可选自定义域名与 VPC endpoints

## 适用场景

- 在自己的 AWS 账号内快速搭建私有生成式 AI 聊天应用
- 在聊天界面中通过 MCP 工具调用 GitLab、Linear 等第三方服务
- 作为 Bedrock + Open WebUI 架构的部署起点进行二次开发

## 场景标签

`聊天机器人` `AI 助手` · 领域:对话与助手

## 证据(README 行号)

> L15: This repository deploys a complete, private generative-AI chatbot on your own AWS account — a polished chat UI back
> L75: Register an account on first visit and start chatting with Bedrock models.

## 星数曲线

```mermaid
xychart-beta
    title "louis-fiori/aws-bedrock-chatbot 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 18 --> 20
    line [19, 19]
```

2026-10-18 19 → 2026-10-30 19（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `dd6a2901dd19` · [字段定义](../../DATASET.md)*
