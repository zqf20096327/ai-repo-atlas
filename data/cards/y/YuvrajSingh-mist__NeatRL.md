# YuvrajSingh-mist/NeatRL

⭐ 241 · Python · Apache-2.0 · 推送 2026-11-25 · [GitHub](https://github.com/YuvrajSingh-mist/NeatRL) · [官网](https://www.neatrl.com) · 个人维护

**研究者可用的单文件 PyTorch 深度强化学习算法库**

以 PyTorch 实现的强化学习算法库，每个算法独立封装在单一文件中，提供 21 个 CLI 别名与 Python API 两种训练入口。支持 Gymnasium 环境、Atari/Box2D/MuJoCo 域、向量化并行训练、视频录制，并通过 Weights & Biases 做实验追踪（默认本地上传需显式 --wandb）。安装分可选 extra：atari/box2d/mujoco 需另行安装。定位研究与实验用途，含超参数调优文档与各算法指南。

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

- 11 种算法（DQN/PPO/SAC/TD3/DDPG 等）的单文件实现，21 个 CLI 别名
- Gymnasium 兼容，覆盖 Classic Control/Atari/Box2D/MuJoCo
- 内置 Weights & Biases 实验追踪与自动视频录制
- 向量化环境并行训练，-cnn 别名自动构建 CNN 架构

## 适用场景

- 一行命令在 CartPole/LunarLander 上训练并对比 RL 算法
- 研究实验中快速扩展新的 RL 算法实现
- Atari/MuJoCo 连续控制任务的基准训练与录像记录

## 场景标签

`强化学习` `模型训练` `模型评测` · 领域:评测与运维

## 证据(README 行号)

> L7: NeatRL provides readable implementations of popular RL algorithms with a focus on simplicity and ease of use. Built 
> L216: - **PPO** (Proximal Policy Optimization) - Policy gradient method with GAE

## 星数曲线

```mermaid
xychart-beta
    title "YuvrajSingh-mist/NeatRL 星数(近 10 点)"
    x-axis ["2026-10-25", "2026-10-29", "2026-10-30", "2026-10-31", "2026-11-06", "2026-11-08", "2026-11-20", "2026-11-22", "2026-11-23", "2026-11-27"]
    y-axis "stars" 231 --> 242
    line [232, 233, 234, 235, 232, 238, 239, 240, 241, 241]
```

2026-10-25 232 → 2026-11-27 241（+9）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 high · 依据 README sha `bc204cd91515` · [字段定义](../../DATASET.md)*
