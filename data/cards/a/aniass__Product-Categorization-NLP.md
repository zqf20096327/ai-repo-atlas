# aniass/Product-Categorization-NLP

⭐ 98 · Jupyter Notebook · 推送 2025-11-26 · [GitHub](https://github.com/aniass/Product-Categorization-NLP) · 个人维护

**基于商品描述的美妆产品多分类文本分类项目**

以 Jupyter Notebook 与 Python 脚本组织的个人分析项目：使用从 makeup API 获取的美妆商品描述数据集（5 个类别），依次完成数据分析、LDA 主题建模、数据清洗，并对比多种文本表示（BoW+TF-IDF、Word2vec、Doc2vec、Distilbert 嵌入）与多种算法（逻辑回归、SVM、朴素贝叶斯、随机森林、梯度提升、MLP、CNN、Distilbert 迁移学习）。报告中 SVM (BOW+TF-IDF) 验证集准确率为 96%。运行方式为 Jupyter Notebook 或 Google Colab。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 覆盖 ML 与神经网络（MLP、CNN、Distilbert）的多算法对比
- 多种文本表示：BoW+TF-IDF、Word2vec、Doc2vec、Distilbert 嵌入
- 附带数据清洗、训练（含 SMOTE）与预测脚本
- README 给出各模型准确率汇总表

## 适用场景

- 学习多类别文本分类的完整流程与多种方法对比
- 参考 Distilbert 迁移学习在小数据集上的用法
- 复用商品描述自动分类的基线方案

## 场景标签

 · 领域:NLP/文本分类

## 证据(README 行号)

> L14: The aim of the project was multi-class text classification to make-up products based on their description. Based on
> L32: To resolve problem of the product categorization based on their description I have applied multi-class text classif

## 星数曲线

```mermaid
xychart-beta
    title "aniass/Product-Categorization-NLP 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-23"]
    y-axis "stars" 97 --> 99
    line [98, 98]
```

2026-10-18 98 → 2026-10-23 98（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `a8daffb5cdd6` · [字段定义](../../DATASET.md)*
