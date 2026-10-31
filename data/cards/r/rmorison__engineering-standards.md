# rmorison/engineering-standards

⭐ 14 · Python · MIT · 推送 2026-10-11 · [GitHub](https://github.com/rmorison/engineering-standards) · [官网](https://rm.rmdashrf.net/) · 个人维护

**面向 AI 辅助软件开发的轻量工程标准与实践集**

一套文档化工程标准库：覆盖文档规范、特性开发工作流、项目规划、Git 分支策略、Issue 组织与仓库基线等流程标准，以及 Python/数据库/Web 代码质量标准。AI 部分定义六层 AI 架构（规则/技能/人格代理/参考/复合/钩子），提供带 Claude Code 配置的项目模板与 agent-team 插件，支持一人指挥多个 AI 代理会话的团队工作流。通过 QUICKSTART.md 分步采纳，标准处于草案状态、季度审查演进。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 六层 AI 架构定义 AI 工具与工程工作流的集成方式
- templates/ 提供带 .claude/ 配置的项目启动套件（技能/代理/钩子）
- agent-team 插件支持一人指挥多 AI 代理会话的运营模型
- 规范驱动的特性开发流程（Intent→Spec→Plan→Execute→Validate）

## 适用场景

- 为团队或个人项目建立轻量工程流程标准
- 将 Claude Code 等 AI 助手以结构化方式接入开发工作流
- 按模板为新项目初始化 AI 配置与工程规范

## 场景标签

 · 领域:软件开发工程/规范文档

## 证据(README 行号)

> L7: ## Purpose
> L124: ## AI / Claude Code Integration
> L128: Defines how AI tooling integrates with software engineering workflows. The architecture is the **abstraction**; sp

## 星数曲线

```mermaid
xychart-beta
    title "rmorison/engineering-standards 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `c5d07530404f` · [字段定义](../../DATASET.md)*
