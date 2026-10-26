# victorb/dogoap

⭐ 205 · Rust · MIT · 推送 2025-11-06 · [GitHub](https://github.com/victorb/dogoap) · [官网](https://victorb.github.io/dogoap/) · 个人维护

**数据导向 GOAP 库，为 Bevy 游戏 NPC 提供目标导向行动计划**

Rust 实现的 Goal-Oriented Action Planning 库，采用数据导向设计，支持在运行时动态设置状态、动作与目标，而非仅编译期定义。规划器根据定义的目标自动推算实体需执行的动作序列（如移动、拾取、放置等依赖任务）。同时提供 bevy_dogoap 集成包，通过 DatumComponent/ActionComponent 组件接入 Bevy ECS，另有独立的 dogoap 核心库可脱离 Bevy 使用。以 crates.io 包形式分发，面向游戏开发者构建 NPC 涌现式行为。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 数据导向 GOAP，支持运行时动态设置状态/动作/目标
- bevy_dogoap 提供 Bevy ECS 紧密集成（组件式 API）
- 规划器自动推算实体达到目标所需的动作序列
- 可脱离 Bevy 作为独立库使用

## 适用场景

- 为依赖链任务（取物→移动→放置）的 NPC 生成行动计划
- 在 Bevy 游戏中实现 NPC 的涌现式行为
- 介于 Utility AI 与 HTN 之间的 NPC 行为方案

## 场景标签

`Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L8: > AKA DOGOAP - GOAP implemented in data-oriented way to facilitate dynamically setting up states/actions/goals rathe
> L10: > Includes bevy_dogoap which provides a neat Bevy integration of the dogoap library
> L23: - If you have NPCs that have to perform tasks that depend on each other (Move to A > pickup item X > move to B > dr

## 星数曲线

```mermaid
xychart-beta
    title "victorb/dogoap 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 204 --> 206
    line [205, 205]
```

2026-10-18 205 → 2026-10-26 205（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `6890dfbb039b` · [字段定义](../../DATASET.md)*
