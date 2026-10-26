# joeycumines/go-behaviortree

⭐ 80 · Go · Apache-2.0 · 推送 2026-07-17 · [GitHub](https://github.com/joeycumines/go-behaviortree) · 个人维护

**Go 行为树库：为游戏 AI 与机器人控制提供行为树运行机制**

Go 语言行为树（behavior tree）实现库：提供核心三类型与 Sequence/Selector 组合子、响应式支持（Memorize/Async/Sync）、NewManager/NewTicker 运行管理器、Tick 实现集合与元数据附加机制，并含基于 fmt.Stringer 的树调试输出；另通过外部仓库 go-pabt 提供实验性 PA-BT 规划算法支持。设计上仅关注运行行为树本身，便于接入外部实现。面向需要用行为树组织决策与控制逻辑的 Go 开发者。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 核心行为树类型与 Sequence/Selector 无状态组合子
- 响应式支持（Memorize/Async/Sync）与 NewManager/NewTicker 运行管理
- Context 机制处理超时等场景，跨 API 边界附加元数据
- 实验性 PA-BT 规划算法支持（经 go-pabt 仓库）

## 适用场景

- 在 Go 项目中用行为树组织游戏 AI 或机器人控制逻辑
- 将复杂切换逻辑分解为可组合、可中断的模块化节点
- 运行与调试带记忆与异步行为的响应式行为树

## 场景标签

 · 领域:游戏 AI/机器人控制

## 证据(README 行号)

> L5: Package behaviortree provides a simple and powerful Go implementation of behavior trees without fluff.
> L9: Wikipedia: Behavior tree - AI, robotics, and control)

## 星数曲线

```mermaid
xychart-beta
    title "joeycumines/go-behaviortree 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 79 --> 81
    line [80, 80]
```

2026-10-18 80 → 2026-10-26 80（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 mid · 依据 README sha `e64affd93370` · [字段定义](../../DATASET.md)*
