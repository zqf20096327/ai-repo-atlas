# jaredzwick/polymarket-trading-bot

⭐ 26 · TypeScript · MIT · 推送 2026-07-07 · [GitHub](https://github.com/jaredzwick/polymarket-trading-bot) · 个人维护

**面向 Polymarket 预测市场的可插拔量化交易机器人框架**

TypeScript + Bun 编写的 Polymarket 预测市场交易机器人：内置事件驱动引擎、真实/模拟 CLOB 客户端（默认 dry-run 不下真实订单）、风险管理（仓位/敞口上限、日亏损熔断）、SQLite 持久化与 WebSocket 实时 React 面板。提供 market-maker、momentum、mean-reversion、bregman-arb 四个策略，新策略约 30 行代码（实现 evaluate() 返回信号）。README 未展示 AI/模型相关功能，策略为规则化算法。给具备 TypeScript 能力、在 Polymarket 上做程序化交易的开发者使用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 真实 + 模拟 CLOB 客户端，默认 dry-run 零配置运行
- 风险管理：仓位上限、总敞口上限、日亏损熔断
- 内置 4 个生产策略，自定义策略约 30 行
- SQLite 持久化订单与持仓 + WebSocket 实时面板

## 适用场景

- 在 Polymarket 上跑做市、动量、均值回归等策略
- 先用 dry-run 模拟验证策略再接真实资金
- 作为框架扩展自己的交易信号逻辑

## 场景标签

`金融量化` · 领域:学习与行业

## 证据(README 行号)

> L66: |Strategy|Description|Signals on|
> L68: |`market-maker`|Places limit orders on both sides of the book to capture spread|Inventory skew + spread|
> L70: |`mean-reversion`|Trades against extreme price moves via z-score|Z-score of rolling mean/stddev|

## 星数曲线

```mermaid
xychart-beta
    title "jaredzwick/polymarket-trading-bot 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 25 --> 27
    line [26, 26]
```

2026-10-18 26 → 2026-10-27 26（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 low · 依据 README sha `05a97c2fe69b` · [字段定义](../../DATASET.md)*
