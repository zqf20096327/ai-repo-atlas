# AdamStelmaszczyk/learning2run

⭐ 55 · Python · MIT · 推送 2026-03-09 · [GitHub](https://github.com/AdamStelmaszczyk/learning2run) · 个人维护

**NIPS 2017 Learning to Run 强化学习竞赛参赛源码**

作者参加 NIPS 2017 Learning to Run 挑战赛（基于 osim-rl 强化学习环境）的解决方案代码库。提供多种训练入口：baselines PPO（含专门的观测预处理）、keras-rl DDPG、进化策略（ES）三种方法，并包含对环境 reward 的修改（reward hacking）。仓库基于 TensorFlow 生态，附 Poster 与 Medium 方案说明链接，另有 arXiv 论文汇总其他参赛方案。以源码形式提供，无打包安装途径。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 提供 baselines PPO、keras-rl DDPG、Evolution Strategies 三种训练入口
- PPO 专门的观测预处理实现
- 包含环境 reward 修改（reward hacking）

## 适用场景

- 复现 NIPS 2017 Learning to Run 参赛方案
- 参考强化学习竞赛中的多种算法实现
- 研究 osim-rl 环境下的观测处理与 reward 设计

## 场景标签

`强化学习` · 领域:训练与推理

## 证据(README 行号)

> L1: # Our NIPS 2017: Learning to Run source code
> L11: - `run_osim.py` to run baselines PPO

## 星数曲线

```mermaid
xychart-beta
    title "AdamStelmaszczyk/learning2run 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 54 --> 56
    line [55, 55]
```

2026-10-18 55 → 2026-10-28 55（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `ccabb4069837` · [字段定义](../../DATASET.md)*
