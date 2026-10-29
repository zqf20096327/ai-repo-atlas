# caiovicentino/hyperliquid-mcp-server

⭐ 36 · Python · MIT · 推送 2025-11-10 · [GitHub](https://github.com/caiovicentino/hyperliquid-mcp-server) · 个人维护

**连接 Claude Desktop 与 Hyperliquid DEX 的 MCP 服务器**

基于 Python 的 Model Context Protocol 服务器，让 Claude Desktop 通过自然语言操作 Hyperliquid 去中心化交易所：提供 27 个工具，覆盖下单/批量/TWAP 交易、仓位与账户管理、行情数据（L2 订单簿、K线、资金费率）与 WebSocket 实时订阅，并含死手开关安全机制。用户自持私钥，凭据存于 .env，支持 testnet/mainnet 切换。安装方式为 git clone 后运行 setup.py 自动脚本，自动配置 Claude Desktop。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 27 个 MCP 工具分 4 类：交易、账户管理、行情数据、WebSocket 订阅
- 自然语言下单、撤单、调杠杆与批量网格交易
- dead man's switch 超时自动撤销全部挂单
- testnet/mainnet 可切换，凭据经 .env 管理

## 适用场景

- 在 Claude Desktop 里用自然语言交易 Hyperliquid 永续合约
- 实时监控订单簿、成交与账户仓位
- 通过 Claude 执行批量网格与 market making 策略

## 场景标签

`金融量化` · 领域:学习与行业

## 证据(README 行号)

> L18: O **Hyperliquid MCP Server** é uma implementação completa do Model Context Protocol (MCP) da Anthropic que permite 
> L28: **Model Context Protocol (MCP)** é um padrão criado pela Anthropic para conectar assistentes de IA (como Claude) a 

## 星数曲线

```mermaid
xychart-beta
    title "caiovicentino/hyperliquid-mcp-server 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 35 --> 37
    line [36, 36]
```

2026-10-18 36 → 2026-10-29 36（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `5206d8c73092` · [字段定义](../../DATASET.md)*
