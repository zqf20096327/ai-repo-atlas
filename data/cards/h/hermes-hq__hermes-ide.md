# hermes-hq/hermes-ide

⭐ 342 · TypeScript · NOASSERTION · 推送 2026-10-19 · [GitHub](https://github.com/hermes-hq/hermes-ide) · [官网](https://hermes-ide.com) · 组织维护

**多编码 agent 统一控制台：并行运行、隔离分支与集中审阅**

面向同时使用多个编码 agent 的开发者的桌面应用（Tauri 2，React/TypeScript 前端与 Rust 后端）。每个 agent 在独立终端与独立 git worktree/分支中运行，提供注意力收件箱汇总等待用户的 agent、按轮次审阅变更的 Review Desk、一步提交/合并、多账号预设与会话费用显示。通过各 agent 自身的 CLI 登录鉴权，不代理权限提示。macOS/Windows/Linux 提供安装包；macOS/Linux 上 agent 会话在应用退出后仍继续运行。源码以 BSL 1.1 许可提供。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 每任务独立分支与 worktree，agent 在真实终端中运行
- 注意力收件箱与单一状态视图汇总所有 agent
- Review Desk 按轮次/文件审阅变更并发送行级评论回 agent
- 支持多个 agent CLI（Claude Code、Codex、Copilot、OpenCode 等）与多账号预设

## 适用场景

- 并行运行多个编码 agent 且避免互相覆盖工作区
- 集中查看哪个 agent 在等我并快速跳转处理
- 审阅、diff 与合并各 agent 产出的代码变更

## 场景标签

`编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L5:  One console for every coding agent.
> L24: Hermes IDE is a desktop app for macOS, Windows and Linux. Every agent runs its own interface in a real terminal, ex
> L71: - **Every agent in its own terminal** — Claude Code, Codex, Antigravity CLI, Gemini CLI, GitHub Copilot CLI, OpenCo

## 星数曲线

```mermaid
xychart-beta
    title "hermes-hq/hermes-ide 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-23"]
    y-axis "stars" 336 --> 343
    line [337, 340, 342]
```

2026-10-18 337 → 2026-10-23 342（+5）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 mid · 依据 README sha `fedbb88ef4dd` · [字段定义](../../DATASET.md)*
