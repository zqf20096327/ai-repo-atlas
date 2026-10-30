# lomi-dev/lomi

⭐ 22 · Rust · Apache-2.0 · 推送 2026-10-29 · [GitHub](https://github.com/lomi-dev/lomi) · [官网](https://lomi.dev/) · 个人维护

**终端驱动开发的桌面工作区：终端+编辑器+Git+AI 一窗**

基于 Tauri 2 与 Rust 构建的本地开发工作区，macOS/Linux/Windows 均有发布包。单一窗口内排列原生终端（Bash/Zsh/Fish/PowerShell 等）、代码编辑器、浏览器预览、Git 视图与 AI 聊天；支持多个命名工作区并在切换时保持终端后台运行。可在终端中运行 Claude Code、Codex、Gemini CLI 等 CLI agent 并经 MCP 控制工作区（MCP 控制目前限 macOS Apple Silicon）。无账户与遥测，API key 存于系统凭据库。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 单窗口集成原生终端、编辑器、浏览器预览、Git 与 AI 聊天
- 支持运行 Claude Code/Codex/Gemini CLI 等 CLI agent 并经 MCP 控制工作区
- 自备 provider API key 的 Chat AI，本地保存对话历史
- 无账户、无遥测，API key 存于系统凭据库

## 适用场景

- 在一个窗口里同时跑终端、写代码、查 Git 和预览页面
- 让 CLI 编码 agent 在工作区内通过 MCP 执行任务
- 为不同任务维护多个独立工作区并保持终端后台运行

## 场景标签

 · 领域:开发者工具/桌面应用

## 证据(README 行号)

> L3:  The open-source desktop workspace for terminal-driven development.
> L22: Lomi is a local development workspace for macOS, Linux and Windows. Open a
> L27: Run Claude Code, Codex, Gemini CLI or any other CLI agent in a Lomi terminal,

## 星数曲线

```mermaid
xychart-beta
    title "lomi-dev/lomi 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-30"]
    y-axis "stars" 20 --> 23
    line [21, 22, 22]
```

2026-10-18 21 → 2026-10-30 22（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 mid · 依据 README sha `2b7f14b66944` · [字段定义](../../DATASET.md)*
