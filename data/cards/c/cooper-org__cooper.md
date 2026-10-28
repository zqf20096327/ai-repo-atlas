# cooper-org/cooper

⭐ 167 · Python · MIT · 推送 2025-11-15 · [GitHub](https://github.com/cooper-org/cooper) · [官网](https://cooper.readthedocs.io/) · 组织维护

**PyTorch 深度学习约束优化库：拉格朗日法求解受限问题**

面向 PyTorch 的约束优化库，实现多种基于拉格朗日的一阶更新方案，可处理包括非凸问题在内的连续约束优化，主要面向基于 mini-batch 梯度估计的深度学习场景，也适用于一般连续约束优化任务。用户实现 ConstrainedMinimizationProblem 定义目标与约束，为原/对偶变量分别建立 torch 优化器并包装为 CooperOptimizer，通过 roll() 方法执行同时或交替的原-对偶更新。以 pip 包分发，附论文与教程 notebook。

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

- 多种基于拉格朗日的一阶原-对偶更新方案
- 适用于非凸约束优化与 mini-batch 梯度估计场景
- 与 torch.optim.Optimizer 集成的 CooperOptimizer.roll() 更新接口
- 多篇顶会论文基于该库完成

## 适用场景

- 深度学习训练中加入不等式/等式约束
- 需要乘子法的非凸约束优化研究
- 复现或开展约束优化相关论文实验

## 场景标签

 · 领域:机器学习/优化

## 证据(README 行号)

> L18: **Cooper** is a library for solving constrained optimization problems in PyTorch.
> L20: **Cooper** implements several Lagrangian-based (first-order) update schemes that are applicable to a wide range of 

## 星数曲线

```mermaid
xychart-beta
    title "cooper-org/cooper 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-28"]
    y-axis "stars" 165 --> 168
    line [166, 167, 167]
```

2026-10-18 166 → 2026-10-28 167（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `da2d68c3a826` · [字段定义](../../DATASET.md)*
