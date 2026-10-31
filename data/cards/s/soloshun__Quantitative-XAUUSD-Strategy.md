# soloshun/Quantitative-XAUUSD-Strategy

⭐ 13 · Jupyter Notebook · MIT · 推送 2026-01-04 · [GitHub](https://github.com/soloshun/Quantitative-XAUUSD-Strategy) · 个人维护

**黄金 XAU/USD 日内交易时段预测的量化研究项目**

量化研究项目，围绕黄金（XAU/USD）日内时段动态建模与预测：以 XGBoost（表格特征）与深度学习模型（LSTM、Transformer，序列数据）双路线对每个研究假设做基准对比，同时做方向分类与收益回归。数据经 MetaTrader5 API 获取，用 backtesting.py 回测；仅 Hypothesis A（亚盘→伦敦盘）已实现，其余假设与综合报告在路线图中未完成。当前实现仅支持 1 小时（H1）周期数据。

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

- XGBoost 与 LSTM/Transformer 双模型路线基准对比
- 分类（方向预测）与回归（收益预测）两类任务
- MetaTrader5 API 数据获取 + backtesting.py 回测
- 研究路线图明确标注：仅 Hypothesis A 已完成

## 适用场景

- 研究交易时段特征对后续时段行为的预测能力
- 对比树模型与深度学习在金融时序预测上的表现
- 基于 MetaTrader5 数据构建可回测的量化流水线

## 场景标签

`金融量化` · 领域:学习与行业

## 证据(README 行号)

> L7: A quantitative research project to model and predict the session dynamics of Gold (XAU/USD). This repository explore
> L9: The project investigates both **classification** (predicting market direction) and **regression** (predicting market

## 星数曲线

```mermaid
xychart-beta
    title "soloshun/Quantitative-XAUUSD-Strategy 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-26", "2026-10-31"]
    y-axis "stars" 11 --> 14
    line [12, 13, 13]
```

2026-10-18 12 → 2026-10-31 13（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `683fd0923b4c` · [字段定义](../../DATASET.md)*
