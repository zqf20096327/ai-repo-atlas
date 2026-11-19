# hexsyro/churn-boosting-showdown

⭐ 30 · Jupyter Notebook · MIT · 推送 2026-11-14 · [GitHub](https://github.com/hexsyro/churn-boosting-showdown) · 个人维护

**XGBoost/LightGBM/CatBoost 客户流失预测对比实验项目**

在 Telco 客户流失数据集（7,043 条，约 26.5% 流失率）上用同一任务训练 XGBoost、LightGBM 和 CatBoost 三个梯度提升库并给出对比结果：测试集 ROC-AUC 分别为 0.8474/0.8376/0.8477，单次训练耗时 2.74s/4.14s/11.89s（LightGBM 最快）。覆盖数据加载、预处理、分层切分、训练与评估的流水线脚本，以及 6 个按序探索的 notebook。面向学习梯度提升理论与实践的开发者/学员。

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

- 三库同数据同任务的测试集指标对比表（含精度/召回/F1/ROC-AUC）
- 调参实验：浅树（depth=3, lr=0.03）优于深树，约 1,900 次额外拟合后验证 AUC 仍约 0.813
- 早停分析：忽略早停导致训练损失降至 0.33 而验证损失停滞在 0.44 附近
- 流水线脚本（data_load→preprocess→train→evaluate）与 6 个 Kaggle notebook

## 适用场景

- 学习 XGBoost/LightGBM/CatBoost 的调参与早停实践
- 比较三个提升库在同一流失预测任务上的准确率与速度
- 理解 boosting 训练/验证损失曲线与过拟合现象

## 场景标签

`教程课程` · 领域:学习与行业

## 证据(README 行号)

> L3: **XGBoost vs LightGBM vs CatBoost: same churn-prediction task, same data, head to head.**
> L5: This project uses the Telco customer churn dataset (7,043 customers; contract type, tenure, internet service, monthl

## 星数曲线

```mermaid
xychart-beta
    title "hexsyro/churn-boosting-showdown 星数(近 2 点)"
    x-axis ["2026-11-15", "2026-11-19"]
    y-axis "stars" 29 --> 31
    line [30, 30]
```

2026-11-15 30 → 2026-11-19 30（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-18 · 置信度 high · 依据 README sha `e4d79463ef39` · [字段定义](../../DATASET.md)*
