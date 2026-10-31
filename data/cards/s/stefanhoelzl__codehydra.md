# stefanhoelzl/codehydra

⭐ 20 · TypeScript · MIT · 推送 2026-10-30 · [GitHub](https://github.com/stefanhoelzl/codehydra) · [官网](https://codehydra.stho.net) · 个人维护

**多工作区 IDE：用 git worktrees 并行运行多个 AI 编码代理**

基于 VSCodium 的多工作区桌面 IDE，面向同时使用多个 AI 编码助手的开发者：以 git worktrees 从单一仓库创建隔离工作区，每个工作区运行独立的 Claude Code 或 OpenCode 代理并配备完整编辑器。内置 codehydra MCP 服务器，代理可执行工作区生命周期、编辑器命令等工具；提供实时状态监控、Alt+X 键盘导航、休眠、仓库钩子与实验性自动工作区。要求 Git 及 Claude Code 或 OpenCode 账号，支持 Linux/macOS/Windows。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- git worktrees 隔离工作区，每区独立分支与 AI 代理
- 内置 Claude Code 与 OpenCode，可全局或按工作区选择
- 内置 codehydra MCP 服务器，代理可执行任意 VS Code 命令
- 每个工作区是带用户扩展与主题的完整 VSCodium 编辑器

## 适用场景

- 在同一仓库上并行运行多个 AI 编码任务互不干扰
- 实时监控多个代理的工作状态并快速切换
- 让代理通过 MCP 驱动编辑器执行命令

## 场景标签

`编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L11: Run multiple AI coding assistants simultaneously in isolated git worktrees
> L38: - **Parallel Workspaces** - Run Claude Code or OpenCode in several workspaces at once
> L88: Every workspace's agent is automatically connected to CodeHydra's `codehydra` MCP

## 星数曲线

```mermaid
xychart-beta
    title "stefanhoelzl/codehydra 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 19 --> 21
    line [20, 20]
```

2026-10-18 20 → 2026-10-31 20（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `a107792fd8b1` · [字段定义](../../DATASET.md)*
