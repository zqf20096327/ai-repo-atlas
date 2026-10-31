# Eldergenix/Proofloop

⭐ 40 · TypeScript · MIT · 推送 2026-05-26 · [GitHub](https://github.com/Eldergenix/Proofloop) · 个人维护

**驱动 Claude/Codex 结对运行的证明式 agent 循环 CLI**

基于 Bun 的命令行工具，将 Claude 与 Codex 以结对模式运行：一个作为主执行者，另一个作为评审/支持，通过 Codex App Server 与 Claude Code Channels 桥接通信。从纯文本提示生成 PLAN.md 并先经评审，任务完成须满足证明要求（质量命令 + 默认 adversarial 安全/性能门）。运行状态持久化于 ~/.loop/runs 下，支持按 run id/session id 恢复、tmux 会话与 git worktree 隔离。面向构建自主编码工作流的开发者，README 建议在沙箱环境运行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Claude/Codex 结对模式：主执行者 + 持续评审/支持角色
- 完成前运行质量命令与 adversarial 安全/性能质量门
- 运行状态持久化并支持按 run id/Claude session/Codex thread 恢复
- 支持 tmux 会话与新建 git worktree 内运行

## 适用场景

- 让两个编码 agent 结对完成自主编码任务
- 要求任务以测试和检查通过作为完成证明
- 长时间自主运行后恢复中断的 agent 会话

## 场景标签

`编码 Agent` `多智能体` · 领域:Agent 开发

## 证据(README 行号)

> L3: Proofloop is a Bun CLI for running Claude and Codex in a proof-driven agent loop. It plans work, keeps paired agents
> L16: - Bridges agent-to-agent messages through Codex App Server and Claude Code Channels.
> L27: 1. Standard reviewer pass with Claude, Codex, or both.

## 星数曲线

```mermaid
xychart-beta
    title "Eldergenix/Proofloop 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 39 --> 41
    line [40, 40]
```

2026-10-18 40 → 2026-10-31 40（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `8e0182aaf174` · [字段定义](../../DATASET.md)*
