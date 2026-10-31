# Strom-Capital/mcp-server-db2i

⭐ 27 · TypeScript · MIT · 推送 2026-10-29 · [GitHub](https://github.com/Strom-Capital/mcp-server-db2i) · [官网](https://db2i-mcp.com/) · 组织维护

**让 Claude/Cursor 等查询 IBM Db2 for i 的只读 MCP 服务器**

Model Context Protocol 服务器，使 Claude Desktop、Claude Code、Cursor 等 AI 客户端能够查询和检视 IBM i（AS/400）上的 Db2 for i 数据库。仅允许 SELECT 查询，通过 IBM i Access ODBC（默认）、JT400 JDBC 或 SSH 上的 Mapepire 连接；用户以自己的 IBM i 账号登录。提供库白名单、列掩码、审计日志、OAuth 2.1 远程接入、多系统连接配置，以及 YAML 定义的 ERP 业务 SQL 工具。npm 全局安装或 Docker 运行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 只读 SELECT 查询，带结果限制、超时取消与查询校验
- 三种驱动：ODBC（默认）/JT400 JDBC/Mapepire over SSH
- 库白名单、列掩码、每次调用的 JSON 审计日志
- OAuth 2.1 远程客户端接入与多 IBM i 系统配置

## 适用场景

- 用 Claude/Cursor 对 IBM i 上的 ERP 数据做自然语言即席分析
- 为构建 REST API 的 agent 提供表结构与 SQL 校验
- BI/ETL 前的源表剖析、DDL 提取与日志（journal）状态检查

## 场景标签

`数据分析` · 领域:效率与自动化

## 证据(README 行号)

> L16: `mcp-server-db2i` is a Model Context Protocol (MCP) server for IBM Db2 for i (Db2i) on IBM i (AS/400). It enables A
> L24: AI clients connect to the MCP Server in one of two ways. Local clients such as Claude Desktop, Claude Code and Curs

## 星数曲线

```mermaid
xychart-beta
    title "Strom-Capital/mcp-server-db2i 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-31"]
    y-axis "stars" 25 --> 28
    line [26, 27, 27]
```

2026-10-18 26 → 2026-10-31 27（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `ee9d9fae2991` · [字段定义](../../DATASET.md)*
