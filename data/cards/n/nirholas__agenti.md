# nirholas/agenti

⭐ 81 · TypeScript · NOASSERTION · 推送 2026-10-26 · [GitHub](https://github.com/nirholas/agenti) · [官网](https://agenti.cash) · 个人维护

**给 AI agent 配加密钱包的支付 SDK 与 MCP 服务器**

面向开发者的 agent 支付基础设施：以 TypeScript SDK 提供 EVM+Solana 钱包生成、x402 协议付费（服务端返回 402 时自动支付重试）、收款开票与余额查询；同时提供 MCP 服务器，使 Claude、Cursor、Windsurf 等 MCP 客户端以工具形式调用支付能力，无需写代码。支持 LangChain、AutoGen、CrewAI、Vercel AI SDK、ElizaOS 等框架集成，并附基于 pump.fun SDK 的 Solana 交易示例。注意：npm 包尚未发布，安装命令当前 404，需从源码 clone 构建。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 一行 agent.pay() 实现 x402 自动付费（402 状态码触发支付重试）
- MCP 服务器提供 create_wallet/pay/create_invoice/check_payment 等工具
- 覆盖 EVM 与 Solana（集成 pump.fun Agent Payments 程序）
- 5 个可运行的 Solana 代币买卖教程示例

## 适用场景

- 让我的 agent 自主为付费 API 付费并获取数据
- 给 Claude/Cursor 等 MCP 客户端加上钱包工具
- agent 之间收款、开票与链上到账核验

## 场景标签

 · 领域:AI agent 支付基础设施/加密货币

## 证据(README 行号)

> L26: - **An SDK** so developers can give any agent financial capability in minutes — LangChain agents, AutoGen pipelines
> L27: - **An MCP server** so Claude, Cursor, Windsurf, and any MCP-compatible client can use money as a native tool witho
> L91: The `@agenti/mcp` package turns every tool in the SDK into an MCP tool that any LLM client can call — no code requi

## 星数曲线

```mermaid
xychart-beta
    title "nirholas/agenti 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-24", "2026-10-28"]
    y-axis "stars" 79 --> 82
    line [80, 81, 81]
```

2026-10-18 80 → 2026-10-28 81（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `9cf4b784b754` · [字段定义](../../DATASET.md)*
