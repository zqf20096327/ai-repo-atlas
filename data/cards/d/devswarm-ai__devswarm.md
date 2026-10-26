# devswarm-ai/devswarm

⭐ 141 · NOASSERTION · 推送 2026-09-24 · [GitHub](https://github.com/devswarm-ai/devswarm) · [官网](https://devswarm.ai) · 组织维护

**桌面端并行运行多个 AI 编码助手的 AI 开发环境（ADE）**

DevSwarm 是一个 macOS/Windows 桌面应用：以 Git worktree 为每个工作区提供隔离的目录、分支与端口，配套 AI 助手终端与代码编辑器，可同时运行 Claude Code、Codex、Gemini、Amazon Q 等多个 CLI 助手并行编码；内置 Review Mode 对比分支 diff、GitHub/Jira OAuth 集成与键盘优先操作。代码留在本机，助手使用用户自己的凭证或本地运行。注意：本仓库仅为公开落地页与 issue 跟踪器，应用本体是独立专有产品，提供免费 beta 下载。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 每个工作区为隔离 Git worktree：独立目录、分支与端口
- 自动检测已安装的 CLI 助手（Claude Code、Codex、Gemini、Amazon Q、Copilot、Cursor CLI 等）
- 内置 Review Mode 分支 diff 对比与语法高亮
- GitHub/Jira OAuth 集成，可从 PR 或 Jira issue 直接创建工作区

## 适用场景

- 让多个 AI 编码助手同时处理重构、测试、文档等不同任务
- 并行开发同一仓库的多个分支并逐一审阅合并
- 从 GitHub PR 或 Jira issue 快速启动隔离工作区

## 场景标签

`多智能体` `代码审查` · 领域:Agent 开发

## 证据(README 行号)

> L3: **DevSwarm is an AI Development Environment (ADE): a desktop app for running multiple AI coding assistants in parall
> L15: - **Bring your own assistant** — DevSwarm detects installed CLI assistants automatically. Supported today: Claude C

## 星数曲线

```mermaid
xychart-beta
    title "devswarm-ai/devswarm 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-25", "2026-10-26"]
    y-axis "stars" 139 --> 142
    line [140, 141, 141]
```

2026-10-18 140 → 2026-10-26 141（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `8eedf4c6f951` · [字段定义](../../DATASET.md)*
