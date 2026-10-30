# LuciferForge/polymarket-btc-autotrader

⭐ 20 · Python · 推送 2026-03-14 · [GitHub](https://github.com/LuciferForge/polymarket-btc-autotrader) · [官网](https://protodex.io) · 个人维护

**面向 Polymarket 的 BTC/SOL 15 分钟自动交易机器人**

在 Polymarket CLOB 上执行真实交易的自动化机器人：每 60 秒扫描 BTC 与 SOL 的 15 分钟预测市场，运行 SNIPE（第 13-14.5 分钟以 $0.93-$0.97 买入近确定方向）与 ARB（YES+NO 合计低于 $0.985 时双边买入）两种策略，通过 py-clob-client 下单，用 SQLite 记录 P&L，链上自动赎回已结算仓位。每笔决策经 ai-decision-tracer 生成 Ed25519 签名、哈希链式收据，可用 audit 命令校验。README 声明的胜率（17W/1L）为作者自述的实盘记录，未经核验。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- SNIPE 与 ARB 双策略，每 60 秒扫描下单
- Ed25519 签名、哈希链式交易收据，audit 命令可校验
- SQLite P&L 数据库与链上自动赎回已结算仓位
- Binance 价格源 + EV 计算器架构

## 适用场景

- 在 Polymarket 15 分钟 BTC/SOL 市场自动执行套利与尾盘策略
- 需要可验证交易记录（签名收据）的自动化交易
- 自动赎回已结算仓位并跟踪盈亏

## 场景标签

`金融量化` · 领域:学习与行业

## 证据(README 行号)

> L3: Autonomous BTC & SOL 15-minute trader for Polymarket. Finds edges, places orders, tracks P&L.
> L58: Every trade decision is recorded as an Ed25519-signed, hash-chained receipt via ai-decision-tracer. Each receipt co

## 星数曲线

```mermaid
xychart-beta
    title "LuciferForge/polymarket-btc-autotrader 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 19 --> 21
    line [20, 20]
```

2026-10-18 20 → 2026-10-30 20（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 mid · 依据 README sha `51b9101f8bbd` · [字段定义](../../DATASET.md)*
