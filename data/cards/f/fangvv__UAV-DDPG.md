# fangvv/UAV-DDPG

⭐ 726 · Python · 推送 2026-10-08 · [GitHub](https://github.com/fangvv/UAV-DDPG) · [官网](https://fangvv.github.io/UAV-DDPG/) · 个人维护 · 中文 README

**无人机辅助 MEC 计算卸载优化的 DDPG 论文代码**

论文《Computation Offloading Optimization for UAV-assisted Mobile Edge Computing: A Deep Deterministic Policy Gradient Approach》（Wireless Networks 2021）的源代码。用 TensorFlow 1.X 实现基于 DDPG 的强化学习算法，在自建仿真环境中联合优化用户调度、任务卸载比例、无人机飞行角度与速度，以最小化最大处理延迟。提供环境模拟器（UAV/UE/信道/能耗模型）、DDPG agent、状态归一化模块、DQN 基线及两个消融变体。面向科研人员复现与扩展研究。

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

- DDPG 算法联合优化用户调度、卸载比例与无人机飞行参数
- 内置含信道模型与能耗模型的 UAV-MEC 仿真环境
- 提供 DQN 基线与去掉探索噪声/状态归一化的两个消融变体
- 依赖 TensorFlow 1.X（如 1.14.0）

## 适用场景

- 复现论文中的 UAV-MEC 计算卸载优化实验
- 在仿真环境上扩展或对比自己的强化学习算法
- 学习 DDPG 在连续动作空间问题中的实现细节

## 场景标签

`科研工具` · 领域:学习与行业

## 证据(README 行号)

> L5: This is the source code for our paper: **Computation Offloading Optimization for UAV-assisted Mobile Edge Computing:
> L7: > Unmanned Aerial Vehicle (UAV) can play an important role in wireless systems as it can be deployed flexibly to hel

## 星数曲线

```mermaid
xychart-beta
    title "fangvv/UAV-DDPG 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-24"]
    y-axis "stars" 723 --> 726
    line [724, 725, 725]
```

2026-10-18 724 → 2026-10-24 725（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `9d04ce29184e` · [字段定义](../../DATASET.md)*
