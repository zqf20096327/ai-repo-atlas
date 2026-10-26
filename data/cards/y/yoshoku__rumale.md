# yoshoku/rumale

⭐ 919 · Ruby · BSD-3-Clause · 推送 2026-09-14 · [GitHub](https://github.com/yoshoku/rumale) · [官网](https://rubygems.org/gems/rumale) · 个人维护

**Ruby 机器学习库：提供类 Scikit-Learn 接口的算法集合**

Rumale 是纯 Ruby 编写的机器学习库，提供与 Python Scikit-Learn 相似接口的算法，覆盖 SVM、逻辑回归、MLP、随机森林、梯度提升、K-Means、DBSCAN、t-SNE、PCA、NMF 等分类、回归、聚类与降维算法。基于 Numo::NArray Alternative 类型数组实现；可选加载 Numo::Linalg Alternative 借助 OpenBLAS 加速矩阵运算，部分估计器通过 Parallel gem 支持 n_jobs 并行。以 Ruby gem 形式分发，面向 Ruby 开发者做数据分析与机器学习。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | BSD-3-Clause |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 提供类 Scikit-Learn 接口的多种分类/回归/聚类/降维算法
- 支持 libsvm 格式数据集加载与交叉验证
- 可选 OpenBLAS 加速（Numo::Linalg Alternative）与 Parallel 并行（n_jobs 参数）

## 适用场景

- 在 Ruby 项目中训练 SVM、随机森林等模型做分类与回归
- 对数据集做聚类与降维（K-Means、t-SNE、PCA）
- 在 Ruby 生态内做数据科学分析，不依赖 Python

## 场景标签

 · 领域:机器学习/数据科学

## 证据(README 行号)

> L11: Rumale (**Ru**by **ma**chine **le**arning) is a machine learning library in Ruby.
> L12: Rumale provides machine learning algorithms with interfaces similar to Scikit-Learn in Python.

## 星数曲线

```mermaid
xychart-beta
    title "yoshoku/rumale 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 918 --> 920
    line [919, 919]
```

2026-10-18 919 → 2026-10-26 919（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `3fd5fc987850` · [字段定义](../../DATASET.md)*
