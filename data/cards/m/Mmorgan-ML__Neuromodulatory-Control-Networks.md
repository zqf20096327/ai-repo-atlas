# Mmorgan-ML/Neuromodulatory-Control-Networks

⭐ 28 · Python · NOASSERTION · 推送 2025-12-11 · [GitHub](https://github.com/Mmorgan-ML/Neuromodulatory-Control-Networks) · 个人维护

**受神经调质系统启发的 LLM 架构改动研究项目**

提出 Neuromodulatory Control Networks（NCNs）：与主 LLM 并行的小型网络，读取全局上下文与控制信号，在前向传播中生成逐层调制向量，动态调节注意力精度（β）、层增益（g）与前馈门控（γ），参数经反向传播隐式自学习，并引入稳态正则化防止控制流形坍缩。当前以 18M 参数模型在 TinyStories 上训练 1 个 epoch 做微观验证（验证 PPL 4.5184），提供已训练 checkpoint（见 releases），并附热力学图等机制可解释性分析；等参数对照实验与规模扩展列为后续工作。面向 LLM 架构研究者。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 并行小网络生成逐层调制向量，动态调节注意力精度/层增益/前馈门控
- 稳态正则化机制防止控制流形坍缩
- 18M 参数模型在 TinyStories 单 epoch 训练，验证 PPL 4.5184
- releases 提供 18M 已训练 checkpoint

## 适用场景

- 研究 LLM 动态自适应处理的架构改动
- 复现微型规模验证实验与机制可解释性分析
- 探索条件计算与推理稀疏化的架构基础

## 场景标签

`模型训练` · 领域:训练与推理

## 证据(README 行号)

> L1: # Neuromodulatory Control Networks (NCNs)
> L5: We propose **Neuromodulatory Control Networks (NCNs)**, a novel architectural modification inspired by the neuromodu
> L13: The Neuromodulatory Control Network architecture operates by running a compact neural network in parallel with the 

## 星数曲线

```mermaid
xychart-beta
    title "Mmorgan-ML/Neuromodulatory-Control-Networks 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 27 --> 29
    line [28, 28]
```

2026-10-18 28 → 2026-10-30 28（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `9e3b482464b9` · [字段定义](../../DATASET.md)*
