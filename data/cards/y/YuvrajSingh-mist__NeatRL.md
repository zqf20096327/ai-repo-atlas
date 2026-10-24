# YuvrajSingh-mist/NeatRL

⭐ 232 · Python · Apache-2.0 · 推送 2026-10-24 · [GitHub](https://github.com/YuvrajSingh-mist/NeatRL) · [官网](https://www.smolhub.com/rl) · 个人维护

**单文件 PyTorch 深度强化学习算法库，供研究与实验**

NeatRL 提供 DQN、Dueling DQN、REINFORCE、DDPG、A2C、TD3、SAC、PPO、PPO-RND 等算法的可读性实现，每个算法自包含于单个文件。基于 PyTorch 构建，兼容 Gymnasium 环境，支持 Atari 自动 CNN 架构、向量化并行环境、自动视频录制及 Weights & Biases 实验跟踪。提供 pip 安装、CLI 预置训练命令与可选环境 extras（Atari/Box2D/Classic/MuJoCo），面向强化学习研究与实验用途。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 每个算法完整实现于一个自包含文件
- 9 种算法：DQN/Dueling DQN/REINFORCE/DDPG/A2C/TD3/SAC/PPO/PPO-RND
- Gymnasium 兼容、Atari 自动 CNN、向量化并行环境
- 内置 Weights & Biases 跟踪、视频录制与 CLI 预置训练命令

## 适用场景

- 研究者在干净的单文件实现上做 RL 算法实验
- 学习 DQN/PPO/SAC 等经典深度 RL 算法的实现细节
- 用 CLI 一条命令跑 CartPole、LunarLander 等预置训练示例

## 场景标签

`强化学习` · 领域:训练与推理

## 证据(README 行号)

> L7: NeatRL provides readable implementations of popular RL algorithms with a focus on simplicity and ease of use. Built 
> L103: - **DQN** (Deep Q-Network) - Classic value-based RL algorithm

## 星数曲线

```mermaid
xychart-beta
    title "YuvrajSingh-mist/NeatRL 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-24"]
    y-axis "stars" 230 --> 233
    line [231, 232, 232]
```

2026-10-18 231 → 2026-10-24 232（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `3b96e573c03a` · [字段定义](../../DATASET.md)*
