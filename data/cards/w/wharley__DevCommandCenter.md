# wharley/DevCommandCenter

⭐ 14 · Rust · Apache-2.0 · 推送 2026-10-29 · [GitHub](https://github.com/wharley/DevCommandCenter) · [官网](https://www.devcommandcenter.com/) · 个人维护

**本地优先的桌面 AI 编码工作台：统一管理多提供商 agent、审查与交付**

基于 Tauri 2 + Rust + React 的桌面应用，面向使用 AI coding agent 的软件开发者：在隔离的 Git worktree 中运行 agent 会话，统一接入 Claude、Codex、Cursor、Grok、Gemini、Droid 等提供商（需各自安装并认证 CLI，DCC 不捆绑），并提供 PR 审查中心、终局审查与守卫撤销、委派子会话、MCP 集成、用量统计与手机端加密中继。状态与会话保存在本地 SQLite；可选集成 ai-memory 侧车做长期记忆。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 同一工作台运行 Claude/Codex/Cursor/Grok/Gemini/Droid 等多提供商 agent 会话
- 隔离 Git worktree 任务工作区与 Last Turn Review、Guarded Undo
- Pull Request Center 支持 GitHub PR 审查与合并、GitLab MR
- 端到端加密手机端中继与本地回环 HTTP API

## 适用场景

- 并行管理多个 AI coding agent 任务与提供商会话
- 在隔离 worktree 中执行并审查 agent 代码变更
- 统一查看 GitHub/GitLab 代码审查与交付流程
- 跨提供商比较模型与 token 用量

## 场景标签

`编码 Agent` `代码审查` · 领域:编码与开发

## 证据(README 行号)

> L11: Dev Command Center (DCC) is a local-first desktop workbench for software
> L12: engineering with AI agents. It connects isolated Git worktrees, multi-provider
> L13: sessions, review and delivery workflows, terminals, usage insights, and local

## 星数曲线

```mermaid
xychart-beta
    title "wharley/DevCommandCenter 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-29", "2026-10-31"]
    y-axis "stars" 12 --> 15
    line [13, 14, 14]
```

2026-10-18 13 → 2026-10-31 14（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `1ff9a6a970e2` · [字段定义](../../DATASET.md)*
