# sebastianbrzustowicz/Robot-Sumo-RL

⭐ 23 · Python · NOASSERTION · 推送 2026-02-21 · [GitHub](https://github.com/sebastianbrzustowicz/Robot-Sumo-RL) · 个人维护

**机器人相扑自主对战智能体的强化学习训练系统**

基于 Python + PyTorch 实现的自主机器人相扑（Robot Sumo）强化学习训练系统：在自研物理仿真环境中用 Actor-Critic 架构（SAC/PPO/A2C）在连续动作空间训练对战策略，采用竞争性 self-play 机制（与 Master 模型或历史版本对打）。环境包含 SAT 碰撞检测、二阶动力学与 11 维归一化观测向量，奖励塑形引擎奖励前压进攻与贴边保护、惩罚倒退与原地旋转。README 提供 SAC/PPO/A2C 的 ELO 锦标赛基准对比，通过 Makefile 安装与运行训练/演示命令。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- SAC/PPO/A2C 三算法在连续动作空间的 self-play 训练
- 11 维归一化观测向量与 SAT 碰撞检测的二阶物理仿真环境
- 奖励塑形引擎：奖励前压进攻、惩罚倒退与原地旋转
- SAC/PPO/A2C 的 ELO 锦标赛基准（SAC 1614 ELO，约 378 episodes 收敛）

## 适用场景

- 训练机器人相扑对战智能体并观看实时对战演示
- 对比 SAC/PPO/A2C 在连续控制任务中的收敛效率
- 研究奖励塑形与 self-play 机制对对抗策略的影响

## 场景标签

`强化学习` · 领域:训练与推理

## 证据(README 行号)

> L16: This project implements an autonomous Robot Sumo combat agent trained using Reinforcement Learning (Actor-Critic ar
> L40: * **Controller (RL Policy):** A neural network-based agent (e.g., SAC, PPO, or A2C) that maps the current observati

## 星数曲线

```mermaid
xychart-beta
    title "sebastianbrzustowicz/Robot-Sumo-RL 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-26", "2026-10-31"]
    y-axis "stars" 21 --> 24
    line [22, 23, 23]
```

2026-10-18 22 → 2026-10-31 23（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `b3556425cbc0` · [字段定义](../../DATASET.md)*
