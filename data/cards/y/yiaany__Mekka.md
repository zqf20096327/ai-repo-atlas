# yiaany/Mekka

⭐ 21 · TypeScript · NOASSERTION · 推送 2026-10-22 · [GitHub](https://github.com/yiaany/Mekka) · 个人维护

**面向人与 AI agent 的 SQLite/libSQL 后端（Baas）实验项目**

基于 Bun/TypeScript 的实验性 source-available 后端：在本地 SQLite 与远程 libSQL 两种数据配置上提供统一类型化 Data API、Auth（JWT/OAuth/OTP）、对象存储、Realtime 原语、迁移、策略与 Studio 管理界面。面向 agent 的部分通过受限 MCP 通道实现：一小时作用域 token、schema 只读为默认、行读取需单独授权、写操作走隔离 preview 分支并需 Studio 人工审批后一次性晋升。不声称完整 PostgreSQL/Supabase 兼容，不支持的操作显式报错。npx 一键启动，提供 Docker 构建。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 本地 SQLite 与远程 libSQL 双数据配置，MEKKA_DATA_ENGINE 切换
- 受限 MCP 面：schema/行读/迁移提案/preview/晋升分能力门控
- agent 写入经隔离 preview + Studio 人工一次性审批后晋升
- Auth/Storage/Realtime/迁移/Studio 同仓提供，npx 一键启动

## 适用场景

- 本地快速搭建带认证与存储的 SQLite 应用后端
- 让 AI agent 以受限 token 安全读写数据库，无需交出凭据
- 通过 Studio 界面管理表、Auth 用户与 agent 审批

## 场景标签

 · 领域:后端服务/数据库与 AI agent 基础设施

## 证据(README 行号)

> L7: Typed data API · local Auth · object Storage · Realtime primitives · Studio · scoped MCP access.
> L142: - One-hour tokens bound to a single tenant tuple and application session
> L172: An AI agent should not need your database password or libSQL JWT. Mekka gives it a short-lived token bound to one 

## 星数曲线

```mermaid
xychart-beta
    title "yiaany/Mekka 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 20 --> 22
    line [21, 21]
```

2026-10-18 21 → 2026-10-28 21（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `39ec0760cfc1` · [字段定义](../../DATASET.md)*
