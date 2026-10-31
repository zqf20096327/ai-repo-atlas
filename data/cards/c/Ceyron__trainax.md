# Ceyron/trainax

⭐ 16 · Python · MIT · 推送 2026-06-01 · [GitHub](https://github.com/Ceyron/trainax) · [官网](https://fkoehler.site/trainax/) · 个人维护

**JAX 自回归神经模拟器训练方法库（PDE 仿真替代）**

基于 optax 构建的训练抽象库，面向用神经网络自回归地模拟时间依赖物理问题（如偏微分方程离散后的仿真算子）。提供轨迹子采样与多种 unrolled 训练方法（监督式、Diverted Chain、Mix Chain、Residuum），支持将参考模拟器纳入训练、在残差条件上训练、裁剪梯度流等。基于 JAX，兼容 Equinox，可在 CPU/GPU/TPU 运行。随 APEBench 论文（NeurIPS 2024）开发，需 Python 3.10+ 与 JAX 0.4.13+。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 多种 unrolled 训练方法（Supervised/Diverted Chain/Mix Chain/Residuum）
- 支持将参考模拟器与可微物理纳入训练
- 轨迹子采样处理，基于 JAX 自动微分与自动向量化
- 兼容 Equinox，支持批并行训练与回调

## 适用场景

- 训练替代 PDE 数值模拟器的神经网络仿真器
- 研究 unrolled 训练策略对自回归模拟器误差的影响
- 在可微物理框架下注入参考模拟器的知识

## 场景标签

 · 领域:科学计算/物理仿真机器学习

## 证据(README 行号)

> L26: Convenience abstractions using `optax` to train neural networks to
> L85: `Trainax` supports way more than just one-step supervised learning, e.g., to
> L108: This package was developed as part of the [APEBench paper

## 星数曲线

```mermaid
xychart-beta
    title "Ceyron/trainax 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-30", "2026-10-31"]
    y-axis "stars" 14 --> 17
    line [15, 16, 16]
```

2026-10-18 15 → 2026-10-31 16（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `ee4aaac4c324` · [字段定义](../../DATASET.md)*
