# antonin-lfv/Online_preprocessing_for_ML

⭐ 16 · Python · MIT · 推送 2025-12-03 · [GitHub](https://github.com/antonin-lfv/Online_preprocessing_for_ML) · 个人维护

**无代码机器学习网页平台：上传数据集、可视化并直接训练模型**

基于 Python 和 Streamlit 部署的 No-code AI 平台，面向不写代码的用户在浏览器中完成机器学习流程：使用内置数据集（iris、penguins）或上传自定义数据集，在页面上完成预处理与编码；提供列分析、相关矩阵与多种图表可视化；支持线性/多项式/Elastic Net/Ridge/Lasso/Poisson 回归，以及 KNN、K-Means、SVM（仅线性核）、决策树分类与 PCA/UMAP/t-SNE 降维，可查看学习曲线、指标、ROC 并用模型做预测。本地运行通过 uv 安装依赖后启动 Streamlit。限制：SVM 仅线性核且仅二分类，修改数据集后需重新下载再上传。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 内置或上传数据集，页面内完成预处理与编码
- 支持回归（线性/多项式/Ridge/Lasso/Elastic Net/Poisson）与分类（KNN/K-Means/SVM/决策树）
- PCA/UMAP/t-SNE 三种降维可视化
- 展示学习曲线、指标与 ROC，模型可用于预测

## 适用场景

- 不写代码在浏览器里训练和评估回归/分类模型
- 对数据集做探索性分析与相关性和降维可视化
- 教学或快速实验中替代手写 sklearn 代码

## 场景标签

`数据分析` · 领域:效率与自动化

## 证据(README 行号)

> L3:  La No-code AI platform est un site développé avec Python et déployé avec Streamlit , qui permet de faire du Machine
> L65: Il vous sera aussi possible d'utiliser le modèle pour faire des prédictions.

## 星数曲线

```mermaid
xychart-beta
    title "antonin-lfv/Online_preprocessing_for_ML 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-31 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `f0478d308d1e` · [字段定义](../../DATASET.md)*
