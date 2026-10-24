# akash-kumar5/CryptoMarket_Regime_Classifier

⭐ 50 · Python · 推送 2025-12-13 · [GitHub](https://github.com/akash-kumar5/CryptoMarket_Regime_Classifier) · 个人维护

**用 HMM+LSTM 检测加密货币市场状态的机器学习管线**

面向加密交易策略的机器学习管线：从 Binance 拉取多时间框（5m/15m）OHLCV 数据，计算动量/趋势/波动率指标并做 PCA 降维，先用 6 状态隐马尔可夫模型无监督发现市场状态（强趋势/弱趋势/区间/剧烈波动/波动尖峰/挤压），再用 LSTM 学习状态转移并预测，输出精确率/召回率/F1 与混淆矩阵。模型和缩放器导出至 /models 供下游系统复用，自带 Streamlit 仪表盘。定位为研究与基础工具，声明不构成财务建议。

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

- HMM 无监督发现 6 种市场状态，BIC 选择状态数
- LSTM 在 HMM 标签上训练以预测状态转移，Keras Tuner 调参
- 多时间框 OHLCV 数据与技术指标特征工程
- 模型与缩放器导出供下游机器人/仪表盘/API 复用

## 适用场景

- 为交易策略选择、仓位与风控提供市场状态识别层
- 研究加密市场不同状态间的转移规律
- 作为实盘系统的状态感知基础组件做二次开发

## 场景标签

`金融量化` · 领域:学习与行业

## 证据(README 行号)

> L9: **CryptoMarket Regime Classifier** is a machine learning pipeline that detects and predicts crypto market regimes us
> L27: **LSTM (Regime Prediction)**

## 星数曲线

```mermaid
xychart-beta
    title "akash-kumar5/CryptoMarket_Regime_Classifier 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 49 --> 51
    line [50, 50]
```

2026-10-18 50 → 2026-10-24 50（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 mid · 依据 README sha `18a7df57b68e` · [字段定义](../../DATASET.md)*
