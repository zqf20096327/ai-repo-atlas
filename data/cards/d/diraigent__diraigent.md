# diraigent/diraigent

⭐ 21 · Rust · Apache-2.0 · 推送 2026-10-12 · [GitHub](https://github.com/diraigent/diraigent) · [官网](https://www.diraigent.com) · 组织维护

**自托管 AI 辅助软件开发协调平台：目标分解与代理执行**

将项目、任务、项目知识、聊天与人工评审整合到共享工作区的平台。Orchestra worker 在隔离的 Git worktree 中运行编码代理并管理任务执行与 Git 交付；默认执行提供方为 OpenCode，Codex 与 Claude Code 为可选替代。API 为认证控制平面（Rust/Axum + PostgreSQL），Web（Angular）与 iOS 客户端经同一 API 访问。任务经固定状态机流转，可在 human_review 处人工介入；支持嵌套项目、六种代理权限、MCP 集成与可选 Orchestra 持久化存储。通过 git clone 与 start.sh（Docker Compose）部署。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- Orchestra worker 在隔离 Git worktree 中运行编码代理并按策略交付
- 任务状态机含 human_review 人工评审环节
- 嵌套项目与六种代理权限（execute/delegate/review/create/decide/manage）
- Web、iOS、TUI（实验性）多客户端经统一 API 访问

## 适用场景

- 团队以自托管方式协调 AI 编码代理完成软件任务
- 在关键环节插入人工评审再合并代码
- 跨任务沉淀项目知识、决策与审计记录

## 场景标签

`多智能体` `编码 Agent` · 领域:Agent 开发

## 证据(README 行号)

> L5: Diraigent brings projects, tasks, project knowledge, chat and human review into one shared workspace. Orchestra work
> L14: - **Task execution and Git delivery** — Orchestra claims ready tasks, runs the selected provider in isolated worktr

## 星数曲线

```mermaid
xychart-beta
    title "diraigent/diraigent 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-25", "2026-10-28"]
    y-axis "stars" 19 --> 22
    line [20, 21, 21]
```

2026-10-18 20 → 2026-10-28 21（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `853658938f9e` · [字段定义](../../DATASET.md)*
