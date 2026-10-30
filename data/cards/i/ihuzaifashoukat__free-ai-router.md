# ihuzaifashoukat/free-ai-router

⭐ 21 · TypeScript · 推送 2026-03-28 · [GitHub](https://github.com/ihuzaifashoukat/free-ai-router) · 个人维护

**Node.js 库：在 20+ 免费层 AI 提供商间自动路由与降级**

零外部依赖的纯 Node.js 库，作为官方 openai SDK 的替换件：更换 import 后现有 OpenAI 代码可直接运行。内置 20 家提供免费额度的提供商（NVIDIA、Groq、Cerebras、OpenRouter 等）支持，遇到 429 限流时自动切换 key 或降级到其他提供商。提供 free:/free:best 等模型别名按质量、延迟、剩余额度动态选模型，支持多 key 轮换、手动路由策略与配额统计，可原生接入 Vercel AI SDK。MIT 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- openai SDK 的替换件，改一处 import 即可复用现有代码
- 20 个免费层提供商开箱即用，429 时自动换 key 或换提供商
- free:/free:fast 等别名按延迟、质量、剩余额度动态映射模型
- 零外部依赖，提供多 key 轮换、路由策略与配额统计接口

## 适用场景

- 把现有 OpenAI 调用代码切换到免费层提供商组合
- 多提供商多 key 场景下自动避开限流
- 在 Vercel AI SDK 等框架中直接使用而无需代理服务器

## 场景标签

`模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L9:  Stop paying for OpenAI when 20+ providers give away free limits.
> L10:  Drop-in replacement for the official Node.js `openai` SDK. Routes around 429s, falls back across providers, and ha
> L38: Create a free account on any provider below to get started. We support 20 of them out of the box.

## 星数曲线

```mermaid
xychart-beta
    title "ihuzaifashoukat/free-ai-router 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 20 --> 22
    line [21, 21]
```

2026-10-18 21 → 2026-10-30 21（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `8174fd7598e6` · [字段定义](../../DATASET.md)*
