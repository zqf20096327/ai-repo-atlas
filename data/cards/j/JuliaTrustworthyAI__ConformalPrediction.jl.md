# JuliaTrustworthyAI/ConformalPrediction.jl

⭐ 148 · Julia · MIT · 推送 2026-02-17 · [GitHub](https://github.com/JuliaTrustworthyAI/ConformalPrediction.jl) · [官网](https://www.taija.org/ConformalPrediction.jl/) · 组织维护

**给 MLJ 用户的 Julia 共形预测不确定性量化包**

Julia 包，为 MLJ 框架中训练的有监督模型提供共形预测（Conformal Prediction）不确定性量化：通过 conformal_model 包装器将常规模型转为共形模型，产出带分布无关保证的预测区间/集合。回归实现 Inductive、Jackknife、Jackknife+、CV+ 等 7 种方法，分类实现 3 种；提供 emp_coverage 与 ssc 评估指标及 Plots 绘图配方。已测试 MLJ 的 8 种回归与 5 种分类模型。自述处于早期开发阶段，核心架构与 API 可能变动。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- conformal_model 包装器将任意 MLJ 模型转为共形模型
- 回归 7 种、分类 3 种共形预测方法
- emp_coverage / ssc 覆盖率评估指标
- JuliaCon 2023 Notebook 竞赛二等奖交互教程

## 适用场景

- 为回归/分类模型生成带统计保证的预测区间
- 评估预测区间的经验覆盖率和条件覆盖
- 在 MLJ 工作流中做预测不确定性量化

## 场景标签

 · 领域:机器学习/不确定性量化

## 证据(README 行号)

> L5: `ConformalPrediction.jl` is a package for Predictive Uncertainty Quantification (UQ) through Conformal Prediction (C
> L79: To turn our conventional model into a conformal model, we just need to declare it as such by using `conformal_model

## 星数曲线

```mermaid
xychart-beta
    title "JuliaTrustworthyAI/ConformalPrediction.jl 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 147 --> 149
    line [148, 148]
```

2026-10-18 148 → 2026-10-29 148（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `252e3f1c2654` · [字段定义](../../DATASET.md)*
