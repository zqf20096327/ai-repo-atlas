# rodrigo-arenas/Sklearn-genetic-opt

⭐ 398 · Python · MIT · 推送 2026-11-25 · [GitHub](https://github.com/rodrigo-arenas/Sklearn-genetic-opt) · [官网](https://sklearngeneticopt.rodrigo-arenas.com) · 个人维护

**scikit-learn 的进化算法超参搜索与特征选择库**

提供 GASearchCV 与 GAFeatureSelectionCV 两个估计器：输入模型、评分器与预算，用交叉验证评估候选、重拟合最优解并可直接 predict。适用于参数或特征组合使穷举搜索代价过高的场景。默认内置 DEAP 引擎，scipy、nevergrad、cmaes、pymoo 四个引擎通过 pip extras 安装，五种引擎均支持实时绘图、早停与从已完成代数恢复。要求 Python 3.12 及以上，以 MIT 许可在 PyPI 发布，附软件引用元数据与基准对比文档。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- GASearchCV 超参搜索与 GAFeatureSelectionCV 特征选择，均基于交叉验证
- 默认 DEAP 引擎，另提供 scipy/nevergrad/cmaes/pymoo 四个可选引擎（pip extras）
- 支持实时绘图、早停、checkpoint 恢复与 CVBudgetStopping 预算控制
- 0.17.0 新增保留 pandas 列名/类型的特征选择与 warm_start_masks 种群预热

## 适用场景

- 对决策树、神经网络等 scikit-learn 模型做超参数调优
- 在候选特征过多时用 GAFeatureSelectionCV 做特征选择
- 搜索空间过大导致 GridSearchCV 穷举代价过高时换用进化搜索
- 长时间运行的超参实验需要 checkpoint 恢复与预算控制

## 场景标签

 · 领域:机器学习工具/AutoML

## 证据(README 行号)

> L10: **Hyperparameter tuning and feature selection for scikit-learn.**
> L11: Give ``GASearchCV`` or ``GAFeatureSelectionCV`` a model, a scorer and a budget.
> L72: DEAP is included by default. Four additional engines are available as extras.

## 星数曲线

```mermaid
xychart-beta
    title "rodrigo-arenas/Sklearn-genetic-opt 星数(近 10 点)"
    x-axis ["2026-10-24", "2026-11-02", "2026-11-06", "2026-11-08", "2026-11-10", "2026-11-15", "2026-11-19", "2026-11-20", "2026-11-23", "2026-11-26"]
    y-axis "stars" 389 --> 399
    line [390, 391, 390, 391, 393, 397, 398, 397, 398, 398]
```

2026-10-24 390 → 2026-11-26 398（+8）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 high · 依据 README sha `746bd1f55ce4` · [字段定义](../../DATASET.md)*
