# Kemperino/ethereum-rpc-mpc

⭐ 21 · TypeScript · MIT · 推送 2026-10-30 · [GitHub](https://github.com/Kemperino/ethereum-rpc-mpc) · 个人维护

**让 MCP 客户端（AI 模型）访问 Ethereum/EVM 链数据的 MCP 服务器**

基于 MCP TypeScript SDK 的 stdio 服务器，通过 HTTP JSON-RPC 端点连接 Ethereum 或其他 EVM 链，向 MCP 客户端提供 13 个只读/模拟工具（余额、区块、交易、日志、eth_call 模拟、gas 估算等）、一个可调用任意 RPC 方法的通用工具及配置资源。支持两代 MCP 协议。服务器不持有私钥、不签名交易；默认端点为 PublicNode，可替换为自建节点。需 Node.js 22+，通过 npx 或源码构建运行。不提供 ABI 编解码、分页、WebSocket 订阅等功能。

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

- 13 个只读/模拟工具 + 通用 RPC 调用工具
- 兼容旧版 MCP 客户端与 2026-07-28 协议
- 服务器不持有私钥、不签名交易
- RPC 响应限制 10 MiB，30 秒默认超时，支持 MCP 取消

## 适用场景

- 让 Claude/Cursor 等 MCP 客户端查询链上余额、区块与交易
- AI 助手模拟合约调用并估算 gas
- 通过通用工具调用节点支持的其他 RPC 方法

## 场景标签

 · 领域:区块链/开发工具

## 证据(README 行号)

> L6: Connect an MCP client to Ethereum or another EVM chain through an HTTP JSON-RPC endpoint. The server provides 13 foc
> L8: The npm package and executable retain the historical spelling **`ethereum-rpc-mpc`** for compatibility. The protocol


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `2eee4f786640` · [字段定义](../../DATASET.md)*
