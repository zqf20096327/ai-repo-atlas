# sidequery/sidemantic

⭐ 131 · Python · AGPL-3.0 · 推送 2026-10-20 · [GitHub](https://github.com/sidequery/sidemantic) · [官网](https://sidemantic.com) · 组织维护

**开源语义层运行时：统一定义治理指标并多格式复用**

Sidemantic 是一个开源语义层运行时（universal metrics layer），允许用户以 YAML、语义 SQL DDL 或 Python 原生定义治理指标，或从 Power BI TMDL/DAX、Cube、dbt MetricFlow、LookML、Malloy、Superset 等 15+ 格式导入既有语义模型，并自动检测格式。它运行在 DuckDB、PostgreSQL、BigQuery、Snowflake、ClickHouse、Spark 等数据仓库上，通过 CLI、语义 SQL、Python、HTTP/Arrow API、PostgreSQL 线协议、MCP 及 AI agent 消费指标。README 自述为年轻项目，较奇特功能可能有粗糙之处。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `viral` | AGPL-3.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 兼容 15+ 语义模型格式（TMDL/DAX、Cube、MetricFlow、LookML、Malloy、TML 等）并支持格式间转换与 TMDL 回写
- 多引擎支持：DuckDB 内置，PostgreSQL/BigQuery/Snowflake/ClickHouse/Databricks/Spark 以 extras 安装
- 多通道消费：CLI、语义 SQL、Python API、HTTP（JSON/Arrow）、PostgreSQL 线协议（供 Tableau/DBeaver 等 BI 工具连接）、MCP
- 提供 Claude Code 与 Codex 插件（modeler / webapp-builder 两个技能），兼容 SKILL.md 格式的其他 agent

## 适用场景

- 把已有的 LookML / Cube / Power BI 模型导入统一语义层再查询
- 让 BI 工具通过 PostgreSQL 协议或 HTTP API 消费治理指标
- 让 AI agent 通过 MCP 与插件技能查询语义模型、生成分析应用
- 从自有 CSV/Parquet/DuckDB 数据自动推断生成语义模型

## 场景标签

 · 领域:数据工程/分析基础设施

## 证据(README 行号)

> L3: Sidemantic is an open-source semantic runtime. Define governed metrics once—or import the semantic models you alread
> L8: - **Consume metrics anywhere:** semantic SQL, CLI, Python, HTTP/Arrow, PostgreSQL wire protocol, MCP, notebooks, Typ
> L14: Sidemantic ships Claude Code and Codex plugin metadata for two skills (`modeler` and `webapp-builder`). See Agent P

## 星数曲线

```mermaid
xychart-beta
    title "sidequery/sidemantic 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-23"]
    y-axis "stars" 130 --> 132
    line [131, 131]
```

2026-10-18 131 → 2026-10-23 131（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 mid · 依据 README sha `6bc63121d7ae` · [字段定义](../../DATASET.md)*
