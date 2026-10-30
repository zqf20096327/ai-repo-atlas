# andreapollastri/larapilot

⭐ 23 · HTML · MIT · 推送 2026-10-15 · [GitHub](https://github.com/andreapollastri/larapilot) · 个人维护

**Laravel 的 spec 驱动工作流：让 AI 编辑器按流程交付已评审代码**

基于 Laravel Boost 的 Composer 包，为 Laravel 项目提供规格驱动开发工作流：通过 AI 编辑器中的 `/larapilot-*` 技能，走完 inception→spec→plan→implement→review 循环，产出 PRD、backlog、技术计划与经评审的代码，全部版本化在 `.larapilot/` 目录。由 Boost 技能、Artisan 命令与 MCP server 三层组成，工作流引擎阻止非法状态转换（如无计划不可实现）。包含 30 个评审 persona、Larastan/Pint 质量门、本地 dashboard 与 API（非 local 环境需登录/令牌）。面向 Laravel 开发者，人始终在环内审批。

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

- 三层架构：Boost 技能（编辑器对话）+ Artisan 命令（状态持久化与流程约束）+ MCP server（会话中读取 backlog/specs）
- 工作流引擎阻止非法转换：无 plan 不可 implement，有未完成 blocks-merge 反馈不可 approve
- 30 个评审 persona（产品/架构/安全/评审等）作为评审视角
- 质量门集成 Larastan level 5+ 与 Laravel Pint，支持 baseline 与 changed-scope 模式

## 适用场景

- 新 Laravel 产品从想法到已评审代码的全流程开发
- 为已上线但无 PRD 的 Laravel 应用补齐规格与流程（adopt）
- 在 AI 编辑器中按用户故事循环实现与评审

## 场景标签

`编码 Agent` `代码审查` · 领域:编码与开发

## 证据(README 行号)

> L5: Larapilot is a spec-driven workflow for Laravel projects, built on Laravel Boost. Install the package, run `/larapil
> L23: |**Boost skills** (`/larapilot-*`)|Drive the conversation in your editor|
> L25: |**MCP server** (`larapilot`)|Lets the agent read backlog, specs, and diagnostics mid-conversation|

## 星数曲线

```mermaid
xychart-beta
    title "andreapollastri/larapilot 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-30"]
    y-axis "stars" 21 --> 24
    line [22, 23, 23]
```

2026-10-18 22 → 2026-10-30 23（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 mid · 依据 README sha `6bf9febfbbd1` · [字段定义](../../DATASET.md)*
