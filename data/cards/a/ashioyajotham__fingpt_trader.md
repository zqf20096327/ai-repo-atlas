# ashioyajotham/fingpt_trader

⭐ 30 · Python · NOASSERTION · 推送 2026-05-14 · [GitHub](https://github.com/ashioyajotham/fingpt_trader) · 个人维护

**Falcon-7B 情感驱动的加密货币量化交易系统**

基于 FinGPT 思想的量化交易平台：用经金融情感微调的 Falcon-7B 模型分析财经新闻，按 60% 置信度加 40% 情感强度的加权评分生成交易信号，结合 RSI/均线等技术指标检测市场低效，异步架构处理行情事件，对接 Binance 测试网执行。README 明确声明仍处早期开发、不适用于实盘，多项功能（最小下单量、回测框架、VaR）为部分实现或规划中。运行需 Python 3.8+、8GB 以上内存与多个 API key。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | `idea` | |

## 能力要点

- Falcon-7B 金融情感模型与置信度加权评分（60/40）
- 情感-价格相关性追踪以调节信号强度
- 异步事件驱动架构与 Binance 测试网集成
- YAML 分层配置（trading/strategies/model/services）

## 适用场景

- 在 Binance 测试网上研究 LLM 情感信号与技术指标结合的交易策略
- 复现 FinGPT 思路在量化交易中的实验
- 学习异步事件驱动的交易系统架构

## 场景标签

`金融量化` · 领域:学习与行业

## 证据(README 行号)

> L3: A quantitative trading system that combines Falcon-7B language model-driven sentiment analysis with technical market
> L9: - **Falcon-7B Model**: Fine-tuned for financial sentiment analysis
> L22:  - ✅ Falcon-7B financial sentiment model implementation

## 星数曲线

```mermaid
xychart-beta
    title "ashioyajotham/fingpt_trader 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 29 --> 31
    line [30, 30]
```

2026-10-18 30 → 2026-10-27 30（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `0251f2e6d472` · [字段定义](../../DATASET.md)*
