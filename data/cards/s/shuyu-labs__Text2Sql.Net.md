# shuyu-labs/Text2Sql.Net

⭐ 139 · C# · Apache-2.0 · 推送 2025-11-08 · [GitHub](https://github.com/shuyu-labs/Text2Sql.Net) · [官网](https://antsk.cn) · 个人维护 · 中文 README

**.NET 自然语言转 SQL 工具，支持 MCP 集成 IDE**

基于 .NET 与 Semantic Kernel 开发的 Text2SQL 工具，面向开发者和数据分析师：输入自然语言描述，结合 LLM 与 SQL 解析技术生成查询语句，并通过语法校验检查正确性。支持 SQL Server、MySQL、PostgreSQL、SQLite 四种数据库（IDatabaseProvider 策略模式适配），内置 Schema 向量化训练与语义相似搜索、问答示例学习机制（相关度阈值 0.7）。可作为 MCP 服务器向 Cursor、Trae 等 IDE 提供 7 个 Text2SQL 工具，前端使用 Blazor。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 自然语言生成 SQL 并自动语法校验，支持 4 种主流数据库
- 可作为 MCP 服务器提供 generate_sql/execute_sql 等 7 个工具
- Schema 向量训练与问答示例语义搜索（默认阈值 0.7）提升生成准确性
- 基于聊天历史理解查询意图

## 适用场景

- 在 Cursor/Trae 等 IDE 中用自然语言查询数据库
- 数据分析师快速生成复杂统计与多表关联查询
- 将 Text2SQL 能力作为 MCP 服务集成到工具链

## 场景标签

`数据分析` · 领域:效率与自动化

## 证据(README 行号)

> L6: Text2Sql.Net是一个基于.NET平台的自然语言转SQL工具，旨在帮助开发者和数据分析师通过简单的自然语言描述快速生成数据库查询语句。项目结合了大型语言模型(LLM)和传统SQL解析技术，支持多种主流数据库。
> L75: Text2Sql.Net 集成了 Model Context Protocol，可以作为 MCP 服务器为各种 AI 开发工具提供 Text2SQL 功能。
> L80: - `generate_sql`: 根据自然语言生成SQL查询

## 星数曲线

```mermaid
xychart-beta
    title "shuyu-labs/Text2Sql.Net 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 138 --> 140
    line [139, 139]
```

2026-10-18 139 → 2026-10-31 139（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 mid · 依据 README sha `05fa26067cc6` · [字段定义](../../DATASET.md)*
