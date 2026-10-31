# DoRmAmMu1997/My-Algo-Trading-Code

⭐ 15 · Python · MIT · 推送 2026-10-30 · [GitHub](https://github.com/DoRmAmMu1997/My-Algo-Trading-Code) · 个人维护

**印度指数期权个人算法交易套件：信号、回测、纸面/实盘与可选 AI 代理**

面向印度 NIFTY/BANKNIFTY/FINNIFTY 指数期权的个人交易代码库：包含历史数据提取器、信号生成器、回测脚本，以及用多线程同时执行约 28 个策略的 Front Test 运行器；经 Dhan API 获取行情，实盘下单可选 Kotak Neo/Shoonya/Flattrade/Dhan，由全局 kill-switch 与逐策略纸面/实盘开关（默认纸面）管控，并带崩溃恢复与 Telegram 告警。AI 部分为两个默认关闭的可选代理：Claude 驱动的 SL Hunting 代理与 Codex 驱动的 CPR Trend-Day Rider（仅可接受/否决主机信号，不可反向）。实盘结果以外部表格记录。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 多线程运行器并行执行约 28 个策略，支持纸面/实盘双门控
- 实盘经纪商四选一（Kotak Neo/Shoonya/Flattrade/Dhan），默认纸面交易
- 可选 Claude SL Hunting 代理与 Codex CPR 代理（默认关闭、fail-soft、只可接受或否决）
- python algo.py backtest 可在 5 年数据上重放策略引擎

## 适用场景

- 在印度指数期权上并行运行多策略并做回测验证
- 先用纸面模式验证策略再受控切换实盘
- 让 AI 代理按既定规则接受或否决主机给出的交易信号

## 场景标签

`金融量化` · 领域:学习与行业

## 证据(README 行号)

> L13: - Data extractors which extract historical data for NIFTY/BANKNIFTY/FINNIFTY indices
> L17: - Live order execution to a real broker — selectable among **Kotak Neo**, **Shoonya (Finvasia)**, **Flattrade Pi v2
> L19: - An **optional, opt-in LLM trading agent** — the "SL Hunting AI Agent" — a Claude agent that trades a discretionar
> L21: - An optional **CPR Codex AI Agent** running the **Trend-Day Rider**: a backtested host gate flags midday trend-day

## 星数曲线

```mermaid
xychart-beta
    title "DoRmAmMu1997/My-Algo-Trading-Code 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-31 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 mid · 依据 README sha `08882d8866ad` · [字段定义](../../DATASET.md)*
