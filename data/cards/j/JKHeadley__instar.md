# JKHeadley/instar

⭐ 84 · TypeScript · MIT · 推送 2026-10-24 · [GitHub](https://github.com/JKHeadley/instar) · [官网](https://instar.sh) · 个人维护

**为 Claude Code/Codex 构建持久化 agent 的基础设施框架**

基于 Node.js 的 agent 基础设施：在 Claude Code 或 Codex CLI 订阅之上运行持久会话进程，提供跨会话记忆（SQLite+FTS5、滚动摘要）、一致性审查（Coherence Gate、9 个审查者）、承诺跟踪、cron 任务调度、崩溃自恢复的 Lifeline，以及 Telegram/WhatsApp/iMessage/Slack 双向消息通道。每个会话是真实的 Claude Code 进程而非 API 封装。另含安全门、多机加密同步、agent 间通信协议与 15 个技能。要求 Node.js 20+ 与 Claude Code CLI。

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

- 跨会话记忆：按主题的 SQLite+FTS5、滚动摘要、自动重注入
- Coherence Gate：LLM 审查响应、9 个专项审查者捕捉矛盾
- Telegram/WhatsApp/iMessage/Slack 多通道与跨平台身份解析
- Lifeline 持久监管：崩溃检测、自动恢复、消息队列

## 适用场景

- 从手机通过 Telegram 长期运行和对话一个 Claude Code agent
- 让 agent 记住历史讨论并跟踪跨重启的承诺
- 运维带调度、自恢复与安全门的自治 agent

## 场景标签

`Agent 框架` `Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L28: Instar is the scaffolding that un-hobbles them. It remembers what you discussed last week, catches its own contradi
> L74: Each session is a **real Claude Code process** with extended thinking, native tools, sub-agents, hooks, skills, and
> L127: |**Cross-framework portability**|First-class Codex CLI support via `instar setup --framework codex-cli`. Codex-onl

## 星数曲线

```mermaid
xychart-beta
    title "JKHeadley/instar 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-24"]
    y-axis "stars" 82 --> 85
    line [83, 84, 84]
```

2026-10-18 83 → 2026-10-24 84（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `f6901a09628a` · [字段定义](../../DATASET.md)*
