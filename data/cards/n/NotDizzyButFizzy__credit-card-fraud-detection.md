# NotDizzyButFizzy/credit-card-fraud-detection

⭐ 17 · Jupyter Notebook · MIT · 推送 2026-08-16 · [GitHub](https://github.com/NotDizzyButFizzy/credit-card-fraud-detection) · [官网](https://credit-card-fraud-detection-cjb9mtzqdgrmahw8rjn77p.streamlit.app/) · 个人维护

**用随机森林识别信用卡欺诈交易的机器学习系统**

基于 Python 与 scikit-learn 的欺诈交易分类系统：针对少于 0.2% 正样本的极端不平衡数据，仅在训练集上用 SMOTE 平衡，训练随机森林分类器，以 recall/precision/F1 为主要评估指标（欺诈类 recall 0.8367、precision 0.8454）。工程上包含模块化代码、实时逐笔交易评分模拟、pytest 测试套件、GitHub Actions CI/CD 与再训练验证门控，并提供 Streamlit 交互式 Web 应用在线试用。数据集需自行从 Kaggle 下载。

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

- SMOTE 仅作用于训练集以避免数据泄漏，处理极端类不平衡
- 随机森林分类器，以 recall/precision/F1 为核心评估指标
- 实时交易流模拟与 Streamlit 在线演示应用
- GitHub Actions CI/CD 与带 recall/precision 门槛的再训练验证管道

## 适用场景

- 我想在浏览器里加载交易样本查看欺诈判定结果
- 学习不平衡数据下的欺诈检测建模与评估方法
- 参考含测试、CI/CD 与模型验证门控的 ML 工程实践

## 场景标签

 · 领域:金融风控/机器学习

## 证据(README 行号)

> L17: This project tackles that head-on. It handles the class imbalance with SMOTE, trains a Random Forest classifier, an
> L35: - **Random Forest classifier** trained and evaluated on unseen data.

## 星数曲线

```mermaid
xychart-beta
    title "NotDizzyButFizzy/credit-card-fraud-detection 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-31"]
    y-axis "stars" 15 --> 18
    line [16, 17, 17]
```

2026-10-18 16 → 2026-10-31 17（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `db17c409fdd4` · [字段定义](../../DATASET.md)*
