# vstorm-co/database-pydantic-ai

⭐ 22 · Python · MIT · 推送 2026-02-07 · [GitHub](https://github.com/vstorm-co/database-pydantic-ai) · [官网](https://vstorm-co.github.io/database-pydantic-ai/) · 组织维护

**给 Pydantic AI agent 的 SQL 数据库工具集：查库表与执行查询**

为 Pydantic AI agent 提供数据库访问能力的 Python 工具集：通过 create_database_toolset() 向 agent 提供 5 个工具（列出表、获取 schema、描述表结构、分析查询计划、执行 SQL）。后端支持 SQLite（aiosqlite）与 PostgreSQL（asyncpg），内置安全控制：默认只读模式拦截 15 个危险 SQL 关键词、多语句拒绝、注释感知解析、CTE 写操作校验，以及查询超时与行数上限。以 pip 包分发，需 Python 3.10+，面向构建数据分析/BI/SQL 助手类 agent 的开发者。

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

- 5 个数据库工具：list_tables / get_schema / describe_table / explain_query / query
- SQLite 与 PostgreSQL 双后端（aiosqlite / asyncpg）
- 默认只读模式拦截 15 个危险 SQL 关键词，含注释感知解析与 CTE 校验
- 查询超时与行数上限（默认 100 行、30 秒超时）

## 适用场景

- 构建可查询数据库做数据分析的 AI agent
- 让 BI 机器人以只读方式访问生产数据库
- 自动发现并梳理数据库 schema 用于文档生成

## 场景标签

`数据分析` · 领域:效率与自动化

## 证据(README 行号)

> L18: **Database Toolset** provides everything your Pydantic AI agent needs to explore schemas, query data, and understan
> L89: The `create_database_toolset()` provides 5 tools to the agent:

## 星数曲线

```mermaid
xychart-beta
    title "vstorm-co/database-pydantic-ai 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 21 --> 23
    line [22, 22]
```

2026-10-18 22 → 2026-10-28 22（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `4d24c94d58b0` · [字段定义](../../DATASET.md)*
