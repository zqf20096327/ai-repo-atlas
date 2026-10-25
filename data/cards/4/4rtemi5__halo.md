# 4rtemi5/halo

⭐ 52 · Python · 推送 2026-04-06 · [GitHub](https://github.com/4rtemi5/halo) · [官网](https://pisoni.ai/posts/halo/) · 个人维护

**替换交叉熵的 PyTorch 损失函数：改进 OOD 检测与校准**

HALO-Loss 是一个可替换标准 Categorical Cross-Entropy 的 PyTorch 损失实现：用平方欧氏距离对特征与类中心做距离有界分类，并设置一个固定在原点的零参数'Abstain'虚拟类用于拒绝 OOD 样本。数学上展开后等价于带 L2 中心范数惩罚的点积，配合可学习温度缩放、理论最优 abstain 偏置与自蒸馏软目标。作者在 CIFAR-10/100 上用 ResNet-18 报告了基准结果。自述为 proof-of-concept，未在大规模模型上验证。面向做分类训练与 OOD/校准实验的研究者和开发者。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 距离有界分类损失，CCE 的即插即用替换（src/losses/halo.py）
- 零参数原点 Abstain 类用于 OOD 拒识
- 可学习温度 γ、理论 abstain 偏置与 teacher-free 自蒸馏
- CIFAR-10/100 + ResNet-18 基准结果与 PCA 可视化报告

## 适用场景

- 训练分类网络时降低过度自信、改进校准（ECE）
- 让模型原生拒绝分布外样本（OOD 检测）
- 复现并扩展小规模基准上的距离几何实验

## 场景标签

 · 领域:机器学习/训练组件

## 证据(README 行号)

> L3: A drop-in replacement for the standard Categorical Cross-Entropy (CCE) loss that forces neural networks to respect E
> L78: The `src/losses/halo.py` file contains a clean, plug-and-play PyTorch implementation designed to act as a simple dr

## 星数曲线

```mermaid
xychart-beta
    title "4rtemi5/halo 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 51 --> 53
    line [52, 52]
```

2026-10-18 52 → 2026-10-25 52（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 mid · 依据 README sha `ba1aa92b1d68` · [字段定义](../../DATASET.md)*
