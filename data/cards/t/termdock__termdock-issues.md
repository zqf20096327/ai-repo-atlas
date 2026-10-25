# termdock/termdock-issues

⭐ 160 · Shell · 推送 2026-10-11 · [GitHub](https://github.com/termdock/termdock-issues) · [官网](https://termdock.com) · 组织维护 · 中文 README

**面向 AI 编码代理会话的 GPU 加速终端（macOS/Windows）**

面向 macOS 与 Windows 的终端优先开发环境：将 Claude Code、Codex、Gemini CLI、OpenCode、GitLab Duo 作为一级托管代理会话运行，代理的权限请求、提问与计划审查进入审批面板，可经 Telegram/Discord 远程监管。内置 Rust 索引管线构建代码图，提供 diff 影响分析、三栏 Git 可视化审查、Tree-sitter+LSP 的 13+ 语言代码智能、Terminal API 与 CLI、本地 HTTP API、局域网点对与 SSH（beta）远程工作区。主仓库仅用于发布下载与问题反馈，开发在私有仓库进行；Linux 支持尚未提供。通过 Homebrew cask 或 DMG/exe 安装包安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- Claude Code/Codex/Gemini CLI/OpenCode/GitLab Duo 作为托管代理会话，权限请求汇入审批面板
- 代码图 diff 影响分析与三栏 Git 可视化审查（blame、Twin Focus）
- WebGL GPU 渲染，重负载下渲染 CPU 降低约 90%，电池模式自动省电
- LAN 点对点（端到端加密）与 SSH（beta）远程工作区，Telegram/Discord 远程监管

## 适用场景

- 在一个工作区内同时运行并监管多个 AI 编码代理会话
- 在合并 AI 生成代码前做影响分析与可视化 Git 审查
- 跨机器挂载远程工作区，从手机端审批代理请求

## 场景标签

`编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L23: The way we build software has changed: the agent writes, you direct. Termdock is a **terminal-first development env
> L27: - **AI-agent native** — first-class sessions for Claude Code, Codex, Gemini CLI, OpenCode, and GitLab Duo; agents w

## 星数曲线

```mermaid
xychart-beta
    title "termdock/termdock-issues 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 159 --> 161
    line [160, 160]
```

2026-10-18 160 → 2026-10-25 160（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `bc624a7591b3` · [字段定义](../../DATASET.md)*
