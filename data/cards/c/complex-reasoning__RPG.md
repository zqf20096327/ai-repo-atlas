# complex-reasoning/RPG

⭐ 78 · Python · MIT · 推送 2026-06-29 · [GitHub](https://github.com/complex-reasoning/RPG) · [官网](https://complex-reasoning.github.io/RPG/) · 组织维护 · 中文 README

**面向 LLM 推理的 KL 正则化策略梯度 RL 训练框架（ICLR 2026 论文代码）**

ICLR 2026 论文 "On the Design of KL-Regularized Policy Gradient Algorithms for LLM Reasoning" 的官方代码库：提供前向/反向 KL（含归一化与未归一化形式）正则目标的策略梯度推导与代理损失实现，覆盖全可微损失与 REINFORCE 式梯度估计器，基于 verl 代码库构建，通过 ray 与脚本复现论文实验。提供数据准备流程（DAPO-Math-17k 训练、AIME/AMC 评测，需转为 parquet 格式），并附带 Qwen-2.5-7B-Instruct 的实验脚本。硬件要求至少 8×80G VRAM（推荐 A100/H100）。面向复现论文或开展 LLM RL 后训练的研究者。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | `gpu-24g` | |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 前向/反向 KL 与归一化/未归一化目标的策略梯度推导与实现
- 全可微损失与 REINFORCE 式梯度估计器两种路径
- 基于 verl 代码库，脚本化复现论文中 7B 模型实验
- 附带 AIME/AMC 评测数据集与数据预处理模板

## 适用场景

- 复现论文中的 RPG 与 RPG-REINFORCE 实验
- 对 LLM 做 KL 正则化的 RL 后训练（RLHF）
- 在数学推理基准（AIME/AMC）上评测训练后模型

## 场景标签

`强化学习` · 领域:训练与推理

## 证据(README 行号)

> L12: - **RPG (Regularized policy gradient)** is a systematic framework for deriving and analyzing KL-regularized policy 
> L24:  - **Comprehensiveness**: We derive policy gradients and corresponding surrogate loss functions for objectives regu
> L107:  - volcengine/verl: verl: Volcano Engine Reinforcement Learning for LLMs for providing coding base

## 星数曲线

```mermaid
xychart-beta
    title "complex-reasoning/RPG 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 77 --> 79
    line [78, 78]
```

2026-10-18 78 → 2026-10-30 78（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 mid · 依据 README sha `b2f922631e65` · [字段定义](../../DATASET.md)*
