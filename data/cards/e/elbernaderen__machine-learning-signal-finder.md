# elbernaderen/machine-learning-signal-finder

⭐ 25 · Python · MIT · 推送 2025-11-27 · [GitHub](https://github.com/elbernaderen/machine-learning-signal-finder) · 个人维护

**用随机森林预测加密货币涨跌并通过 Telegram 发送交易信号的脚本集**

围绕随机森林（Random Tree Forest）分类器的加密货币交易工具集，由多个 Python 脚本组成：amplitudes 从 Binance 下载的 K 线历史数据计算 MACD、RSI、成交量、振幅等技术指标生成训练样本并训练模型，保存为 .sav 文件；backtest_amplitudes / backtest_strategy 对策略与模型做回测并输出 .xlsx 报表；messenger_d.py 用已训练模型对最新数据预测价格上升并通过 Telegram bot 发送买入信号，API 配置存于 yml 文件。运行方式为命令行交互输入参数，供个人交易者与量化爱好者使用。

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

- 从 K 线历史数据生成含 MACD/RSI/成交量/振幅指标的训练样本并训练随机森林模型
- 模型以 .sav 文件保存，可供回测与信号发送脚本复用
- 回测脚本输出含买卖决策与后续涨跌验证的 .xlsx 报表
- messenger_d.py 通过 Telegram bot 发送模型预测的买入信号

## 适用场景

- 训练并回测基于技术指标的加密货币涨跌预测模型
- 让 bot 监控行情并在模型预测上涨时通过 Telegram 推送信号
- 调整 RSI、成交量、斜率等过滤参数改进交易策略

## 场景标签

`金融量化` · 领域:学习与行业

## 证据(README 行号)

> L19: Once we have ran over all the Cryptocurrency Historical Data we determined and generated the mentionated rows with 
> L21: Then, with the model we can predict if the prices will rise and send a signal with the telegram bot, and so we'll k
> L163: Here we have a signal bot trading, that using telegram sends signals found with a predictor made with Machine Lear

## 星数曲线

```mermaid
xychart-beta
    title "elbernaderen/machine-learning-signal-finder 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-31"]
    y-axis "stars" 23 --> 26
    line [24, 25, 25]
```

2026-10-18 24 → 2026-10-31 25（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `747fc1d2525e` · [字段定义](../../DATASET.md)*
