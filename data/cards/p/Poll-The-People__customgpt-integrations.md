# Poll-The-People/customgpt-integrations

⭐ 16 · Python · 推送 2025-12-23 · [GitHub](https://github.com/Poll-The-People/customgpt-integrations) · [官网](https://customgpt-integrations.vercel.app) · 组织维护

**CustomGPT.ai 的官方集成合集：跨消息平台部署 AI 客服机器人**

CustomGPT.ai 维护的 monorepo，包含 13 个生产可用的集成，分四类：9 个消息平台机器人（WhatsApp/Discord/Slack/Telegram/Teams/Google Chat/Rocket.Chat/Instagram/FB Messenger）、2 个网站聊天挂件（含语音与 3D 虚拟形象）、1 个白标 Chrome 扩展、1 个 n8n/Make.com 工作流自动化模板。所有集成都通过 CustomGPT.ai API 调用其 RAG agent，需自行注册获取 API key。支持 Vercel/Railway/Docker 等多种部署方式，部分集成（Instagram 为 Beta，FB Messenger 为 WIP）尚未达到 Ready 状态。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 覆盖 9 个消息平台的 AI 机器人集成，多数为 Ready 状态
- 网站挂件支持语音模式、3D 虚拟形象与多 TTS 提供商
- Chrome 扩展支持白标与零用户配置
- 提供 Vercel/Railway/Docker/Kubernetes 等部署选项与视频教程

## 适用场景

- 把 CustomGPT.ai 的知识库问答接入 Slack、WhatsApp 等内部或客服渠道
- 在企业网站嵌入带语音和引用来源的 AI 助手挂件
- 用 n8n/Make.com 模板把 CustomGPT 接入工作流自动化

## 场景标签

`聊天机器人` `AI 助手` `文档问答` · 领域:对话与助手

## 证据(README 行号)

> L3: A comprehensive collection of integrations, widgets, and tools for CustomGPT.ai, allowing you to deploy AI-powered e
> L5: You will need our API to use any of these below listed integration, create your API key here.
> L43: This monorepo contains **13 production-ready integrations** for CustomGPT across four major categories:

## 星数曲线

```mermaid
xychart-beta
    title "Poll-The-People/customgpt-integrations 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-30", "2026-10-31"]
    y-axis "stars" 14 --> 17
    line [15, 16, 16]
```

2026-10-18 15 → 2026-10-31 16（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `9978086d6d6c` · [字段定义](../../DATASET.md)*
