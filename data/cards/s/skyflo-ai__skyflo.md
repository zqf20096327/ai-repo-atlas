# skyflo-ai/skyflo

⭐ 121 · Python · Apache-2.0 · 推送 2026-10-02 · [GitHub](https://github.com/skyflo-ai/skyflo) · [官网](https://skyflo.ai) · 组织维护

**面向跨仓库工程任务的 AI agent 协调控制平面（开源版已弃用）**

本仓库原为开源的 Kubernetes/DevOps AI agent，现已弃用；现行 Skyflo Desktop 为独立闭源产品，协调 Codex、Claude Code、Cursor Agent 等编码 agent 在多仓库任务中协作：用户定义目标、审批计划、由编码专家在隔离 Git worktree 内执行，再由只读 reviewer 独立审查结果。执行留在本地 Mac，BYOK 凭据存于 macOS 钥匙串，并具备跨任务的记忆与可复用 Skill 机制。遗留代码、部署资产与 Apache 2.0 许可仍保留可用，但不提供自动迁移。macOS 14+，Apple silicon 与 Intel。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 多 agent（Codex/Claude Code/Cursor Agent 等）在单一任务内跨仓库协调
- 计划审批门控 + 只读 reviewer 独立审查 + 隔离 Git worktree 执行
- 任务间记忆与可复用 Skill，学习内容可审查与撤销
- BYOK 凭据存储于 macOS Keychain，执行留在本地 Mac

## 适用场景

- 跨多个仓库的工程变更任务（API 修改后同步客户端与基础设施配置）
- 在一个工作区内管理编码 agent 的计划、执行与审查全流程
- 既有部署继续运行遗留的 Kubernetes agent

## 场景标签

`多智能体` `编码 Agent` · 领域:Agent 开发

## 证据(README 行号)

> L7: Coordinate **Codex, Claude Code, Cursor Agent, and your own agents** across repositories, from an approved plan to a
> L26: |Your preferred coding agents|Run Codex, Claude Code, Cursor Agent, and other supported agents inside a Skyflo miss
> L9: Skyflo Desktop brings your agents, models, code, browser, and terminal into one durable mission. Define the objectiv

## 星数曲线

```mermaid
xychart-beta
    title "skyflo-ai/skyflo 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 120 --> 122
    line [121, 121]
```

2026-10-18 121 → 2026-10-24 121（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `da45560d2d14` · [字段定义](../../DATASET.md)*
