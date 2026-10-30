# ryan-yuuu/crypto-trading-arena

⭐ 130 · Python · Apache-2.0 · 推送 2026-07-08 · [GitHub](https://github.com/ryan-yuuu/crypto-trading-arena) · 个人维护

**多 AI agent 加密货币交易竞技场：接入实时行情自主交易**

基于 calfkit SDK 构建的多 agent 加密货币交易竞技场：交易所连接器将 Coinbase 或 Binance 的实时行情转为事件流，每个 agent 内嵌自己的 LLM 客户端，基于最新价格与 K 线推理后自主调用工具（下单、查持仓、计算器）执行买卖。提供仪表盘、响应查看器、CSV 交易与持仓快照记录；每个 agent 可选用不同模型与提供商。运行需 Python 3.10+、uv、Docker（本地 Kafka broker）与 LLM API key；Binance 连接器标注为实验性。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 交易所连接器将实时行情以事件流形式扇出给所有 agent
- 每个 agent 内嵌独立模型客户端，可用不同 LLM 与提供商
- 交易、持仓快照自动记录为 CSV（价格、费用、P&L）
- 共享交易工具集经 ToolContext 在运行时识别调用 agent 身份

## 适用场景

- 让多个 LLM agent 在真实加密行情下互相竞技交易
- 观察与记录不同模型/策略的自主交易表现
- 作为 calfkit 事件驱动多 agent 系统的参考实现

## 场景标签

`多智能体` `金融量化` · 领域:Agent 开发

## 证据(README 行号)

> L9: A multi-agent crypto trading arena where AI agents compete against each other, trading with live crypto market data 
> L38: - **Per-agent model selection**: Each agent embeds its own model client, so different agents can use different LLMs
> L124: Deploy an agent with an embedded model client and a trading strategy. Each agent runs its own LLM inference. See `

## 星数曲线

```mermaid
xychart-beta
    title "ryan-yuuu/crypto-trading-arena 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 129 --> 131
    line [130, 130]
```

2026-10-18 130 → 2026-10-30 130（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `79b9772b9d40` · [字段定义](../../DATASET.md)*
