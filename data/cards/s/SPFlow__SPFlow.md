# SPFlow/SPFlow

⭐ 314 · Python · Apache-2.0 · 推送 2026-04-14 · [GitHub](https://github.com/SPFlow/SPFlow) · [官网](https://spflow.github.io) · 组织维护

**构建与推理和积网络/概率电路的 Python 库**

基于 PyTorch 的 Sum-Product Networks（SPN）与 Probabilistic Circuits（PC）构建与推理库，提供精确概率推理（边际、条件、最可能解释）、手动设计或自动结构学习、梯度下降/EM 等学习算法，支持缺失数据、多种分布类型与 GPU 加速，并附带含 Naive Bayes 的 spflow.zoo 现成模型。面向需要可 tractable 概率推断的研究者与开发者，以 PyPI 包提供，另有可选的 scikit-learn 兼容封装。

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

- 精确概率推理：边际、条件、最可能解释
- 支持梯度下降、期望最大化与自动结构学习
- GPU 加速（基于 PyTorch）
- spflow.zoo 提供现成概率电路模型（如 Naive Bayes）

## 适用场景

- 构建和积网络并做多项式时间的精确概率推断
- 对含缺失数据的数据集做密度估计或分类
- 研究与扩展概率电路结构学习算法

## 场景标签

 · 领域:机器学习/概率图模型

## 证据(README 行号)

> L11: **SPFlow** is a flexible, modular library for building and reasoning with **Sum-Product Networks (SPNs)** and **Pro
> L14: - Exact probabilistic inference: marginals, conditionals, most probable explanations

## 星数曲线

```mermaid
xychart-beta
    title "SPFlow/SPFlow 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 313 --> 315
    line [314, 314]
```

2026-10-18 314 → 2026-10-28 314（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `cf4128939be2` · [字段定义](../../DATASET.md)*
