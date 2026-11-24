# Breadstick-Crumbs/fanout

⭐ 5 · JavaScript · MIT · 推送 2026-11-08 · [GitHub](https://github.com/Breadstick-Crumbs/fanout) · [官网](https://github.com/Breadstick-Crumbs/fanout#install) · 个人维护

**协调并行 coding agent 会话，防止合并到 main 时互相破坏**

在多个并行 agent 会话（各自 worktree/分支）之下运行的协调工具：合并每个分支运行测试、把失败回传给肇因的 agent，并在会话工作期间通知其依赖代码被他人改动。通过 Sonnet 调用判定重复任务并拒绝第二个会话开工。支持 Claude Code 插件安装、Codex 技能安装，或任何读取 AGENTS.md 的 agent；无 npm 依赖，要求 Node 18+ 与 git 2.38+。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 分支合排测试（rehearsal）：单独通过、合在一起失败的分支在进 main 前被捕获
- 会话间变更通知：他人提交改动本会话读过的文件时推送 diff
- 任务声明去重：Sonnet 调用判定相同工作并拒绝新会话
- plan 机制：文件所有权、冻结共享接口、合并顺序

## 适用场景

- 多个 Claude Code/Codex 会话并行开发同一仓库时避免合并冲突
- 把一个大任务拆给多个 agent 并排执行
- 团队用 worktree 工作流时自动同步各会话认知

## 场景标签

`多智能体` `编码 Agent` · 领域:Agent 开发

## 证据(README 行号)

> L14: You run several agents, each in its own worktree and branch. Every branch passes its tests. Then you merge, and the
> L18: - **Branches that pass alone but break together are caught before main.** fanout merges every session's branch, run
> L21: - **Works with what you already use.** Worktrees, orchestrators and Claude's session messaging keep working; fanout

## 星数曲线

```mermaid
xychart-beta
    title "Breadstick-Crumbs/fanout 星数(近 3 点)"
    x-axis ["2026-10-28", "2026-11-08", "2026-11-24"]
    y-axis "stars" 3 --> 6
    line [4, 5, 5]
```

2026-10-28 4 → 2026-11-24 5（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-21 · 置信度 high · 依据 README sha `380a2ba85a55` · [字段定义](../../DATASET.md)*
