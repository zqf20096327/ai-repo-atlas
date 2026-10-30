# yamato-me/reinforcement-learning-replications

⭐ 23 · Python · MIT · 推送 2026-04-04 · [GitHub](https://github.com/yamato-me/reinforcement-learning-replications) · 个人维护

**PyTorch 强化学习算法复现实现集（VPG/TRPO/PPO/DDPG/TD3）**

提供多种经典强化学习算法的 PyTorch 实现，覆盖 VPG、TRPO、PPO、DDPG、TD3；使用 Python 标准日志库记录训练过程，支持 TensorBoard 可视化。附 benchmark 结果（每个实验 3 个随机种子，日志与训练脚本、模型存于 benchmarks 目录），基准基于 Benchmarks for Spinning Up Implementations。示例为在 CartPole-v1 上训练 PPO，可用 Google Colab 运行；本地验证使用 tox。面向需要学习或对照复现强化学习算法的开发者。

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

- 实现 VPG/TRPO/PPO/DDPG/TD3 五种算法
- 每个实验 3 个随机种子并附训练日志、脚本与已训练模型
- 支持 TensorBoard，使用 Python 标准日志库
- 提供 Google Colab 可运行的示例 notebook

## 适用场景

- 学习或对照经典强化学习算法的 PyTorch 实现
- 在 Gymnasium 环境（如 CartPole-v1）上训练与调试
- 查看基准结果比较各算法表现

## 场景标签

`强化学习` · 领域:训练与推理

## 证据(README 行号)

> L2: Reinforcement Learning Replications is a set of Pytorch implementations of reinforcement learning algorithms.
> L6: - Implement Algorithms

## 星数曲线

```mermaid
xychart-beta
    title "yamato-me/reinforcement-learning-replications 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 22 --> 24
    line [23, 23]
```

2026-10-18 23 → 2026-10-30 23（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `92bd63614b11` · [字段定义](../../DATASET.md)*
