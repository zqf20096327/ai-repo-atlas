# mlr-org/mlr3db

⭐ 23 · R · LGPL-3.0 · 推送 2026-09-23 · [GitHub](https://github.com/mlr-org/mlr3db) · [官网](https://mlr3db.mlr-org.com) · 组织维护

**R 包：让 mlr3 透明对接数据库的数据后端扩展**

mlr3 生态的 R 扩展包，为 mlr3 机器学习框架提供三种 DataBackend，使其能透明地在数据库上执行机器学习任务：DataBackendDplyr 基于 dplyr/dbplyr 抽象支持 SQLite、MySQL、MariaDB、PostgreSQL 等 DBMS；DataBackendDuckDB 对接 DuckDB 并支持 Parquet 文件；DataBackendPolars 对接 polars。连接需用户通过 DBI 包自行建立，包内为 SQLite 与 DuckDB 提供 as_sqlite_backend() 与 as_duckdb_backend() 转换函数。面向使用 mlr3 的 R 开发者，经 CRAN 或 GitHub 安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `viral` | LGPL-3.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 三种数据后端：dplyr/dbplyr 抽象、DuckDB（含 Parquet 支持）、polars
- 支持 SQLite、MySQL、MariaDB、PostgreSQL 等多种 DBMS
- 提供 as_sqlite_backend()/as_duckdb_backend() 快捷转换函数

## 适用场景

- 在 mlr3 流程中直接对远程数据库数据训练模型，无需先导出到内存
- 用 DuckDB 后端读取 Parquet 文件做机器学习

## 场景标签

 · 领域:机器学习/数据工程

## 证据(README 行号)

> L11: Extends the mlr3 package with a DataBackend
> L15: - `DataBackendDplyr`: Relies internally on the abstraction of
> L19: - `DataBackendDuckDB`: Connector to

## 星数曲线

```mermaid
xychart-beta
    title "mlr-org/mlr3db 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 22 --> 24
    line [23, 23]
```

2026-10-18 23 → 2026-10-31 23（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `327262ff19e8` · [字段定义](../../DATASET.md)*
