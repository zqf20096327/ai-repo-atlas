# fschur/DDQN-with-PyTorch-for-OpenAI-Gym

⭐ 71 · Python · MIT · 推送 2026-07-18 · [GitHub](https://github.com/fschur/DDQN-with-PyTorch-for-OpenAI-Gym) · 个人维护

**面向 OpenAI Gym 离散动作环境的 Double DQN 实现**

用 PyTorch 实现的 Double DQN 强化学习算法，针对 OpenAI Gym 中离散动作空间的环境运行；性能以样本效率定义，即训练使用 x 轮环境交互后的平均回报。README 说明标准 DQN 因 argmax 选择高估 Q 值的问题，本实现用两个 Q 网络防止高估，仅对一个网络做梯度更新并周期性同步目标网络参数，给出了 Double DQN 目标式与损失函数。相关论文为 Hasselt 2010。以源码仓库形式提供，未见安装命令。

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

- PyTorch 实现的 Double DQN 算法
- 支持 OpenAI Gym 离散动作空间环境
- 以样本效率（平均回报 vs 训练轮数）衡量性能

## 适用场景

- 在 Gym 离散动作环境（如 CartPole）上训练 DDQN
- 学习/参考 Double DQN 的 PyTorch 实现细节

## 场景标签

`强化学习` · 领域:训练与推理

## 证据(README 行号)

> L1: # DDQN with PyTorch for OpenAI Gym
> L2: Implementation of Double DQN reinforcement learning for OpenAI Gym environments with discrete action spaces. Perform

## 星数曲线

```mermaid
xychart-beta
    title "fschur/DDQN-with-PyTorch-for-OpenAI-Gym 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 70 --> 72
    line [71, 71]
```

2026-10-18 71 → 2026-10-31 71（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `961450b90c61` · [字段定义](../../DATASET.md)*
