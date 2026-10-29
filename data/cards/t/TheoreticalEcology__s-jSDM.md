# TheoreticalEcology/s-jSDM

⭐ 79 · R · GPL-3.0 · 推送 2026-10-17 · [GitHub](https://github.com/TheoreticalEcology/s-jSDM) · [官网](https://cran.r-project.org/web/packages/sjSDM/index.html) · 组织维护

**生态学研究者用的可扩展联合物种分布模型 R 包**

sjSDM 是估计联合物种分布模型（jSDM）的 R 包：以 GLMM 建模多物种对环境、空间与协方差项的响应，刻画物种间条件相关性。区别于潜变量近似方案，其在似然中拟合完整协方差矩阵并通过模拟做数值近似，以提升大规模群落数据的计算速度。1.1.0 版起基于 torch（libtorch）重写核心，不再依赖 Python/conda。经 CRAN 分发，支持 GPU 与 Apple silicon MPS。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 在似然中拟合完整协方差矩阵，通过模拟做数值近似
- 核心基于 R torch（libtorch），无需 Python/conda/独立 PyTorch 安装
- 支持 GPU（device="gpu"）与 Apple silicon（device="mps"）
- 提供 ANOVA 变异分解与集合群内部结构分析（Leibold et al., 2022）

## 适用场景

- 对大尺度群落数据拟合联合物种分布模型并推断物种关联
- 用 ANOVA 分解环境、空间与协方差项的解释变异
- 分析和可视化集合群内部结构以研究群落构建过程

## 场景标签

`科研工具` · 领域:学习与行业

## 证据(README 行号)

> L9: The sjSDM package is an R package for estimating joint species distribution models. A jSDM is a GLMM that models a m
> L13: A big challenge in jSDM implementation is computational speed. The goal of the sjSDM (which stands for "scalable jo
> L15: Since version 1.1.0 the core code of sjSDM is implemented in R on top of torch (libtorch). Earlier versions wrapped

## 星数曲线

```mermaid
xychart-beta
    title "TheoreticalEcology/s-jSDM 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 78 --> 80
    line [79, 79]
```

2026-10-18 79 → 2026-10-29 79（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `e5affea746f6` · [字段定义](../../DATASET.md)*
