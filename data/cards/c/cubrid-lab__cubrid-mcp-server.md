# cubrid-lab/cubrid-mcp-server

⭐ 33 · Python · MIT · 推送 2026-10-28 · [GitHub](https://github.com/cubrid-lab/cubrid-mcp-server) · [官网](https://cubrid-lab.github.io/cubrid-mcp-server/) · 组织维护

**CUBRID 数据库的 MCP 服务器：让 LLM 安全查 schema 与执行只读查询**

基于 pycubrid 与 FastMCP 实现的 Model Context Protocol 服务器，向 MCP 客户端（Claude Desktop、Claude Code、Cursor）暴露 CUBRID 数据库的 schema 检查与只读 SQL 查询能力。提供 12 个工具（表名列表、schema 定义、索引、执行计划、行数统计、只读查询等）、只读 MCP Resources（含 agent 指南与全库 schema 索引）以及 10 个纯引导型 Prompt 模板。默认只读：代码级 SQL 白名单仅放行 SELECT/SHOW/DESC/DESCRIBE/WITH，并拒绝 INCR/DECR、序列推进等 SELECT 内数据变更；写模式（execute_write 单条 DML）默认关闭需显式开启。支持环境变量配置与同进程多数据库连接。

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

- 12 个 MCP 工具覆盖 schema 检查、执行计划（SHOW TRACE）、只读查询与健康检查
- 默认只读 SQL 白名单，拒绝多语句、DDL、事务控制、CALL/EVALUATE/KILL 及 SELECT 内数据变更
- opt-in 写模式：execute_write 仅接受单条 INSERT/UPDATE/DELETE，原子事务执行
- 同进程多连接：通过 CUBRID_CONNECTIONS 与 CUBRID_<NAME>_* 变量服务多个 CUBRID 数据库
- opt-in 审计日志：每条执行语句输出一条脱敏 JSON 记录到 stderr

## 适用场景

- 让 Claude Desktop/Cursor 等 MCP 客户端安全浏览我的 CUBRID 数据库结构
- 通过对话让 AI 用只读查询分析数据库中的数据
- 在开启写模式后让 AI 执行受控的单条 DML 语句

## 场景标签

`数据分析` · 领域:效率与自动化

## 证据(README 行号)

> L8: A Model Context Protocol server for CUBRID, enabling LLMs to safely inspect schemas and execute read-only queries vi
> L161: ## MCP Client Integration

## 星数曲线

```mermaid
xychart-beta
    title "cubrid-lab/cubrid-mcp-server 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 31 --> 33
    line [32, 32]
```

2026-10-18 32 → 2026-10-28 32（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `0d2c46179b94` · [字段定义](../../DATASET.md)*
