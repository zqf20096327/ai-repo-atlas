# mlr-org/mlr3proba

⭐ 150 · R · LGPL-3.0 · 推送 2026-10-12 · [GitHub](https://github.com/mlr-org/mlr3proba) · [官网](https://mlr3proba.mlr-org.com/) · 组织维护

**面向 mlr3 的概率学习 R 包：生存分析、密度估计与概率回归**

mlr3 生态系统中的机器学习工具包，提供三类概率学习能力：带右删失的单事件预测性生存分析、单变量无监督密度估计、以预测分布为返回类型的概率监督回归。核心机制包括 TaskSurv 任务框架、统一的 $train()/$predict() 接口（兼容频率派、贝叶斯、深度学习等模型）、distr6 分布接口、多种性能度量，以及与 mlr3pipelines 集成的流水线构建与生存任务降维策略。README 声明本包将于 2026 年归档，后续开发转移至 mlr3survival 等包；不上架 CRAN，经 R-universe 或 GitHub 安装。

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

- 预测性生存分析任务框架 TaskSurv 与统一 train/predict 接口
- distr6 接口下的生存概率分布预测
- 多种生存度量（D-Calibration、C-index、Integrated Brier Score 等）
- 与 mlr3pipelines 集成的 ML 流水线构建与降维策略

## 适用场景

- 在 R 中做带右删失的生存分析建模与评估
- 进行单变量密度估计与概率监督回归
- 把生存任务转换为分类/回归任务进行降维建模

## 场景标签

 · 领域:机器学习/统计建模

## 证据(README 行号)

> L29: `mlr3proba` is a machine learning toolkit for probabilistic learning
> L33: 1. **Predictive survival analysis** for single-event tasks with

## 星数曲线

```mermaid
xychart-beta
    title "mlr-org/mlr3proba 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 149 --> 151
    line [150, 150]
```

2026-10-18 150 → 2026-10-28 150（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `d0b7f5751308` · [字段定义](../../DATASET.md)*
