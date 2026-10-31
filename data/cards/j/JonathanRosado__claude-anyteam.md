# JonathanRosado/claude-anyteam

⭐ 21 · Python · 推送 2026-05-12 · [GitHub](https://github.com/JonathanRosado/claude-anyteam) · [官网](https://github.com/JonathanRosado/claude-anyteam) · 个人维护

**让外部 agent CLI 以原生队友身份加入 Claude Code 团队**

为 Claude Code 的 Agent Teams 功能提供适配层：通过队友名前缀（codex-*/gemini-*/kimi-*）将 OpenAI Codex CLI、Gemini CLI、Kimi CLI 等外部 agent 接入同一团队协议，Claude Code 会话负责编排、外部 agent 负责执行。适配器直接使用 mailbox I/O、任务认领、中逋试次转向（turn/steer）与线程 fork 等机制，无需聊天包装层。要求 Python 3.12+、Node 18+（仅安装器）、各后端 CLI 在 PATH 上、Claude Code 2.1+ 及 tmux/psmux。GLM 与 DeepSeek 适配器列为待开发。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 前缀路由机制把 Codex/Gemini/Kimi CLI 接入 Claude Code Agent Teams
- 适配器直接使用团队协议：mailbox I/O、原子任务认领、shutdown 生命周期
- 支持中逋试次转向（turn/steer）与跨任务线程 fork（Codex App Server 模式）
- npx 一条命令安装，自动探测依赖并记录安装状态以支持对称卸载

## 适用场景

- 在 Claude Code 团队中混编 Codex 执行者、Gemini 审查者、Kimi 架构审查者
- 让不同厂商的 agent CLI 以原生队友 UX 协作
- 复用已有的 Codex/Gemini/Kimi CLI 订阅与登录参与多 agent 开发

## 场景标签

`多智能体` `编码 Agent` · 领域:Agent 开发

## 证据(README 行号)

> L19: Claude Code's Agent Teams feature is built for multi-agent collaboration — but every teammate is a Claude instance.
> L21: Your Claude Code session orchestrates. External agents execute. No chat-wrapper overhead. No "Claude pretending to 
> L72: |Codex via OpenAI Codex CLI 0.120+|`codex-*`|✅ Supported today|App Server mode for mid-task steer and `thread/fork`

## 星数曲线

```mermaid
xychart-beta
    title "JonathanRosado/claude-anyteam 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 20 --> 22
    line [21, 21]
```

2026-10-18 21 → 2026-10-31 21（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `58913e729d34` · [字段定义](../../DATASET.md)*
