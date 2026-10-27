# rasinmuhammed/misata

⭐ — · [GitHub]() · 个人维护

**按声明的业务结果精确生成多表关系型合成数据（Python+MCP）**

面向工程师、测试与数据团队的合成数据生成器：用户声明目标结果（收入曲线、欺诈率等）或提供 YAML schema、DDL、Django 模型、活数据库，Misata 求解出逐行数据使聚合结果误差为 $0.00，采用闭式 Gamma 条件和机制（arXiv:2606.08736），数据路径中不含机器学习模型。支持拓扑排序的外键解析（0 孤儿外键）、CHECK/UNIQUE/时序因果约束、15+ 行业的组合式文本生成，以及向量化速度。内置 MCP 服务器，供 Cursor、Claude Code、Windsurf 创建预填充的 SQLite 沙箱；可内省并填充 PostgreSQL/MySQL/SQLite 数据库。提供 pip 安装、CLI、pytest 插件与事件日志/进程挖掘输出。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 声明聚合结果后生成误差为 $0.00 的微行数据（闭式 Gamma 条件和机制）
- 拓扑 DAG 排序保证 0 孤儿外键，支持复合键、自引用层级与时序因果
- 内置 MCP 服务器，AI 编码 agent 可 2 秒创建预填充 SQLite 沙箱
- misata seed 内省 PostgreSQL/MySQL/SQLite 并在单事务中填充数据

## 适用场景

- 为 dbt/Spark/SQL 管道做已知答案测试，验证转换返回精确 KPI
- 给 Cursor/Claude Code/Windsurf 提供隔离预填充数据库来验证 SQL
- 为演示仪表盘填充带季节性的真实感数据，无 PII 暴露
- 校准欺诈率、违约曲线等指标用于风控与 AML 测试

## 场景标签

 · 领域:数据工程/合成数据生成

## 证据(README 行号)

> L29: Misata works in reverse: **you declare the outcome, and Misata solves for the individual rows that hit it to $0.00 
> L150: Misata includes a native Model Context Protocol (MCP) server. Cursor, Claude Code, and Windsurf can call `create_s
> L152: pip install "misata[mcp]" && misata mcp install --client all

## 星数曲线

```mermaid
xychart-beta
    title "rasinmuhammed/misata 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 69 --> 71
    line [70, 70]
```

2026-10-18 70 → 2026-10-26 70（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `f5cc107a6845` · [字段定义](../../DATASET.md)*
