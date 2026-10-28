# PredictionMarketTrader/openthomas

⭐ 25 · Python · MIT · 推送 2026-09-12 · [GitHub](https://github.com/PredictionMarketTrader/openthomas) · [官网](https://openthomas.com) · 组织维护

**自主交易气象预测市场的 AI agent（Kalshi/Polymarket）**

在 Kalshi 与 Polymarket 上交易每日站点气温预测市场的自主 AI agent：按结算站点聚合七个 NWP 模型形成逐 strike 概率，通过无泄漏 hindcast 学习各站点系统偏差，LLM 集成仅在硬边界内调整统计基线，并以 fractional Kelly 与风险限额管理仓位。默认纸面交易模式无需钱包与交易所密钥，交易日志、校准与规则手册存储于本地 SQLite。风险管理在 LLM 之外的确定性代码中执行，支持 Ollama/vLLM 等本地模型与 MCP 客户端调用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 七模型 NWP 共识 + 站点偏差学习生成逐 strike 概率，LLM 仅在基线 ±0.15 内调整
- fractional Kelly 仓位与确定性风险引擎（限额、回撤熔断、longshot 过滤）
- 默认纸面交易模拟真实订单簿，无需钱包或交易所 API key
- 提供 MCP 服务器供 Claude 等 MCP 客户端调用，hindcast/replay/report/publish 等 CLI 子命令

## 适用场景

- 纸面模式下观察 agent 在 Kalshi/Polymarket 气温市场的交易行为
- 用本地模型（Ollama/vLLM）跑预测与反思节点避免 API 费用
- 通过 MCP 让 Claude 等 agent 提案交易并由风险引擎约束

## 场景标签

`金融量化` · 领域:学习与行业

## 证据(README 行号)

> L7: **An autonomous AI agent that trades weather markets on Kalshi and Polymarket. It knows the exact NWS station each m
> L42: |**Weather baseline**|Seven independent NWP models — including our own **GraphCast** point forecast and **GenCast**
> L43: |**Forecast engine**|LLM ensemble (median of N independent estimates), grounded in resolution rules and base rates 

## 星数曲线

```mermaid
xychart-beta
    title "PredictionMarketTrader/openthomas 星数(近 4 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-24", "2026-10-28"]
    y-axis "stars" 22 --> 26
    line [23, 24, 25, 25]
```

2026-10-18 23 → 2026-10-28 25（+2）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `13a6494ce101` · [字段定义](../../DATASET.md)*
