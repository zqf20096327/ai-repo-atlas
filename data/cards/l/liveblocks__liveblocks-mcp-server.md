# liveblocks/liveblocks-mcp-server

⭐ 19 · TypeScript · Apache-2.0 · 推送 2026-10-30 · [GitHub](https://github.com/liveblocks/liveblocks-mcp-server) · [官网](https://liveblocks.io/docs/tools/mcp-server) · 组织维护

**让 AI 通过 MCP 操作 Liveblocks 协作平台的服务器**

Liveblocks 官方发布的 MCP server：把 Liveblocks REST API 的功能暴露为 AI 可调用工具，支持创建、修改、删除 rooms、threads、comments、notifications 等对象，并可只读访问 Storage 与 Yjs 数据。需要 Liveblocks 项目的 secret key 认证，通过 npx 从 GitHub 仓库运行，README 提供 Cursor、Claude Code、Claude Desktop、Codex 四种客户端的接入配置步骤。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 通过 REST API 操作 rooms、threads、comments、notifications
- 对 Storage 与 Yjs 具有只读访问
- 提供 Cursor、Claude Code、Claude Desktop、Codex 配置指引
- npx 从 GitHub 仓库直接运行

## 适用场景

- 在 Claude/Cursor 等客户端中用 AI 管理 Liveblocks 房间与评论
- 让 AI 读取 Storage 与 Yjs 数据做分析

## 场景标签

 · 领域:AI Agent 基础设施/协作 SaaS

## 证据(README 行号)

> L8: # `liveblocks-mcp-server`
> L10: This MCP server allows AI to use a number of functions from our REST API. For example, it can create, modify, and d

## 星数曲线

```mermaid
xychart-beta
    title "liveblocks/liveblocks-mcp-server 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 18 --> 20
    line [19, 19]
```

2026-10-18 19 → 2026-10-31 19（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `f82f4b4bfdfb` · [字段定义](../../DATASET.md)*
