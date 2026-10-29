# mlr-org/mlr3fselect

⭐ 43 · R · LGPL-3.0 · 推送 2026-09-23 · [GitHub](https://github.com/mlr-org/mlr3fselect) · [官网](https://mlr3fselect.mlr-org.com/) · 组织维护

**mlr3 生态的特征选择 R 包：为任意 learner 选最优特征集**

mlr3fselect 是 mlr3 机器学习生态中的特征选择 R 包，面向使用 R 做机器学习建模的开发者与科研用户。它为任意 mlr3 learner 选择最优特征集，支持随机搜索、递归特征消除、遗传搜索等多种优化算法，支持单目标与多目标（多性能度量）优化，并可通过嵌套重采样估计优化后特征集的性能。包构建在优化框架 bbotk 之上，通过 fsi() 构建优化问题实例、fs() 指定算法并调用 optimize() 执行，结果与全部评估记录存于 instance 中，可直接用最优特征集训练最终模型。经 CRAN 与 GitHub 安装。限制：依赖 mlr3 生态，仅适用于 R 环境。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `viral` | LGPL-3.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 为任意 mlr3 learner 选择最优特征集
- 支持随机搜索、递归特征消除、遗传搜索等优化算法
- 支持多性能度量（多目标）特征选择
- 嵌套重采样估计优化特征集的性能；包含混合集成特征选择（hEFS）组件

## 适用场景

- 在高维数据上为分类/回归模型筛选最优特征子集
- 通过嵌套重采样无偏估计特征选择后模型的性能
- 多性能度量下做多目标特征选择

## 场景标签

 · 领域:机器学习/特征工程

## 证据(README 行号)

> L12: *mlr3fselect* is the feature selection package of the
> L13: mlr3 ecosystem. It selects the optimal feature
> L20: The package is built on the optimization framework

## 星数曲线

```mermaid
xychart-beta
    title "mlr-org/mlr3fselect 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 42 --> 44
    line [43, 43]
```

2026-10-18 43 → 2026-10-29 43（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `2e70a9a6a63f` · [字段定义](../../DATASET.md)*
