# repaera/chat

⭐ 27 · TypeScript · NOASSERTION · 推送 2026-06-20 · [GitHub](https://github.com/repaera/chat) · 个人维护 · 中文 README

**面向服务的通用 AI 聊天界面：连接任意 MCP 服务器对话交互**

基于 Next.js App Router、Vercel AI SDK v6 与 Prisma v7 构建的通用 AI 聊天界面，通过 Streamable HTTP 连接一个外部 MCP 服务器，让用户以自然语言对话调用其工具。支持流式输出、图片附件与 LLM 图片输出、地理位置分享、邮箱/Google 认证、11 种语言自定义 i18n、每周消息配额，并可经 Chat SDK 接入 Telegram/WhatsApp/Slack 等多个平台。LLM 提供 9 个 provider 可选，图片存储用 Cloudflare R2，后台任务用 Trigger.dev，VPS 有一键安装脚本。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 经 Streamable HTTP 连接任意 MCP 服务器并以对话调用工具
- 9 个 LLM provider 可选（OpenAI/Anthropic/Azure/Bedrock/Vertex/xAI/OpenRouter 等）
- 图片附件强制裁剪后发送、存 Cloudflare R2，含孤儿图片清理
- 可经 Chat SDK 接入 Telegram/WhatsApp/Slack/Teams 等 8 个平台

## 适用场景

- 给配送、预约、任务管理等自有服务快速挂一个对话界面
- 自托管一套带认证与多语言的多平台 AI 客服/助手
- 通过 MCP 协议让 LLM 调用自己后端服务的工具

## 场景标签

`AI 助手` `聊天机器人` · 领域:对话与助手

## 证据(README 行号)

> L7: A general-purpose AI chat interface powered by MCP. Connect any MCP server — delivery service, handyman booking, tas
> L33: |LLM Provider|9 providers via Vercel AI SDK — OpenAI, Anthropic, Azure OpenAI, Azure AI Foundry, AWS Bedrock, Googl

## 星数曲线

```mermaid
xychart-beta
    title "repaera/chat 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 26 --> 28
    line [27, 27]
```

2026-10-18 27 → 2026-10-31 27（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 mid · 依据 README sha `22ac6457b023` · [字段定义](../../DATASET.md)*
