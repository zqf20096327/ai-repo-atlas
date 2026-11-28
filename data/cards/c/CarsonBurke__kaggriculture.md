# CarsonBurke/kaggriculture

⭐ 13 · Python · MIT · 推送 2026-10-02 · [GitHub](https://github.com/CarsonBurke/kaggriculture) · [官网](https://www.kaggle.com/competitions/kaggriculture/leaderboard) · 个人维护

**Kaggle 农业策略竞赛的强化学习求解方案复现库**

作者对 Kaggle Kaggriculture 竞赛的个人参赛方案，最终在公开排行榜约 10,246 队中位列第 10。核心机制：用 Rust 精确复刻官方游戏引擎作为批量并行模拟环境（经 PyO3 暴露给 Python），先在高分对局回放上做行为克隆，再用 PPO 自博弈联盟训练约 947k 参数的 actor，配套 LeJEPA 世界模型与集中式 critic。训练约需 10 小时与 CUDA GPU。仓库含训练、评估、提交脚本与技术文档。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Rust 精确复刻官方引擎的批量并行模拟器（PyO3 绑定 + 一致性校验）
- 行为克隆 + PPO 自博弈联盟训练流水线
- LeJEPA 世界模型与集中式 Win/Draw/Loss critic 共享骨干
- 提供训练/评估/提交脚本、TensorBoard 日志与消融记录

## 适用场景

- 复现或研究该 Kaggle 竞赛的强化学习方案
- 学习行为克隆与 PPO 自博弈联盟的训练组合
- 参考 Rust 精确复刻游戏引擎作为 RL 环境

## 场景标签

`强化学习` · 领域:训练与推理

## 证据(README 行号)

> L5: The final submissions placed ~10th of 10,246 teams on the public leaderboard.
> L7: I trained an ~947k parameter actor for about 10 hours on an RTX 5090. Behavioural Cloning on leaderboard data from S
> L44: - **Entity-attention policy.** Farms are encoded as 200 tile tokens plus 20

## 星数曲线

```mermaid
xychart-beta
    title "CarsonBurke/kaggriculture 星数(近 3 点)"
    x-axis ["2026-11-19", "2026-11-22", "2026-11-28"]
    y-axis "stars" 11 --> 14
    line [12, 13, 13]
```

2026-11-19 12 → 2026-11-28 13（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-19 · 置信度 high · 依据 README sha `8830598ae6c8` · [字段定义](../../DATASET.md)*
