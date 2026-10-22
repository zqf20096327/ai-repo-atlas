# Zulko/easyAI

⭐ 663 · Python · NOASSERTION · 推送 2026-01-20 · [GitHub](https://github.com/Zulko/easyAI) · [官网](http://zulko.github.io/easyAI/) · 个人维护

**双人抽象博弈的 Python AI 框架：定义游戏规则并对抗/求解**

纯 Python 实现的两人抽象博弈（井字棋、Connect 4、黑白棋等）人工智能框架。用户通过继承 TwoPlayerGame 类定义游戏机制（合法走法、胜负判定、计分），即可与计算机对弈或求解整局游戏。核心算法为带 alpha-beta 剪枝与置换表的 Negamax，支持迭代加深求解，求解后可基于置换表完美对弈。通过 pip 安装，运行示例需额外安装 Numpy。MIT 许可，由 Zulko 与 JohnAD 维护。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Negamax 算法 + alpha-beta 剪枝 + 置换表
- 继承 TwoPlayerGame 类即可定义自定义游戏
- solve_with_iterative_deepening 迭代加深求解游戏胜负与最优首步
- 基于置换表实现无需搜索的完美对弈

## 适用场景

- 为井字棋、Connect 4、黑白棋等双人游戏编写 AI 对手
- 求解双人完全信息博弈的必胜/必败结论
- 学习博弈搜索算法（Negamax、alpha-beta、置换表）的教学实践

## 场景标签

 · 领域:游戏/算法库

## 证据(README 行号)

> L3: EasyAI (full documentation here_) is a pure-Python artificial intelligence framework for two-players abstract games 
> L5: Under the hood, the AI is a Negamax algorithm with alpha-beta pruning and transposition tables as described on Wikip

## 星数曲线

```mermaid
xychart-beta
    title "Zulko/easyAI 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-22"]
    y-axis "stars" 665 --> 667
    line [666, 666]
```

2026-10-18 666 → 2026-10-22 666（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `b8fa91b1e2a9` · [字段定义](../../DATASET.md)*
