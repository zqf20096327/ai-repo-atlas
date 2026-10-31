# Indie-Kit/nextjs-saas-starter

⭐ 28 · TypeScript · MIT · 推送 2026-10-02 · [GitHub](https://github.com/Indie-Kit/nextjs-saas-starter) · [官网](https://indiekit.pro/) · 个人维护

**AI 友好的 Next.js SaaS 启动模板（Indie Kit Pro 开源版）**

Indie Kit Pro 的开源/Lite 版本：基于 Next.js 16 (App Router)、TypeScript、Tailwind v4、Shadcn UI、Better Auth（社交登录+魔法链接）、Drizzle ORM（支持 Supabase/Neon 等任意 Postgres）、Stripe 订阅与 UploadThing 的 SaaS 脚手架，含落地页、认证页、法务页等预建页面。其特色是‘AI Context Rules’：通过 .cursor/rules、.claude/skills 等结构让 Cursor/Windsurf/Copilot 等 AI 工具理解代码库、复用既有模式生成代码，支持一条 /bootstrap 提示词生成 MVP 计划。MIT 许可，提供 npx 脚手架 CLI 与手动克隆两种安装方式；付费 Pro 版含完整支付、多租户、RBAC 等功能。

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

- Next.js 16 + Drizzle ORM + Better Auth + Stripe 的 SaaS 全栈脚手架
- AI Context Rules（.cursor/rules、.claude/skills）供 LLM 理解代码库并复用既有模式
- npx indiekit@latest 交互式脚手架 CLI，自动安装依赖
- Bring Your Own Database：可接 Supabase、Neon 或任意 Postgres 提供商

## 适用场景

- 独立开发者快速搭建可收费的 SaaS MVP
- 在 Cursor/Copilot 等 AI 工具中让 AI 按项目规则生成代码
- 作为 Next.js + Postgres 认证/支付场景的学习模板

## 场景标签

 · 领域:Web 开发/SaaS 脚手架

## 证据(README 行号)

> L16: This is the **Open Source / Lite Version** of Indie Kit Pro. It combines a production-grade tech stack with **"AI C
> L45: - **Self-Documenting Code**: Your AI knows _exactly_ where auth lives (`.claude/skills/auth-handler`), how to migra

## 星数曲线

```mermaid
xychart-beta
    title "Indie-Kit/nextjs-saas-starter 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 27 --> 29
    line [28, 28]
```

2026-10-18 28 → 2026-10-31 28（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `1834339390e9` · [字段定义](../../DATASET.md)*
