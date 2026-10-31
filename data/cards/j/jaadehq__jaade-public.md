# jaadehq/jaade-public

⭐ 13 · 推送 2026-10-29 · [GitHub](https://github.com/jaadehq/jaade-public) · [官网](https://jaade.app) · 组织维护

**本地运行 Claude Code 与 Codex agent 的 macOS 桌面 IDE**

面向开发者代理编程的本地 macOS 桌面应用：在统一工作区内运行 Claude Code 与 Codex 会话，提供会话仪表盘、内联 diff 与冲突解决、可检索的会话历史、token 用量统计、cron/间隔定时自动化，以及插件、MCP 服务器与技能管理。支持实验性接入 OpenCode 与 Cursor，默认模型为 Claude Opus 4.8，支持第三方模型。以 .dmg/.zip 二进制发布，支持 Apple Silicon 与 Intel；源码未托管，本仓库仅用于沟通、issue 与发布。

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

- 统一工作区：文件、diff、计划、历史、插件与技能与 agent 会话并列
- 并行多 agent 会话管理与可恢复的会话上下文（提示、模型、分支、变更文件）
- 定时自动化：手动、cron 与间隔触发，含健康历史
- 插件、MCP 服务器与 SKILL.md 技能管理，密钥存于 keychain

## 适用场景

- 在可检查的桌面环境中并行运行和审查多个编程 agent
- 回顾 agent 会话历史、token 消耗与提交记录
- 定时触发 agent 任务并跟踪执行状态

## 场景标签

`编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L5: Jaade — *Just Another Agentic Development Environment* — is a local desktop IDE
> L6: for running Claude Code and
> L7: Codex agents. It keeps your files, diffs, plans,

## 星数曲线

```mermaid
xychart-beta
    title "jaadehq/jaade-public 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 12 --> 14
    line [13, 13]
```

2026-10-18 13 → 2026-10-31 13（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `dd3c587a3ace` · [字段定义](../../DATASET.md)*
