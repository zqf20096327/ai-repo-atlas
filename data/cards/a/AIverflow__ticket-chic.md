# AIverflow/ticket-chic

⭐ 3 · Python · MIT · 推送 2026-11-08 · [GitHub](https://github.com/AIverflow/ticket-chic) · 个人维护

**为 AI 编码 agent 提供基于 git 的极简工单/看板系统**

单文件 Python（约 590 行，仅标准库）实现的工单系统：工单为 .tickets/ 目录下的 markdown 文件，提供静态 HTML 看板（过滤、搜索、无需服务器），git hook 在 commit 主题含 (T12) 时自动关闭工单。面向 AI 编码 agent 设计：工单带难度与体量字段，模块定义 orchestrator/implementer/reviewer 三种角色、chain/validate 两种工作模式及 worktree 并行规则。.tickets/ 为独立 git 仓库，支持 sync 多机同步（官方注明仅轻度测试，不建议团队跟踪用）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 单 Python 文件，仅依赖标准库，需 git
- markdown 工单 + 静态 HTML 看板，无服务器
- git commit 主题带 (T12) 即由 hook 关闭工单
- 面向 agent 的角色分工、chain/validate 模式与 worktree 并行

## 适用场景

- 让 Claude Code/Codex 等 agent 按工单依次或并行完成任务
- 用 commit 消息自动追踪工单关闭状态
- 在多个机器间用 git 远程同步工单

## 场景标签

`工作流自动化` · 领域:效率与自动化

## 证据(README 行号)

> L3: A minimal ticket system for your projects and the AI agents working on them. It needs only git and Python, no packag
> L9: - **Made for agents.** Each ticket has a difficulty and a size. Modules give agents roles and worktree rules.


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-24 · 置信度 high · 依据 README sha `5be4e2eb6653` · [字段定义](../../DATASET.md)*
