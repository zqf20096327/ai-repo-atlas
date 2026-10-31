# freema/codeforge

⭐ 15 · Go · MIT · 推送 2026-10-25 · [GitHub](https://github.com/freema/codeforge) · [官网](https://codeforge.tomasgrasl.cz) · 个人维护

**自托管后端编排器：在 git 仓库上运行 AI CLI 会话与自动 PR 审查**

CodeForge 是用 Go + React 构建的 AI 代码工作编排后端：以会话为单位克隆仓库、运行 AI CLI（Claude Code / Codex / Cursor）、SSE 实时流式输出工具调用与成本、保留工作区供后续追问与开 PR。提供 Server（队列 + worker + API + UI）与 CI Action（GitHub Action / GitLab CI 步骤，用于自动 PR 审查）两种模式，含蓝图模板、定时会话、成本配额与 Prometheus 指标。安全上会话与服务器同容器运行，尚无每会话沙箱隔离。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 多轮会话支持原生对话恢复（claude --resume）
- 实时流式输出工具调用、计划进度与每轮 token/美元成本（SSE）
- Blueprints 可复用会话模板与 cron 定时会话
- 内置 PR 审查，可由 GitHub/GitLab webhook 自动触发

## 适用场景

- 在自托管环境中批量运行 AI 编码会话并人工审查 diff 后再开 PR
- 通过 webhook 自动化 PR 审查流程
- 按计划周期性执行仓库审查与知识文档更新

## 场景标签

`代码审查` `编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L13: CodeForge is a backend orchestrator for AI-powered code work over git repositories. A **session** is a stateful wor
> L15: **Two modes:** Server (queue + workers + API + UI) or **CI Action** (self-contained GitHub Action / GitLab CI step 
> L27: - **Multi-CLI** (Claude Code, Codex, Cursor) selectable per session, plus MCP tool integration

## 星数曲线

```mermaid
xychart-beta
    title "freema/codeforge 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-31"]
    y-axis "stars" 13 --> 16
    line [14, 15, 15]
```

2026-10-18 14 → 2026-10-31 15（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `11b8e5516936` · [字段定义](../../DATASET.md)*
