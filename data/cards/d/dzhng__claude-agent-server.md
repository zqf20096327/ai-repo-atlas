# dzhng/claude-agent-server

⭐ 585 · TypeScript · 推送 2025-12-28 · [GitHub](https://github.com/dzhng/claude-agent-server) · [官网](https://x.com/dzhng/status/1991154972558581889?s=20) · 个人维护

**封装 Claude Agent SDK 的 WebSocket 服务器，可部署到 E2B 沙箱**

用 Bun 实现的 WebSocket 服务器，包裹 Claude Agent SDK，提供单个 WebSocket 客户端与 Claude 之间的双向消息中继：支持通过 /config 端点预设 agents、allowedTools 与 systemPrompt，消息入队后交由 SDK 流处理并即时回传，同时只接受一个活跃连接，支持 interrupt 中断。主要部署方式是用 bun run build:e2b 构建为 E2B 沙箱模板，配套 TypeScript 客户端库 @dzhng/claude-agent 负责沙箱创建、连接与清理；也可在 localhost:3000 本地运行调试，内置网页测试客户端。面向需要在自己的应用中接入 Claude Code/Agent 能力的开发者。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- WebSocket 与 Claude Agent SDK 之间的单连接消息中继架构
- 通过 /config 端点预配置 agents、allowedTools、systemPrompt
- 配套 @dzhng/claude-agent 客户端库管理 E2B 沙箱生命周期
- 支持本地 localhost 与 E2B 云沙箱两种运行方式

## 适用场景

- 在自己的 TypeScript 应用中通过客户端库接入沙箱化的 Claude Agent
- 把 Claude Code 运行在隔离的 E2B 沙箱中并实时收发消息
- 定制服务器行为后重新构建 E2B 模板部署

## 场景标签

`Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L5: A WebSocket server that wraps the Claude Agent SDK, allowing real-time bidirectional communication with Claude throu
> L340: The server is a simple **1-to-1 relay** between a single WebSocket client and the Claude Agent SDK:

## 星数曲线

```mermaid
xychart-beta
    title "dzhng/claude-agent-server 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-25", "2026-10-26"]
    y-axis "stars" 584 --> 587
    line [586, 585, 585]
```

2026-10-18 586 → 2026-10-26 585（-1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `beda9db6bbc6` · [字段定义](../../DATASET.md)*
