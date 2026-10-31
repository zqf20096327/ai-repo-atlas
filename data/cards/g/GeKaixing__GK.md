# GeKaixing/GK

⭐ 28 · TypeScript · MIT · 推送 2026-08-18 · [GitHub](https://github.com/GeKaixing/GK) · [官网](https://gekaixing.vercel.app) · 个人维护 · 中文 README

**用 TypeScript 全栈实现的 Twitter/X 式社交平台，含 AI 集成点**

基于 Next.js 16 + Auth.js + Prisma + PostgreSQL 的全栈社交平台，功能覆盖发帖、回复、点赞、收藏、分享、关注关系与私信；认证采用 JWT（以 user.id 为标准身份），Feed 缓存使用 Upstash Redis。预留 GLM / OpenAI 兼容接口的 AI 集成点与可选新闻、支付等集成。全程 TypeScript 单一 Node 工具链，本地开发可用 docker compose 启动 PostgreSQL 与 Redis，提供中文部署手册；当前分支已从 Supabase 迁移离开。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 发帖/回复/点赞/收藏/关注/私信等完整社交功能
- Auth.js + JWT 认证，user.id 为标准身份
- 预留 GLM / OpenAI 兼容 AI 集成点
- docker compose 一键启动本地 PostgreSQL 与 Redis

## 适用场景

- 自建部署一个 Twitter/X 式社交平台
- 在其上接入 GLM 等 OpenAI 兼容 AI 能力
- 学习 Next.js 全栈社交应用的架构与认证约定

## 场景标签

 · 领域:Web 应用/社交平台

## 证据(README 行号)

> L7: A social platform built entirely with TypeScript — Next.js + Auth.js + Prisma.
> L16: - Social features: posts, replies, likes, bookmarks, shares, follow graph, messaging
> L20: - AI hooks: GLM / OpenAI-compatible integration points

## 星数曲线

```mermaid
xychart-beta
    title "GeKaixing/GK 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 27 --> 29
    line [28, 28]
```

2026-10-18 28 → 2026-10-31 28（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 mid · 依据 README sha `24824c362257` · [字段定义](../../DATASET.md)*
