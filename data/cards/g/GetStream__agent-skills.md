# GetStream/agent-skills

⭐ 20 · Python · Apache-2.0 · 推送 2026-10-28 · [GitHub](https://github.com/GetStream/agent-skills) · 组织维护

**让 AI 编码代理构建、查询、管理 Stream 产品的技能包**

Stream 官方发布的 agent 技能仓库：以 SKILL.md 形式提供路由技能 `/stream` 与 8 个平台技能（React/Swift/Android/React Native/Flutter/Unity/Unreal/Feeds 迁移），由 `getstream` CLI 安装，指导 AI 编码代理搭建应用、集成 Chat/Video/Feeds/Moderation、审计与迁移 SDK、通过 CLI 查询数据与配置应用。同时以 Claude Code 与 Cursor 插件形式分发，并附带 Stream MCP 服务器（mcp.getstream.io），可用 Stream 账号登录让代理调用 Stream API。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- `/stream` 路由技能做意图分类并调度平台技能与 CLI 命令
- 覆盖 React/Swift/Android/React Native/Flutter/Unity/Unreal/Feeds 迁移 8 类平台技能
- 提供 Claude Code 与 Cursor 插件及 Stream MCP 服务器
- `getstream` CLI 支持自然语言查询线上数据与配置审核策略

## 适用场景

- 让 AI 编码代理一键搭建集成 Stream Chat/Video 的应用
- 把 Sendbird 应用迁移到 Stream 或升级现有 Stream SDK
- 生成 Feeds v2 到 v3 的同步映射并规划代码迁移

## 场景标签

`编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L3: Give your AI coding agent the ability to build, query, and manage Stream - Chat, Video, Feeds, and Moderation across
> L19: The skills also ship as a plugin for Claude Code and Cursor, together with the Stream MCP server (`https://mcp.gets

## 星数曲线

```mermaid
xychart-beta
    title "GetStream/agent-skills 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 19 --> 21
    line [20, 20]
```

2026-10-18 20 → 2026-10-29 20（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `f184f76c9335` · [字段定义](../../DATASET.md)*
