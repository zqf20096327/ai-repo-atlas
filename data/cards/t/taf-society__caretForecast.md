# taf-society/caretForecast

⭐ 30 · R · GPL-3.0 · 推送 2026-01-31 · [GitHub](https://github.com/taf-society/caretForecast) · [官网](https://taf-society.github.io/caretForecast) · 组织维护

**R 包：用 caret 机器学习模型做时间序列预测**

面向 R 用户的时序预测包，位于 CRAN（GPLv3，lifecycle 标注 maturing）。允许通过 caret 包训练任意回归模型（glmboost、cubist、SVM、ridge 等示例）做时间序列预测；自动特征工程包括滞后项与傅里叶季节项，支持通过 xreg 加入促销、节假日等外部回归变量，兼容 hts 包的层级/分组时序。自 0.1.2 版起实现按预测视野的保形预测区间，通过滚动起点校准获得随视野自然变宽的区间。由维也纳非营利组织 TAFS 维护。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 使用 caret 包中任意回归模型做时间序列预测
- 滞后值与傅里叶项的自动特征工程
- 按预测视野的保形预测区间（滚动起点校准，默认开启）
- 支持外部回归变量与 hts 层级/分组时序

## 适用场景

- 用机器学习模型替代传统统计模型做零售等时序预测
- 为预测结果获取经校准的置信区间
- 纳入促销、节假日等外部变量进行预测建模

## 场景标签

`数据分析` · 领域:效率与自动化

## 证据(README 行号)

> L18: caretForecast aspires to equip users with the means of using machine
> L23: - Use any regression model from the caret package for time series

## 星数曲线

```mermaid
xychart-beta
    title "taf-society/caretForecast 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-30"]
    y-axis "stars" 28 --> 31
    line [29, 30, 30]
```

2026-10-18 29 → 2026-10-30 30（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `9c40e66502a5` · [字段定义](../../DATASET.md)*
