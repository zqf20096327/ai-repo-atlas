# devopam/MCPg

⭐ 14 · Python · MIT · 推送 2026-10-28 · [GitHub](https://github.com/devopam/MCPg) · [官网](https://devopam.github.io/MCPg/) · 个人维护

**面向 AI agent 的 PostgreSQL MCP 服务器，279 个工具**

为 PostgreSQL 提供的 Model Context Protocol 服务器，让 AI agent 检查、查询、操作和调优 Postgres 数据库：覆盖目录内省、NL→SQL、结构 diff、混合搜索、图查询、健康检查、索引调优、vacuum、迁移等 279 个工具。默认只读模式，SQL 经 AST 白名单校验后执行；支持 stdio/HTTP/SSE 传输、多租户 SET ROLE、读副本路由、Prometheus 指标与审计日志。通过 pip、Docker 或源码安装，兼容 PG 14–19，集成 TimescaleDB/pgvector/PostGIS/Apache AGE。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 279 个工具：从数据查询到 DBA 级运维（EXPLAIN、索引调优、vacuum、迁移）
- 默认只读 + AST 白名单 SQL 校验，DDL/shell 等高危能力需显式开启
- NL→SQL 支持 22 个内置 provider，可按调用指定
- Prometheus /metrics 与凭据脱敏的审计事件，多租户与读副本路由

## 适用场景

- 在 Claude Desktop 或 Cursor 等 MCP 客户端中用自然语言查询和调优 Postgres
- 为 agent 提供带只读保护与审计的数据库访问通道
- 通过 HTTP 传输为 IDE 或 Web 应用提供多租户数据库工具服务

## 场景标签

`数据分析` · 领域:效率与自动化

## 证据(README 行号)

> L5: **A production-grade Model Context Protocol
> L7: tune a Postgres database — 279 tools spanning catalog introspection,
> L40: |Install|`pip install mcpg`|

## 星数曲线

```mermaid
xychart-beta
    title "devopam/MCPg 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-31"]
    y-axis "stars" 12 --> 15
    line [13, 14, 14]
```

2026-10-18 13 → 2026-10-31 14（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `2512577533dd` · [字段定义](../../DATASET.md)*
