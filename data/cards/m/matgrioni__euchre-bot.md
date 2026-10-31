# matgrioni/euchre-bot

⭐ 18 · Go · 推送 2025-12-01 · [GitHub](https://github.com/matgrioni/euchre-bot) · 个人维护

**Go 编写的 euchre 纸牌游戏 AI（MCTS/minimax/规则）**

个人学习项目：用 Go 实现的 euchre 纸牌游戏 AI，比较三种玩家策略——MCTS（基于 UCB 的节点选择与均匀 determinization 采样）、minimax（明牌基准）与规则方法。游戏无关的 AI 库位于 src/ai，各策略通过 src/player 的玩家接口实现。README 记录了 1000 个随机生成局面上的非配对与配对评测方法及结果（配对下 MCTS 达到最优结果的 91.6% 次数）。未提供安装运行命令。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- MCTS 用于实际出牌，感知机用于叫牌决策（已实现但未启用）
- minimax 明牌玩家作为最优基准用于评测
- 1000 个随机局面的配对/非配对评测流程与结果记录

## 适用场景

- 研究比较 MCTS、minimax 与规则方法在纸牌博弈中的表现
- 复用游戏无关的 AI 库做其他牌类实验

## 场景标签

 · 领域:游戏 AI/算法实验

## 证据(README 行号)

> L1: # Albert: The Euchre AI
> L5: The AI algorithms in use now or that have already been implemented but are not currently in use are the perceptron f
> L11: The game agnostic AI libraries live in `src/ai`. These libraries are used by the different player logic found in `s

## 星数曲线

```mermaid
xychart-beta
    title "matgrioni/euchre-bot 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 17 --> 19
    line [18, 18]
```

2026-10-18 18 → 2026-10-31 18（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `2510530c7967` · [字段定义](../../DATASET.md)*
