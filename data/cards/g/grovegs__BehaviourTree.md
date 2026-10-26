# grovegs/BehaviourTree

⭐ 33 · C# · MIT · 推送 2026-10-22 · [GitHub](https://github.com/grovegs/BehaviourTree) · 组织维护

**面向 .NET/Unity/Godot 的轻量行为树框架**

Grove Games 开发的 C# 行为树框架，用于游戏 AI 行为构建：通过流式构建 API 组合 Composite、Decorator 与自定义 Action 节点，提供编译期类型安全的 Blackboard（值类型免装箱）、可复用 ChildTree 子树；核心不使用反射与运行时代码生成，兼容 IL2CPP 与 NativeAOT，目标 netstandard2.1 与 net10.0。分别提供 Unity 集成（BehaviourTreeMono 基类与可视化调试窗口）和 Godot 集成（GodotBehaviourTree 节点与调试器面板）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 流式构建 API：Selector/Sequence/Parallel/Conditional/Cooldown 等节点类型
- 类型安全 Blackboard，值类型存储不做装箱
- Unity 与 Godot 一等集成，各自带可视化调试器
- AOT 友好：无反射与运行时代码生成，支持 IL2CPP/NativeAOT

## 适用场景

- 在 Unity 或 Godot 游戏中为角色搭建 AI 行为树
- 用可视化调试器实时查看节点状态与求值路径
- 跨 .NET 项目复用同一套行为树逻辑

## 场景标签

 · 领域:游戏开发/游戏 AI

## 证据(README 行号)

> L8: A modular, allocation-conscious behaviour tree framework for AI development in C#, with first-class **Unity** and **
> L14: - **Fluent builder API** — compose trees with chainable extension methods: `Selector`, `Sequence`, `Parallel`, `Con

## 星数曲线

```mermaid
xychart-beta
    title "grovegs/BehaviourTree 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-24", "2026-10-26"]
    y-axis "stars" 31 --> 34
    line [32, 33, 33]
```

2026-10-18 32 → 2026-10-26 33（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `5a2c239279f9` · [字段定义](../../DATASET.md)*
