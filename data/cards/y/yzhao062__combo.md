# yzhao062/combo

⭐ 660 · Python · BSD-2-Clause · 推送 2026-09-08 · [GitHub](https://github.com/yzhao062/combo) · [官网](https://pycombo.readthedocs.io) · 个人维护

**面向开发者的机器学习模型与分数组合 Python 工具库**

combo 是一个用于组合机器学习模型与分数的 Python 工具库，属于集成学习子任务，发表于 AAAI 2020 demo track。它提供统一 API，将来自 scikit-learn、xgboost、LightGBM 等库的模型组合起来，覆盖分类、聚类、异常检测与原始分数四类任务，实现 Stacking、DCS、DES、EAC、LSCP、XGBOD 等约 15 种组合算法，并通过 numba 与 joblib 进行 JIT 与并行优化。限制：仅支持 Python 3.5/3.6/3.7，依赖 numpy/numba/pyod/scipy/scikit-learn/joblib。以 pip 安装或源码 setup.py 安装提供。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | BSD-2-Clause |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 统一 API 组合来自 scikit-learn/xgboost/LightGBM 的模型与分数
- 覆盖分类、聚类、异常检测、原始分数四类任务约 15 种算法
- 使用 numba 与 joblib 进行 JIT 加速与并行化
- 所有算法均附带示例与交互式 Jupyter Notebook（Binder）

## 适用场景

- 在数据科学竞赛或实际任务中组合多个基学习器提升预测
- 组合多个异常检测器或聚类结果得到统一输出
- 在研究与教学中复现模型组合（Stacking/DCS/DES 等）算法

## 场景标签

 · 领域:机器学习/数据科学

## 证据(README 行号)

> L59: **combo** is a comprehensive Python toolbox for **combining machine learning (ML) models and scores**.
> L67: for crucial tasks including classification, clustering, anomaly detection.
> L76: * **Unified APIs, detailed documentation, and interactive examples** across various algorithms.

## 星数曲线

```mermaid
xychart-beta
    title "yzhao062/combo 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 659 --> 661
    line [660, 660]
```

2026-10-18 660 → 2026-10-28 660（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `58213887f009` · [字段定义](../../DATASET.md)*
