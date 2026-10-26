# Calamari/BehaviorTree.js

⭐ 339 · JavaScript · 推送 2026-03-09 · [GitHub](https://github.com/Calamari/BehaviorTree.js) · 个人维护

**给游戏开发者的 JavaScript 行为树实现库**

一个零依赖的 JavaScript 行为树（Behavior Tree）库，面向需要在游戏循环中实现 AI 行为逻辑的开发者。提供 Task、Sequence、Selector、Random Selector 等节点类型与 Decorator 机制（如 InvertDecorator、CooldownDecorator），通过 blackboard 共享状态，在游戏循环中调用 step() 驱动执行；支持任务注册表按名引用、从 JSON 定义导入树结构、Introspector 调试（不建议生产环境使用）。支持 ES modules 与 CommonJS（含 node v8），提供 UMD 包供浏览器直接使用，TypeScript 支持在 typescript 分支开发中（将随 3.0 发布）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 提供 Task/Sequence/Selector/Random Selector 与 Decorator 机制
- BehaviorTreeImporter 可从 JSON 定义构建树
- Introspector 接口收集每次 step 的运行统计用于调试
- 零自身依赖，支持 ES modules/CommonJS 与浏览器 UMD 包

## 适用场景

- 在游戏循环中驱动 NPC 或人工玩家的行为决策
- 用 JSON 定义行为树并动态加载
- 调试和检查行为树的执行路径与返回状态

## 场景标签

 · 领域:游戏开发/AI 行为控制

## 证据(README 行号)

> L3: A JavaScript implementation of Behavior Trees. They are useful for implementing AIs. If you need more information ab
> L116: The `blackboard` you specified will be passed into every `start()`, `end()` and `run()` method as first argument. 

## 星数曲线

```mermaid
xychart-beta
    title "Calamari/BehaviorTree.js 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 338 --> 340
    line [339, 339]
```

2026-10-18 339 → 2026-10-26 339（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 mid · 依据 README sha `e30a64b9d06b` · [字段定义](../../DATASET.md)*
