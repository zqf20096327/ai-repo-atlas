# gamzeakkurt/deep-learning-stock-prediction

⭐ 25 · Python · MIT · 推送 2026-03-31 · [GitHub](https://github.com/gamzeakkurt/deep-learning-stock-prediction) · [官网](https://www.kaggle.com/code/gamzeakkurt/yahoo-stock-forecasting-60-days-lstm-arima-prophet) · 个人维护

**用 LSTM 与线性回归预测美股股价的分析项目**

面向金融数据分析与机器学习学习者的股价预测项目：通过 yfinance 从 Yahoo Finance 获取 AAPL/MSFT/AMZN/TSLA 历史数据，依次执行 EDA、技术指标特征工程（RSI/MACD/布林带/均线）、归一化预处理，再训练 Linear Regression 与 3 层双向 BiLSTM（18 特征输入、Adam 优化器、Huber 损失）预测收盘价，用 RMSE/MAE 评估并可视化。以 git clone + pip 安装依赖后运行 main.py 的 Python 脚本方式提供。

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

- yfinance 获取四只美股（AAPL/MSFT/AMZN/TSLA）历史数据
- 技术指标特征工程：RSI、MACD、布林带、SMA/EMA
- 3 层双向 BiLSTM（64 单元×3）+ 线性回归双模型预测
- RMSE/MAE 评估与实际 vs 预测对比可视化

## 适用场景

- 我想学习如何用 LSTM 做时间序列股价预测
- 我需要对几只美股做 EDA 与技术指标分析
- 我想比较线性回归与深度学习在股价预测上的误差表现

## 场景标签

`金融量化` · 领域:学习与行业

## 证据(README 行号)

> L7: Using **Yahoo Finance data**, we apply **Exploratory Data Analysis (EDA), Feature Engineering, Preprocessing, and Lo
> L17: ✅ Implement an **LSTM and Linear Regression models** for stock price forecasting 🧠

## 星数曲线

```mermaid
xychart-beta
    title "gamzeakkurt/deep-learning-stock-prediction 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 24 --> 26
    line [25, 25]
```

2026-10-18 25 → 2026-10-28 25（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `327ab09dab5e` · [字段定义](../../DATASET.md)*
