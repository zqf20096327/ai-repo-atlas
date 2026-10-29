# PaSympa/discord-mcp

⭐ 29 · TypeScript · MIT · 推送 2026-10-11 · [GitHub](https://github.com/PaSympa/discord-mcp) · 个人维护

**用自然语言管理 Discord 服务器的 MCP 服务器（95+ 工具）**

TypeScript + Node.js 实现的 Discord MCP 服务器，向 Claude Desktop、Claude Code、Cursor、VS Code Copilot 等 MCP 客户端暴露 99 个工具，覆盖消息读写、频道管理、角色与权限、成员管理（踢/封/禁言）、论坛、Webhook、定时活动与邀请等，支持多服务器且可用 DISCORD_ALLOWED_GUILDS 与工具集开关限定范围。需自建 Discord bot 并提供 DISCORD_TOKEN；消息均经 REST 获取而非事件订阅。安装途径为 npx/npm、Docker 或源码构建。

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

- 99 个工具覆盖消息、频道、角色、权限、成员、论坛、Webhook 等类别
- 支持多服务器，DISCORD_ALLOWED_GUILDS 与 DISCORD_MCP_TOOLSETS 可限定作用范围
- npm/npx、Docker、源码三种安装方式
- 消息通过 REST API 获取，不订阅消息事件

## 适用场景

- 在 Claude 或 Cursor 中用自然语言管理 Discord 服务器的消息和频道
- 通过 MCP 客户端执行成员管理与审核操作
- 多服务器场景下统一管理 Discord 社区

## 场景标签

 · 领域:AI 工具接入/社区管理

## 证据(README 行号)

> L3: **A lightweight, multi-guild Discord MCP server with 95+ tools**
> L13: Manage your entire Discord server from **Claude Desktop**, **Claude Code**, **Cursor**, **VS Code Copilot**, or any

## 星数曲线

```mermaid
xychart-beta
    title "PaSympa/discord-mcp 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-29"]
    y-axis "stars" 27 --> 30
    line [28, 29, 29]
```

2026-10-18 28 → 2026-10-29 29（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `86535bd3d465` · [字段定义](../../DATASET.md)*
