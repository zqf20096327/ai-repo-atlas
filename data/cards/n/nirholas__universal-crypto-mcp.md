# nirholas/universal-crypto-mcp

⭐ 44 · TypeScript · NOASSERTION · 推送 2026-10-25 · [GitHub](https://github.com/nirholas/universal-crypto-mcp) · [官网](https://mcp.giving) · 个人维护

**让 AI agent 通过自然语言操作区块链的通用 MCP 服务器**

面向 EVM 兼容网络及 Solana、Cosmos、Near、Sui、Aptos 等链的 Model Context Protocol 服务器，使 Claude、ChatGPT、Cursor 等 AI agent 以自然语言执行代币兑换（1inch/0x/ParaSwap）、跨链桥、质押、借贷、合约部署、安全检测（蜜罐/Rug pull/GoPlus）、行情与 DeFi 分析等 380+ 工具操作。整合 10+ 个 MIT 许可的社区 MCP 项目，支持 stdio/HTTP/SSE 三种传输模式，通过 npx 运行。含 x402 支付协议实现，agent 可用 USDs 稳定币自动支付 API 费用并获取收益；涉及真实资金操作，需配置私钥环境变量。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 380+ 工具覆盖兑换/桥/质押/借贷/治理/合约部署等链上操作
- 支持 20+ 条 EVM 链及 Cosmos、Near、Sui、Aptos、Solana 等多链
- x402 支付协议：agent 持有钱包自动支付 API 费用（14 个工具）
- 整合 10+ 个社区 MIT 项目并保留原许可与署名

## 适用场景

- 在 Claude/ChatGPT/Cursor 中用自然语言查询行情与 DeFi 数据
- 通过对话完成代币兑换、跨链桥、质押与借贷操作
- 对代币合约做蜜罐与 Rug pull 安全检查
- 为 AI agent 接入自动支付通道以调用付费 API

## 场景标签

 · 领域:区块链/DeFi 工具

## 证据(README 行号)

> L77: A Universal Model Context Protocol server for all EVM-compatible networks + Solana.
> L79: Enable AI agents (Claude, ChatGPT, Cursor) to interact with any EVM blockchain through natural language.
> L93: |**Transport**|stdio, HTTP, SSE|Usually only stdio|

## 星数曲线

```mermaid
xychart-beta
    title "nirholas/universal-crypto-mcp 星数(近 4 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-25", "2026-10-26"]
    y-axis "stars" 41 --> 45
    line [42, 43, 44, 44]
```

2026-10-18 42 → 2026-10-26 44（+2）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `ca5249390c9f` · [字段定义](../../DATASET.md)*
