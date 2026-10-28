# sankeer28/stock-predictor

⭐ 32 · TypeScript · 推送 2026-07-03 · [GitHub](https://github.com/sankeer28/stock-predictor) · [官网](https://stock-predictor-v2.vercel.app) · 个人维护

**股票分析与 ML 预测平台：多模型预测+技术面+情绪面+组合追踪**

基于 Node.js/Next.js 的股票分析 Web 应用：提供恐惧贪婪指数、市场涨跌榜、股票筛选器、K线图、RSI/MACD 指标、成交量分布、交易信号、图表形态检测、期权链、内部人交易与国会议员交易追踪等。ML 预测通过 TensorFlow.js 在浏览器端运行 8 种算法（LSTM/GRU/CNN-LSTM/ARIMA/Prophet-Lite 等），另有分钟级日内集成预测引擎与基于规则的新闻/Reddit 情绪分析。AI 分析调用 Groq API 生成书面评级。运行需 Node.js 18+ 及 NewsAPI、Groq、Alpha Vantage 密钥。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 浏览器端 TensorFlow.js 运行 8 种预测算法并可缓存结果
- 日内集成预测引擎：四子模型加权投票并在线 mini-batch 再训练
- 规则式 NLP 情绪引擎（否定词、强度修饰、100+ 金融关键词）
- 形态检测（楔形/三角形/双顶/头肩等）与组合追踪、收益预测

## 适用场景

- 在浏览器中对个股做多模型价格预测与技术面分析
- 追踪新闻、Reddit 与 ApeWisdom 的个股情绪
- 管理个人股票组合并查看股息估算与长期收益预测

## 场景标签

`金融量化` · 领域:学习与行业

## 证据(README 行号)

> L81: Multi-model price forecasting panel supporting eight algorithms run client-side via TensorFlow.js:
> L101: Intraday ensemble prediction engine that runs continuously in the browser. Four sub-models (Trend, Momentum, Rever
> L119: Sends current stock data to the Groq API (Llama model) for a comprehensive written analysis covering valuation ver

## 星数曲线

```mermaid
xychart-beta
    title "sankeer28/stock-predictor 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 31 --> 33
    line [32, 32]
```

2026-10-18 32 → 2026-10-28 32（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `23c7026c0954` · [字段定义](../../DATASET.md)*
