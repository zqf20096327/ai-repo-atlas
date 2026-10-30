# AnisKaram/Unity-Modular-Game-Architecture

⭐ 16 · C# · 推送 2026-10-03 · [GitHub](https://github.com/AnisKaram/Unity-Modular-Game-Architecture) · 个人维护

**Unity 6 模块化游戏架构示例框架，含 MVP/FSM/Utility AI 等多个系统**

面向 Unity 开发者的模块化游戏架构框架示例：以 Clean Architecture 组织代码，包含 MVP 背包系统（拖拽/堆叠/JSON 存读档）、FSM 物理角色控制器、VContainer 依赖注入、Utility AI NPC（基于评分与响应曲线决策）、EventBus 交互系统、命令模式时间回溯系统，以及 UI Toolkit 物品编辑器工具。核心逻辑为纯 C#，提供 NUnit EditMode 单元测试，在 Unity 6 中打开即可运行原型场景。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- MVP 背包系统，Model 为纯 C# 且带 JSON 存读档
- FSM 角色控制器（Idle/Move/Jump）与 ScriptableObject 数据驱动调参
- Utility AI NPC：评分考量（0.0-1.0）+ AnimationCurve 响应曲线，控制 FSM 角色并消费背包物品
- 命令模式时间回溯：CircularBuffer 存储位置/旋转，静止时不录制

## 适用场景

- 学习 Unity 中 Clean Architecture 与 MVP/FSM 的落地方式
- 参考 Utility AI 实现 NPC 的涌现式决策行为
- 复用事件总线、存档服务、时间回溯等模块到自己的游戏项目

## 场景标签

 · 领域:游戏开发/架构框架

## 证据(README 行号)

> L3: A production-ready, modular Game Architecture Framework demonstrating **Clean Architecture**, **Dependency Injection
> L33: * **🧠 Utility AI Brain:** A non-linear decision-making system where NPCs evaluate actions based on scored considera

## 星数曲线

```mermaid
xychart-beta
    title "AnisKaram/Unity-Modular-Game-Architecture 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-30"]
    y-axis "stars" 14 --> 17
    line [15, 16, 16]
```

2026-10-18 15 → 2026-10-30 16（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `bce79ccc9363` · [字段定义](../../DATASET.md)*
