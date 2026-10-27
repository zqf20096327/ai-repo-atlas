# parkervg/blendsql

⭐ 169 · Python · Apache-2.0 · 推送 2026-10-03 · [GitHub](https://github.com/parkervg/blendsql) · [官网](https://parkervg.github.io/blendsql/) · 个人维护

**SQL 超集查询语言：在结构化与非结构化数据上混合 SQL 与本地 LLM**

BlendSQL 是 SQL 的超集，允许在查询中嵌入 LLM 函数（LLMQA/LLMMap/LLMJoin 等），对表格、文本、图像等异构数据源做混合问答与问题分解。机制上：复用现有 DBMS（SQLite/PostgreSQL/DuckDB/Pandas）的优化能力，只将逻辑必需的数据子集传给 LLM；基于 sqlglot 遍历抽象语法树以减少 LLM 调用；借助 guidance 做类型约束解码，保证输出语法有效；支持 vLLM 异步并行与基于 diskcache 的函数缓存。以 Python 库形式经 pip 安装，面向开发者提供，附论文引用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- SQL 超集，在查询中调用类型约束的 LLM 函数（LLMQA/LLMMap/LLMJoin）
- 支持 SQLite、PostgreSQL、DuckDB、Pandas 多种 DBMS，编译回原生 SQL 执行
- sqlglot 语法树分析最小化 LLM 调用，guidance 约束解码保证输出有效
- vLLM 优化集成与异步并行，diskcache 支持函数缓存

## 适用场景

- 在表格与文本文档混合数据上做自然语言问答
- 对数据库行做 LLM 分类、多标签分类与 join
- 以声明式 SQL 程序分解复杂问题并约束 LLM 输出类型

## 场景标签

`RAG` `数据分析` · 领域:效率与自动化

## 证据(README 行号)

> L35: BlendSQL is a *superset of SQL* for problem decomposition and hybrid question-answering with LLMs.
> L39: - 🥤 ...operations over heterogeneous data sources (e.g. tables, text, images)
> L62: - Supports many DBMS 💾

## 星数曲线

```mermaid
xychart-beta
    title "parkervg/blendsql 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 168 --> 170
    line [169, 169]
```

2026-10-18 169 → 2026-10-27 169（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `68e2bad18b64` · [字段定义](../../DATASET.md)*
