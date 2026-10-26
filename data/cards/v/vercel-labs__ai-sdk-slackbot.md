# vercel-labs/ai-sdk-slackbot

⭐ 131 · TypeScript · 推送 2026-06-05 · [GitHub](https://github.com/vercel-labs/ai-sdk-slackbot) · [官网](https://ai-sdk.dev) · 组织维护

**基于 AI SDK 的 Slack AI 聊天机器人，带工具调用与策略门控**

用 Vercel AI SDK 构建的 Slack 聊天机器人：响应私信与频道 @提及，在线程和私信中维持对话上下文。内置天气查询、Exa 网络搜索、沙箱化 bash 等工具，且每次工具调用都经过 Open Policy Agent（Rego）策略门控，编辑策略无需改 TypeScript。默认使用 OpenAI（gpt-4o），也可切换本地 Ollama（本地开发用，部署到 Vercel 后无法访问 localhost）。需 Node.js 18+、Slack 管理员权限与 Exa API key，部署到 Vercel 等托管平台。README 明确说明策略只约束工具调用、不约束模型自由文本。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Slack 私信与 @提及双通道，线程内维持上下文
- 每次工具调用经 OPA（Rego）策略门控，改策略无需改代码
- 内置天气、Exa 网络搜索、沙箱 bash 工具，可扩展自定义工具
- 支持 OpenAI 或本地 Ollama 作为模型后端

## 适用场景

- 在 Slack 工作区部署一个能查天气、搜网页、执行命令的 AI 助手
- 通过编辑 Rego 策略控制机器人允许执行的操作
- 本地用 Ollama 免费离线运行进行开发测试

## 场景标签

`AI 助手` `聊天机器人` · 领域:对话与助手

## 证据(README 行号)

> L5: An AI-powered chatbot for Slack powered by the AI SDK by Vercel.
> L10: - Use any LLM with the AI SDK (easily switch between providers)
> L13: - Built-in tools for enhanced capabilities:

## 星数曲线

```mermaid
xychart-beta
    title "vercel-labs/ai-sdk-slackbot 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-25", "2026-10-26"]
    y-axis "stars" 130 --> 133
    line [132, 131, 131]
```

2026-10-18 132 → 2026-10-26 131（-1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `c7602a838e84` · [字段定义](../../DATASET.md)*
