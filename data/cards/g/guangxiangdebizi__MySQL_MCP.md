# guangxiangdebizi/MySQL_MCP

⭐ 81 · TypeScript · 推送 2025-12-17 · [GitHub](https://github.com/guangxiangdebizi/MySQL_MCP) · 个人维护 · 中文 README

**让 AI 助手安全操作 MySQL 数据库的 MCP 服务器**

基于 MCP StreamableHTTP 协议的 MySQL 服务器（TypeScript/Express 实现），向 Claude Desktop、Cursor 等 MCP 客户端提供连接管理（add/list/select/remove）与查询工具（execute_query、show_tables、describe_table 等）。支持多数据库同时连接与随时切换，提供 Header 预配置（凭证不暴露给 AI）和 AI 对话动态添加连接两种接入方式；v4.0.5+ 使用连接池、Keep-Alive 与自动重连。要求 Node.js 18+ 与 MySQL 5.7+/8.0+；v3.x 的事务管理与回滚功能在 v4.0 重写后未列入当前工具表。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 基于最新 MCP StreamableHTTP 协议（v4.0 重写）
- 多数据库连接管理，Header 预配置使凭证不暴露给 AI
- 连接池 + Keep-Alive + 自动重连 + 并发查询（v4.0.5+）
- 提供 8 个 MCP 工具覆盖连接管理与查询操作

## 适用场景

- 在 Claude Desktop / Cursor 中用自然语言查询和操作 MySQL 数据库
- 同时管理生产库与测试库并在对话中切换
- 通过 AI 动态添加数据库连接而无需手动改配置

## 场景标签

`数据分析` · 领域:效率与自动化

## 证据(README 行号)

> L5: 一个功能强大且易用的 MySQL 数据库 MCP（Model Context Protocol）服务器，支持 AI 助手安全地操作 MySQL 数据库。
> L9: - 🌐 **StreamableHTTP 协议** - 基于最新 MCP 规范实现

## 星数曲线

```mermaid
xychart-beta
    title "guangxiangdebizi/MySQL_MCP 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 80 --> 82
    line [81, 81]
```

2026-10-18 81 → 2026-10-25 81（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 mid · 依据 README sha `0df2f000cec9` · [字段定义](../../DATASET.md)*
