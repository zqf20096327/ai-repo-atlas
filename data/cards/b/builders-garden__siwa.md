# builders-garden/siwa

⭐ 43 · TypeScript · MIT · 推送 2026-04-29 · [GitHub](https://github.com/builders-garden/siwa) · [官网](https://siwa.id) · 组织维护

**AI agent 链上身份认证 SDK：签名证明 ERC-8004 身份归属**

面向开发者与 AI agent 生态的身份认证工具包。agent 用私钥对 SIWA 消息签名，证明其持有 ERC-8004 链上身份 NFT；服务端核验签名与链上归属后签发验证回执，后续 API 调用通过 ERC-8128 HTTP 消息签名附带回执。提供 npm SDK（@buildersgarden/siwa），含核心签名/验证模块、多种钱包 Signer 工厂（Circle/Openfort/Privy/本地私钥等）、Next.js/Express/Hono/Fastify 服务端中间件，以及私钥隔离的 keyring proxy 与 Telegram 2FA 审批组件；支持 Docker Compose 部署。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- ERC-8004 身份 NFT 链上归属验证 + 验证回执签发
- ERC-8128 HTTP 消息签名用于后续 API 调用
- 6 种钱包 Signer 与 4 种服务端框架中间件
- keyring proxy 私钥隔离与 Telegram 2FA 签名审批

## 适用场景

- 让我的 AI agent 在调用 API 前证明链上身份
- 为 Next.js/Express/Hono/Fastify 服务接入 agent 身份认证
- 把 agent 私钥隔离在独立代理进程中使用

## 场景标签

 · 领域:AI agent 基础设施/区块链认证

## 证据(README 行号)

> L5: SIWA lets AI agents prove who they are. Think Sign In With Ethereum, but for agents instead of humans.
> L7: An agent signs a message proving it owns an ERC-8004 identity NFT. The server verifies the signature and checks onch
> L75: |`packages/siwa`|Core SDK: signing, verification, registry helpers, ERC-8128, server wrappers|

## 星数曲线

```mermaid
xychart-beta
    title "builders-garden/siwa 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 42 --> 44
    line [43, 43]
```

2026-10-18 43 → 2026-10-27 43（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `01286127b2ab` · [字段定义](../../DATASET.md)*
