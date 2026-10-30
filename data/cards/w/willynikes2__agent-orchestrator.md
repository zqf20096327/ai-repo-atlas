# willynikes2/agent-orchestrator

⭐ 67 · Python · MIT · 推送 2026-10-14 · [GitHub](https://github.com/willynikes2/agent-orchestrator) · 个人维护

**多 agent CLI 编排器：Claude/Codex/Gemini 等自动故障切换**

基于终端的多智能体编排工具，封装 Claude、Codex、Gemini、Grok、Antigravity 五个 CLI（可选 Argon API 审查者）。消息按角色链路由（orchestrator/implementation/uidocs/review/intel），某 agent 达限额或故障时自动切换到链上下一个；自动检测限流、配额耗尽与认证失败并加冷却或禁用。通过封装现有 CLI 订阅而非按 token 计费，所有 agent 经知识库服务器共享上下文。单文件 Python 实现（约 1100 行），需 Python 3.10+ 且至少安装一个 AI CLI。Codex/Gemini 默认 full-host-unattended 无审批模式，Grok/Antigravity 默认沙箱。

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

- 角色链路由与 next-man-up 自动故障切换
- 自动检测限流/配额耗尽/认证失败并禁用恢复
- 封装现有 CLI 订阅，无按 token 计费
- 每条响应前自动检索知识库服务器获取上下文

## 适用场景

- 在一个终端里调度多个 AI CLI 订阅完成规划、实现、审查等分工
- 某 agent 达用量上限时自动切换到下一个可用 agent
- 通过 @ 直接指定 agent 或用 impl:/ui: 前缀按角色路由

## 场景标签

`多智能体` · 领域:Agent 开发

## 证据(README 行号)

> L5: A terminal-based multi-agent orchestrator that wraps Claude, Codex, Gemini, Grok, and Antigravity CLIs (plus an opti
> L28: - **Next-man-up failover** — if an agent is down, the next one in the chain takes over automatically
> L30: - **CLI wrapping** — uses your existing Claude/Codex/Gemini/Grok CLI subscriptions, not per-token API billing

## 星数曲线

```mermaid
xychart-beta
    title "willynikes2/agent-orchestrator 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 66 --> 68
    line [67, 67]
```

2026-10-18 67 → 2026-10-30 67（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 mid · 依据 README sha `28a342800721` · [字段定义](../../DATASET.md)*
