# Baran-phys/Tropical-Attention

⭐ 34 · Python · MIT · 推送 2026-05-21 · [GitHub](https://github.com/Baran-phys/Tropical-Attention) · 组织维护

**基于热带几何的注意力机制，用于组合算法的神经算法推理**

NeurIPS 2025 论文官方代码：将注意力核提升到热带射影空间，使推理呈分段线性且 1-Lipschitz，以保持组合推理的多面体决策结构。理论上证明 Multi-Head Tropical Attention 可通用逼近热带电路，将神经算法推理从 PTIME 扩展到 NP-hard/complete 问题。在 11 个组合任务（Floyd–Warshall、背包、装箱等）上实验，报告长度与取值上的分布外泛化与抗噪表现。内核以 Python 文件与 PyTorch 模块形式提供，可通过 tropical-gemm 的 SIMD CPU 或 CUDA DLPack 后端加速，支持从零训练模型。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

-  TropicalAttention.py 提供可独立使用的热带注意力内核
- 11 个组合算法任务的训练与评测（含 NP-hard/complete 分类任务）
- max-plus 乘积可切换 torch / tropical-gemm 后端
- 实验脚本按 job 文件行选任务训练并记录到 outputs 目录

## 适用场景

- 在组合算法任务上做神经算法推理研究
- 将热带注意力作为可复用模块嵌入自有 PyTorch 模型
- 复现论文的长度/取值分布外泛化实验

## 场景标签

 · 领域:机器学习研究/神经算法推理

## 证据(README 行号)

> L2: **[NeurIPS 2025] Tropical Attention: Neural Algorithmic Reasoning for Combinatorial Algorithms.** (paper)
> L5: To answer this, we introduce Tropical Attention, an attention mechanism grounded in tropical geometry that lifts the
> L42: from TropicalAttention import TropicalAttention

## 星数曲线

```mermaid
xychart-beta
    title "Baran-phys/Tropical-Attention 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 33 --> 35
    line [34, 34]
```

2026-10-18 34 → 2026-10-29 34（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `b8172dde8ae5` · [字段定义](../../DATASET.md)*
