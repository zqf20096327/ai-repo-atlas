# rochecompaan/patchmill

⭐ 15 · TypeScript · Apache-2.0 · 推送 2026-10-29 · [GitHub](https://github.com/rochecompaan/patchmill) · [官网](https://patchmill.dev) · 个人维护

**面向团队的 agent 驱动软件工厂，把议题自动变成已审查的代码变更**

Patchmill 是一个 npm 分发的 CLI 工具，连接 issue 托管平台（GitHub/Forgejo/Gitea）、仓库策略、git worktree 与可配置 agent 技能，将产品工作转化为经审查、可落地的变更。流程覆盖：triage 分类议题、规划、隔离实现（总是创建 PR）、收集证据、审查后落地。支持 Superpowers 技能包提供规划与审查纪律，前端变更要求离线 HTML mockup 与独立复审。自动选择串行执行，显式指定 issue 可并行但并发不受支持。Apache-2.0 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 连接 issue 主机、git worktree 与可配置 agent 技能的端到端流水线
- 支持 GitHub（gh CLI）与 Forgejo/Gitea（tea CLI）
- 实现阶段总是创建 PR，PR 合并后可续跑检查点
- 与 Superpowers 技能包配合提供规划/实现/审查纪律

## 适用场景

- 团队用 agent 自动分诊并推进开源仓库的 issue 到 PR
- 在隔离的 git worktree 中并行处理独立 issue
- 对前端变更执行独立复审与证据收集

## 场景标签

`编码 Agent` `代码审查` · 领域:编码与开发

## 证据(README 行号)

> L3: Patchmill is an agent-driven software factory for turning product work into
> L7: It connects an issue host, repository policy, git worktrees, and configurable

## 星数曲线

```mermaid
xychart-beta
    title "rochecompaan/patchmill 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-30 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `9a39a710aa42` · [字段定义](../../DATASET.md)*
