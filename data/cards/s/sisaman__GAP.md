# sisaman/GAP

⭐ 50 · Jupyter Notebook · CC0-1.0 · 推送 2026-10-20 · [GitHub](https://github.com/sisaman/GAP) · 个人维护

**论文官方实现：差分隐私图神经网络训练与复现代码**

USENIX Security 2023 论文 GAP（Aggregation Perturbation 差分隐私图神经网络）的官方实现，Python 3.9 基于 PyTorch-Geometric 2.1.0 与 PyTorch 1.13.1，用 uv 管理依赖。提供边级与节点级差分隐私训练（GAP-EDP/NDP），含加速边采样的自定义 C++ 算子（运行时自动编译，需 C++ 编译器）。支持单机顺序运行实验或经 Dask 提交到 SGE/SLURM 等集群并行，用 WandB 记录训练过程（仅复现论文结果需账号），并以 results.ipynb 可视化。面向需要复现论文或做隐私保护 GNN 研究的科研用户。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | CC0-1.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 边级（GAP-EDP）与节点级（GAP-NDP）差分隐私训练
- 加速边采样的自定义 C++ 算子（运行时自动构建）
- Dask 支持在 SGE/SLURM 等集群并行运行多组实验
- 提供实验生成脚本与结果可视化 notebook

## 适用场景

- 复现论文在 Facebook/Reddit/Amazon 数据集上的结果
- 研究差分隐私下图神经网络的训练方法
- 基于代码开展隐私保护图学习的后续研究

## 场景标签

`科研工具` · 领域:学习与行业

## 证据(README 行号)

> L3: This repository is the official implementation of the paper:
> L9: This code is implemented in Python 3.9 using PyTorch-Geometric 2.1.0 and PyTorch 1.13.1.

## 星数曲线

```mermaid
xychart-beta
    title "sisaman/GAP 星数(近 2 点)"
    x-axis ["2026-10-22", "2026-10-31"]
    y-axis "stars" 49 --> 51
    line [50, 50]
```

2026-10-22 50 → 2026-10-31 50（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `36ac11f265a0` · [字段定义](../../DATASET.md)*
