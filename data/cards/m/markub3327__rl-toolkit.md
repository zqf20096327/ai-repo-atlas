# markub3327/rl-toolkit

⭐ 21 · Python · MIT · 推送 2026-01-22 · [GitHub](https://github.com/markub3327/rl-toolkit) · 个人维护

**机器人学研究用分布式强化学习训练框架（SAC/DQN/TQC/gSDE）**

面向机器人学与深度强化学习研究的训练框架：实现 SAC、TQC、DQN 等agent算法，支持 gSDE 探索与 Huber/LogCosh 损失，采用 Server/Agent/Learner/Tester 分布式架构，经验回放基于 DeepMind Reverb。提供 BipedalWalker 与 FlappyBird 等环境并附实测得分，支持 PyBullet、Gymnasium、DeepMind Control Suite。通过 PyPI 安装（Ubuntu/Debian 需先装 swig），另给出 NVIDIA Jetson 上从源码构建 Reverb 的详细步骤。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Server/Agent/Learner/Tester 分布式训练架构，回放基于 DeepMind Reverb
- 实现 SAC、TQC、DQN 等 RL 算法及 gSDE 探索
- 支持 BipedalWalker、FlappyBird、PyBullet、DM Control 等环境并附实测结果
- 提供 NVIDIA Jetson（arm64）源码构建 Reverb 的安装路径

## 适用场景

- 我在机器人仿真环境中训练连续控制的 RL agent
- 做分布式强化学习实验（Server/Agent/Learner 分离部署）
- 在 Jetson 等边缘设备上复现 SAC/TQC 训练

## 场景标签

`强化学习` · 领域:训练与推理

## 证据(README 行号)

> L36:       rl_toolkit rl_toolkit -c ./config/sac.yaml -a sac -e BipedalWalkerHardcore-v3 server
> L44:       rl_toolkit -c ./config/sac.yaml -a sac -e BipedalWalkerHardcore-v3 learner --db_server 192.168.1.2
> L148: **Frameworks:** Tensorflow, DeepMind Reverb, Gymnasium, DeepMind Control Suite, WanDB, OpenCV

## 星数曲线

```mermaid
xychart-beta
    title "markub3327/rl-toolkit 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 20 --> 22
    line [21, 21]
```

2026-10-18 21 → 2026-10-31 21（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `7fe04dd2b26b` · [字段定义](../../DATASET.md)*
