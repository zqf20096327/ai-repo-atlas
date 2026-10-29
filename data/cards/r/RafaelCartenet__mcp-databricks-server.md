# RafaelCartenet/mcp-databricks-server

⭐ 43 · Python · MIT · 推送 2026-03-28 · [GitHub](https://github.com/RafaelCartenet/mcp-databricks-server) · 个人维护

**让 AI agent 访问 Databricks Unity Catalog 元数据的 MCP 服务器**

基于 Model Context Protocol 的服务器，通过 Databricks SDK 向 LLM agent 提供一组工具：列出/描述 Unity Catalog 的 catalog、schema、table，获取表级与 notebook/job 级血缘信息，并通过 SQL Warehouse 执行 SQL 查询。工具输出为 Markdown 格式供 LLM 消费；agent 可据此探索数据结构、分析血缘、读取 notebook 代码后自主构造查询。运行需 Python 3.10+、配置 Databricks 主机/Token/SQL Warehouse ID 环境变量，并要求相应的 UC 与 Warehouse 权限；支持 stdio 传输，可配合 Cursor 等 MCP 客户端使用。

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

- Unity Catalog 的 catalog/schema/table 列出与描述工具（含列级详情）
- 综合性血缘：上下游表、读写该表的 notebook 与 job、可读取 notebook 源码
- execute_sql_query 经 Databricks SQL Warehouse 执行 SQL 并返回结果
- 工具输出为 Markdown，面向 LLM 解析优化

## 适用场景

- 让编码/对话 agent 在 Databricks 中自主做数据发现与查询
- 分析表级与 notebook/job 级血缘做影响分析
- 让 agent 阅读 notebook 中的转换逻辑与数据质量检查

## 场景标签

`数据分析` · 领域:效率与自动化

## 证据(README 行号)

> L16: This Model Context Protocol (MCP) server is designed to interact with Databricks, with a strong focus on leveraging
> L45: This MCP server provides a suite of tools designed to empower an LLM agent interacting with Databricks:

## 星数曲线

```mermaid
xychart-beta
    title "RafaelCartenet/mcp-databricks-server 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 42 --> 44
    line [43, 43]
```

2026-10-18 43 → 2026-10-29 43（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `9b3690de8040` · [字段定义](../../DATASET.md)*
