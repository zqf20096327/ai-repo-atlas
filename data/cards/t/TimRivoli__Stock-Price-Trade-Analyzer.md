# TimRivoli/Stock-Price-Trade-Analyzer

⭐ 78 · Python · GPL-3.0 · 推送 2026-05-23 · [GitHub](https://github.com/TimRivoli/Stock-Price-Trade-Analyzer) · 个人维护

**股价分析与交易策略回测工具包，含 TensorFlow 价格预测**

Python 3 工具包，含两个模块：PriceTradeAnalyzer 通过 Yahoo Finance 拉取历史 OHLCV 数据，缓存为 CSV 并载入 Pandas，提供技术指标计算、图表绘制、投资组合模拟与策略回测（含 Buy and Hold、Seasonal、Trending 示例策略），结果导出 CSV/PNG；SeriesPrediction 基于 TensorFlow/Keras 构建双输出神经网络，同时预测价格变动方向与幅度。可选 SQL Server 数据库后端以支持大规模股票池分析。声明仅供教育研究用途。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 历史数据获取、技术指标计算与策略回测框架，结果导出 CSV/PNG
- 双输出神经网络（方向 Sigmoid + 幅度 ReLU）预测价格变动
- 可选 Microsoft SQL Server 后端，支持大规模股票池与逐笔交易深度分析

## 适用场景

- 对自定买卖策略在数十年历史数据上做回测
- 用 LSTM/CNN/GRU 等神经网络实验价格预测
- 搭建 SQL Server 数据库管理多标的行情与回测数据

## 场景标签

`金融量化` · 领域:学习与行业

## 证据(README 行号)

> L3: A Python 3 toolkit for downloading, analyzing, and backtesting stock trading strategies, with optional deep-learning
> L10: - **SeriesPrediction** — neural-network price forecasting (LSTM, CNN, GRU, BiLSTM, and more)
> L54: A dual-output neural network built with TensorFlow and Keras that predicts both the **direction** and **magnitude**

## 星数曲线

```mermaid
xychart-beta
    title "TimRivoli/Stock-Price-Trade-Analyzer 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 77 --> 79
    line [78, 78]
```

2026-10-18 78 → 2026-10-25 78（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `cdc038a32035` · [字段定义](../../DATASET.md)*
