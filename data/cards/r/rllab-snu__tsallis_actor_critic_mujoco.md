# rllab-snu/tsallis_actor_critic_mujoco

⭐ 61 · Jupyter Notebook · 推送 2025-11-24 · [GitHub](https://github.com/rllab-snu/tsallis_actor_critic_mujoco) · [官网](https://arxiv.org/abs/1902.00137) · 组织维护

**Tsallis 熵强化学习算法实现：用于 MuJoCo 环境的 Actor-Critic**

基于 OpenAI Spinning Up 教学框架实现的 Tsallis Actor Critic（TAC）算法，将强化学习中标准的 Shannon-Gibbs 熵最大化推广为 Tsallis 熵。支持 MuJoCo 与 Robotics 环境的实验，提供熵指数 q、熵类型（log/q-log）、分布类型（gaussian/q-gaussian）及调度策略等参数配置；附带 Tsallis 熵动态规划与多臂赌博机示例 Notebook。需先安装 libopenmpi-dev，通过 pip -e 源码安装，含自定义 Gym 环境包。

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

- TAC 将 Shannon-Gibbs 熵最大化推广为 Tsallis 熵
- 支持 q 值、熵类型、分布类型与调度策略等参数配置
- 提供 Tsallis 熵 MDP 与多臂赌博机的 Jupyter 示例
- 附自定义 Gym 环境包与批量实验脚本

## 适用场景

- 在 MuJoCo 连续控制环境中复现 TAC 实验
- 研究 Tsallis 熵正则化对强化学习的影响
- 参照示例 Notebook 学习 Tsallis 熵统计性质

## 场景标签

`强化学习` · 领域:训练与推理

## 证据(README 行号)

> L2: This repository provides the implementation of Tsallis actor critic (TAC) method based on Spinningup packages which 
> L4: Kyungjae Lee, Sungyub Kim, Sungbin Lim, Sungjoon Choi, Mineui Hong, Jaein Kim, Yong-Lae Park and Songhwai Oh, "Gener
> L55: python -m spinup.run tac --env HalfCheetah-v2

## 星数曲线

```mermaid
xychart-beta
    title "rllab-snu/tsallis_actor_critic_mujoco 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 60 --> 62
    line [61, 61]
```

2026-10-18 61 → 2026-10-31 61（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `4df7ad314873` · [字段定义](../../DATASET.md)*
