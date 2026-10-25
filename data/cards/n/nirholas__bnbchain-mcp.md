# nirholas/bnbchain-mcp

⭐ 35 · TypeScript · NOASSERTION · 推送 2026-10-09 · [GitHub](https://github.com/nirholas/bnbchain-mcp) · [官网](https://nirholas.github.io/bnbchain-mcp/) · 个人维护

**面向 AI agent 的 BNB Chain/EVM 区块链 MCP 服务器**

基于 TypeScript 的 Model Context Protocol（MCP）服务器，面向 BNB Chain 与 opBNB 优化，同时支持 Ethereum、Arbitrum、Base 等 12 条以上 EVM 网络。使 Claude、ChatGPT、Cursor 等 AI 助手通过自然语言读写链上数据：查询价格/TVL/DEX 池、执行代币交换与转账、部署智能合约、蜜罐与拉盘风险检测等，工具分核心链上操作、代币、DeFi、安全、行情数据五类（共 100+ 工具）。集成 CoinGecko、DefiLlama、GoPlus 等数据源；不配置 PRIVATE_KEY 时仅以只读模式运行。支持 stdio/HTTP/SSE 三种模式，可经 npx、源码或 Docker 运行，需 Node.js 18+。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 支持 12+ EVM 网络，覆盖 BNB Chain 与 opBNB 的读写操作
- 100+ 工具：价格/DEX/借贷/质押/桥接/合约部署/治理
- GoPlus 蜜罐检测、拉盘风险评估等安全工具
- 无 PRIVATE_KEY 时默认只读模式，私有钥仅内存使用不存储

## 适用场景

- 让 Claude/Cursor 等 AI 助手查询币价、TVL 与 DEX 池数据
- 通过对话执行代币交换、转账与跨链桥接
- 投资前用 AI 检查代币蜜罐与合约安全
- 用 AI 助手部署和验证智能合约

## 场景标签

 · 领域:区块链/加密货币开发工具

## 证据(README 行号)

> L32: **BNB Chain MCP** is a Model Context Protocol (MCP) server optimized for BNB Chain and opBNB, while also supporting
> L269: |**stdio**|`npx @nirholas/bnbchain-mcp`|Claude Desktop, Cursor|

## 星数曲线

```mermaid
xychart-beta
    title "nirholas/bnbchain-mcp 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-25"]
    y-axis "stars" 33 --> 36
    line [34, 35, 35]
```

2026-10-18 34 → 2026-10-25 35（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `ae490db349ff` · [字段定义](../../DATASET.md)*
