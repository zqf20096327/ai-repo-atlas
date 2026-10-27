# yzxingtu2026/novusai-saas

⭐ 27 · Python · MIT · 推送 2026-10-18 · [GitHub](https://github.com/yzxingtu2026/novusai-saas) · [官网](https://nvuai.cc) · 组织维护 · 中文 README

**面向二次开发的多租户 AI SaaS 开发框架**

基于 FastAPI + Vue 3 + PostgreSQL 的多租户 SaaS 开发框架，内置 admin/tenant/user 三端应用、RBAC 权限、插件系统、Agent→Skill→AIGateway 的 AI 运行链路、RAG 相关文档处理、Celery 异步任务、Socket.IO 实时通知、CRUD 代码生成与 Alembic 迁移等能力，定位为企业级 SaaS 与 AI 原生业务系统的工程底座。提供源码开发与 Docker Compose 全栈两种启动方式，附生产编排参考文件。环境需 Python 3.10+、Node.js 20.19+、PostgreSQL、Redis。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Agent → Skill → AIGateway 的 AI 业务链路，可扩展模型/技能/知识库/工具
- admin/tenant/user 三端隔离 + 多租户数据访问模型
- 后端/前端插件系统与插件生命周期、扩展点
- CRUD 代码生成与回滚清单机制

## 适用场景

- 作为企业级 SaaS 或行业应用的二次开发底座
- 构建带 AI Agent 与知识库的多租户业务系统
- 通过插件与扩展目录组织交付项目

## 场景标签

`RAG` `Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L14: NovusAI SaaS 是一个面向二次开发的多租户 AI SaaS 开发框架。它提供平台管理端、企业端、用户端、权限体系、插件系统、AI Agent 运行链路、实时通知、附件存储、代码生成与数据库迁移等基础能力，适合作为企业级 
> L27: |AI 运行时|支持 **Agent → Skill → AIGateway** 的业务 AI 链路，可扩展模型、技能、知识库与工具调用。|

## 星数曲线

```mermaid
xychart-beta
    title "yzxingtu2026/novusai-saas 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-27"]
    y-axis "stars" 25 --> 28
    line [26, 27, 27]
```

2026-10-18 26 → 2026-10-27 27（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 mid · 依据 README sha `8a8d755dd464` · [字段定义](../../DATASET.md)*
