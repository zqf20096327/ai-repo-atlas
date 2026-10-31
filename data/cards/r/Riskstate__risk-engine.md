# Riskstate/risk-engine

⭐ 14 · 推送 2026-09-10 · [GitHub](https://github.com/Riskstate/risk-engine) · [官网](https://riskstate.ai) · 组织维护

**面向加密交易 agent 的盘前风险 API：BTC/ETH 敞口治理**

RiskState 提供托管 REST API，将 30+ 实时信号（价格与衍生品、链上、宏观、DeFi 健康度、情绪）转化为动态风险权限：最大仓位比例、杠杆上限、允许/禁止动作与结构性阻断项，每 60 秒更新。评估以美元计价，仅覆盖 BTC/USD 与 ETH/USD。输出按固定优先级约束 agent 行为（结构阻断优先于仓位/杠杆）。支持现货、永续合约与 DeFi 借贷场景，另提供 SKILL.md 与 MCP Server 接入方式。定价分层，beta 期间免费，限 60 请求/分钟。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 一次 API 调用返回 30+ 信号计算出的仓位上限、杠杆上限与允许动作
- 5 级风险策略（BLOCK Survival 到 GREEN Expansion）与结构阻断熔断
- 兼容 Claude Code/Copilot/Cursor/Gemini 的 SKILL.md 与 MCP Server 接入
- 数据源覆盖 Binance/OKX/Bybit、FRED、Aave V3、Spark Protocol 等

## 适用场景

- AI 交易 agent 在下单前调用 API 获取动态仓位与杠杆上限
- 量化交易系统在执行订单前做盘前风险检查
- DeFi 借贷场景按钱包健康因子获取清算感知的风险限额

## 场景标签

`金融量化` · 领域:学习与行业

## 证据(README 行号)

> L18: A deterministic engine that converts live market state into **dynamic risk permissions** — exposure limits, leverag
> L67: **In an AI trading agent (Python):**
> L129: Drop `SKILL.md` into your agent's repo. Compatible with Claude Code, Copilot, Cursor, and Gemini via skills.sh.

## 星数曲线

```mermaid
xychart-beta
    title "Riskstate/risk-engine 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 mid · 依据 README sha `3dbdccf95f19` · [字段定义](../../DATASET.md)*
