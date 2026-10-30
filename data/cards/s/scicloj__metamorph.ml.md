# scicloj/metamorph.ml

⭐ 32 · Clojure · EPL-2.0 · 推送 2026-10-04 · [GitHub](https://github.com/scicloj/metamorph.ml) · 组织维护

**Clojure 机器学习库：统一数据预处理与模型超参调优**

基于 tech.ml.dataset 与 metamorph 的 Clojure 机器学习库，核心思路是将数据预处理与模型超参数调优统一在同一流程中：通过 optimize-hyperparameter 对 metamorph 管道函数序列执行 fit/transform 训练与评估，支持 holdout、k-fold 等交叉验证策略，返回含评分与执行时间的评估结果。本体只内置线性回归一种模型，其余模型由插件库提供（Smile、Tribuo、sklearn-clj、XGBoost4J），面向 Clojure 数据科学开发者。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | EPL-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 统一调优数据预处理与模型超参数的管道评估机制
- 内置 train/predict/evaluate 与 optimize-hyperparameter 函数
- 模型由外部插件库提供（Smile/Tribuo/sklearn/XGBoost）
- 支持多种交叉验证策略并返回完整评估指标（metric/mean/min/max/timing）

## 适用场景

- 在 Clojure 中训练与评估含预处理的机器学习管道
- 对整个数据转换管道做超参数搜索
- 组合不同模型插件库比较模型表现

## 场景标签

`MLOps` · 领域:训练与推理

## 证据(README 行号)

> L9: Machine learning functions based on tech.ml.dataset and metamorph.
> L51: `metamorph.ml` is a ML framework, containing just a single model type of a linear regression.
> L63: For training a model, we have function `train` , `predict` and `evaluate`:

## 星数曲线

```mermaid
xychart-beta
    title "scicloj/metamorph.ml 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 31 --> 33
    line [32, 32]
```

2026-10-18 32 → 2026-10-30 32（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `79bf357a82bc` · [字段定义](../../DATASET.md)*
