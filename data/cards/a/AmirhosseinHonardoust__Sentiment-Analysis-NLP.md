# AmirhosseinHonardoust/Sentiment-Analysis-NLP

⭐ 26 · Python · MIT · 推送 2026-09-06 · [GitHub](https://github.com/AmirhosseinHonardoust/Sentiment-Analysis-NLP) · 个人维护

**面向学习/作品集的合成评论情感分类参考实现**

Python + scikit-learn 的客户评论情感分类流水线：生成确定性的模板化合成评论数据（非真实评论），经清洗、分词、停用词去除与词形还原后做 TF-IDF（unigram+bigram）向量化，训练并比较 Multinomial Naive Bayes、Logistic Regression、Random Forest 三种分类器，按 macro-F1 选优，输出混淆矩阵、词云与分类报告。明确定位为教学与作品集参考实现，声明合成数据上三模型均达 macro-F1=1.000，不代表真实数据表现；不提供 API 服务。含 24 个测试与 CI 质量门禁。

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

- 确定性合成评论数据生成（固定 --seed 字节级复现）
- TF-IDF + 三分类器比较，按 macro-F1 选优
- 混淆矩阵、词云、top 特征等可视化报告输出
- 24 个自动化测试与 CI 质量门禁（ruff/black/mypy/pytest）

## 适用场景

- 学习 TF-IDF 文本分类完整工作流
- 参考带测试与 CI 的 ML 项目结构
- 作品集展示用途

## 场景标签

`教程课程` · 领域:学习与行业

## 证据(README 行号)

> L10: A customer-review sentiment classifier built on a **TF-IDF + classical ML** pipeline (Naive Bayes, Logistic Regress
> L37: - Train and compare Multinomial Naive Bayes, Logistic Regression, and Random Forest

## 星数曲线

```mermaid
xychart-beta
    title "AmirhosseinHonardoust/Sentiment-Analysis-NLP 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 25 --> 27
    line [26, 26]
```

2026-10-18 26 → 2026-10-30 26（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 mid · 依据 README sha `d7d256ae27c7` · [字段定义](../../DATASET.md)*
