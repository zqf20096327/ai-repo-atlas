# NiclasOlofsson/dbt-core-mcp

⭐ 15 · Python · MIT · 推送 2026-04-27 · [GitHub](https://github.com/NiclasOlofsson/dbt-core-mcp) · 个人维护

**让 AI 助手通过 MCP 操作 dbt 项目的服务器**

基于 Model Context Protocol 的 dbt 项目交互服务器，供 VS Code Copilot 等 AI 助手查询 dbt 项目元数据、模型/源/测试信息、血缘与影响分析、编译 SQL，并以桥接方式在用户自己的 Python 环境中执行 dbt 命令与测试；服务端本身不依赖 dbt-core 与适配器，自动检测用户项目的 dbt 版本与适配器（duckdb/snowflake/postgres 等）。限制：不支持 Python 模型，需 dbt Core 1.9.0+，安装途径为 VS Code 一键安装或 uvx/pipx 配置。

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

- 服务端自身零 dbt 依赖，通过桥接执行复用用户环境的 dbt
- 提供资源发现、血缘与影响分析、编译 SQL、CTE 查询等工具
- 智能选择：仅运行变更模型及下游测试
- 支持任意 dbt 适配器（duckdb/snowflake/postgres/bigquery/databricks）

## 适用场景

- 在 VS Code 中让 Copilot 执行 dbt 构建与下游测试
- 用自然语言查询项目模型、血缘与影响范围
- 调试模型时查看编译后 SQL 与 CTE 中间结果

## 场景标签

`数据分析` · 领域:效率与自动化

## 证据(README 行号)

> L57: This server provides tools to interact with dbt projects via the Model Context Protocol, enabling AI assistants to:
> L45: - **🔥 Zero dbt Dependencies**: Server has NO dbt-core, NO adapters - ultimate environment respect

## 星数曲线

```mermaid
xychart-beta
    title "NiclasOlofsson/dbt-core-mcp 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-31 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 mid · 依据 README sha `c0838e20fb13` · [字段定义](../../DATASET.md)*
