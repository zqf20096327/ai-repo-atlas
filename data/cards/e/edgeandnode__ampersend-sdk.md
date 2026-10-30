# edgeandnode/ampersend-sdk

⭐ 24 · TypeScript · Apache-2.0 · 推送 2026-07-17 · [GitHub](https://github.com/edgeandnode/ampersend-sdk) · 组织维护

**面向开发者的 x402 支付多语言 SDK：为 AI 应用加支付能力**

提供 Python 与 TypeScript 两种语言的 SDK，用于构建具备 x402 支付能力的应用，支持买方（客户端发起带支付的请求）与卖方（服务端校验支付）两种角色。Python 侧集成 A2A 协议与支付中间件，TypeScript 侧集成 MCP 协议的 client、proxy 与 server，另支持 HTTP 传输。核心组件包括授权跟踪支付的 Treasurer、签名支付证明的 Wallet（支持 EOA 与智能账户）。开发依赖 uv/Python 3.13+ 与 Node.js 18+/pnpm，测试需测试 USDC 与以太坊私钥。

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

- Python（A2A）与 TypeScript（MCP/HTTP）双语言实现
- 买方/卖方角色分离，含支付验证与授权模式
- Treasurer 支付授权跟踪与 Wallet 签名（EOA/智能账户）
- 通过 skills CLI 为编码 agent 安装使用技能

## 适用场景

- 为 AI agent 应用接入按请求计费的 x402 支付
- 构建带支付能力的 A2A/MCP 服务端与客户端
- 让 Claude Code/Cursor 等编码代理具备在线支付能力

## 场景标签

 · 领域:AI 基础设施/支付协议

## 证据(README 行号)

> L3: Multi-language SDK for building applications with x402 payment capabilities.
> L64: **x402 Protocol** - Transport-agnostic payment protocol for agent and LLM applications that enables pay-per-request
> L69: - **A2A** (Agent-to-Agent) - Transport protocol for agent communication with payment capabilities

## 星数曲线

```mermaid
xychart-beta
    title "edgeandnode/ampersend-sdk 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 23 --> 25
    line [24, 24]
```

2026-10-18 24 → 2026-10-30 24（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `6a5333d50893` · [字段定义](../../DATASET.md)*
