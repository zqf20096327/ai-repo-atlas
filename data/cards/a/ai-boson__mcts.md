# ai-boson/mcts

⭐ 34 · Ruby · MIT · 推送 2026-08-19 · [GitHub](https://github.com/ai-boson/mcts) · [官网](https://ai-boson.github.io/mcts/) · 个人维护

**MCTS 算法教程：逐函数讲解代码并演示在游戏 AI 中的应用**

面向熟悉基础 Python 的读者，以教程形式讲解蒙特卡洛树搜索（MCTS）算法：逐段展示 MonteCarloTreeSearchNode 类的实现，覆盖选择（UCT 公式）、扩展、模拟（rollout）、反向传播四步，并逐函数注释。以作者自研的 9x9 Sudoku 式井字棋（Sudo Tic Tac Toe，Google Play 上架）为例说明算法在高分支因子、minimax 不适用的场景下的应用；同时给出将代码迁移到自研游戏需修改的接口函数清单。代码依赖 numpy，属教学性仓库而非可安装的库。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 逐函数讲解 MCTS 节点类实现（选择/扩展/模拟/反向传播）
- 以 9x9 Sudoku 式井字棋演示高分支因子场景下的应用
- 列出迁移到自研游戏需修改的接口函数（get_legal_actions/is_game_over/game_result/move）

## 适用场景

- 学习蒙特卡洛树搜索算法的原理与代码实现
- 为自己的棋类游戏接入 MCTS 决策 AI
- 理解高分支因子博弈中 minimax 不适用时的替代方案

## 场景标签

`教程课程` · 领域:学习与行业

## 证据(README 行号)

> L1: # Monte Carlo Tree Search (MCTS) algorithm tutorial with Python code. Application of MCTS to create A.I for simple g
> L3: In this tutorial we will be explaining the Monte Carlo Tree Search algorithm and each part of the code. Recently we 

## 星数曲线

```mermaid
xychart-beta
    title "ai-boson/mcts 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 33 --> 35
    line [34, 34]
```

2026-10-18 34 → 2026-10-26 34（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `79cd8fbe76aa` · [字段定义](../../DATASET.md)*
