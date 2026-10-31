# jacktan1/Options-Project

⭐ 19 · Jupyter Notebook · GPL-3.0 · 推送 2026-03-26 · [GitHub](https://github.com/jacktan1/Options-Project) · 个人维护

**用机器学习预测期权策略收益的研究项目**

个人研究项目：从日终期权快照提取 Greeks、自定义 VIX、未平仓量变化等特征，用基线模型与 XGBoost 训练多个不同到期期限（1 至 520 天）的子模型，通过核密度估计生成预测分布，再据此选择期权与构建垂直价差等交易策略。数据来源为 Alpha Vantage、Questrade API 与 FRED，分别获取历史股价、现价与国债收益率。README 未给出安装或运行命令，XGBoost 演示标注为进行中。

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

- 按 12 种期限训练子模型并用核密度估计生成预测分布
- 基线模型与去趋势（ARIMA/ADF）的 XGBoost 模型
- 基于预测分布选择期权构建牛市看涨价差策略
- Greeks（Delta/VIX 参数化）与未平仓量/成交量自定义特征工程

## 适用场景

- 研究机器学习在期权策略收益预测中的应用
- 复现特征工程与预测分布的建模流程
- 参考期权数据清洗与拆股调整方法

## 场景标签

`金融量化` · 领域:学习与行业

## 证据(README 行号)

> L5: **Goal:** Use Greeks and sentiment features derived from end-of-day (EOD) option snapshots to predict performance of
> L55: - **Part 5: Fit & Predict Models**
> L67:  - **XGBoost model**

## 星数曲线

```mermaid
xychart-beta
    title "jacktan1/Options-Project 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 18 --> 20
    line [19, 19]
```

2026-10-18 19 → 2026-10-31 19（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `fe9260e24761` · [字段定义](../../DATASET.md)*
