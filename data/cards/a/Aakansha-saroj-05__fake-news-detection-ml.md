# Aakansha-saroj-05/fake-news-detection-ml

⭐ 14 · Jupyter Notebook · MIT · 推送 2026-07-21 · [GitHub](https://github.com/Aakansha-saroj-05/fake-news-detection-ml) · 个人维护

**基于 TF-IDF 与多模型比较的假新闻分类项目（笔记本）**

以 Jupyter/Google Colab 笔记本形式实现的假新闻检测项目：对新闻文本做清洗与预处理，用 TF-IDF 向量化后训练 Logistic Regression、Multinomial Naive Bayes、Random Forest、Linear SVM 四种模型，按 Accuracy/Precision/Recall/F1 与混淆矩阵比较并选取最优模型，用 Joblib 保存，支持输入自定义新闻文本预测 Real/Fake。安装方式为 git clone 源码并 pip 安装依赖库，无独立打包发布。

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

- TF-IDF 特征提取 + 四种监督学习模型训练与比较
- 完整评估流程：混淆矩阵、分类报告与多种指标
- 支持自定义新闻文本预测并用 Joblib 保存最优模型

## 适用场景

- 学习 NLP 文本分类的端到端流程
- 在 Colab 上快速复现假新闻检测实验
- 对比经典机器学习模型在文本分类上的表现

## 场景标签

`教程课程` · 领域:学习与行业

## 证据(README 行号)

> L3: A machine learning project that classifies news articles as **Real** or **Fake** using Natural Language Processing (
> L16: - TF-IDF Vectorization
> L40: - Logistic Regression

## 星数曲线

```mermaid
xychart-beta
    title "Aakansha-saroj-05/fake-news-detection-ml 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 mid · 依据 README sha `0d10594ccd91` · [字段定义](../../DATASET.md)*
