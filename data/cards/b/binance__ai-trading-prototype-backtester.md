# binance/ai-trading-prototype-backtester

⭐ 65 · Python · MIT · 推送 2026-04-16 · [GitHub](https://github.com/binance/ai-trading-prototype-backtester) · 组织维护

**情绪分析加密货币交易策略的回测器，配套实盘机器人**

Binance 维护的开源回测工具，为配套实盘项目 ai-trading-prototype 提供历史模拟：按 K 线间隔读取标题情绪数据（CSV），依据 bullish/bearish 信号执行买卖，输出结果表、逐笔交易明细与 HTML/PNG 交易可视化。支持自定义策略构建、三种风险档位配置（激进/保守/标准）、手续费与仓位上限设置，并通过 data.binance.vision 自动下载行情数据。需用户提供符合指定格式的情绪数据文件；README 附风险免责声明。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 按 K 线间隔读取标题情绪 CSV 并模拟买卖
- 输出结果表、逐笔明细与 HTML/PNG 交易可视化
- 自动从 data.binance.vision 下载行情数据
- 内置激进/保守/标准三种风险档位策略配置

## 适用场景

- 回测基于新闻情绪的加密货币交易策略
- 对比不同风险参数下策略的历史表现
- 为 ai-trading-prototype 实盘机器人做策略验证

## 场景标签

`金融量化` · 领域:学习与行业

## 证据(README 行号)

> L3: This project is a backtester for the sentiment-analysis cryptocurrency trading strategy that pairs with the live tra
> L61: * During the backtesting process, the backtester checks `/sentiment_data/sentiment_data.csv` for a published headli
> L62: * If a headline was published during the current time-period, it reads the sentiment of the headline.

## 星数曲线

```mermaid
xychart-beta
    title "binance/ai-trading-prototype-backtester 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 64 --> 66
    line [65, 65]
```

2026-10-18 65 → 2026-10-30 65（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 mid · 依据 README sha `f7227934d3dd` · [字段定义](../../DATASET.md)*
