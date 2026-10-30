# dexoryn-china/polymarket-arbitrage-bot

⭐ 42 · Python · 推送 2026-09-29 · [GitHub](https://github.com/dexoryn-china/polymarket-arbitrage-bot) · 个人维护 · 中文 README

**Polymarket 预测市场自主 AI 交易代理：发现、研究、预测、风控、执行**

面向 Polymarket 预测市场的自主交易代理，运行完整闭环：通过 Gamma API 扫描市场并按正则分类，按类别做站点限定搜索与 HTML 提取搜集证据，用 GPT-4o/Claude/Gemini 三模型加权集成预测概率（Platt 缩放与 Brier 分数校准），经 15+ 项风控检查（Kelly 仓位、回撤热度、流动性/价差过滤、巨鲸信号 Edge 调整）后执行交易。默认模拟交易，实盘需三道独立解锁。提供 Flask 仪表盘（端口 2345）、SQLite 审计链、Telegram/Discord/Slack 告警。需 OpenAI 与 SerpAPI 密钥，支持 Docker 运行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 三模型 LLM 集成预测概率，含 Platt 缩放与结算后自动重训校准
- 15+ 项交易前风控检查与三重模拟门（默认 Paper Trading）
- 巨鲸钱包扫描与 Edge 加成/惩罚集成
- 9 标签页实时仪表盘与 SHA-256 决策审计链

## 适用场景

- 在 Polymarket 上跑自动化的研究—预测—下单闭环
- 模拟模式下先验证预测与风控策略再切实盘
- 追踪聪明钱钱包并对照模型预测调整仓位

## 场景标签

`金融量化` · 领域:学习与行业

## 证据(README 行号)

> L3: 面向 Polymarket 预测市场的自主交易代理。自动发现市场、搜集证据、通过多模型 AI 集成预测概率，并在严格风控下执行交易。
> L19: - **独立预测** — 三模型 LLM 集成（GPT-4o、Claude、Gemini）估算概率，不锚定当前市场价格

## 星数曲线

```mermaid
xychart-beta
    title "dexoryn-china/polymarket-arbitrage-bot 星数(近 2 点)"
    x-axis ["2026-10-23", "2026-10-30"]
    y-axis "stars" 41 --> 43
    line [42, 42]
```

2026-10-23 42 → 2026-10-30 42（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `25e080e17db1` · [字段定义](../../DATASET.md)*
