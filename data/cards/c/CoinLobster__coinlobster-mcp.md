# CoinLobster/coinlobster-mcp

⭐ 14 · JavaScript · MIT · 推送 2026-10-15 · [GitHub](https://github.com/CoinLobster/coinlobster-mcp) · [官网](https://coinlobster.com/connect) · 组织维护

**加密市场数据 MCP 服务器：向 AI 提供鲸鱼交易与链上数据**

MCP 服务器，为 Claude、ChatGPT、Cursor 等 AI 客户端提供加密货币市场数据：18 个交易所的鲸鱼成交、Ethereum/Base/Arbitrum DEX 交换、Hyperliquid 账户持仓、清算、资金费率与未平仓合约，以及带失误记录的信号历史。数据为描述性，不提供预测或建议。以托管 HTTP 连接器为主，另有本地 stdio 中继包（npx 运行，转发至托管服务，本地不存储数据）。免费档无账号可查询 30 分钟前的数据，付费档提供实时数据与告警。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 18 个交易所鲸鱼成交与 3 条链 DEX 交换数据
- 本地 stdio 中继包转发至托管服务，新工具无需更新
- 每个历史信号附带事后价格表现与失误记录
- 无需 API key 即可用（数据延迟 30 分钟）

## 适用场景

- 向 AI 助手询问加密市场当前的鲸鱼活动与清算情况
- 查询 Hyperliquid 账户的持仓与清算价格
- 让 AI 设置市场异动 webhook 告警（付费档）

## 场景标签

`金融量化` · 领域:学习与行业

## 证据(README 行号)

> L1: # CoinLobster MCP · live crypto market data for your AI
> L35: For clients that only speak stdio. It relays to the hosted server, including its tools, prompts, resources and inst

## 星数曲线

```mermaid
xychart-beta
    title "CoinLobster/coinlobster-mcp 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `513735426592` · [字段定义](../../DATASET.md)*
