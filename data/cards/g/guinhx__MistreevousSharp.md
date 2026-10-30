# guinhx/MistreevousSharp

⭐ 15 · C# · 推送 2025-11-22 · [GitHub](https://github.com/guinhx/MistreevousSharp) · 个人维护

**C# 行为树库：用 JSON/DSL 定义游戏 AI 决策逻辑**

面向 .NET 9.0 与 .NET Standard 2.1 的行为树库，由 TypeScript 库 mistreevous 移植。开发者用 JSON 或 MDSL DSL 定义行为树，内置 Sequence/Selector/Parallel/Race/Lotto 等组合节点与 Repeat/Retry 等装饰节点，支持异步动作、生命周期回调、守卫中断、可种子化的随机数以实现确定性树执行，并提供节点状态查看等调试手段。面向游戏、仿真与交互式 agent 开发者，声明可用于 Unity、Godot 与游戏服务器。通过 NuGet 安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- JSON 或 MDSL DSL 两种行为树定义方式
- 内置组合/装饰/叶子节点与异步动作、守卫中断
- 可注入种子化随机函数实现确定性树执行
- 跨 .NET 9.0、.NET Standard 2.1、Unity、Godot 运行

## 适用场景

- 为游戏 NPC 定义模块化 AI 决策行为
- 在仿真或交互式 agent 中组织任务序列与控制流
- Unity/Godot/游戏服务器项目中嵌入行为树逻辑

## 场景标签

`Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L5: **MistreevousSharp** is a lightweight, C# behaviour tree library for .NET 9.0 and .NET Standard 2.1, ported from the
> L23: Behaviour trees are hierarchical structures designed to model decision-making processes and are used to create comp

## 星数曲线

```mermaid
xychart-beta
    title "guinhx/MistreevousSharp 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-28", "2026-10-30"]
    y-axis "stars" 13 --> 16
    line [14, 15, 15]
```

2026-10-18 14 → 2026-10-30 15（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `50b60e2e44d5` · [字段定义](../../DATASET.md)*
