# berkedenizbozyigit/novel-artificial-neurons

⭐ 16 · Python · MIT · 推送 2026-04-06 · [GitHub](https://github.com/berkedenizbozyigit/novel-artificial-neurons) · 个人维护

**硕士研究项目：用可学习非线性聚合函数替代神经元加权和**

约克大学 MSc 人工智能学位论文项目，在 PyTorch 中实现三种新型人工神经元架构：可学习广义 F-Mean 聚合（幂参数 p）、成对高斯亲和的 Gaussian Support 神经元，以及带可学习混合权重的三路混合结构。在标准与加噪 CIFAR-10 上评估，3-Way Hybrid 取得 55.21%（标准）与 54.72%（加噪）准确率，并分析训练中聚合参数的演化。面向深度学习研究人员，完整论文以 Google Drive 链接提供，实验在 Google Colab A100 GPU 上完成。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- F-Mean、Gaussian Support 与三路混合三种可学习聚合神经元实现
- 标准/加噪 CIFAR-10 对照评估（3-Way Hybrid：55.21%/54.72%）
- 训练中聚合参数演化的实证分析（p、σ、混合权重）
- PyTorch 实现，MIT 许可

## 适用场景

- 研究替代加权求和的神经元聚合函数
- 复现或扩展噪声鲁棒性实验到其他数据集
- 作为学位论文配套代码学习混合神经元架构

## 场景标签

`模型训练` · 领域:训练与推理

## 证据(README 行号)

> L13: This repository contains the implementation and evaluation of novel artificial neuron architectures that replace tr
> L15: 1. **F-Mean Neuron**: Uses learnable generalized F-mean aggregation with power parameter *p*

## 星数曲线

```mermaid
xychart-beta
    title "berkedenizbozyigit/novel-artificial-neurons 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-30 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `437adfc55c22` · [字段定义](../../DATASET.md)*
