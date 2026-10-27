# mlr-org/mlr3cluster

⭐ 27 · R · LGPL-3.0 · 推送 2026-10-18 · [GitHub](https://github.com/mlr-org/mlr3cluster) · [官网](https://mlr3cluster.mlr-org.com/) · 组织维护

**R 的 mlr3 生态聚类分析扩展包：39 种聚类学习器**

mlr-org 维护的 mlr3 生态扩展包，为 mlr3 机器学习框架提供聚类分析能力，接替 mlr2 的聚类功能。当前包含 39 个聚类学习器（划分、层次、模糊、基于密度、混合模型等类型）、12 个聚类性能度量（轮廓系数、Calinski-Harabasz 等）和 2 个内置任务；与 mlr3viz 集成可一行代码生成可视化。各学习器依赖 cluster、dbscan、RWeka 等第三方 R 包。通过 CRAN 或 GitHub 安装，计划后续接入 mlr3pipelines。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | LGPL-3.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 39 个聚类学习器覆盖划分/层次/模糊/密度/混合模型等类型
- 12 个聚类性能度量（轮廓系数、Dunn、Davies-Bouldin 等）
- 与 mlr3viz 集成，一行代码生成可视化
- 提供 2 个内置任务供上手

## 适用场景

- 在 mlr3 工作流中执行聚类建模与性能评估
- 快速尝试多种聚类算法并对比结果
- 聚类结果可视化展示

## 场景标签

 · 领域:机器学习/聚类分析

## 证据(README 行号)

> L14: **mlr3cluster** is an extension package for cluster analysis within the
> L38: - A selection of 39 clustering learners that represent a wide variety of
> L40: - A selection of 12 performance measures

## 星数曲线

```mermaid
xychart-beta
    title "mlr-org/mlr3cluster 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 26 --> 28
    line [27, 27]
```

2026-10-18 27 → 2026-10-27 27（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `41fb1c2d8496` · [字段定义](../../DATASET.md)*
