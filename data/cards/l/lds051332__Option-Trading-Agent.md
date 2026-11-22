# lds051332/Option-Trading-Agent

⭐ 32 · Python · 推送 2026-11-19 · [GitHub](https://github.com/lds051332/Option-Trading-Agent) · [官网](https://option.xdashan.top/) · 个人维护 · 中文 README

**美股短周期轮式策略决策台：给建议，不报单**

面向美股期权卖方的短周期轮式决策工具，支持持币卖 put（CSP/牛价差）与持股卖 covered call 两本账，DTE 3–9 天。流水线为筛选期权链→日历闸门（财报/FOMC 硬跳过）→事件侦察→结构化决策，用 yfinance 实时链与 Black-Scholes 估算 Delta，结合 VIX/SPY 市场状态、趋势与历史突破率给出保守/标准两档。LLM 用于检索日历外事件，无 API key 时回退启发式规则。提供 CLI 与 SSE 流式的 Web 端，持仓簿存 localStorage，明确不含下单功能。

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

- 持币卖 put 与持股卖 covered call 两本账共享同一条决策流水线
- 日历闸门：财报/FOMC 硬跳过，CPI/NFP/PCE 软标签
- LLM 搜索日历外事件缺口，无 key 时回退启发式
- 支持 DeepSeek/OpenAI/OpenAI 兼容端点，CLI 与 Web（SSE 流式）双形态

## 适用场景

- 卖出 3–9 天的现金担保 put 前做结构筛选
- 对已持股规划 covered call 并判断履约成本
- 对已开的 CSP/covered call 持仓获取 HOLD/CLOSE/ROLL 建议

## 场景标签

`金融量化` · 领域:学习与行业

## 证据(README 行号)

> L3: A short-dated US-equity **wheel desk**. It recommends. It does not send orders. Try it at https://option.xdashan.top
> L26: - The LLM searches fixed queries for off-calendar gaps (export controls, capex, lawsuits, …)
> L30: - Runs without an API key: event classification and the desk fall back to heuristics

## 星数曲线

```mermaid
xychart-beta
    title "lds051332/Option-Trading-Agent 星数(近 2 点)"
    x-axis ["2026-10-31", "2026-11-22"]
    y-axis "stars" 31 --> 33
    line [32, 32]
```

2026-10-31 32 → 2026-11-22 32（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-20 · 置信度 mid · 依据 README sha `df94a05ae067` · [字段定义](../../DATASET.md)*
