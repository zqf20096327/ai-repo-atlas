# berserkdisruptors/buildforce-cli

⭐ 35 · TypeScript · Apache-2.0 · 推送 2026-02-20 · [GitHub](https://github.com/berserkdisruptors/buildforce-cli) · [官网](https://buildforce.dev) · 组织维护

**给 AI 编码 agent 用的工程纪律框架：结构化规范与持久上下文库**

面向使用 AI 编码助手（Claude Code、Cursor 等）的开发者的 CLI 与斜杠命令框架。通过 buildforce init 在项目内生成 .buildforce/ 上下文仓库，将用户意图固化为 spec.yaml（需求与验收标准）与 plan.yaml（执行计划），用 /buildforce.research、/buildforce.plan、/buildforce.build、/buildforce.complete 四阶段工作流编排开发过程，记录实现偏差并沉淀设计决策到版本化的 YAML 上下文文件，供后续会话引用。上下文以 YAML 文件存于代码库中随版本管理累积。

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

- research/plan/build/complete 四阶段斜杠命令工作流
- 用户意图固化为 spec.yaml 与 plan.yaml，偏差记录含 Original→Actual→Reason
- 持久上下文仓库 .buildforce/context/ 跨会话累积项目知识
- /buildforce.build 支持无会话的独立模式处理快速修改

## 适用场景

- 让 AI 编码助手在新功能开发时遵循既有架构决策
- 为需求建立结构化规范与验收标准后再实施
- 团队共享跨会话累积的项目上下文知识

## 场景标签

`Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L10: Buildforce brings **engineering discipline to AI-assisted development** through CLI initialization and slash comman
> L12: It materializes user intent into structured specifications, generates actionable plans, and tracks execution with f
> L110: Buildforce uses slash commands inside AI assistant conversations to orchestrate a structured workflow. Unlike typi

## 星数曲线

```mermaid
xychart-beta
    title "berserkdisruptors/buildforce-cli 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 34 --> 36
    line [35, 35]
```

2026-10-18 35 → 2026-10-28 35（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `1ee5a576ea0e` · [字段定义](../../DATASET.md)*
