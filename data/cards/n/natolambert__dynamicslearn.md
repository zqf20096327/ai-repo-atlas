# natolambert/dynamicslearn

⭐ 56 · Python · MIT · 推送 2026-10-14 · [GitHub](https://github.com/natolambert/dynamicslearn) · 个人维护

**实验机器人的模型学习与控制研究代码库（四旋翼/Ionocraft）**

面向新型机器人（测试成本高、动力学难建模）的基于模型强化学习研究工作目录。提供 PyTorch 概率神经网络动力学模型、高斯损失函数、可自定义代价函数的 random shooting MPC，以及实验数据训练、仿真 MPC 运行、贝叶斯优化生成 PID 参数等脚本；通过 Hydra 配置。已在 Ionocraft 与 Crazyflie 2.0 平台上开展实验，作者声明仍在积极开发中，README 准确性可能滞后。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- PyTorch 概率神经网络动力学模型与高斯损失函数
- 可自定义代价/奖励函数的 random shooting MPC 实现
- Hydra 配置的训练脚本（learn/trainer.py）
- Ionocraft 受控飞行与 Crazyflie 2.0 迁移学习实验

## 适用场景

- 在实验机器人数据上训练动力学模型
- 用 MPC 在仿真环境中运行基于模型的强化学习
- 以动力学模型作仿真环境用贝叶斯优化生成 PID 参数

## 场景标签

`强化学习` · 领域:训练与推理

## 证据(README 行号)

> L2: Working directory for my work on model-based reinforcement learning for novel robots. Best for robots with high test
> L15: - probablistic nueral network in pytorch
> L25: - `learn/trainer.py`: is for training dynamics models (P,PE,D,DE) on experimental data. The training process uses H

## 星数曲线

```mermaid
xychart-beta
    title "natolambert/dynamicslearn 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-28"]
    y-axis "stars" 55 --> 58
    line [57, 56, 56]
```

2026-10-18 57 → 2026-10-28 56（-1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `ec854487183f` · [字段定义](../../DATASET.md)*
