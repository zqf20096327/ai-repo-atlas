# orecus/faber

⭐ 28 · TypeScript · AGPL-3.0 · 推送 2026-04-10 · [GitHub](https://github.com/orecus/faber) · 个人维护

**编排多种 CLI 编码 agent 的跨平台桌面应用**

基于 Tauri 2 的跨平台桌面应用，用于编排 AI 编码 agent：将 Claude Code、Codex CLI、Copilot CLI、Cursor Agent、Gemini CLI、OpenCode 等 CLI agent（需单独安装，从 PATH 自动检测）包装进任务驱动的工作流，提供看板、git worktree 隔离、多窗格终端会话、队列模式、GitHub 集成（issue 导入、PR 创建、提交图）、技能与规则管理，以及内嵌 MCP server 用于 agent 向应用回报进度。后端为 Rust + SQLite，前端 React 19。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `viral` | AGPL-3.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 支持 6 种 CLI 编码 agent，从 PATH 自动检测
- 每任务独立 git worktree 与分支，多 agent 并行不冲突
- 看板任务管理 + 多窗格终端会话 + 队列模式
- GitHub 集成与内嵌 MCP server 进度上报

## 适用场景

- 用看板管理编码任务并并行运行多个 AI agent
- 在独立 worktree 中让多个 agent 同时改代码避免冲突
- 从 GitHub issue 导入任务、审阅 diff 并直接创建 PR

## 场景标签

`多智能体` `代码审查` · 领域:Agent 开发

## 证据(README 行号)

> L13:  A cross-platform desktop app for orchestrating AI coding agents.
> L38: - **Multi-agent support** — Claude Code, Codex CLI, Copilot CLI, Cursor Agent, Gemini CLI, and OpenCode — all auto-

## 星数曲线

```mermaid
xychart-beta
    title "orecus/faber 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 27 --> 29
    line [28, 28]
```

2026-10-18 28 → 2026-10-29 28（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 mid · 依据 README sha `50f25908d46c` · [字段定义](../../DATASET.md)*
