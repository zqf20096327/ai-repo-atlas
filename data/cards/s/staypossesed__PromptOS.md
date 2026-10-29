# staypossesed/PromptOS

⭐ 17 · TypeScript · 推送 2026-10-21 · [GitHub](https://github.com/staypossesed/PromptOS) · [官网](https://www.umprompt.com/) · 个人维护

**面向普通用户的 AI 提示词构建工作台，把粗略想法转为可用提示词**

Umprompt 是一个 Next.js 15 构建的 Web 工作台，帮助不熟悉提示词工程的用户把粗略想法整理为结构化、可复制到 Claude/Cursor/ChatGPT 等助手的提示词。流程为：输入想法、按需回答最多两个澄清问题、生成结果、可选质量评分与优化，支持历史保存与模板。附带 Chrome 侧边栏扩展（0.1.2，商店审核中）。AI 层用 Vercel AI SDK 接入 Anthropic 与 OpenRouter；数据在 Supabase/PostgreSQL（行级安全），支付走 Stripe，提供免费生成额度与月付/买断方案。自部署需 Node.js 22+、Supabase 项目、AI provider 凭据及八个 SQL 迁移文件。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 想法到结构化提示词的生成流程，含最多两轮澄清问题与可选评分
- 支持 Anthropic 与 OpenRouter 双 provider，可配置生成/评分模型
- 私有上下文 profile 与可复用 playbook 库，行级安全保护
- Chrome 侧边栏扩展（v0.1.2），与网站共享账户历史

## 适用场景

- 把模糊的想法整理成可复制给 AI 助手的提示词
- 保存和复用上下文 profile 与提示词模板
- 在浏览器侧边栏中随时优化和复制请求

## 场景标签

`提示工程` · 领域:Agent 开发

## 证据(README 行号)

> L3: Turn rough ideas into clear, ready-to-use AI prompts.
> L66: |AI|Vercel AI SDK 4 with Anthropic and OpenRouter providers|

## 星数曲线

```mermaid
xychart-beta
    title "staypossesed/PromptOS 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-28", "2026-10-29"]
    y-axis "stars" 15 --> 18
    line [16, 17, 17]
```

2026-10-18 16 → 2026-10-29 17（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `5f5db669ac5d` · [字段定义](../../DATASET.md)*
