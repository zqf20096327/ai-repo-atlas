# AmirhosseinHonardoust/Stock-LSTM-Forecasting

⭐ 38 · Python · MIT · 推送 2026-05-29 · [GitHub](https://github.com/AmirhosseinHonardoust/Stock-LSTM-Forecasting) · 个人维护

**用 PyTorch LSTM 预测股价的时间序列学习项目**

端到端股价预测示例工程：读取 CSV 或经 yfinance 下载 OHLCV 日线数据，做缩放与滑动窗口构造，训练带 dropout 的 LSTM（Adam 优化器、早停），用 RMSE/MAE/MAPE 评估并输出训练曲线、预测对比与短周期未来预测图，产物保存为 best_lstm.pt、scaler.pkl、metrics.json。附带合成数据集可跳过下载直接训练，定位为教学与作品集展示。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- CSV/yfinance 数据获取与滑动窗口预处理
- LSTM 训练含 dropout、Adam 与早停
- RMSE/MAE/MAPE 指标评估与可视化
- 附带合成数据集与可复现命令（seed）

## 适用场景

- 学习如何用 LSTM 做时间序列预测
- 作为深度学习/金融建模的作品集项目
- 在自带数据上跑通训练与评估流程

## 场景标签

`金融量化` · 领域:学习与行业

## 证据(README 行号)

> L3: Stock Price Prediction with LSTM is a hands-on deep learning project that demonstrates how sequential models can be 
> L5: The pipeline handles everything from preprocessing and sliding-window dataset creation to model training with early 

## 星数曲线

```mermaid
xychart-beta
    title "AmirhosseinHonardoust/Stock-LSTM-Forecasting 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 37 --> 39
    line [38, 38]
```

2026-10-18 38 → 2026-10-29 38（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `f33f2b133732` · [字段定义](../../DATASET.md)*
