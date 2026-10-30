# Cyb3rWard0g/agent-jupyter-toolkit

⭐ 25 · Python · Apache-2.0 · 推送 2026-10-22 · [GitHub](https://github.com/Cyb3rWard0g/agent-jupyter-toolkit) · 个人维护

**让 AI agent 通过 Jupyter 内核执行代码的 Python 工具包与 MCP 服务器**

由 Cyb3rWard0g（ Roberto Rodriguez ，安全研究领域个人维护者）提供的开源项目：核心是 Python 库，支持本地/远程/附着式异步 Jupyter 内核会话、代码执行、notebook 传输、单元格编辑、包管理、依赖跟踪、变量检查与 MIME 序列化；另发布 MCP 服务器 mcp-jupyter-notebook，将同一能力以标准化工具暴露给 AI agent，附带可选的 PostgreSQL 工具（schema 探索、查询转 DataFrame）与 Azure Monitor Logs/Sentinel 查询工具。通过 pip 安装，提供 Docker Compose 快速启动。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 本地/远程/附着式异步内核会话与代码执行
- MCP 服务器将工具集标准化暴露给任意 agent 框架
- 可选 PostgreSQL 工具：schema 探索、查询结果转 DataFrame
- 可选 Azure Monitor Logs 工具：KQL 查询以可见代码单元格形式执行

## 适用场景

- 为我的 AI agent 提供可持久化、可复现的 Jupyter 代码执行环境
- 让 agent 连接远程 Jupyter 服务器操作 notebook
- 让 agent 在内核内查询 PostgreSQL 或 Azure Monitor 日志并继续分析 DataFrame

## 场景标签

`Agent 框架` `数据分析` · 领域:Agent 开发

## 证据(README 行号)

> L8: An open-source project to provide the right tools for AI agents to execute
> L14: Model Context Protocol (MCP), the project also ships an MCP server that exposes

## 星数曲线

```mermaid
xychart-beta
    title "Cyb3rWard0g/agent-jupyter-toolkit 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 24 --> 26
    line [25, 25]
```

2026-10-18 25 → 2026-10-30 25（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `d86e9e549ea3` · [字段定义](../../DATASET.md)*
