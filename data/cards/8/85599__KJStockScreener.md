# 85599/KJStockScreener

⭐ 12 · Python · MIT · 推送 2026-10-21 · [GitHub](https://github.com/85599/KJStockScreener) · [官网](https://kjstockscreener.streamlit.app/) · 个人维护

**面向 NSE 印度股市的 AI 选股器：突破扫描+AI 交易代理**

基于 Python + Streamlit 的印度国家证券交易所（NSE）股票筛选应用，核心为多线程技术面筛选引擎（突破、盘整、RSI、均线交叉、K线形态），并内置对话式 AI 交易代理（基于 openai-agents，支持 OpenAI/Anthropic/Groq 及任意 OpenAI 兼容端点，自带 5 个交易人格）、实时 NSE 期权链查看器、基于 ML 的 Nifty 跳空预测器，以及从 screener.in 抓取基本面的 LedgerLens 浏览器。需自备 LLM API key；需 Python 3.13；提供 Docker 镜像与在线演示。声明为研究教育工具，不构成投资建议。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 多线程技术面筛选引擎：突破/盘整/RSI/均线交叉/K线形态
- 对话式 AI 交易代理，5 个内置交易人格，支持定时自动扫描
- 实时 NSE 期权链（NIFTY/BANKNIFTY/F&O）与 TradingView 跳转
- LedgerLens 从 screener.in 抓取完整财务数据，导出 CSV/JSON/Excel/ZIP

## 适用场景

- 扫描 NSE 各指数的突破与盘整待突破股票
- 用自然语言让 AI 代理代为执行筛选策略
- 盘中查看 NIFTY/BANKNIFTY 实时期权链
- 查询某公司完整基本面与同行对比并导出数据

## 场景标签

`金融量化` · 领域:学习与行业

## 证据(README 行号)

> L3: ### AI-Native Stock Screener for the Indian Stock Market (NSE)
> L26: **KJStockScreener** is a Python + Streamlit screener for **NSE (India)** stocks that goes beyond a typical breakout
> L42: - A conversational chat tab (OpenWebUI-style UI) backed by `openai-agents` — talk to your screener instead of click

## 星数曲线

```mermaid
xychart-beta
    title "85599/KJStockScreener 星数(近 6 点)"
    x-axis ["2026-10-19", "2026-10-27", "2026-11-06", "2026-11-08", "2026-11-21", "2026-11-22"]
    y-axis "stars" 9 --> 13
    line [10, 11, 10, 11, 12, 12]
```

2026-10-19 10 → 2026-11-22 12（+2）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-19 · 置信度 high · 依据 README sha `6abf7c9d000a` · [字段定义](../../DATASET.md)*
