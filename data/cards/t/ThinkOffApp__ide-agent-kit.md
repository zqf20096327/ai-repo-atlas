# ThinkOffApp/ide-agent-kit

⭐ 45 · JavaScript · AGPL-3.0 · 推送 2026-10-14 · [GitHub](https://github.com/ThinkOffApp/ide-agent-kit) · [官网](https://thinkoff.io) · 组织维护

**让 IDE AI 参与团队协作的多 agent 协调工具包**

面向 Claude Code、Codex、Cursor、VS Code 等 IDE agent 与本地 LLM 助手的多 agent 协调工具包：通过 GitHub webhook 接收、GroupMind 房间轮询、Moltbook 评论轮询把消息投递给真实 IDE agent，由 agent 自行决定回复（工具包本身不代为生成回复）。含 tmux 运行器（allowlist 命令执行）、append-only JSONL 回执、OpenClaw 舰队管理 CLI、Claude Code hooks 自动装配与 SessionStart 自举。本地优先，默认无外部服务器；需 Node.js 20+、npm、git、tmux，macOS/Linux 一键安装脚本（不执行 sudo 安装，需显式同意）。npm 全局包目前为过期的 0.2.0 版本，官方建议用安装脚本或 git clone。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `viral` | AGPL-3.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Webhook/房间轮询/tmux 三条消息投递路径，投递给真实 IDE agent 决策
- append-only JSONL 回执，含 trace ID 与幂等键
- 支持 Claude Code、Codex、Gemini、Cursor、VS Code、Grok Build 等多种 IDE/agent 环境的 init 配置生成
- OpenClaw 舰队管理 CLI（网关健康、会话、exec 审批、cron）

## 适用场景

- 让手机/聊天室里的消息即时驱动本地 IDE agent 执行任务
- 为 GitHub issue 与 webhook 事件接入 agent 自动处理流程
- 多 agent 并发值守聊天房间并留有可审计回执

## 场景标签

`多智能体` `编码 Agent` · 领域:Agent 开发

## 证据(README 行号)

> L5: Multi-agent coordination toolkit for IDE AIs (Claude Code, Codex, Cursor, VS Code agents, local LLM assistants). Roo
> L81: IDE Agent Kit is a **message delivery and coordination layer**, not an autoresponder. It delivers messages to your 

## 星数曲线

```mermaid
xychart-beta
    title "ThinkOffApp/ide-agent-kit 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 44 --> 46
    line [45, 45]
```

2026-10-18 45 → 2026-10-29 45（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `e4f03ba92be5` · [字段定义](../../DATASET.md)*
