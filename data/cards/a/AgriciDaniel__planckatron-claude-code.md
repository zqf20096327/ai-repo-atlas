# AgriciDaniel/planckatron-claude-code

⭐ 31 · PowerShell · MIT · 推送 2026-04-10 · [GitHub](https://github.com/AgriciDaniel/planckatron-claude-code) · [官网](https://agricidaniel.com) · 个人维护

**Claude Code 的多 agent 并行编排技能（SKILL.md）**

一个置于项目 .planckatron 目录中的 Claude Code 技能定义：由 Claude 担任 Orchestrator，Team Leads 分析任务并生成 mini-agents 并行执行，宣称避免冲突；提供可视化计划图、实时进度板、完成报告、重试流程与验证门等机制，支持前端、后端、全栈、自动化、库与 monorepo 等项目类型。运行需 Claude Code CLI 或 VS Code 扩展，以及 Node.js 18+（用于质量检查）。MIT 许可。

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

- Orchestrator–Team Leads–mini-agents 层级并行编排
- 视觉化 Quantum Plan 计划图与 Alpha/Beta/Gamma 实时进度板
- 重试流程与验证门机制
- 以 .planckatron/SKILL.md 形式嵌入项目，通过 CLAUDE.md 触发

## 适用场景

- 在 Claude Code 中用多个并行 agent 开发前端/后端/全栈项目
- 对 monorepo 或库项目做任务拆分与并行执行
- 通过命令与进度板跟踪多 agent 任务进展

## 场景标签

`多智能体` `编码 Agent` · 领域:Agent 开发

## 证据(README 行号)

> L10: **Hierarchical Multi-Agent Orchestration System (v3.0)**
> L123: - Claude Code CLI or VS Code extension
> L32: **Key:** Team Leads analyze tasks and spawn mini-agents. Maximum parallelism.

## 星数曲线

```mermaid
xychart-beta
    title "AgriciDaniel/planckatron-claude-code 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 30 --> 32
    line [31, 31]
```

2026-10-18 31 → 2026-10-26 31（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 mid · 依据 README sha `3bd69f611c6f` · [字段定义](../../DATASET.md)*
