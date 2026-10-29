# maghdam/chatgpt-trading-strategy-assistant

⭐ 42 · Python · MIT · 推送 2026-09-14 · [GitHub](https://github.com/maghdam/chatgpt-trading-strategy-assistant) · 个人维护

**ChatGPT 交易助手后端：经 cTrader API 分析行情并下单记账**

基于 FastAPI 的后端服务，通过 ChatGPT Custom GPT Actions 作为交易者的对话界面：从 cTrader Open API 拉取实时 OHLC 数据，运行默认的 Smart Money Concepts（SMC）多时间框架结构化分析（CHOCH/BOS/订单块/FVG/加权共振评分），支持市价/限价/止损单下单、查询持仓与挂单，并可把交易记录写入 Notion。仓库定位为可复用模式：保留连接与执行管道，替换策略层即可适配 EMA、RSI 背离、突破等其他策略。自述为教学与实验性软件，建议先在模拟盘验证。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- /analyze 返回结构化多时间frame分析（HTF_Bias/Checklist/Confluence），供 GPT 直接引用而非自行推导
- 通过 /place-order 在 cTrader 下市价、限价、止损单，支持外汇、指数与股票
- 策略层与管道分离：替换 analysis.py、GPT 指令与 Action schema 即可适配其他策略
- 含冒烟测试脚本（仅用标准库）验证 /health、/fetch-data、/analyze

## 适用场景

- 在 ChatGPT 里用自然语言分析行情、下单并记录交易日志
- 以 SMC 原型为基础替换策略层，构建自己的策略专属交易助手
- 把交易 setup 自动 journal 到 Notion 做复盘

## 场景标签

`金融量化` · 领域:学习与行业

## 证据(README 行号)

> L3: A ChatGPT-powered trading assistant backend for cTrader that can analyze markets, journal setups, and place trades t
> L8: - use FastAPI as the action backend
> L24: 1. a ChatGPT Custom GPT with Actions

## 星数曲线

```mermaid
xychart-beta
    title "maghdam/chatgpt-trading-strategy-assistant 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-27", "2026-10-29"]
    y-axis "stars" 40 --> 43
    line [41, 42, 42]
```

2026-10-18 41 → 2026-10-29 42（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `4a0bfaf940ee` · [字段定义](../../DATASET.md)*
