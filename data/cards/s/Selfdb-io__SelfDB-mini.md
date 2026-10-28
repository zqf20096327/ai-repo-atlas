# Selfdb-io/SelfDB-mini

⭐ 26 · C · MIT · 推送 2025-12-15 · [GitHub](https://github.com/Selfdb-io/SelfDB-mini) · [官网](https://selfdb.io) · 组织维护

**自托管后端即服务最小实现：FastAPI+React+PostgreSQL 全栈**

SelfDB 的精简实现，提供 FastAPI 后端、React+TypeScript 前端、PostgreSQL 数据库与 PgBouncer 连接池的完整技术栈。通过 setup.sh 一键构建并启动 Docker 容器服务，支持端口自定义配置、热重载本地开发、基于 OpenAPI 规范的 TypeScript/Python/Swift SDK 生成，以及 Schemathesis 契约测试、Apache Bench 与 Locust 负载测试。内置备份恢复系统：cron 定时备份、Web UI 与 CLI 恢复、登录页一键恢复。面向需要自托管后端的开发者。另提供付费 Stable 版本，宣称性能更优并面向生产与 AI 应用场景。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- FastAPI + React + PostgreSQL + PgBouncer 容器化全栈，setup.sh 一键启动
- 基于 OpenAPI 规范生成多语言客户端 SDK（hey-api / Swagger Codegen）
- Schemathesis 契约测试 + Apache Bench / Locust 负载测试工具链
- 备份系统：cron 调度、Web UI 与 CLI 恢复、服务器迁移登录页恢复

## 适用场景

- 自托管部署一套带前端管理界面的后端与数据库服务
- 为 API 项目生成类型安全的 TypeScript 客户端 SDK
- 对后端 API 做契约测试与负载测试
- 定时备份数据库并迁移到新服务器

## 场景标签

 · 领域:后端即服务/数据库

## 证据(README 行号)

> L15: |**Best For**|Testing & hobby|**Production & AI apps**|
> L22: A minimal implementation of SelfDB with only the essential features: **FastAPI** backend, **React + TypeScript** fr

## 星数曲线

```mermaid
xychart-beta
    title "Selfdb-io/SelfDB-mini 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 25 --> 27
    line [26, 26]
```

2026-10-18 26 → 2026-10-28 26（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 low · 依据 README sha `84238e35f3f4` · [字段定义](../../DATASET.md)*
