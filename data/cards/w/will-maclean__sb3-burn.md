# will-maclean/sb3-burn

⭐ 22 · Rust · MIT · 推送 2025-11-24 · [GitHub](https://github.com/will-maclean/sb3-burn) · 个人维护

**Rust 实现的 Stable-Baselines3 风格强化学习库**

基于 burn 深度学习库用 Rust 编写的强化学习库，参照 Stable-Baselines3 的算法设计，提供可理解、可扩展的常见 RL 算法实现。目前 DQN 已实现，SAC 在 main 分支开发中，PPO 在计划内；内置 Gym 风格环境接口及 Gridworld、Cartpole、Pendulum、MountainCar 等 Rust 实现，Python gym 适配器在开发中。利用 Rust 泛型支持自定义状态/动作类型环境。CPU 训练用 Ndarray 后端，GPU 需安装 libtorch。项目自称 work in progress，尚未发布 crates.io。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | `cpu-ok` | |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | `idea` | |

## 能力要点

- DQN 已实现，SAC 开发中，PPO 计划中
- Gym 风格环境接口与多个 Rust 原生环境实现
- 利用 Rust 泛型支持自定义状态/动作类型环境
- 支持 Ndarray（CPU）与 LibTorch（GPU）等多种 burn 后端

## 适用场景

- 在 Rust 项目中训练强化学习智能体
- 在自定义状态/动作类型的环境上做 RL 实验
- 需要非 CUDA 硬件后端的 RL 训练

## 场景标签

`强化学习` · 领域:训练与推理

## 证据(README 行号)

> L5: `sb3-burn` is a reinforcement learning (RL) library written in rust using the burn deep learning library. It is base
> L26: The project currently contains a working DQN algorithm, as well as a set of implemented environments. The planned w
> L43: |DQN|Implemented|

## 星数曲线

```mermaid
xychart-beta
    title "will-maclean/sb3-burn 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 21 --> 23
    line [22, 22]
```

2026-10-18 22 → 2026-10-28 22（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `ef035279d7bd` · [字段定义](../../DATASET.md)*
