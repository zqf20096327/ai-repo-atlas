# oso95/Codirigent

⭐ 109 · Rust · GPL-3.0 · 推送 2026-07-09 · [GitHub](https://github.com/oso95/Codirigent) · [官网](https://codirigent.dev/) · 个人维护 · 中文 README

**并排运行多个 AI 编码 CLI 的终端工作区（Rust/TUI）**

用 Rust 编写的 Tmux 风格终端工作区，面向同时使用 Claude Code、Codex、Gemini 的开发者：可在单一视图中并排运行多个 AI 编码 CLI 会话，支持自定义网格布局、文件树随焦点同步、Git worktree 隔离分支、会话自动恢复与智能剪贴板。通过自动安装 hooks（codirigent-hook 写入各 CLI 配置）实现实时状态指示（Idle/Working/Attention/Ready）。提供 Windows .msi 与 macOS .dmg 安装包，也可 cargo 源码构建；Linux 支持未完成，自称早期 alpha。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 单一视图中并排运行 Claude Code / Codex / Gemini，带实时状态指示
- hooks 自动安装到各 CLI 配置，实现 Working/Attention/Ready 状态跟踪
- Git worktree 支持多 agent 隔离分支并行
- 会话自动检测与恢复，自定义网格布局可保存

## 适用场景

- 同时给多个项目跑 AI 编码 agent，不再手动开终端排窗口
- 用 Git worktree 让多个 agent 在隔离分支上并行改代码
- 通过状态指示一眼看出哪个 agent 在等确认、哪个已完成

## 场景标签

`多智能体` · 领域:Agent 开发

## 证据(README 行号)

> L5:  A terminal workspace for running multiple AI coding CLIs in parallel
> L22: Codirigent is a Tmux-style workspace built for this workflow. Open it once, and your sessions are already where you
> L61: Codirigent uses lightweight hooks to track agent status in real time — showing whether each session is Working, Nee

## 星数曲线

```mermaid
xychart-beta
    title "oso95/Codirigent 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 108 --> 110
    line [109, 109]
```

2026-10-18 109 → 2026-10-26 109（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `4885a873ccf4` · [字段定义](../../DATASET.md)*
