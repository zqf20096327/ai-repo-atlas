# mx-space/core

⭐ 565 · TypeScript · NOASSERTION · 推送 2026-10-23 · [GitHub](https://github.com/mx-space/core) · 个人维护 · 中文 README

**面向个人博客与创作者的 AI 增强无头 CMS 全栈 monorepo**

Mix Space 的工作区仓库，构建个人 CMS 全栈：核心服务（NestJS + Fastify + PostgreSQL + Redis 的 AI 无头 CMS 服务器）、内置 React 19 管理 SPA、原生 iOS 管理客户端、独立部署的 APNs 推送中继与遥测收集器，另含 API SDK、CLI、共享 AI 契约等包。AI 能力（摘要/翻译等）作为 CMS 功能嵌入，去掉 AI 后 CMS 本身仍可运行。仓库提供 pnpm 命令的开发/构建/测试流程，各应用部署文档在各自 README。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- NestJS + Fastify + PostgreSQL + Redis 的无头 CMS 核心服务
- 含管理 SPA、iOS 客户端、APNs 推送中继与共享 SDK 的 monorepo
- 提供 MongoDB→PostgreSQL 一次性数据迁移工具（mongo-pg-cli）
- AI 契约包定义服务端与客户端共享的 SSE 事件联合类型

## 适用场景

- 搭建个人博客或创作者主页的内容后台
- 通过无头 API 配合 Next.js 等前端发布内容
- 在服务器与多个客户端间共享类型化 API SDK

## 场景标签

 · 领域:内容管理/博客系统

## 证据(README 行号)

> L18: Mix Space is an AI-powered, headless CMS for personal blogs, creator homepages, and
> L35: |`apps/core`|`@mx-space/core`|The heart of the stack — AI-powered headless CMS server (NestJS + Fastify + PostgreSQ

## 星数曲线

```mermaid
xychart-beta
    title "mx-space/core 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 564 --> 566
    line [565, 565]
```

2026-10-18 565 → 2026-10-24 565（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 mid · 依据 README sha `77aa56eace15` · [字段定义](../../DATASET.md)*
