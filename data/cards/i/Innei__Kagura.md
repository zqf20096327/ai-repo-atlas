# Innei/Kagura

⭐ 55 · TypeScript · MIT · 推送 2026-10-24 · [GitHub](https://github.com/Innei/Kagura) · 个人维护

**在 Slack 中运行 Claude/Codex 编码 agent 的 Socket Mode 机器人**

TypeScript 编写的 Slack 应用，通过 Socket Mode 将 Anthropic Claude Agent SDK、OpenAI Codex CLI 或 Pi Agent 接入工作区：按线程路由会话到指定仓库，渲染 Slack 富文本与实时进度，以 SQLite 存储分层记忆。提供 Web 代码审查面板（diff/源码视图）、A2A 多 agent 协作线程、斜杠命令与交互式初始化向导。要求 Node.js ≥ 24，需 Slack 应用与对应 AI CLI 登录后方可使用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Socket Mode 接入 Claude Agent SDK / Codex CLI / Pi Agent 三类 provider
- 线程感知的多模态上下文与跨重启的会话恢复
- SQLite 分层记忆（全局/工作区/偏好）与后台清理整理器
- 只读 Web 代码审查面板：文件树、GitHub 式 diff、Shiki 高亮

## 适用场景

- 在 Slack 里直接对仓库提需求，让编码 agent 完成改动
- 团队在 Slack 线程中查看 agent 的代码改动 diff
- 多 agent 协作：@用户组触发 lead 协调的 A2A 线程

## 场景标签

`编码 Agent` `代码审查` · 领域:编码与开发

## 证据(README 行号)

> L14: **Kagura** brings that spirit to Slack. Run Anthropic Claude Agent SDK or OpenAI Codex CLI natively in your workspa
> L18: Running a coding agent inside Slack requires gluing together thread context, workspace routing, streaming UX, sessi

## 星数曲线

```mermaid
xychart-beta
    title "Innei/Kagura 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 54 --> 56
    line [55, 55]
```

2026-10-18 55 → 2026-10-26 55（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 mid · 依据 README sha `45b2824cfb30` · [字段定义](../../DATASET.md)*
