# bodo-ai/PyDough

⭐ 43 · Python · Apache-2.0 · 推送 2026-10-23 · [GitHub](https://github.com/bodo-ai/PyDough) · 组织维护

**Python 分析型 DSL：以逻辑文档模型表达问题并翻译为 SQL 执行**

PyDough 是一种嵌入 Python 的分析 DSL，基于知识图谱语义层（含层级与关系）表达分析问题，抽象掉 join 与聚合键等 SQL 细节，采用惰性求值，请求时翻译为任意 SQL 方言在数据库上执行。主要执行方式是 Jupyter notebook 的 cell magic。其设计兼顾人类书写与 LLM 生成：问题文本与 PyDough 代码的相关性更强，使 LLM 生成查询代码更简单，并可在多种数据库间移植。通过 pip 安装，测试覆盖 SQLite、Snowflake、MySQL、Postgres、Trino、Oracle、Databricks、DuckDB 等方言。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Python DSL + 知识图谱语义层表达分析问题
- 惰性求值，执行时翻译为任意 SQL 方言
- 抽象 join/聚合语义，代码比等价 SQL 更紧凑
- 设计目标之一是便于 LLM 生成查询代码

## 适用场景

- 用 Python 语义层替代手写复杂 SQL 做数据分析
- 让 LLM 生成更可靠的分析查询代码（text-to-analytics）
- 同一份查询代码在多种 SQL 数据库间移植执行

## 场景标签

`数据分析` · 领域:效率与自动化

## 证据(README 行号)

> L39: PyDough as a DSL has several benefits over other solutions, both for human use and LLM generation:
> L42: - When a question is being asked, the PyDough code to answer it will look more similar to the text of the question 

## 星数曲线

```mermaid
xychart-beta
    title "bodo-ai/PyDough 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 41 --> 43
    line [42, 42]
```

2026-10-18 42 → 2026-10-25 42（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `2210e0458876` · [字段定义](../../DATASET.md)*
