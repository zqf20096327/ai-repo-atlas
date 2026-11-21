# PrzeChoj/gips

⭐ 10 · R · GPL-3.0 · 推送 2026-11-09 · [GitHub](https://github.com/PrzeChoj/gips) · [官网](https://przechoj.github.io/gips/) · 组织维护

**高斯变量置换对称性发现与协方差估计的 R 包**

面向统计学与数据分析用户的 R 包，在多元高斯样本中搜索变量间的置换对称性，并利用对称约束降低协方差估计的样本量要求。核心机制是基于贝叶斯模型（find_MAP）量化近似对称是否成立，再通过 project_matrix 将协方差矩阵投影到对称约束下，得到可用于 n<p 情形的估计量；支持探索性数据分析与建模两类用途，支持多独立样本共享对称性的情形。发布于 CRAN，另有配套 JSS 论文。

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

- find_MAP 以贝叶斯模型量化变量间近似对称关系
- 对称约束降低 MLE 存在所需的样本量条件（n<p 场景可用）
- project_matrix 生成受约束的协方差估计
- 支持多独立样本共享置换对称性

## 适用场景

- 探索性数据分析中寻找变量间的隐藏对称结构
- 变量数多于观测数时的协方差估计
- 对高维小样本数据做降维建模

## 场景标签

`数据分析` · 领域:效率与自动化

## 证据(README 行号)

> L14: `gips` is an R package that looks for permutation symmetries in the
> L22: 1. Finding hidden symmetries between the variables. `gips` can be used
> L26: 2. Covariance estimation. For an i.i.d. sample from a nondegenerate

## 星数曲线

```mermaid
xychart-beta
    title "PrzeChoj/gips 星数(近 2 点)"
    x-axis ["2026-10-19", "2026-11-21"]
    y-axis "stars" 9 --> 11
    line [10, 10]
```

2026-10-19 10 → 2026-11-21 10（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-20 · 置信度 high · 依据 README sha `19c2bb8dc105` · [字段定义](../../DATASET.md)*
