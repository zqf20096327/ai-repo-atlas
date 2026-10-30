# Anil-matcha/open-character-ai

⭐ 61 · JavaScript · 推送 2026-09-29 · [GitHub](https://github.com/Anil-matcha/open-character-ai) · [官网](https://muapi.ai?utm_source=github&utm_medium=about&utm_campaign=open-character-ai) · 个人维护

**自托管的 AI 角色对话门户，可预设或自建角色并按对话调参**

基于 Next.js (App Router) 的自托管 SaaS 应用：用户浏览预设角色或通过可视化构建器创建自定义角色，在聊天界面中按对话线程调整 Temperature、Max Tokens 与 System Prompt。集成 NextAuth Google 登录、Stripe 按量计费积分、Prisma/PostgreSQL 聊天持久化，LLM 调用通过 muapi.ai 的 API 路由。面向 Vercel serverless 环境部署，需配置数据库、认证、Stripe 等多项环境变量；本地开发需 Node.js 18+ 与 PostgreSQL 实例。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 可视化角色构建器：名称、问候、性格、系统指令、头像与公开/私可见性
- 按对话线程实时调整 Temperature / Max Tokens / System Prompt 的调参面板
- 内置 Google OAuth 登录与 Stripe 积分按量计费（webhook 实时到账）
- 聊天历史与角色数据经 Prisma 持久化到 PostgreSQL

## 适用场景

- 搭建自己的 AI 陪伴/角色对话站点
- 创作者或品牌方自建角色门户并按积分收费
- 在对话中实时试验不同 LLM 生成参数

## 场景标签

`聊天机器人` · 领域:对话与助手

## 证据(README 行号)

> L3: > **An interactive, high-fidelity AI companion portal where users explore preset personas, forge custom AI character
> L19: Sign in with Google to explore preset characters, customize your own companion, tune generation parameters in real-

## 星数曲线

```mermaid
xychart-beta
    title "Anil-matcha/open-character-ai 星数(近 4 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-23", "2026-10-30"]
    y-axis "stars" 55 --> 62
    line [56, 57, 60, 61]
```

2026-10-18 56 → 2026-10-30 61（+5）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 mid · 依据 README sha `c405dfb440d2` · [字段定义](../../DATASET.md)*
