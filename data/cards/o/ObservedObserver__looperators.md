# ObservedObserver/looperators

⭐ 49 · TypeScript · Apache-2.0 · 推送 2026-09-27 · [GitHub](https://github.com/ObservedObserver/looperators) · 个人维护 · 中文 README

**把 AI 编程 agent 放上画布并连成自动循环的 macOS 工作台**

面向使用多个 AI 编程 agent 的开发者：将 Claude Code、Codex、Grok Build 等 agent 会话作为节点放到画布上，用边定义触发、上下文传递与停止条件，上游 agent 完成后输出沿边驱动下游，形成自动运行的多 agent 循环。内置 Review-until-clean、多模型辩论（Plan Council）、目标达成判定、事件监听等现成循环，Master Agent 可根据目标生成工作流提案。机制部分（事件匹配、激活、停止规则、持久化）确定性执行，判断部分交给模型。当前为早期 alpha，仅提供 macOS Apple Silicon 构建，其他平台需 npm 从源码运行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 画布上的边可执行：定义触发、上下文传递与停止条件
- 内置 Plan Council 多模型辩论与 Review-until-clean 循环
- Master Agent 根据目标提案参与方、关系与停止条件
- 支持最大轮数、预算、审批门等治理控制

## 适用场景

- 让编码 agent 与审查 agent 组成循环自动迭代直至通过
- 多模型同时起草方案并相互质询直至收敛
- 定时、Git 变更或 webhook 触发的自动化维护循环

## 场景标签

`多智能体` `编码 Agent` `工作流自动化` · 领域:Agent 开发

## 证据(README 行号)

> L28: loop is finished. looperators hands all three to the graph. Agents sit on a canvas,
> L79: Choose a ready-made loop or describe the goal to a Master Agent. The system can
> L252: 2. Install and sign in to at least one supported code agent—Claude Code,

## 星数曲线

```mermaid
xychart-beta
    title "ObservedObserver/looperators 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 48 --> 50
    line [49, 49]
```

2026-10-18 49 → 2026-10-27 49（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `79332b22ce02` · [字段定义](../../DATASET.md)*
