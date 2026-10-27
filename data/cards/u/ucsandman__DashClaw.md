# ucsandman/DashClaw

⭐ 313 · TypeScript · MIT · 推送 2026-10-25 · [GitHub](https://github.com/ucsandman/DashClaw) · [官网](https://www.dashclaw.io/) · 个人维护

**无人值守 AI agent 的远程审批与执行治理层**

面向独立开发者或小团队长时间无人值守运行 coding agent 的场景，在 agent 决定调用工具与工具实际执行之间设置 fail-closed 审批层：通过 Claude Code/Codex/Hermes 的 PreToolUse 钩子、OpenClaw 网关或 dashclaw_invoke 拦截高危操作（如 rm -rf、force push、读取 .env 外传），经网页收件箱、CLI、手机 PWA、Telegram 或 Discord 远程批准/拒绝。决策写入签名账本（Ed25519 回执），支持策略阈值、标准授权、prompt-injection 扫描与执行探活。钩子之外的 SDK/API/MCP 集成为协作式（调用方须自觉遵守）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 钩子 seams 处 fail-closed 拦截工具调用，决策格为 allow<warn<allow_contained<require_approval<block，block 不可降级
- 决策账本记录、Ed25519 签名回执与可签名导出
- 审批以一句英文说明命令实际作用并标注不可撤销项
- 维护者声明为 AI agent 在人类宪章（MAINTAINER.md 五条不变量）约束下维护

## 适用场景

- 夜间或 CI 中长时间运行 coding agent 时拦截破坏性命令并远程审批
- 多运行时（Claude Code/Codex/Hermes/OpenClaw）共享一套治理策略
- 为 agent 操作留存可审计的决策记录与签名证据

## 场景标签

`Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L58: At a supported enforcement seam, DashClaw is a fail-closed approval layer between an agent *deciding* to call a too
> L5:  With a supported enforcement integration, when your AI agent (OpenClaw, Hermes, Claude Code, Codex) tries something

## 星数曲线

```mermaid
xychart-beta
    title "ucsandman/DashClaw 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 312 --> 314
    line [313, 313]
```

2026-10-18 313 → 2026-10-27 313（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `88102315cc56` · [字段定义](../../DATASET.md)*
