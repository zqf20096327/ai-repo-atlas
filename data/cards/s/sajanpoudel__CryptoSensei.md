# sajanpoudel/CryptoSensei

⭐ 23 · TypeScript · 推送 2026-01-11 · [GitHub](https://github.com/sajanpoudel/CryptoSensei) · [官网](https://crypto-sensei.vercel.app) · 个人维护

**实时加密货币分析平台：技术面+情绪+AI预测生成交易建议**

基于 Next.js 14 与 TensorFlow.js 的加密货币实时分析平台，面向交易决策用户：整合 CoinGecko 行情数据、NewsData 新闻数据与 WebSocket 实时流，提供 RSI/MACD/布林带等技术指标、市场阶段识别、情绪分析、风险管理评估，并用三个 ML 模型（TrendModel/PriceModel/LevelModel）输出趋势方向与价格预测，自动生成含入场点/止损/仓位的交易策略。免费 CoinGecko API 存在速率限制，需要 NewsData 与 Gemini API key。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- RSI/MACD/均线/布林带/成交量分布等技术指标与支撑阻力识别
- TrendModel/PriceModel/LevelModel 三个 TensorFlow.js 模型做趋势与价格预测
- 新闻聚合与情绪分析、来源可信度评分
- 自动生成含入场点、止损、仓位建议的交易策略

## 适用场景

- 实时跟踪多时间周期的加密货币行情并查看技术分析
- 结合新闻情绪与 ML 预测辅助交易决策
- 获取带风险控制参数的交易策略建议

## 场景标签

`金融量化` · 领域:学习与行业

## 证据(README 行号)

> L17: - AI-powered price predictions
> L112: ### Machine Learning Models (`src/services/ml/models.ts`)
> L113: - TrendModel: Predicts market trend direction

## 星数曲线

```mermaid
xychart-beta
    title "sajanpoudel/CryptoSensei 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 22 --> 24
    line [23, 23]
```

2026-10-18 23 → 2026-10-29 23（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `9d2ee3fdbcce` · [字段定义](../../DATASET.md)*
