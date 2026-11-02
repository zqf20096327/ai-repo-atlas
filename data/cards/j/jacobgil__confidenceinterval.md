# jacobgil/confidenceinterval

⭐ 146 · Python · MIT · 推送 2026-11-01 · [GitHub](https://github.com/jacobgil/confidenceinterval) · 个人维护

**为机器学习指标计算置信区间的 Python 库**

提供 F1、Precision、Recall、ROC AUC、accuracy、PPV、NPV 等常见分类指标的置信区间计算，接口遵循 scikit-learn 命名惯例。支持解析法（Takahashi 2022 方法、DeLong、Wilson 等二项比例方法）与自助法（bootstrap_bca/percentile/basic）两种计算路径；macro F1 的解析区间由作者用 delta 方法推导。附带 bootstrap_ci 函数可为任意自定义指标计算置信区间，并提供带置信区间的分类报告输出。面向 Python 数据科学/机器学习用户。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- F1/Precision/Recall 的 Macro/Micro/Binary 解析置信区间（基于 Takahashi 2022，macro 由 delta 方法推导）
- ROC AUC 置信区间的 DeLong 快速实现
- 多种 bootstrap 方法（bca/percentile/basic）及二项比例区间（wilson/normal/agresti_coull/beta/jeffreys 等）
- bootstrap_ci 可为任意 y_true/y_pred 自定义指标计算置信区间

## 适用场景

- 论文或实验报告中给出模型指标的置信区间
- 判断指标高低是否在小样本下由随机性导致
- 为 scikit-learn 的 balanced accuracy 等外部指标附上置信区间

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L11: This is a package that computes common machine learning metrics like F1, and returns their confidence intervals.
> L110: ## Get a confidence interval for any custom metric with Bootstrapping


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-02 · 置信度 high · 依据 README sha `23617d44279b` · [字段定义](../../DATASET.md)*
