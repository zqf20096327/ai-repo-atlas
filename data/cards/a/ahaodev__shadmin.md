# ahaodev/shadmin

⭐ 178 · TypeScript · MIT · 推送 2026-11-24 · [GitHub](https://github.com/ahaodev/shadmin) · [官网](https://shadmin.ahaodev.com) · 个人维护 · 中文 README

**Go+React 全栈 RBAC 权限管理系统脚手架**

以 Go（Gin + Ent ORM + Casbin）为后端、React + TypeScript + Shadcn UI + Tailwind 为前端的全栈 RBAC 权限管理系统，采用 Controller→Usecase→Repository 分层架构。功能覆盖 API 与菜单的细粒度角色权限控制、后端驱动的动态菜单、全局搜索、数据可视化仪表盘、明暗主题与响应式布局。缓存支持 Redis 或 go-cache（可选），默认使用 SQLite，亦支持 PostgreSQL 与 MySQL。默认账号 admin/admin123，首次启动自动初始化数据库并写入种子数据，提供 Swagger 文档，另有面向 AI agent 的 CLI 文档入口。MIT 许可。

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

- 基于 Casbin 的 API 与菜单细粒度 RBAC 权限控制
- 后端驱动的动态菜单树，按权限渲染
- SQLite（默认）/PostgreSQL/MySQL 多数据库开箱即用
- 提供 Swagger API 文档与 AI agent CLI 文档入口

## 适用场景

- 搭建需要角色权限管理的中后台管理系统
- 以 Go + React 技术栈为基础二次开发企业内部系统
- 参考 Clean Architecture 分层组织 Go 后端代码

## 场景标签

 · 领域:企业管理系统/开发脚手架

## 证据(README 行号)

> L3: **An Enterprise-Grade Full-Stack RBAC Permission Management System Built with Go + React**
> L64: - CLI for AI agents

## 星数曲线

```mermaid
xychart-beta
    title "ahaodev/shadmin 星数(近 7 点)"
    x-axis ["2026-10-25", "2026-11-02", "2026-11-06", "2026-11-08", "2026-11-12", "2026-11-22", "2026-11-27"]
    y-axis "stars" 172 --> 179
    line [174, 173, 174, 175, 176, 177, 178]
```

2026-10-25 174 → 2026-11-27 178（+4）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 low · 依据 README sha `ecdc9c2a5bd6` · [字段定义](../../DATASET.md)*
