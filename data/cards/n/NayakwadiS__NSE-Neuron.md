# NayakwadiS/NSE-Neuron

⭐ 27 · Python · MIT · 推送 2026-10-28 · [GitHub](https://github.com/NayakwadiS/NSE-Neuron) · 个人维护

**深度学习预测印度 NSE 股票未来 5 日行情的应用**

面向印度国家证券交易所（NSE）上市股票的预测工具：获取历史数据，用 LSTM、BiLSTM、GRU、CNN-LSTM 四种深度学习模型预测未来 5 个交易日的高/低/收盘价，各模型自带信号分类器输出 BUY/HOLD/SELL 信号；附带市场状态识别（牛市/熊市/震荡）并推荐最佳模型，检测 K 线形态与状态交叉参照。以 FastAPI 后端加 React 前端的 Web UI（start.bat 一键启动）和 CLI（python main.py）两种形式提供。

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

- 4 种模型（LSTM/BiLSTM/GRU/CNN-LSTM）各配信号分类器
- Run All 模式一次训练全部模型并按 RMSE 排名
- 市场状态识别（BULL/BEAR/SIDEWAYS）与最佳模型推荐
- 可缩放 OHLC 图表叠加预测与信号标记

## 适用场景

- 查看某只 NSE 股票未来 5 日价格预测与买卖信号
- 对比多种深度学习模型在同一股票上的表现
- 结合 K 线形态与市场状态参考持仓决策

## 场景标签

`金融量化` · 领域:学习与行业

## 证据(README 行号)

> L14: NSE-Neuron fetches historical data for any NSE-listed stock and uses deep learning to forecast the next **5 trading
> L22: - 🤖 **4 models** — LSTM · BiLSTM · GRU · CNN-LSTM, each with its own signal classifier

## 星数曲线

```mermaid
xychart-beta
    title "NayakwadiS/NSE-Neuron 星数(近 4 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-27", "2026-10-29"]
    y-axis "stars" 23 --> 28
    line [24, 25, 27, 27]
```

2026-10-18 24 → 2026-10-29 27（+3）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `40228c9ef6f6` · [字段定义](../../DATASET.md)*
