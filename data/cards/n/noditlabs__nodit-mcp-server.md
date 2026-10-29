# noditlabs/nodit-mcp-server

⭐ 23 · TypeScript · Apache-2.0 · 推送 2026-10-19 · [GitHub](https://github.com/noditlabs/nodit-mcp-server) · [官网](https://nodit.io) · 组织维护

**让 AI agent 通过 Nodit API 访问多链区块链数据的 MCP 服务器**

由 Nodit 团队维护的 Model Context Protocol（MCP）服务器，供 AI agent 与开发者以标准化工具调用的方式访问 Nodit 的 Web3 基础设施：RPC Node API、Web3 Data API、Aptos GraphQL 索引与 Multichain API。工具按发现 API 类别、列出操作、获取规范、执行调用四步模块化组织以降低 token 消耗。支持 Ethereum、Arbitrum、Bitcoin、TRON、Solana 等多条 EVM 与非 EVM 链。需 Nodit API Key，本地运行依赖 Node.js 18+，仅支持 stdio 通信，另提供远程 MCP 端点。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 四步模块化工具链：列类别→列操作→取规范→调 API，降低 token 消耗
- 覆盖 EVM（Ethereum/Base/Optimism 等）与非 EVM（Bitcoin/TRON/Solana 等）多链
- 支持本地 npx 运行与远程 SSE 端点两种接入方式
- 提供 Cursor IDE、Claude Desktop、Claude CLI 的接入配置说明

## 适用场景

- 在 Claude 或 Cursor 中用自然语言查询多链钱包余额、交易与 NFT 持仓
- 构建分析链上活动、智能合约交互的 AI agent
- Web3 应用开发中让 LLM 直接生成调用 Nodit API 的代码
- 生成钱包持仓与资金流向的日常汇总报告

## 场景标签

 · 领域:区块链/Web3 数据基础设施

## 证据(README 行号)

> L3: A Model Context Protocol (MCP) server that connects AI agents and developers to structured, context-ready blockchain
> L31: Nodit MCP Server provides tools enabling AI agents to dynamically discover, understand, and interact with Nodit's W
> L56: Nodit MCP Server communicates using the standard JSON-RPC over stdio protocol, following the Model Context Protocol

## 星数曲线

```mermaid
xychart-beta
    title "noditlabs/nodit-mcp-server 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 22 --> 24
    line [23, 23]
```

2026-10-18 23 → 2026-10-29 23（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `8d79b430ab19` · [字段定义](../../DATASET.md)*
