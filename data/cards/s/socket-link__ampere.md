# socket-link/ampere

⭐ 40 · Kotlin · Apache-2.0 · 推送 2026-10-28 · [GitHub](https://github.com/socket-link/ampere) · 组织维护

**Kotlin 多平台 AI agent 框架：每个决策发出可查询事件**

面向 Kotlin/JVM/Android/iOS 开发者的多平台 agent 框架，核心机制是 PROPEL 认知循环（Perceive→Recall→Observe→Plan→Execute→Learn），每个阶段转换都发出结构化事件，供实时审计与多 agent 间响应式协调。提供 CLI（ampere-cli，含 TUI 仪表盘）与可嵌入的 ampere-core 库（Maven Central）。支持置信度低于阈值时升级到人工介入。注意：AgentTeam DSL 已废弃且不实际运行，当前托管运行需通过 CLI。需 Java 21+。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- PROPEL 认知循环六阶段均发出结构化可查询事件
- 多 agent 并行时互相观察推理过程实现响应式协调
- 置信度低于阈值时升级到人工介入
- 提供 CLI TUI 仪表盘与 Maven Central 嵌入式库

## 适用场景

- 在 Kotlin 项目中构建可审计的多 agent 系统
- 实时观察与调试 agent 的感知、规划与执行过程
- 需要人工介入机制的高风险 agent 决策场景

## 场景标签

`Agent 框架` `多智能体` `LLM 可观测性` · 领域:Agent 开发

## 证据(README 行号)

> L9: Ampere is a Kotlin Multiplatform framework where every agent decision emits a structured, queryable event — providin
> L92: Most agent frameworks bolt on observability after the fact — attaching tools like LangSmith or Langfuse to reconstr
> L142: Every phase transition is emitted as an event, ensuring every action inside an agent can be audited and traced.

## 星数曲线

```mermaid
xychart-beta
    title "socket-link/ampere 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 39 --> 41
    line [40, 40]
```

2026-10-18 40 → 2026-10-30 40（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `8064646aa92a` · [字段定义](../../DATASET.md)*
