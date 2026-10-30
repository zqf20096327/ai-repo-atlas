# TianhongDai/reinforcement-learning-algorithms

⭐ 698 · Python · 推送 2025-12-18 · [GitHub](https://github.com/TianhongDai/reinforcement-learning-algorithms) · 个人维护

**PyTorch 实现的经典深度强化学习算法集合**

以教学清晰为目标，用 PyTorch 实现多种经典深度强化学习算法：DQN（含 Double DQN、Dueling）、DDPG（含 HER）、A2C、TRPO、PPO、SAC，ACKTR 在清单中标注未完成。自含 rl_utils 模块提供环境包装、经验回放、MPI 训练工具与随机种子设置，支持 Atari、Box2d、MuJoCo 环境。安装需 pip 安装 rl_utils 并另装 MuJoCo、Atari/Box2d，训练与演示通过各算法目录下的 train.py / demo.py 脚本运行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- PyTorch 实现的 DQN/DDPG/A2C/TRPO/PPO/SAC 等算法
- 自带 rl_utils 模块（环境包装、经验回放、MPI 工具、随机种子）
- PPO 支持 Atari 与 MuJoCo 环境，提供实验结果图
- 各算法独立目录，附训练与演示脚本

## 适用场景

- 学习经典深度强化学习算法的实现细节
- 在 Atari/Box2d/MuJoCo 环境上训练和演示 RL 智能体
- 作为算法实现的参考代码

## 场景标签

`强化学习` · 领域:训练与推理

## 证据(README 行号)

> L5: This repository will implement the classic deep reinforcement learning algorithms by using **PyTorch**. The aim of t
> L7: - [x] Deep Q-Learning Network (DQN)

## 星数曲线

```mermaid
xychart-beta
    title "TianhongDai/reinforcement-learning-algorithms 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 697 --> 699
    line [698, 698]
```

2026-10-18 698 → 2026-10-30 698（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `1df0f8c0bb1d` · [字段定义](../../DATASET.md)*
