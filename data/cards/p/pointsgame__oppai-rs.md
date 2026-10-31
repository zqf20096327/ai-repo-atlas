# pointsgame/oppai-rs

⭐ 14 · Rust · AGPL-3.0 · 推送 2026-10-15 · [GitHub](https://github.com/pointsgame/oppai-rs) · 个人维护

**Points 棋类游戏的 AI 引擎：搜索最优落子**

用 Rust 编写的棋类游戏 Points 的人工智能程序，附带基于 iced 模块的可对弈界面。核心是两种最优着法搜索算法：UCT（蒙特卡洛树搜索，支持树复用）与 Minimax（含 PVS/NegaScout 和 MTD(f) 两种实现），并提供无锁多线程、Zobrist 哈希置换表、DFA 模式匹配、通用征子求解器等机制。需安装 Rust 后以 cargo 编译运行，支持 target-cpu=native 提升性能。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | AGPL-3.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- UCT 与 Minimax 两种搜索算法，Minimax 含 PVS/NegaScout 与 MTD(f) 实现
- 无锁多线程与 Zobrist 哈希置换表
- DFA 模式匹配与通用征子（ladder）求解器
- UCT 树在着法间复用

## 适用场景

- 与 AI 对弈 Points 游戏
- 研究 UCT/Minimax 搜索算法的实现
- 作为棋类 AI 引擎二次开发的基础

## 场景标签

 · 领域:游戏/棋类 AI

## 证据(README 行号)

> L5: Oppai-rs (acronym for "OPen Points Artificial Intelligence") is an artificial
> L6: intelligence for the game of points.
> L12: * Two algorithms for searching the optimal move: UCT, Minimax.

## 星数曲线

```mermaid
xychart-beta
    title "pointsgame/oppai-rs 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `3acfd6bdd2c4` · [字段定义](../../DATASET.md)*
