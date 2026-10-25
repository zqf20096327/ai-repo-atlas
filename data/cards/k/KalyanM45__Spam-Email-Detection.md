# KalyanM45/Spam-Email-Detection

⭐ 37 · Jupyter Notebook · 推送 2025-12-25 · [GitHub](https://github.com/KalyanM45/Spam-Email-Detection) · 个人维护

**垃圾邮件分类系统：多模型训练与 Streamlit 交互界面**

基于 Scikit-learn 的邮件 Spam/Ham 二分类系统，采用模块化管道分离数据摄取、转换与训练，评估 SVM、逻辑回归、决策树、随机森林等多种算法，5 折交叉验证后选取最优模型推理。提供 Streamlit Web 界面支持单封邮件预测与 .mbox 归档批量处理（结果导出 CSV），并可重新训练模型、通过配置文件调整超参数与路径。面向需要快速部署或实验垃圾邮件过滤的开发者。

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

- 多算法评估（SVM/逻辑回归/决策树/随机森林）与 5 折交叉验证选优
- Streamlit Web 界面：单封预测带置信度、mbox 批量处理导出 CSV
- 模块化训练管道，支持在新数据上重新训练
- 通过配置文件调整超参数、路径与交叉验证参数

## 适用场景

- 粘贴邮件内容即时判断是否为垃圾邮件
- 批量处理整个 mbox 邮件归档并导出分类结果
- 在自己的数据集上重新训练垃圾邮件分类模型

## 场景标签

 · 领域:机器学习/邮件安全

## 证据(README 行号)

> L3: A production-grade machine learning system designed to robustly classify emails as "Spam" or "Ham" (legitimate). Thi
> L8: - **Multiple Model Support**: evaluation of various algorithms including SVM, Logistic Regression, Decision Trees, a

## 星数曲线

```mermaid
xychart-beta
    title "KalyanM45/Spam-Email-Detection 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 36 --> 38
    line [37, 37]
```

2026-10-18 37 → 2026-10-25 37（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `ec7a6231e0d3` · [字段定义](../../DATASET.md)*
