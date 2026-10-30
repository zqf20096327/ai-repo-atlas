# Lollorm/Super-Mario-AI

⭐ 18 · Python · MIT · 推送 2026-05-21 · [GitHub](https://github.com/Lollorm/Super-Mario-AI) · 个人维护

**用 NEAT 与 PPO 训练 AI 智能体通关马里奥游戏的实验仓库**

个人研究型仓库，包含两套完整实现：在 Gym Super Mario Bros 环境中用 NEAT-Python 演化循环神经网络（帧截图灰度化降维为 1024 维输入，靠网络内部状态处理时序而非帧堆叠），适应度函数综合 x 轴进度、跳跃奖励与到达旗杆/死亡/卡住的终端奖惩；在 Gym Retro 中用 stable-baselines3 的 PPO 训练 CNN 策略通关 Super Mario World，含手工定位内存地址、自定义奖励 JSON 配置与随机关卡泛化训练。DDQN 部分标注为 WIP。给强化学习学习者和游戏 AI 实验者参考使用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- NEAT 循环网络实现，以网络内部状态替代帧堆叠处理时序信息
- 完整的数学化适应度函数（旗杆 +10000、死亡 -150、卡住 -100）
- PPO + Gym Retro 手工集成：内存地址定位、自定义奖励 JSON、随机关卡泛化训练
- 训练代码开放于仓库内，可修改适应度函数改变智能体行为

## 适用场景

- 学习 NEAT 神经进化算法并复现通关 1-1 关的实验
- 参考 PPO 在 Super Mario World 上的自定义环境集成方法
- 通过随机关卡训练 setup 实验智能体的泛化能力

## 场景标签

`强化学习` · 领域:训练与推理

## 证据(README 行号)

> L2: >This repository explores multiple artificial intelligence approaches used to train agents to play Super Mario Bros 
> L12: An AI agent trained with the NeuroEvolution of Augmenting Topologies (NEAT) algorithm successfully beating Level 1-
> L113: This time, I implemented it using stable-baselines3 library and following ClarityCoders's tutorial on PPO and adap
> L153: This PPO implementation uses a Convolutional Neural Network (CNN) policy to process visual observations directly f

## 星数曲线

```mermaid
xychart-beta
    title "Lollorm/Super-Mario-AI 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 17 --> 19
    line [18, 18]
```

2026-10-18 18 → 2026-10-30 18（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 mid · 依据 README sha `b7a24c4db53e` · [字段定义](../../DATASET.md)*
