# snowfluke/sentimeter

⭐ 23 · TypeScript · MIT · 推送 2026-04-28 · [GitHub](https://github.com/snowfluke/sentimeter) · [官网](https://sentimeter.my.id) · 个人维护

**印尼股市情绪选股机器人：AI 分析新闻生成每日买入建议**

面向印尼证券交易所（IHSG/IDX）个人投资者的情绪选股系统：爬取 14 个印尼财经门户新闻，经 Google Gemini 提取股票代码并打情绪/相关度分，从 Yahoo Finance 拉取行情与基本面数据，计算 SMA/ATR/支撑阻力等技术指标后生成含入场价、止损、目标价与持有天数的买入建议（总分≥65 且 BUY 才保存），并跟踪预测状态。LLM 调用经本地 Antigravity Manager 代理路由到 Gemini，需 Bun 运行时，附 REST API 与 React 面板，每日定时运行两次。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 爬取 14 个印尼财经门户新闻，Gemini 提取代码并打情绪/相关度分
- 生成含入场价、止损、目标价、持有天数与四类评分的 BUY 建议
- 预测状态跟踪（pending/entry_hit/target_hit/sl_hit/expired）
- REST API + React 面板 + SSE 实时日志，每日两次定时分析

## 适用场景

- 每天开盘前获取印尼股市的 AI 买入建议与价格计划
- 跟踪历史推荐的命中情况与盈亏状态
- 在自建面板上查看推荐与触发手动分析

## 场景标签

`金融量化` · 领域:学习与行业

## 证据(README 行号)

> L3: A sentiment-based stock trading bot for the Indonesian Stock Exchange (IHSG/IDX). Sentimeter crawls financial news f
> L13: - AI-Powered Analysis: Uses Google Gemini to extract stock tickers and analyze sentiment

## 星数曲线

```mermaid
xychart-beta
    title "snowfluke/sentimeter 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 22 --> 24
    line [23, 23]
```

2026-10-18 23 → 2026-10-28 23（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 mid · 依据 README sha `80d30970a202` · [字段定义](../../DATASET.md)*
