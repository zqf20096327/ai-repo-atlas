# felixriese/susi

⭐ 118 · Python · BSD-3-Clause · 推送 2026-03-17 · [GitHub](https://github.com/felixriese/susi) · [官网](https://felixriese.github.io/susi) · 个人维护

**给科研与数据科学家的监督/半监督自组织映射(SOM) Python 库**

SuSi 是一个实现自组织映射（SOM）的 Python 包，提供三种估计器：SOMClustering（无监督聚类）、SOMRegressor（半监督/监督回归）与 SOMClassifier（半监督/监督分类）。API 遵循 scikit-learn 规范，可用 GridSearchCV 调优超参数；配套 Read the Docs 文档与多个 Jupyter Notebook 示例。方法发表于 Remote Sensing 2020 论文，面向高光谱数据场景。通过 pip 与 conda-forge 分发，采用 3-Clause BSD 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | BSD-3-Clause |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 无监督 SOMClustering、监督/半监督 SOMRegressor 与 SOMClassifier 三种估计器
- 遵循 scikit-learn API 规范，支持 GridSearchCV 超参数优化
- 附带配套论文（Remote Sensing, 2020）与文档、Jupyter 示例
- pip 与 conda-forge 双渠道安装

## 适用场景

- 对高光谱遥感数据做回归与分类建模
- 用 SOM 做无监督聚类与数据探索
- 在半监督场景下利用标注与未标注数据训练 SOM

## 场景标签

 · 领域:机器学习/遥感数据分析

## 证据(README 行号)

> L34: Python package for unsupervised, supervised and semi-supervised self-organizing maps (SOM)
> L41: - SOMClustering: Unsupervised SOM for clustering
> L42: - SOMRegressor: (Semi-)Supervised Regression SOM
> L43: - SOMClassifier: (Semi-)Supervised Classification SOM

## 星数曲线

```mermaid
xychart-beta
    title "felixriese/susi 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 117 --> 119
    line [118, 118]
```

2026-10-18 118 → 2026-10-27 118（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `030909c7396a` · [字段定义](../../DATASET.md)*
