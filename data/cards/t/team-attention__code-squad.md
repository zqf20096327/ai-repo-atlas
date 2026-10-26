# team-attention/code-squad

⭐ 61 · TypeScript · MIT · 推送 2026-02-15 · [GitHub](https://github.com/team-attention/code-squad) · [官网](https://marketplace.visualstudio.com/items?itemName=JakePark.code-squad) · 组织维护

**基于 tmux 与 VSCode 的多 worktree 开发管理工具**

提供两部分：code-squad-cli（npm 安装）以 tmux 面板管理多个 git worktree，支持键盘快捷键创建/删除/切换分支工作区，自动安装 tmux，并将 .env 等配置文件复制到新 worktree；VSCode 扩展面向 AI 辅助开发，提供线程管理（多个 AI agent 各自隔离的 worktree）、文件级/函数级 diff 视图、行内评论发送给 AI，并可自动检测 claude、codex、gemini、opencode 等工具。使用者为主要在多分支并行开发并结合 AI agent 的开发者。

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

- tmux 面板用键盘快捷键管理多个 git worktree
- VSCode 扩展为多个 AI agent 提供隔离 worktree 的线程管理
- 自动检测 claude/codex/gemini/opencode 等 AI 工具
- 自动安装 tmux 并同步 .env 等配置文件到新 worktree

## 适用场景

- 多分支并行开发时在一个面板内切换各分支工作区
- 同时运行多个 AI agent，各自在隔离的 worktree 中工作
- 在 VSCode 中以 diff 与行内评论方式审查 AI 生成的代码改动

## 场景标签

`代码审查` · 领域:编码与开发

## 证据(README 行号)

> L76: - **Thread Management** - Multiple AI agents in isolated workspaces
> L80: - **Auto-Detect** - Detects claude, codex, gemini, opencode
> L43: - **Tmux Dashboard** - Manage worktrees with keyboard shortcuts

## 星数曲线

```mermaid
xychart-beta
    title "team-attention/code-squad 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 60 --> 62
    line [61, 61]
```

2026-10-18 61 → 2026-10-26 61（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 mid · 依据 README sha `625b8ab6822e` · [字段定义](../../DATASET.md)*
