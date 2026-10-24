# aliyun/alibabacloud-dms-mcp-server

⭐ — · [GitHub]() · 组织维护 · 中文 README

**给 AI Agent 用的多云数据访问 MCP Server，统一接入 40+ 数据源**

阿里云开源的 DMS MCP Server，作为 AI 时代的数据安全访问网关：为 MCP 客户端提供 40+ 数据库/数据仓库（MySQL、PostgreSQL、Oracle、ClickHouse、BigQuery 及阿里云 RDS/PolarDB/Maxcompute 等）的统一接入。内置 NL2SQL 算法，将自然语言问题转为 SQL 并执行；提供实例/库/表/字段/行级权限控制、高风险 SQL 识别阻断与 SQL 审计日志。支持多实例与单数据库两种模式，仅绑定 127.0.0.1，需阿里云 AK/SK 与 DMS 权限。另附独立于 MCP 协议的 Agent Skills。

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

- 统一接入 40+ 数据库/数据仓库，覆盖阿里云全系列与主流数据库
- 内置 NL2SQL：自然语言问题生成 SQL 并执行返回结果
- 实例/库/表/字段/行级权限控制与高风险 SQL 识别阻断、SQL 审计
- 提供 16 个 MCP 工具，另附基于 OpenAPI 的 AI Agent Skills

## 适用场景

- 让 Claude/Cursor 等 MCP 客户端用自然语言查询公司数据库
- DBA 统一管理并访问多环境异构数据库实例
- 数据分析师以自然语言做订单、用户等业务数据查询
- 在 SQL 执行场景下按最小权限与审计要求做安全管控

## 场景标签

`数据分析` · 领域:效率与自动化

## 证据(README 行号)

> L16: - **Built-in NL2SQL Algorithm**: Based on natural language input questions, it intelligently matches data tables, u
> L94: |askDatabase|Natural language querying of a database (NL2SQL + execute SQL).|Single Database Mode|

## 星数曲线

```mermaid
xychart-beta
    title "aliyun/alibabacloud-dms-mcp-server 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-19"]
    y-axis "stars" 53 --> 55
    line [54, 54]
```

2026-10-18 54 → 2026-10-19 54（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `cc2baa219acc` · [字段定义](../../DATASET.md)*
