# jmschrei/apricot

⭐ 537 · Jupyter Notebook · MIT · 推送 2025-11-17 · [GitHub](https://github.com/jmschrei/apricot) · 个人维护

**子模优化数据集摘要库：从海量数据选出代表性子集**

Python 库，实现子模优化以从大规模数据集中选取低冗余、有代表性的样本子集，用于数据可视化、以少量样本训练模型或作为贪心 k-means 质心。内置 Feature-based、Facility Location、Graph Cut 等子模函数，以及 Lazy Greedy、Stochastic Greedy、GreeDi 等 9 种优化器；selector API 遵循 scikit-learn transformer 风格，提供 fit/transform/fit_transform。支持自定义初始子集以避免与已选样本冗余。限制：依赖相似度矩阵的函数内存为平方级，数据量不大时收益有限。

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

- 内置多种子模函数与 9 种贪心优化器
- API 遵循 scikit-learn transformer 风格（fit/transform）
- 支持自定义初始子集进行增量式选择
- 子集可用于训练模型、数据可视化与贪心聚类质心

## 适用场景

- 海量数据集太大时训练前压缩样本规模
- 用代表性子集做数据可视化或聚类质心
- 替代多次随机采样获得更优训练子集

## 场景标签

`MLOps` · 领域:训练与推理

## 证据(README 行号)

> L7: apricot implements submodular optimization for the purpose of summarizing massive data sets into minimally redundant
> L9: Submodular optimization is a well studied field that focuses on set functions which have the *diminishing return* pr

## 星数曲线

```mermaid
xychart-beta
    title "jmschrei/apricot 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 536 --> 538
    line [537, 537]
```

2026-10-18 537 → 2026-10-31 537（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `a126c235cb4f` · [字段定义](../../DATASET.md)*
