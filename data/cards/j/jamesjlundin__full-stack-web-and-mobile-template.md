# jamesjlundin/full-stack-web-and-mobile-template

⭐ 34 · TypeScript · MIT · 推送 2026-03-09 · [GitHub](https://github.com/jamesjlundin/full-stack-web-and-mobile-template) · [官网](https://full-stack-web-and-mobile-template.vercel.app) · 个人维护

**全栈 Web 与移动应用模板：Web/移动共享代码，内置认证与 AI 聊天**

pnpm workspaces + Turborepo 的 monorepo GitHub 模板，用 Next.js 16 Web 应用与 React Native 移动应用共享业务逻辑与类型。内置 Better Auth（邮箱密码 + OAuth）、PostgreSQL + Drizzle ORM 自动迁移、Resend 邮件、Upstash Redis 限流、GitHub Actions CI/CD 与 Vercel 部署、Playwright/Vitest 测试、Fastlane iOS TestFlight。AI 部分为可选功能：OpenAI/Anthropic/Google 的流式聊天、工具调用与图像生成，需自行配置 API key。面向要快速启动全栈项目的开发者。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Next.js 16 + React Native 共享代码的 monorepo 结构
- 内置 Better Auth 认证（web 会话 / 移动 JWT）与 Drizzle 迁移
- AI Agent 演示：流式聊天、工具调用、图像生成（可选 API key）
- GitHub Actions CI/CD + Vercel 部署 + Fastlane iOS TestFlight

## 适用场景

- 以模板快速启动同时要 Web 和移动端的全栈项目
- 跳过认证、数据库、邮件等基础设施搭建直接开发业务功能
- 接入 LLM API key 后获得带限流的流式 AI 聊天功能

## 场景标签

 · 领域:Web/移动应用开发模板

## 证据(README 行号)

> L7: A production-ready GitHub template for building full-stack applications with a shared codebase across web and mobile
> L15: - **AI-ready** — OpenAI integration with streaming, tool calling, and rate limiting built-in
> L28: |**AI Agent Demo**|Streaming chat with tool calling & image generation|

## 星数曲线

```mermaid
xychart-beta
    title "jamesjlundin/full-stack-web-and-mobile-template 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 33 --> 35
    line [34, 34]
```

2026-10-18 34 → 2026-10-30 34（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `278017a933b7` · [字段定义](../../DATASET.md)*
