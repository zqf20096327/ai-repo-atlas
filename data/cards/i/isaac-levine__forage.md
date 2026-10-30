# isaac-levine/forage

⭐ 19 · TypeScript · MIT · 推送 2026-02-21 · [GitHub](https://github.com/isaac-levine/forage) · [官网](https://www.npmjs.com/package/forage-mcp) · 个人维护

**让 AI agent 自动发现并安装新 MCP 工具的网关服务器**

一个 MCP 网关/代理服务器：安装一次后，AI agent 可通过 forage_search 在 MCP Registry、Smithery 与 npm 并行搜索 MCP 服务器，经用户确认后以子进程方式安装并代理其工具，无需重启即可通过 list_changed 通知生效；forage_learn 将用法写入 CLAUDE.md 等规则文件，manifest 支持下次会话自动启动。状态存于 ~/.forage/，含安装审计日志；无远程后端，环境变量不持久化。面向使用 Claude Code、Cursor 等 agent 客户端的开发者，另提供人类可用的 CLI。

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

- 跨 MCP Registry、Smithery、npm 并行搜索 MCP 服务器
- 以代理子进程方式安装并即时暴露新工具（无需重启）
- forage_learn 持久化用法说明到 agent 规则文件
- 每次安装需显式确认并写入审计日志

## 适用场景

- 让编码 agent 在会话中自行补装所需的 MCP 工具
- 统一管理多个 MCP 服务器的安装与启动
- 减少为 agent 手动配置新 MCP server 的操作

## 场景标签

`Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L13: Forage is an MCP server that lets AI agents discover, install, and learn to use new tools — automatically. When an 
> L59: Forage is a **gateway/proxy** MCP server:

## 星数曲线

```mermaid
xychart-beta
    title "isaac-levine/forage 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 18 --> 20
    line [19, 19]
```

2026-10-18 19 → 2026-10-30 19（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `b680c956caec` · [字段定义](../../DATASET.md)*
