# microsoft/devsquad-copilot

⭐ 50 · MIT · 推送 2026-10-30 · [GitHub](https://github.com/microsoft/devsquad-copilot) · [官网](https://aka.ms/devsquad-copilot) · 组织维护

**基于 GitHub Copilot 的团队交付框架：从业务意图到实现**

面向多人协作团队的开发交付框架，运行于 GitHub Copilot 之上：由一个 conductor agent 调度 13 个专职子 agent，按 envisioning→spec→ADR→任务分解→TDD 实现→审查→持续细化的循环推进工作，任务流入 GitHub Issues 或 Azure DevOps。决策以持久化产物（spec、ADR、计划）形式留存；子 agent 上下文隔离、按影响分级授权，高影响变更需显式批准。仅要求 Node.js，可通过自定义指令/技能/agent/hook 扩展，无需修改核心。项目处于活跃开发期，1.0 前次版本可能出现破坏性变更。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- conductor agent 调度 13 个专职子 agent 的交付循环
- 任务流入 GitHub Issues / Azure DevOps 真实工作项
- 子 agent 上下文隔离与最小权限工具暴露
- 仅 Node.js 前置依赖，无框架专属 CLI/Python/语言专用工具链

## 适用场景

- 多人团队希望以持久化 spec 和 ADR 保留决策上下文
- 把用户故事分解为任务并同步到 GitHub Issues/Azure DevOps
- 在 TDD 与安全审查纪律下用 agent 辅助实现增量交付

## 场景标签

`多智能体` `编码 Agent` · 领域:Agent 开发

## 证据(README 行号)

> L5: A delivery framework for GitHub Copilot with agents that guide teams from **business intent** to **implementation**,
> L34: The loop is the unit of delivery. The whole system is orchestrated by a conductor agent that guides developers and 
> L59: See the Getting Started guide for installation on VS Code and GitHub Copilot CLI, prerequisites, and project initia

## 星数曲线

```mermaid
xychart-beta
    title "microsoft/devsquad-copilot 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-31"]
    y-axis "stars" 48 --> 51
    line [49, 50, 50]
```

2026-10-18 49 → 2026-10-31 50（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `6a6eba77ae34` · [字段定义](../../DATASET.md)*
