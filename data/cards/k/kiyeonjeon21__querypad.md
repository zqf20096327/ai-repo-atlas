# kiyeonjeon21/querypad

⭐ 27 · TypeScript · MIT · 推送 2026-07-25 · [GitHub](https://github.com/kiyeonjeon21/querypad) · [官网](https://querypad.io) · 个人维护

**本地优先的 AI 数据分析工作台：理解数据集后用 DuckDB 回答业务问题**

面向 CSV/Parquet/JSON 文件夹或 Postgres/MySQL/SQLite 数据库的 CLI 与浏览器应用。inspect 命令剖析每个文件、推断外键关系与置信度、生成语义模型（维度/度量/同义词，确定性无 AI），产物写入 .datactx/ 供 agent 读取；ask 命令运行 agentic 循环，将用户措辞映射到 schema 并编译成 join 防护的 SQL 在 DuckDB 上执行，含自纠错与结果核验；mcp 命令将同样的只读工具以 MCP 服务器形式交给 Claude Code/Cursor；另含引擎/agent/A/B 三类评测套件。Agent 循环 Anthropic 优先，OpenAI 回退到单次管线。全部工具只读，外部数据库附件为 READ_ONLY。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- inspect 推断外键关系与置信度并生成语义模型（确定性，无 AI）
- ask 的 agentic 循环含 resolve_terms 术语映射与 query_metric 防扇出 SQL 编译器
- mcp 命令向 Claude Code/Cursor 暴露同一套只读工具
- 内置引擎/agent/A/B 三层评测，附两个含陷阱的评测数据集

## 适用场景

- 在本地分析一堆 CSV 文件之间的关联并回答业务问题
- 让 Claude Code 或 Cursor 通过 MCP 成为数据分析师
- 在不写 SQL 的前提下弄清各表字段含义与正确 join 方式

## 场景标签

`数据分析` · 领域:效率与自动化

## 证据(README 行号)

> L5: QueryPad points an AI at a folder of CSV/Parquet/JSON files, profiles them,
> L92: querypad ask "total payment amount by user plan" ./data

## 星数曲线

```mermaid
xychart-beta
    title "kiyeonjeon21/querypad 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 26 --> 28
    line [27, 27]
```

2026-10-18 27 → 2026-10-26 27（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 mid · 依据 README sha `4db167df3403` · [字段定义](../../DATASET.md)*
