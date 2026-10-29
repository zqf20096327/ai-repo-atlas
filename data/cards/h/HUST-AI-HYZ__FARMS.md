# HUST-AI-HYZ/FARMS

⭐ 44 · Python · 推送 2025-11-14 · [GitHub](https://github.com/HUST-AI-HYZ/FARMS) · [官网](https://arxiv.org/abs/2506.06280) · 组织维护

**ICML 2025 论文代码：无长宽比偏置的神经网络特征谱分析方法 FARMS**

FARMS（Fixed-Aspect-Ratio Matrix Subsampling）是 ICML 2025 论文 Eigenspectrum Analysis of Neural Networks without Aspect Ratio Bias 的开源实现：以固定长宽比子采样子矩阵并归一化权重矩阵，测量子矩阵平均 ESD 以替代原始 ESD 的重尾性度量。覆盖三个方向：图像分类（基于 TempBalance 代码修改）、LLM 剪枝（依赖与 AlphaPruning 相同）、以及 SciML（DPOT 目录）。通过 conda 环境 + pip 依赖安装，运行 bash 脚本执行实验。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 固定长宽比子矩阵采样消除特征谱分析中的长宽比偏置
- 支持图像分类（基于 TempBalance 修改）与 LLM 剪枝（对齐 AlphaPruning 流程）
- SciML 方向代码基于 DPOT，见单独 ReadME

## 适用场景

- 复现论文的图像分类与 LLM 剪枝实验
- 研究神经网络权重特征谱与重尾性度量
- 在自有模型上用 Tempbalance_FARMS 做分析

## 场景标签

 · 领域:机器学习研究/模型压缩

## 证据(README 行号)

> L1: # Eigenspectrum Analysis of Neural Networks without Aspect Ratio Bias [ICML 2025]
> L8: FARMS (Fixed-Aspect-Ratio Matrix Subsampling) is a method that
> L15: - [x] (June 19th, 2025) We released the code for Image Classification / LLM Pruning.

## 星数曲线

```mermaid
xychart-beta
    title "HUST-AI-HYZ/FARMS 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 43 --> 45
    line [44, 44]
```

2026-10-18 44 → 2026-10-29 44（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `8440305cf141` · [字段定义](../../DATASET.md)*
