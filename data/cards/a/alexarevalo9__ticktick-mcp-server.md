# alexarevalo9/ticktick-mcp-server

⭐ 73 · TypeScript · 推送 2026-09-01 · [GitHub](https://github.com/alexarevalo9/ticktick-mcp-server) · 个人维护

**为 AI 客户端接入 TickTick 任务管理的 MCP 服务器**

基于 Node.js 的 Model Context Protocol 服务器，封装 TickTick Open API，向 AI 客户端暴露 11 个工具：任务的增删改查、完成、子任务管理，以及项目的增删改查（支持 list/kanban/timeline 视图与 TASK/NOTE 类型）。采用 OAuth2 认证，通过浏览器授权流程生成访问令牌（有效期 180 天）。面向使用 Claude Desktop 等 MCP 客户端的开发者，提供 npx 运行、Docker 与 Smithery 安装方式。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 11 个工具覆盖任务/项目/子任务的完整 CRUD 操作
- 完整 OAuth2 授权流程与访问令牌管理（180 天有效期）
- 支持任务优先级、iCalendar 提醒与 RFC 5545 重复规则
- 提供 npx、Docker、Smithery 三种安装运行方式

## 适用场景

- 在 Claude Desktop 中通过对话创建和管理 TickTick 任务
- 让 AI 助手读取项目与任务列表以获取上下文
- 自动化设置带提醒与重复规则的任务

## 场景标签

`工作流自动化` · 领域:效率与自动化

## 证据(README 行号)

> L1: # TickTick MCP Server
> L3: MCP Server for the TickTick API, enabling task management, project organization, habit tracking, and more.

## 星数曲线

```mermaid
xychart-beta
    title "alexarevalo9/ticktick-mcp-server 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 72 --> 74
    line [73, 73]
```

2026-10-18 73 → 2026-10-24 73（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `f7b772cd98df` · [字段定义](../../DATASET.md)*
