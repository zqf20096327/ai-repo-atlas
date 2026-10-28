# breimanntools/aaanalysis

⭐ 89 · Jupyter Notebook · BSD-3-Clause · 推送 2026-10-11 · [GitHub](https://github.com/breimanntools/aaanalysis) · [官网](https://aaanalysis.readthedocs.io) · 个人维护

**面向蛋白质预测的可解释特征工程 Python 框架**

AAanalysis 是基于序列的蛋白质预测 Python 框架，核心算法包括 CPP（两组蛋白序列的理化特征比较）、dPULearn（确定性 PU 学习，支持不平衡小数据集训练）与 AAclust（k 优化的聚类封装，用于氨基酸标度降冗余）。提供基准数据集与氨基酸标度加载功能及两层分类 AAontology，结合 SHAP 实现单残基分辨率的样本级预测解释，并提供绘图函数生成出版级图表。通过 pip 安装，[pro] 扩展包含可解释 AI 模块。

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

- CPP 比较两组蛋白序列识别最具区分性的特征
- dPULearn 确定性 PU 学习支持不平衡小数据集
- AAclust 选择冗余度降低的氨基酸标度集合
- 结合 SHAP 提供单残基分辨率的预测解释

## 适用场景

- 在小样本、不平衡数据上训练蛋白质预测模型
- 解释模型预测并定位关键残基
- 生成出版级的数据可视化图表

## 场景标签

 · 领域:生物信息学/蛋白质预测

## 证据(README 行号)

> L69: **AAanalysis** (Amino Acid analysis) is a Python framework for interpretable sequence-based protein prediction.
> L81: AI `SHAP <https://shap.readthedocs.io/en/latest/index.html>`_ framework to explain sample level predictions with

## 星数曲线

```mermaid
xychart-beta
    title "breimanntools/aaanalysis 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-28"]
    y-axis "stars" 87 --> 90
    line [88, 89, 89]
```

2026-10-18 88 → 2026-10-28 89（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `a2e9b44a414d` · [字段定义](../../DATASET.md)*
