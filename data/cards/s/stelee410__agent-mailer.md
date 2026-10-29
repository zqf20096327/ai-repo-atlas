# stelee410/agent-mailer

⭐ 19 · Python · 推送 2026-06-08 · [GitHub](https://github.com/stelee410/agent-mailer) · [官网](https://amp.linkyun.co) · 组织维护 · 中文 README

**AI agent 异步邮箱协议：让多个 agent 通过消息收发协同**

自托管的 Agent Mailer Protocol（AMP）：为每个 AI agent 提供持久身份、收件箱、线程化消息与运营控制台，agent 之间以 send/reply/forward 显式消息交接替代共享聊天上下文或 DAG/RPC 粘合。包含 FastAPI broker（本地 SQLite、生产 PostgreSQL/Docker Compose）与 agent-mailer CLI——轮询收件箱、拉起 headless Claude Code/Codex、维护会话恢复、死信重试与线程记忆。支持 Claude Code、Cursor、OpenClaw 等运行时，一键命令生成 planner/coder/reviewer/runner 四 agent 团队。限制：需 Python 3.11+ 与 tmux，短命令默认 bypassPermissions 权限模式。

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

- 异步邮件原语：send/reply/forward/inbox 与线程查询
- 持久 agent 身份与地址（如 coder@alice.amp.linkyun.co）
- headless 运行时 CLI：会话恢复、死信重试、全局与线程级记忆
- 一条命令（amp codex / amp claude-code）生成本地四 agent 团队

## 适用场景

- 让 planner/coder/reviewer/runner 多个 agent 通过消息交接协同完成项目
- 把 agent 变成无人值守服务，自动轮询收件箱处理任务
- 通过浏览器 Operator Console 查看 agent 收件箱、线程与统计

## 场景标签

`多智能体` · 领域:Agent 开发

## 证据(README 行号)

> L14: **Agent Mailer Protocol (AMP)** is a self-hosted async mail protocol for AI agents. It gives every agent a durable 
> L16: If you want Claude Code, Cursor, OpenClaw, Dreamfactory, Linkyun Infiniti Agent, or your own agent runtime to colla
> L246: In addition to the broker, this repo ships **`agent-mailer`**, a per-workdir

## 星数曲线

```mermaid
xychart-beta
    title "stelee410/agent-mailer 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 18 --> 20
    line [19, 19]
```

2026-10-18 19 → 2026-10-29 19（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 mid · 依据 README sha `5dcf6a1363b9` · [字段定义](../../DATASET.md)*
