# lds051332/OptionTradingAgent

⭐ 31 · Python · 推送 2026-09-28 · [GitHub](https://github.com/lds051332/OptionTradingAgent) · [官网](https://option.xdashan.top/) · 个人维护 · 中文 README

**美股短周期轮式策略（卖put/covered call）决策建议台，只给建议不下单**

面向美股期权个人交易者的短周期（DTE 3–9 天）轮式策略决策工具：持币筛选现金担保 put / 牛市 put 价差，持股筛选 covered call。流水线为：拉取 yfinance 实时期权链、估算 Delta 分两档（约0.10Δ/0.20Δ）、比较 ATM IV 与已实现波动率、日历闸门（财报/FOMC 硬跳过）、LLM 搜索财报外事件，输出 SKIP/OPEN 及合约建议。LLM 可选（DeepSeek/OpenAI/兼容端点），无 API key 时回退启发式；HOLD/CLOSE/ROLL 位置管理为纯规则，无 LLM 参与。提供 CLI 与本地/云端 Web（SSE 流式、Docker Compose 单容器），明确不做经纪下单与多用户。持仓记录仅存浏览器 localStorage。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `none` | — |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- yfinance 实时期权链 + Black-Scholes 估算 Delta，双档（conservative/standard）筛选
- 财报/FOMC 在持有窗口内硬跳过，VIX/SPY/QQQ 市况为减仓信号
- LLM 可选（DeepSeek/OpenAI/兼容端点），无 key 时回退启发式规则
- Web 端 SSE 流式输出与可选持仓管理（HOLD/CLOSE/ROLL，localStorage 存储）

## 适用场景

- 持币时筛选 3–9 天 DTE 的现金担保 put 开仓建议
- 已持股时获取 covered call 卖出建议与到期 P/L 图
- 记录已成交的 CSP/covered call 并实时估值、获得 HOLD/CLOSE/ROLL 建议

## 场景标签

`金融量化` · 领域:学习与行业

## 证据(README 行号)

> L19: - Pulls a **live option chain** from yfinance and **estimates** put / call Delta with chain IV + Black-Scholes (not
> L25: - The LLM searches fixed queries for off-calendar gaps (export controls, capex, lawsuits, …)
> L26: - The desk may only emit `SKIP | OPEN` plus structure plus bucket plus a **`contract_id` already in that bucket**

## 星数曲线

```mermaid
xychart-beta
    title "lds051332/OptionTradingAgent 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 30 --> 32
    line [31, 31]
```

2026-10-18 31 → 2026-10-26 31（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 mid · 依据 README sha `94313ea5936f` · [字段定义](../../DATASET.md)*
