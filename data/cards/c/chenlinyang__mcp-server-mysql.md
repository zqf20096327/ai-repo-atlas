# chenlinyang/mcp-server-mysql

⭐ 22 · JavaScript · MIT · 推送 2025-11-16 · [GitHub](https://github.com/chenlinyang/mcp-server-mysql) · 个人维护 · 中文 README

**面向 Claude Code 的 MySQL MCP 服务器：只读为主、可选写入**

基于 Node.js 的模型上下文协议（MCP）服务器，基于 @benborba29/mcp-server-mysql 针对 Claude Code 做增强：让 LLM 检查数据库模式、执行 SQL 查询。默认只读，INSERT/UPDATE/DELETE/DDL 需逐项用环境变量启用；支持 SSH 隧道、跨库查询拦截、多数据库模式与模式级权限、预准备语句、速率限制、查询复杂度分析与结果缓存。要求 Node.js v20+ 与 MySQL 5.7+，提供全局 npm 安装或源码克隆运行两种方式。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 默认只读事务，写入操作（INSERT/UPDATE/DELETE/DDL）需环境变量逐项启用
- 内置远程数据库 SSH 隧道与 Claude 启动/停止钩子
- 多数据库模式与模式特定权限（SCHEMA_*_PERMISSIONS）
- 预准备语句、速率限制、查询复杂度分析与结果缓存

## 适用场景

- 在 Claude Code 中用自然语言查询和分析 MySQL 数据库
- 通过 SSH 隧道安全访问远程数据库
- 按数据库粒度控制 LLM 的读写权限

## 场景标签

`数据分析` · 领域:效率与自动化

## 证据(README 行号)

> L26: 一个模型上下文协议服务器，通过 SSH 隧道提供对 MySQL 数据库的访问。该服务器使 Claude 和其他大型语言模型能够安全地检查数据库模式和执行 SQL 查询。
> L173: - mysql_query

## 星数曲线

```mermaid
xychart-beta
    title "chenlinyang/mcp-server-mysql 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-31"]
    y-axis "stars" 20 --> 23
    line [21, 22, 22]
```

2026-10-18 21 → 2026-10-31 22（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `021487c96742` · [字段定义](../../DATASET.md)*
