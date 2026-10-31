# VersorAI/Versor

⭐ 13 · Python · Apache-2.0 · 推送 2026-04-30 · [GitHub](https://github.com/VersorAI/Versor) · [官网](https://arxiv.org/pdf/2602.10195) · 组织维护

**基于共形几何代数 Cl(4,1) 的几何序列 Transformer 架构**

面向几何深度学习研究者的 PyTorch 神经网络架构实现：以共形几何代数 Cl(4,1) 的多重向量表示与几何积为核心，提供 VersorTransformer、几何积注意力（GPA）、保持多重向量结构的线性层与旋子序列池化等组件，并实现 Cl(4,1) 的几何积/外积/内积等代数运算。附 quickstart 笔记本教程，内置 NLP（Dyck 语言）、视觉（CIFAR）、物理（N 体）及 MD17/WikiText-103 基准任务；CUDA 为可选加速，自定义内核自动编译。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 基于 Cl(4,1) 多重向量表示与几何积的 Transformer 架构
- Geometric Product Attention 与保持多重向量结构的线性层
- 旋子（rotor）递归累积实现序列池化
- 内置 Dyck/CIFAR/N 体/MD17/WikiText-103 任务脚本与 quickstart 教程

## 适用场景

- 在几何深度学习任务中训练基于几何代数的序列模型
- 复现论文的 Dyck/CIFAR/N 体/MD17 基准实验
- 参照 quickstart 模板将架构适配到自定义回归或分类问题

## 场景标签

`模型训练` · 领域:训练与推理

## 证据(README 行号)

> L4: A native Geometric Algebra Transformer architecture based on Conformal Geometric Algebra $\mathcal{C}l(4,1)$, implem
> L60: - **VersorTransformer**: Full geometric transformer for Cl(4,1)

## 星数曲线

```mermaid
xychart-beta
    title "VersorAI/Versor 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-27", "2026-10-31"]
    y-axis "stars" 11 --> 14
    line [12, 13, 13]
```

2026-10-18 12 → 2026-10-31 13（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 mid · 依据 README sha `e77118090f06` · [字段定义](../../DATASET.md)*
