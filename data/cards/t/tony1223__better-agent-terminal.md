# tony1223/better-agent-terminal

⭐ 519 · Rust · MIT · 推送 2026-10-19 · [GitHub](https://github.com/tony1223/better-agent-terminal) · 个人维护 · 中文 README

**多工作区终端聚合器，内置 Claude Code/Codex agent 面板**

基于 Tauri（Rust host + React 渲染）的桌面终端聚合应用：按项目目录组织多工作区，每个工作区可挂多个持久终端（xterm.js），并内置文件浏览器、git 提交/PR 查看器、代码片段管理器（SQLite）、Procfile worker 面板与远程访问。AI 部分通过 Claude Code SDK 直接在应用内运行 agent，支持权限分级、会话恢复/fork、token 与费用统计、多账号切换、缓存成本提示；另可选用 Codex app-server 作为备选 agent 后端，以及可选的 cx tree-sitter 语义代码导航。提供桌面安装包与 iOS/Android 移动端（v3.1.3+）。终端功能不依赖 agent，agent 为内置面板。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 多工作区终端聚合，每工作区绑定目录并支持独立环境变量
- 内置 Claude Code SDK agent 面板：权限分级、会话恢复/fork、子 agent 跟踪
- 状态栏 15 项指标：token、费用、5h/7d 限额用量、缓存效率等
- 可选 Codex agent 后端与 cx tree-sitter 语义代码导航

## 适用场景

- 在单窗口同时管理多个项目的终端与 AI agent
- 以权限分级与 worktree 隔离方式运行 Claude Code 做代码任务
- 跟踪 agent 的 token 用量、费用与 API 限额

## 场景标签

 · 领域:开发者工具/终端

## 证据(README 行号)

> L12: Manage multiple project terminals in one window, with built-in Claude Code and Codex agent panels, file browser, gi
> L48: - **Multi-Workspace** — Organize terminals by project folders; each workspace binds to a directory
> L60: - **Agent presets** — Pre-configured terminal roles: Claude Code, Claude Code (worktree), Codex Agent, or plain ter

## 星数曲线

```mermaid
xychart-beta
    title "tony1223/better-agent-terminal 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-22"]
    y-axis "stars" 518 --> 520
    line [519, 519]
```

2026-10-18 519 → 2026-10-22 519（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 mid · 依据 README sha `2b5126f505c7` · [字段定义](../../DATASET.md)*
