# carlsverre/kosho

⭐ 43 · Go · MIT · 推送 2026-07-20 · [GitHub](https://github.com/carlsverre/kosho) · [官网](https://kosho.ai) · 个人维护

**管理 git worktree 以并行运行多个 AI 编码代理的 CLI 工具**

用 Go 编写的命令行工具，在仓库根目录的 .kosho/ 目录下创建和管理 git worktree，使多个分支可同时拥有独立工作区而无需克隆多份仓库。核心场景是并行运行多个 AI 编码代理（如 Claude Code），每个代理在隔离的 worktree 中工作。提供 run/list/prune 三个命令，支持 create 与 run 两类钩子脚本（通过环境变量传递上下文），并为 bash/zsh/fish/PowerShell 提供 shell 补全。通过 go install 安装，prune 不删除 git 分支。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- run/list/prune 三个命令管理 .kosho/ 下的 worktree
- 为并行运行多个 AI 编码代理提供隔离工作区
- 支持 create/run 钩子脚本与环境变量上下文注入
- bash/zsh/fish/PowerShell shell 补全

## 适用场景

- 同时开多个 Claude Code 会话在不同分支上开发
- 在同一仓库内并行处理多个特性而不切换上下文
- 定期用 prune 清理已完成的工作区

## 场景标签

 · 领域:开发者工具/git 工作流

## 证据(README 行号)

> L4: **Kosho** creates and manages [git worktree]s in `.kosho/` directories, making it easy to work on multiple branches 
> L12: Kosho is well-suited for **running multiple concurrent AI coding agents** like Claude Code, each working on differe
> L14: - **🤖 Multiple AI Agents**: Run Claude Code (or other AI tools) in separate worktrees simultaneously

## 星数曲线

```mermaid
xychart-beta
    title "carlsverre/kosho 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 42 --> 44
    line [43, 43]
```

2026-10-18 43 → 2026-10-28 43（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `36e44654d5ab` · [字段定义](../../DATASET.md)*
