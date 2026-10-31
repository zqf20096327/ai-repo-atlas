# meller/laneconductor

⭐ 14 · JavaScript · NOASSERTION · 推送 2026-10-09 · [GitHub](https://github.com/meller/laneconductor) · [官网](https://laneconductor.com) · 个人维护

**本地优先的多 AI agent 开发编排控制台，带实时看板**

面向开发者的多 agent 编排控制平面：将 Claude Code 与 Gemini CLI 等 agent 组织到 Plan→Implement→Review→Quality Gate→Done 流水线中，以 Markdown 文件系统消息总线为事实源，通过 Git Worktree 隔离执行，提供实时 Kanban 仪表盘与 CLI。本地模式用本地 SQLite/Postgres 运行，无云依赖；远程团队模式经 Google Cloud Functions 与 Neon Postgres 扩展。许可为 Elastic 2.0，禁止作为托管服务向第三方提供。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Plan→Implement→Review→Quality Gate→Done 流水线与自动化质量门
- Git Worktree 隔离执行，保持主仓库干净，支持 PR 审批与合并
- Markdown 文件系统消息总线（conductor/tracks/）作为人与 agent 共享事实源
- Vite+React 实时 Kanban 仪表盘，另有免 CLI/DB 的 Claude 技能模式

## 适用场景

- 我在多个仓库上并行调度多个 AI agent 完成开发任务
- 通过看板实时查看各任务轨道的状态并审批 PR
- 以结构化流水线和质量门约束 agent 的代码修改

## 场景标签

`多智能体` `编码 Agent` · 领域:Agent 开发

## 证据(README 行号)

> L10: LaneConductor is a **sovereign developer environment** that orchestrates AI agents (Claude, Gemini, and more) acros
> L22: - **The Conductor Pattern**: A structured **Plan → Implement → Review → Quality Gate → Done** pipeline. Compatible 

## 星数曲线

```mermaid
xychart-beta
    title "meller/laneconductor 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `af54904d4fae` · [字段定义](../../DATASET.md)*
