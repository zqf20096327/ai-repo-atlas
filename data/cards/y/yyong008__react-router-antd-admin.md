# yyong008/react-router-antd-admin

⭐ 92 · TypeScript · MIT · 推送 2026-07-15 · [GitHub](https://github.com/yyong008/react-router-antd-admin) · [官网](https://remix-antd-admin.vercel.app) · 个人维护 · 中文 README

**基于 React Router/Antd/Drizzle 的全栈管理后台模板（WIP）**

由 Remix Antd Admin 迁移而来的全栈 Web 管理后台模板：采用 React Router v8 Framework mode、Antd v6、Drizzle ORM、Hono、TanStack Query，组织为 monorepo（web/admin/api）。内置 RBAC 权限、better-auth 认证、Paraglide JS 国际化、Cloudflare Worker/R2/D1 部署支持，AI 部分由 LangChain 迁移至 ai-sdk 并使用 AntdX 作为 AI Client。README 自述使用不稳定的中间件新特性，不适合生产环境，仍在开发中（Hono API 迁移、API Client、邮件与 Turnstile 等未完成）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- monorepo 结构（web/admin/api）与 React Router v8 Framework mode
- 集成 better-auth、RBAC、Paraglide JS i18n、Cloudflare R2/D1
- AI 部分采用 ai-sdk 与 AntdX AI Client
- 提供 Fumadocs 文档 CMS 与 Vitest

## 适用场景

- 以此模板快速搭建带权限系统的管理后台
- 学习 React Router v8 全栈模式与 Drizzle/Hono 组合
- 需要 AI 对话客户端功能的后台项目原型

## 场景标签

`聊天机器人` · 领域:对话与助手

## 证据(README 行号)

> L38: 一个基于 React Router、React、Antd、Drizzle ORM 和 RBAC 的现代全栈 Web 解决方案（WIP）。
> L34: - [x] AI：LangChain -> ai-sdk

## 星数曲线

```mermaid
xychart-beta
    title "yyong008/react-router-antd-admin 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 91 --> 93
    line [92, 92]
```

2026-10-18 92 → 2026-10-26 92（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 mid · 依据 README sha `86648d901c68` · [字段定义](../../DATASET.md)*
