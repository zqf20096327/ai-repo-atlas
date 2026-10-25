# ConnorBritain/mssql-mcp-server

⭐ 36 · C# · MIT · 推送 2026-08-04 · [GitHub](https://github.com/ConnorBritain/mssql-mcp-server) · 个人维护

**面向 DBA 的 SQL Server MCP 服务器，20 个工具覆盖探查与管理**

基于 Node.js 的 Model Context Protocol 服务器，连接 Microsoft SQL Server，向 MCP 客户端（Windsurf、Claude Desktop 等）暴露 20 个工具：模糊搜索表/列的语义式 schema 发现、表画像（空值率/基数/分位数）、外键与依赖分析、带预览确认的数据增删改、DDL、命名 SQL 脚本执行。支持 SQL/Windows/Azure AD 三种认证、多环境 JSON 配置、审计日志（JSON Lines、参数自动脱敏）与可插拔密钥链（env/dotenv/file）。面向在受监管环境与 UAT 中配合 AI 助手操作企业数据库的 DBA 与数据工程师。需 Node.js 18+（推荐 20 LTS）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- search_schema 模糊分页搜索表/列，控制上下文窗口占用
- update/delete 先预览受影响行并要求显式确认
- 全工具调用写入 JSON Lines 审计日志并自动脱敏参数
- ${secret:NAME} 占位符 + env/dotenv/file 密钥提供者链

## 适用场景

- 让 Claude Desktop 等 MCP 客户端直接探查和操作 SQL Server 数据库
- 在 UAT 环境用 AI 验证数据管道后安全推进到生产
- DBA 通过预审批命名脚本执行受治理的 SQL 操作

## 场景标签

 · 领域:数据库管理/AI 工具链

## 证据(README 行号)

> L6: **Enterprise-grade Model Context Protocol server for Microsoft SQL Server.**
> L41: - **MCP-native** – Works with Windsurf, Claude Desktop, and any MCP-compatible client.

## 星数曲线

```mermaid
xychart-beta
    title "ConnorBritain/mssql-mcp-server 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-25"]
    y-axis "stars" 33 --> 36
    line [34, 35, 35]
```

2026-10-18 34 → 2026-10-25 35（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `262f7f9df329` · [字段定义](../../DATASET.md)*
