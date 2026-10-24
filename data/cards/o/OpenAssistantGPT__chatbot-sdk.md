# OpenAssistantGPT/chatbot-sdk

⭐ 62 · TypeScript · Apache-2.0 · 推送 2025-10-28 · [GitHub](https://github.com/OpenAssistantGPT/chatbot-sdk) · [官网](https://sdk.openassistantgpt.io) · 组织维护

**基于 NextJS/Vercel 构建 GPT 聊天机器人的 SDK**

OpenAssistantGPT 团队维护的 chatbot SDK，是 vercel/ai SDK 的扩展，面向用 NextJS 部署到 Vercel 的开发者。通过 OpenAI Assistant API 提供后端路由（@openassistantgpt/assistant）与可嵌入网页 iframe 的聊天 UI 组件（@openassistantgpt/ui），配置 OPENAI_API_KEY 与 OPENAI_ASSISTANT_ID 环境变量即可运行。另有带高级分析、内容爬取与安全功能的托管版本。需 Node.js 18+ 与 pnpm。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- vercel/ai SDK 的扩展，新增聊天机器人相关功能
- @openassistantgpt/assistant 后端路由与 @openassistantgpt/ui 组件两个包
- 基于 OpenAI Assistant API，可 iframe 嵌入任意网站
- 提供 Vercel 一键部署示例与多种集成示例

## 适用场景

- 用 NextJS 快速搭建并部署 GPT 聊天机器人到 Vercel
- 将聊天组件嵌入自己的网站
- 基于示例扩展自定义 API 与窗口式集成

## 场景标签

`聊天机器人` · 领域:对话与助手

## 证据(README 行号)

> L5: This SDK is an extension of the vercel/ai SDK with more features, addapted to our use case and maintained by the Ope
> L53: OPENAI_API_KEY=xxxxxxx

## 星数曲线

```mermaid
xychart-beta
    title "OpenAssistantGPT/chatbot-sdk 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 61 --> 63
    line [62, 62]
```

2026-10-18 62 → 2026-10-24 62（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `da76470d6a2a` · [字段定义](../../DATASET.md)*
