# hoangtng/real-estate-agents

⭐ 28 · MIT · 推送 2026-05-15 · [GitHub](https://github.com/hoangtng/real-estate-agents) · 个人维护

**面向 Claude 的房地产垂直 agent 与技能库：12 个角色 + 12 个交付技能**

基于 msitarzewski/agency-agents 框架构建的房地产行业扩展库，由两部分组成：12 个以 Markdown 系统提示定义的 agent 角色（如挂牌经纪人、市场分析师、合规顾问）与 12 个以 SKILL.md 工作流定义的技能（生成 CMA、报价策略、营销方案、投资测算、合规审计等结构化交付物）。安装方式为将文件复制到 ~/.claude/agents/ 与 ~/.claude/skills/，在 Claude Code 或 Claude.ai 中通过自然语言触发，技能根据任务语境自动激活。本身不含模型，运行依赖 Claude。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 12 个带人设、规则与交付模板的 agent 角色
- 12 个技能生成 CMA、报价简报、NOI/BRRRR 测算、合规审计等结构化文档
- 技能根据任务语境自动激活，无需显式指定技能名
- README 给出挂牌、买方代理、投资收购三条多 agent 协作工作流示例

## 适用场景

- 让 Claude 以专业角色生成比较市场分析（CMA）与定价建议
- 为投资房产生成 NOI、资本化率与 BRRRR 测算模型
- 对挂牌文案做公平住房合规审查
- 按工作流串联多角色完成从委托到交割的全流程文档

## 场景标签

`多智能体` `提示工程` · 领域:Agent 开发

## 证据(README 行号)

> L5: > A complete real estate agency in two parts: **12 AI agent personas** (the team) + **12 production skills** (the de
> L23: |**What it is**|A persona Claude becomes|A deliverable Claude produces|
> L24: |**Format**|`agents/realestate-*.md` (system prompt)|`skills/*/SKILL.md` (workflow)|

## 星数曲线

```mermaid
xychart-beta
    title "hoangtng/real-estate-agents 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-28"]
    y-axis "stars" 26 --> 29
    line [27, 28, 28]
```

2026-10-18 27 → 2026-10-28 28（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 mid · 依据 README sha `cede3e079997` · [字段定义](../../DATASET.md)*
