# mustafahasankhan/duckdb-mcp-server

⭐ 19 · Python · MIT · 推送 2026-03-10 · [GitHub](https://github.com/mustafahasankhan/duckdb-mcp-server) · 个人维护

**让 AI 助手通过 MCP 直接用 SQL 查询 DuckDB 的服务器**

面向 MCP 兼容客户端（Claude Desktop、Cursor、VS Code 等）的 DuckDB 接入服务器：AI 助手可对本地 CSV/Parquet/JSON 文件及 S3/GCS 存储桶执行任意 SQL（结果上限 1 万行），并提供 schema 描述、统计摘要、可视化建议与跨调用会话等工具；内置三个 SQL/数据导入/可视化文档资源。需 Python 3.10+ 与 MCP 客户端，pip 安装后以命令行参数指定数据库路径，支持只读模式与 AWS 凭证链解析。

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

- 对本地文件与 S3/GCS 执行任意 SQL（结果上限 10,000 行）
- analyze_schema / analyze_data / suggest_visualizations 等分析工具
- create_session 支持跨调用上下文跟踪
- 支持只读模式与 AWS 环境变量/profile/凭证链三种凭证解析

## 适用场景

- 让 Claude Desktop 等客户端直接分析本地 CSV/Parquet 数据
- 通过对话缓存并查询 S3 上的 parquet 数据
- 对数据库做统计摘要与可视化建议而无需手写 SQL

## 场景标签

`数据分析` · 领域:效率与自动化

## 证据(README 行号)

> L7: A Model Context Protocol (MCP) server that gives AI assistants full access to DuckDB — query local files, S3 buckets
> L17: This server exposes DuckDB to any MCP-compatible client (Claude Desktop, Cursor, VS Code, etc.). The assistant can:

## 星数曲线

```mermaid
xychart-beta
    title "mustafahasankhan/duckdb-mcp-server 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 18 --> 20
    line [19, 19]
```

2026-10-18 19 → 2026-10-31 19（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `8e516f7bef1b` · [字段定义](../../DATASET.md)*
