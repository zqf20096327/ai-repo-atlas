# shiaho777/turn-mcp

⭐ 39 · TypeScript · MIT · 推送 2026-10-13 · [GitHub](https://github.com/shiaho777/turn-mcp) · 个人维护 · 中文 README

**自托管 MCP 服务器：让 agent 单次运行中实现人工介入循环**

以 Node.js/TypeScript 实现的自托管 MCP 服务器，附带浏览器控制台：agent 调用 turn.wait 工具后执行暂停，人工在 Web 界面回复，同一运行继续而不重启。提供 Streamable HTTP 与 stdio 两种 MCP 接入方式、供非 MCP 框架的 Python 客户端与 REST 长轮询 API，支持持久化历史、webhook/Telegram 通知、operator/viewer 两级鉴权。面向需要审批、分支决策、运营交接等 human-in-the-loop 场景的 agent 开发者。一次命令本地启动，默认端口 3737，非回环绑定强制 API key。

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

- turn.wait 工具将人工检查点保持在同一执行循环内，等待以 reply/timeout/cancel/interrupt 终态结束
- 浏览器控制台实时回复，附带会话列表、快捷回复、超时控制与 SSE 更新
- Streamable HTTP 与 stdio 双 MCP 传输，另有 Python 客户端与 REST 长轮询 API
- webhook（JSON/Slack/Discord 格式）与 Telegram 通知，operator/viewer 鉴权角色

## 适用场景

- agent 执行中需要人工审批或确认后继续
- 分支决策、运营交接与审查队列等长时间辅助工作流
- 在不直接支持 MCP 的 Python agent 框架中接入人工检查点

## 场景标签

`Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L5: `turn-mcp-web` is a self-hosted MCP server with a browser console. An agent calls `turn.wait`, execution pauses, a h
> L44: - REST long-poll API for Python and non-MCP agent frameworks

## 星数曲线

```mermaid
xychart-beta
    title "shiaho777/turn-mcp 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 38 --> 40
    line [39, 39]
```

2026-10-18 39 → 2026-10-27 39（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `48d1d2265e44` · [字段定义](../../DATASET.md)*
