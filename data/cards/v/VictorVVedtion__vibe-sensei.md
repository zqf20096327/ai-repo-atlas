# VictorVVedtion/vibe-sensei

⭐ 24 · TypeScript · MIT · 推送 2026-04-15 · [GitHub](https://github.com/VictorVVedtion/vibe-sensei) · [官网](https://jcti.rivercore.ai/) · 个人维护

**终端原生 AI 交易副驾驶：68 位历史投资大师陪练纸面交易**

基于 Bun + React Ink 的终端 AI 交易工具：用户获得确定分配的守护大师角色，在每次交易前进行 9 项风险检查与熔断，两位大师辩论后再确认下单。包含 10 个'幽灵警告'、反向测试引擎（盲文权益曲线）、30 天跨源情绪简报、以及基于 JSONL 事件与 LLM 编译 wiki 的持久知识库。默认纸面交易沙盒（10 万 USDT 起始资金），通过 CCXT 纸面模式执行，市场数据来自 Hyperliquid。支持 Google Gemini 免费层、OpenAI、Anthropic 等多种模型接入，需 Bun >= 1.3 运行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Pre-Trade Gate：9 项风险检查 + 熔断器 + ATR 止损建议
- 68 位历史大师守护者（5 稀有度、9 原型），守护者由用户 ID 确定性分配
- 10 个幽灵警告（SBF、Do Kwon 等）在重复同类错误时出现
- 持久知识库：JSONL 事件存储 + LLM 编译 wiki（6 种操作）

## 适用场景

- 在纸面交易沙盒中练习加密货币交易并获得风险提醒
- 回测 Livermore 等历史交易员策略并与自身对比
- 查询 30 天跨 Reddit/HN/Polymarket/YouTube 的情绪简报

## 场景标签

`金融量化` · 领域:学习与行业

## 证据(README 行号)

> L12: Vibe Sensei is a terminal-native AI trading copilot where historical legends — Buffett, Soros, Livermore, Graham, S
> L50: 1. You type `/buy BTC 50000`
> L130: |`/login`|3-way provider picker (Anthropic / OpenAI / Gemini) with PKCE OAuth|

## 星数曲线

```mermaid
xychart-beta
    title "VictorVVedtion/vibe-sensei 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 23 --> 25
    line [24, 24]
```

2026-10-18 24 → 2026-10-31 24（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `86e799ff5faf` · [字段定义](../../DATASET.md)*
