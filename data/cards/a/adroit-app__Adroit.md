# adroit-app/Adroit

⭐ 15 · Rust · MIT · 推送 2026-11-17 · [GitHub](https://github.com/adroit-app/Adroit) · [官网](https://adroit-app.github.io/) · 组织维护

**Vim 用户的编码 agent 工作区：并排管理多个 Claude Code/Codex 会话**

面向习惯 Vim 操作的开发者的桌面工作区应用：将 Claude Code、Codex、Pi、OpenCode 等编码 agent 会话并排放在同一窗口，各 agent 使用自身原有界面。提示词在为 Adroit 配置的 Neovim 中编写，支持标签页、分屏、树与详情面板间的 Vim 移动；会话按仓库与 worktree 分组，等待用户的会话排在前面。会话与 shell 在窗口关闭后持续运行。提供 MCP 工具供会话间互相发现与协作，并支持远程主机与多实例。macOS 经 Homebrew cask 或 Nix 安装，Windows 需 Rust/MSVC/LLVM 从源码构建。README 声明项目处于早期阶段。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | `idea` | |

## 能力要点

- 同一窗口并排运行 Claude Code、Codex、Pi、OpenCode 会话，各用 agent 原生界面
- 提示词与控制台读写经 Neovim，支持 Vim 移动、分屏与按键绑定
- 内置 MCP 工具（sessions/models/start_session/send）支持会话间协作
- 会话按仓库与 worktree 分组，关窗后持续运行

## 适用场景

- 同时跑多个编码 agent 会话并在其间切换
- 用 Vim 操作方式编写提示词并浏览 agent 控制台输出
- 让一个 agent 会话读取或开启另一个会话协同工作

## 场景标签

 · 领域:开发者工具/编码 agent

## 证据(README 行号)

> L5: An Agent Workspace for people who live in Vim: drive any coding agent in its own
> L11: Claude Code, Codex, Pi and OpenCode sessions stand side by side in one window,
> L41: Adroit needs git and at least one supported agent on `PATH`. The macOS app


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-18 · 置信度 high · 依据 README sha `b7056bef21a7` · [字段定义](../../DATASET.md)*
