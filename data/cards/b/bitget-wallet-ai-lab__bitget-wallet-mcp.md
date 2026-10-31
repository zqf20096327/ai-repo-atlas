# bitget-wallet-ai-lab/bitget-wallet-mcp

⭐ 18 · Python · MIT · 推送 2026-04-16 · [GitHub](https://github.com/bitget-wallet-ai-lab/bitget-wallet-mcp) · [官网](https://web3.bitget.com) · 组织维护

**把 Bitget Wallet 链上 API 暴露为 AI agent 工具的 MCP 服务器**

由 Bitget Wallet AI Lab 维护的 MCP (Model Context Protocol) 服务器，将 Bitget Wallet 链上 API 封装为 39 个供 AI agent 调用的工具，覆盖市场数据（代币信息、K线、持仓人分析、安全审计）、聪明钱地址发现、RWA 股票交易、跨 11 条链的代币兑换与转账、批量余额查询。面向通过 Claude Desktop、Cursor、Windsurf 等 MCP 客户端使用 AI agent 的开发者。pip 源码安装后运行 server.py，无需 API key（SHA256 签名），仅与单一 API 端点通信，依赖仅 requests 与 mcp。

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

- 39 个工具：21 市场数据 + 聪明钱 + 6 RWA 股票 + 7 Swap + 3 转账 + 余额
- 支持 Ethereum/Solana/BNB 等 11 条链的兑换、转账与 gasless 转账
- 无需 API key，SHA256 哈希签名认证
- 支持 Claude Desktop / Cursor / Windsurf 的 MCP 配置

## 适用场景

- 让 AI agent 查询代币行情、持仓人与安全审计数据
- 通过 agent 执行跨链 swap 与代币转账
- 查询多链代币余额与 RWA 股票持仓

## 场景标签

`数据分析` · 领域:效率与自动化

## 证据(README 行号)

> L3: An MCP (Model Context Protocol) server that exposes Bitget Wallet on-chain API as tools for AI agents.
> L100: ## Tools (39)

## 星数曲线

```mermaid
xychart-beta
    title "bitget-wallet-ai-lab/bitget-wallet-mcp 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 17 --> 19
    line [18, 18]
```

2026-10-18 18 → 2026-10-31 18（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `5f369f4e45c1` · [字段定义](../../DATASET.md)*
