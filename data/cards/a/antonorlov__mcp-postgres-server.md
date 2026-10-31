# antonorlov/mcp-postgres-server

⭐ 24 · TypeScript · MIT · 推送 2026-09-16 · [GitHub](https://github.com/antonorlov/mcp-postgres-server) · [官网](https://www.npmjs.com/package/mcp-postgres-server) · 个人维护

**让 MCP 客户端通过工具查询 PostgreSQL 的 MCP 服务器**

面向 VS Code、Cursor、Claude Code、Codex、Windsurf 等 stdio MCP 客户端的 PostgreSQL 服务器：通过 DATABASE_URL 或 PG_* 环境变量配置，向模型暴露 query、list_schemas、list_tables、describe_table、execute 等工具。默认只读，由引擎以 BEGIN READ ONLY 事务强制执行；写入需显式设置 PG_ALLOW_WRITE=true。支持本地/Docker/RDS/Neon/Supabase 数据库、SSL、预编译参数、结果字节上限、可选 SSH 隧道（强制主机密钥校验）。需 Node.js 20+，四个运行时依赖。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 默认只读，由引擎 BEGIN READ ONLY 事务强制而非客户端 SQL 解析
- 结果字节预算（默认 32 KiB）与 truncated 标记，避免刷爆模型上下文
- 支持本地/Docker/RDS/Neon/Supabase，SSL 多模式与自定义 CA
- 可选 SSH 隧道，主机密钥指纹强制校验（fail-closed）

## 适用场景

- 让 Claude Code/Cursor 等 MCP 客户端直接查询我的 Postgres 数据库
- 以只读模式让模型安全地浏览数据库结构与数据
- 通过 SSH 堡垒机访问内网数据库

## 场景标签

 · 领域:AI 基础设施/数据库

## 证据(README 行号)

> L6: A Model Context Protocol (MCP) server for PostgreSQL: local, Docker, RDS, Neon,
> L29: The same JSON works in any MCP client that speaks stdio: VS Code, Cursor, Claude Code, Codex, Windsurf.

## 星数曲线

```mermaid
xychart-beta
    title "antonorlov/mcp-postgres-server 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 23 --> 25
    line [24, 24]
```

2026-10-18 24 → 2026-10-31 24（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `6126d2b91f0b` · [字段定义](../../DATASET.md)*
