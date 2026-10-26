# guided-engineering/OpenPrompt-Specification

⭐ 27 · 推送 2026-05-17 · [GitHub](https://github.com/guided-engineering/OpenPrompt-Specification) · 组织维护

**面向工程师的规范驱动开发（SDD）框架：用版本化 YAML 提示词编排 AI 代理**

一套名为 Guided Engineering 的 Spec-Driven Development 方法论与规范仓库：以版本化的 YAML 提示词、specs、personas 和 JSON Schema 为核心，让工程师以人类主导的方式编排 LLM 等代理执行软件开发生命周期中的小型可追溯任务；所有执行产出 Markdown 文档存入 .guides/ 目录，形成需求↔规范↔测试↔提交的可追溯矩阵。仓库本身即按该方法维护，提供示例规范（用户登录）与提示词模板，但 spec-first 定位下示例无配套实现，conformance 报告标记为 DEMO。配套 CLI、Portal 等工具由生态另行提供。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 版本化 YAML 提示词 + persona + JSON Schema 校验的执行体系
- .guides/ 目录组织 specs、traceability 矩阵、ADR、worklog 等产物
- 覆盖 discovery 到 conformance-check 的完整 SDD 提示词集
- 仓库自身按 Guided Engineering 模式维护，所有变更经提示词与 persona 记录

## 适用场景

- 团队将软件开发流程改为可审计、可追溯的提示词驱动工作流
- 用 SDD 规范统一需求、设计、测试与提交的追溯链
- 为工程师定义与 AI 代理协作的标准化提示词和角色模板

## 场景标签

`提示工程` · 领域:Agent 开发

## 证据(README 行号)

> L8: ~~Vibe Coding~~ → **Guided Engineering** is a structured, traceable, and executable framework for **Spec-Driven Deve
> L59: It defines a new way of working where **engineers coordinate agents** (e.g., LLMs, tools, automations) to execute s
> L141: - **Human-led by design**: AI and agents assist, but direction, judgment, and intent come from humans.

## 星数曲线

```mermaid
xychart-beta
    title "guided-engineering/OpenPrompt-Specification 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 26 --> 28
    line [27, 27]
```

2026-10-18 27 → 2026-10-26 27（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `0f4fe36bb7d6` · [字段定义](../../DATASET.md)*
