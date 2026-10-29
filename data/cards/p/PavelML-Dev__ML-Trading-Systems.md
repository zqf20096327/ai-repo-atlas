# PavelML-Dev/ML-Trading-Systems

⭐ 18 · MIT · 推送 2026-06-08 · [GitHub](https://github.com/PavelML-Dev/ML-Trading-Systems) · 个人维护

**Pine Script 实现的 DQN+LSTM 强化学习交易指标，浏览器内自学习**

用纯 Pine Script 在 TradingView 中实现的强化学习交易系统：4 层 MLP 的 Deep Q-Network 从 8 个 ATR 乘数动作中选择，LSTM（BPTT）捕捉时序模式，Prioritized Experience Replay（7 万条缓冲）与 Adam 优化器在线训练，提取 RSI/MACD/ATR 等 20+ 特征。无需 Python、GPU 或外部库，粘贴到 Pine Editor 即可运行。README 声明为教育用途的实验性研究项目，非生产交易系统，不构成投资建议，无盈利保证。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 纯 Pine Script 实现 DQN + LSTM + PER + Adam，无需 Python/GPU/外部库
- 实时在线学习：每 10 根 K 线训练一次，动态时间步 8-20
- 20+ 市场特征提取（RSI、MACD、ATR、Ichimoku、VWAP 等）
- 提供 TD-Error/EMA Error/Q 值等训练监控指标与调试面板

## 适用场景

- 在 TradingView 图表上运行自适应 SuperTrend 型交易指标
- 学习从零实现 DQN、LSTM、BPTT、优先经验回放等强化学习技术
- 研究受限环境下（无外部库）的在线神经网络的交易策略

## 场景标签

`金融量化` `强化学习` `教程课程` · 领域:学习与行业

## 证据(README 行号)

> L8: > **First fully-working LSTM + Deep Q-Network trading system implemented in Pine Script!**
> L16: - ✅ **Learns from experience** using Deep Q-Learning
> L34: **This is an experimental research project for educational purposes.**

## 星数曲线

```mermaid
xychart-beta
    title "PavelML-Dev/ML-Trading-Systems 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 17 --> 19
    line [18, 18]
```

2026-10-18 18 → 2026-10-29 18（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `4c91b5a4f7e0` · [字段定义](../../DATASET.md)*
