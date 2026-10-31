# Anroshka/snake-ai

⭐ 14 · Python · MIT · 推送 2025-11-20 · [GitHub](https://github.com/Anroshka/snake-ai) · 个人维护

**用深度 Q-Learning 自学贪吃蛇的强化学习实现**

基于 PyTorch 与 Pygame 的贪吃蛇 AI 训练项目：DQN 网络（17 输入神经元、512 隐层、4 动作输出）配合优先经验回放（PER）训练智能体玩游戏，支持 2-6 条蛇同时训练的多智能体环境。提供实时可视化 HUD、训练统计图表、自动 checkpoint 与最优模型保存，支持 CUDA 加速与 AMP 混合精度，并自动在 GPU/CPU 间选择设备。面向强化学习学习与实验场景，从源码克隆安装，需 Python 3.10+。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- DQN + 优先经验回放（PER）训练贪吃蛇智能体
- 2-6 条蛇同时训练的多智能体支持
- CUDA 加速、AMP 混合精度与 GPU/CPU 自动选择
- 实时可视化 HUD、训练图表与自动 checkpoint

## 适用场景

- 学习与实验深度强化学习（DQN）算法
- 观察多智能体同时训练的可视化过程
- 作为强化学习教学或课程项目参考

## 场景标签

`强化学习` · 领域:训练与推理

## 证据(README 行号)

> L3: An advanced implementation of a Snake game AI that learns through Deep Q-Learning, featuring real-time visualization
> L28: - 🧠 Deep Q-Network with Priority Experience Replay (PER)

## 星数曲线

```mermaid
xychart-beta
    title "Anroshka/snake-ai 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 mid · 依据 README sha `c63d30f9a26f` · [字段定义](../../DATASET.md)*
