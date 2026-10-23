# business-science/modeltime

⭐ 585 · R · NOASSERTION · 推送 2026-01-30 · [GitHub](https://github.com/business-science/modeltime) · [官网](https://business-science.github.io/modeltime/) · 组织维护

**R 语言时间序列预测统一框架：机器学习与经典模型并用**

R 包，为时间序列建模与预测提供统一基础设施：在 tidymodels 工作流中接入经典模型（ARIMA/ETS，arima_reg()/arima_boost()/exp_smoothing()）、Facebook Prophet（prophet_reg()/prophet_boost()）及任意 parsnip 机器学习模型（随机森林、XGBoost、SVM 等）。提供 CRAN 与 GitHub 两种安装途径，配套文档教程与 11 分钟入门视频，并属于含 GluonTS 深度学习、集成、回测等包的 modeltime 生态。README 同时推广付费课程。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 在单一框架内使用 ARIMA/ETS 与机器学习模型做预测
- 支持 Facebook Prophet（prophet_reg()/prophet_boost()）
- 接入任意 parsnip 模型（rand_forest/boost_tree/svm_rbf 等）
- 属于含 H2O AutoML、GluonTS、Ensemble、Resample 的生态体系

## 适用场景

- 在 R 中做时间序列预测而不在多框架间切换
- 用机器学习模型（XGBoost/随机森林）结合滞后特征做预测
- 构建含集成与回测的预测工作流

## 场景标签

 · 领域:数据科学/时间序列预测

## 证据(README 行号)

> L9: > Tidy time series forecasting in `R`.
> L64: - **forecast**: Use ARIMA, ETS, and more models coming (`arima_reg()`,
> L68: - **tidymodels**: Use any `parsnip` model: `rand_forest()`,

## 星数曲线

```mermaid
xychart-beta
    title "business-science/modeltime 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-23"]
    y-axis "stars" 583 --> 586
    line [584, 585, 585]
```

2026-10-18 584 → 2026-10-23 585（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `3f5f9282af64` · [字段定义](../../DATASET.md)*
