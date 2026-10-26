# ahaodev/shadmin

⭐ 174 · TypeScript · MIT · 推送 2026-10-25 · [GitHub](https://github.com/ahaodev/shadmin) · [官网](https://shadmin.ahaodev.com) · 个人维护 · 中文 README

**Go+React 全栈 RBAC 权限管理系统模板，含面向 AI Agent 的 CLI**

基于 Gin、Ent ORM、Casbin、Shadcn UI、TanStack Router 与 Tailwind CSS 的全栈后台权限管理系统：采用 Controller→Usecase→Repository 分层架构，提供基于 Casbin 的细粒度 RBAC（API 与菜单）、JWT 双令牌认证、后端驱动的动态菜单、全局搜索、数据看板与明暗主题；缓存可选 Redis 或 go-cache，数据库默认 SQLite 并支持 PostgreSQL/MySQL。面向需要搭建后台权限系统的开发者，文档部分包含面向 AI Agent 的 CLI 说明。运行需 Go 1.27.1+ 与 Node.js 22+/pnpm 11+，通过 git clone 源码方式启动。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Casbin 驱动的细粒度 RBAC，覆盖 API 与菜单权限
- JWT access+refresh 令牌认证与前端权限守卫（usePermission/hasPermission）
- 多数据库支持：SQLite（默认）、PostgreSQL、MySQL
- 面向 AI Agent 的 CLI 文档与双语架构/部署文档

## 适用场景

- 作为企业后台管理系统的起点模板，快速获得 RBAC 权限体系
- 让 AI Agent 通过 CLI 操作项目相关任务
- 搭建带动态菜单与权限感知 UI 的管理后台

## 场景标签

 · 领域:Web 后台管理/权限系统

## 证据(README 行号)

> L3: **An Enterprise-Grade Full-Stack RBAC Permission Management System Built with Go + React**
> L68: - CLI for AI agents · 面向 AI Agent 的 CLI(中文)

## 星数曲线

```mermaid
xychart-beta
    title "ahaodev/shadmin 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-26"]
    y-axis "stars" 172 --> 175
    line [173, 174, 174]
```

2026-10-18 173 → 2026-10-26 174（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `aa6878603c23` · [字段定义](../../DATASET.md)*
