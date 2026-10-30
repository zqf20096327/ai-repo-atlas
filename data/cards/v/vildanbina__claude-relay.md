# vildanbina/claude-relay

⭐ 61 · TypeScript · MIT · 推送 2026-09-03 · [GitHub](https://github.com/vildanbina/claude-relay) · 个人维护

**让本机多个 Claude Code 会话用自然语言互发消息的插件**

以 Claude Code 插件形式提供的跨会话通信工具：会话内用自然语言让另一个会话回答问题或向所有会话广播，回复以通知形式流回。架构为三部分——会话、每会话一个 MCP channel、单机 Hub 守护进程经 Unix socket 路由消息，Hub 在最后一个对端断开五分钟后自退出。依赖 Claude Code 的 notifications/claude/channel 能力（research preview），启动需加 --dangerously-load-development-channels 标志。限制：不持久化、单机单用户、仅同主机。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 提供 relay_peers/relay_ask/relay_reply/relay_broadcast/relay_rename 五个 MCP 工具
- Hub 守护进程经 Unix socket 跨会话路由消息
- 支持 CLAUDE_RELAY_PRESET_NAME 环境变量为编排器预注册会话名
- 11 个错误码覆盖对端失联、超时、命名冲突等场景

## 适用场景

- 同时开发多个项目时让不同 Claude Code 会话互相询问进展
- 向所有活跃会话广播状态查询并汇总回复
- 由父进程批量启动会话并按预设名称注册管理

## 场景标签

 · 领域:AI 开发者工具

## 证据(README 行号)

> L11: Claude Relay ships as a Claude Code plugin. Three steps.
> L116: - **Channel** — per-session MCP server (this plugin). Exposes the `relay_*` tools to Claude and listens for incomi

## 星数曲线

```mermaid
xychart-beta
    title "vildanbina/claude-relay 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 60 --> 62
    line [61, 61]
```

2026-10-18 61 → 2026-10-30 61（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `76a55171e86f` · [字段定义](../../DATASET.md)*
