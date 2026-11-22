# kaluarachchiteshan/agromaster-ml

⭐ 5 · Jupyter Notebook · 推送 2026-11-16 · [GitHub](https://github.com/kaluarachchiteshan/agromaster-ml) · 组织维护

**面向农业市场研究者：用机器学习预测商品七天后价格下跌风险等级**

AgroMaster 是 University of Ruhuna 的机器学习课程/研究项目，基于 AGMARKNET 印度批发市场每日价格数据，将商品在七天后出现价格下跌的风险分类为 Low/Medium/High。仅使用价格历史、地点与日历信息构造 25 个特征，对五种监督算法（Logistic Regression、Gaussian NB、决策树、随机森林、XGBoost）与两个基线在严格时间顺序划分下调参比较，含 SHAP 解释。数据不入库，需经 kagglehub 下载约 1.4 GB，依赖 Google Colab 运行 9 个 notebook。

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

- 五种监督模型与两个基线在严格按时间顺序的评估下对比
- 严格防泄漏流程：阈值/缩放/编码仅在训练行上拟合，最终测试期为 2024-01 至 2025-10
- XGBoost 增益重要性、TreeSHAP 与误差分析做解释
- 项目明确声明所选模型在 macro F1 上未超过持续性基线等局限

## 适用场景

- 我想预测印度批发市场蔬菜七天后的价格下跌风险
- 我想按时间顺序无泄漏地复现一个时间序列分类实验流程
- 我想研究 SHAP 对梯度提升模型特征重要性的解释

## 场景标签

`数据分析` · 领域:效率与自动化

## 证据(README 行号)

> L13: This project classifies the price-decline risk of a commodity in an Indian wholesale market (mandi) as **Low**, **M
> L15: Five supervised algorithms are tuned and compared against two simple baselines under a strictly chronological evalu
> L56: 1. Open a notebook in Google Colab.

## 星数曲线

```mermaid
xychart-beta
    title "kaluarachchiteshan/agromaster-ml 星数(近 2 点)"
    x-axis ["2026-11-16", "2026-11-22"]
    y-axis "stars" 4 --> 6
    line [5, 5]
```

2026-11-16 5 → 2026-11-22 5（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-21 · 置信度 high · 依据 README sha `f71eb8147cac` · [字段定义](../../DATASET.md)*
