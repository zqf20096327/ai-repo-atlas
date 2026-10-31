# mohdshamii/HamOrSpam-Classifier

⭐ 16 · Jupyter Notebook · 推送 2026-05-15 · [GitHub](https://github.com/mohdshamii/HamOrSpam-Classifier) · 个人维护

**垃圾邮件分类系统：TF-IDF+逻辑回归识别 ham/spam**

基于 Python 与 scikit-learn 的邮件垃圾分类应用：TF-IDF 向量化结合逻辑回归，在 Enron Spam 数据集（5,000+ 样本）上训练，用 SMOTE 处理类别不平衡，README 报告 98.2% 准确率。提供 Streamlit 深色界面（预测、分析看板、词云）、校准概率输出与可调阈值（默认 0.85）、/predict REST 端点及模型导出。面向需要快速部署垃圾邮件检测的开发者，支持 Streamlit Cloud 与自托管。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- TF-IDF + 逻辑回归管道，报告 98.2% 准确率
- SMOTE 过采样处理 70/30 类别不平衡
- Streamlit UI + /predict REST 端点 + 可导出模型
- 阈值、特征数等通过 .env 配置

## 适用场景

- 对邮件文本做实时 spam/ham 分类并查看置信度
- 通过分析看板查看混淆矩阵与关键词分布
- 自托管部署后以 REST 接口接入现有邮件系统

## 场景标签

 · 领域:NLP/文本分类

## 证据(README 行号)

> L12: HamOrSpam is a production-grade spam detection system that combines TF-IDF vectorization with logistic regression t
> L18: Email spam detection remains a core challenge in messaging infrastructure. HamOrSpam addresses this with a lightwei

## 星数曲线

```mermaid
xychart-beta
    title "mohdshamii/HamOrSpam-Classifier 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-31 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `890807077bda` · [字段定义](../../DATASET.md)*
