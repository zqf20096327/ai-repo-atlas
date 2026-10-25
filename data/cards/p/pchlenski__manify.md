# pchlenski/manify

⭐ 76 · Jupyter Notebook · MIT · 推送 2026-07-29 · [GitHub](https://github.com/pchlenski/manify) · [官网](https://manify.readthedocs.io/en/latest/) · 组织维护

**非欧几里得表示学习 Python 库：流形嵌入与机器学习**

基于 geoopt 构建、遵循 scikit-learn API 约定的 Python 库，面向黎曼（乘积）流形上的表示学习：支持指数/对数映射、平行移动与距离计算等基本流形操作、高斯分布与混合高斯采样、曲率估计（delta-hyperbolicity、截面曲率）、在乘积流形上学习嵌入（坐标学习、Siamese 网络、VAE），并在流形嵌入上训练决策树、随机森林、SVM、感知机、神经网络及 Riemannian 模糊 K-Means 聚类。提供 PyPI 安装与 Jupyter 教程，附 arXiv 论文。

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

- 基本流形操作：指数/对数映射、平行移动、距离计算
- 曲率估计：delta-hyperbolicity、截面曲vature、贪心签名选择
- 乘积流形嵌入器：坐标学习、Siamese 网络、变分自编码器
- 流形上的预测器：决策树/随机森林、SVM、感知机、Kappa GCN 及 Riemannian 模糊 K-Means

## 适用场景

- 在双曲/混合曲率空间学习数据嵌入
- 对图或度量数据进行曲率估计与流形结构分析
- 直接在非欧嵌入上训练分类、回归与聚类模型

## 场景标签

 · 领域:机器学习/几何表示学习

## 证据(README 行号)

> L12: Manify is a Python library for non-Euclidean representation learning.
> L18: - Training machine learning models on manifold-valued embeddings, including decision trees, random forests, SVMs,

## 星数曲线

```mermaid
xychart-beta
    title "pchlenski/manify 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 75 --> 77
    line [76, 76]
```

2026-10-18 76 → 2026-10-25 76（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `ce8f00b08ac5` · [字段定义](../../DATASET.md)*
