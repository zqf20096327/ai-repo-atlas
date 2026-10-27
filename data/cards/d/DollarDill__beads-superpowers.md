# DollarDill/beads-superpowers

⭐ 32 · Shell · MIT · 推送 2026-10-24 · [GitHub](https://github.com/DollarDill/beads-superpowers) · [官网](https://algocents.com/beads-superpowers/) · 个人维护

**为 AI 编程 agent 提供流程纪律与跨会话任务记忆的插件**

面向 Claude Code、Codex CLI、OpenCode、Cursor、Gemini CLI、GitHub Copilot CLI、Kimi Code、Antigravity、Factory Droid、Pi 等 10 种 AI 编程 agent 的插件。以可组合的 skills 强制执行开发流程：先研究/头脑风暴出经人批准的规格，再写计划，实现阶段执行 TDD（无失败测试不写实现）、系统化调试、子代理并行开发与代码审查。所有任务、决策与经验存入 bd（基于 Dolt 数据库）实现跨会话持久记忆，输入 "where are we" 即可恢复上下文。安装前需先装 bd（brew 或 npm），并声明与 obra/superpowers 不兼容（技能名冲突）。

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

- 10 种 AI 编程 agent 的插件化接入（plugin marketplace / extensions / npx / 脚本安装）
- 强制工作流 skills：TDD、系统化调试、规格压力测试、完成前验证
- bd（Dolt 数据库）持久存储任务/决策/经验，跨会话恢复上下文
- subagent-driven-development：每任务独立子代理与 git worktree 隔离

## 适用场景

- 让 Claude Code/Codex 等 agent 按规格→计划→TDD 的流程写代码
- 跨会话保留项目任务与决策记忆，不依赖聊天历史
- 并行派发子代理执行批量任务并做代码审查

## 场景标签

`编码 Agent` `Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L11: A plugin for Claude Code, Codex, OpenCode, and 7 more AI coding agents that makes your agent write tests before cod
> L108: When you start a task, the agent runs **brainstorming** to nail down requirements before touching code, then **wri
> L136: **Install `bd` before the plugin.** Its hooks call `bd` on every session start; without it they fail silently and 

## 星数曲线

```mermaid
xychart-beta
    title "DollarDill/beads-superpowers 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-27"]
    y-axis "stars" 30 --> 33
    line [31, 32, 32]
```

2026-10-18 31 → 2026-10-27 32（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `4ad61fcf1133` · [字段定义](../../DATASET.md)*
