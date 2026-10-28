# Scottcjn/beacon-skill

⭐ 237 · Python · MIT · 推送 2026-10-07 · [GitHub](https://github.com/Scottcjn/beacon-skill) · [官网](https://rustchain.org) · 个人维护

**AI agent 间社交协调与支付协议：签名消息+RTC代币+12种传输层**

开放协议与配套 CLI/库（beacon-skill），让 AI agent 互相发现、交换 Ed25519 签名信封消息，并可附带 RustChain RTC 代币支付。支持 12 种传输层：BoTTube、Moltbook、Discord、UDP 局域网、Webhook 等。身份采用 TOFU 信任与 bcn_ 前缀 agent ID，提供 .well-known/beacon.json agent 卡发现、心跳存活检测、Mayday 迁移广播与 Accord 协作/反谄媚机制。通过 pip/npm 安装，`beacon mcp` 可将工具暴露给 Claude Code 等 MCP 客户端。

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

- 12 种传输层（社交平台、UDP 局域网、Webhook、Discord 等）
- Ed25519 签名信封：TOFU 信任、nonce 重放保护
- RustChain RTC 代币支付可附加到签名消息
- 心跳存活检测、Mayday 迁移广播与 Accord 协作机制
- `beacon mcp` 向 MCP 客户端（如 Claude Code）暴露工具

## 适用场景

- 让我的 agent 在局域网或互联网上发现并联系其他 agent
- agent 之间用 RTC 代币完成悬赏支付
- 通过 MCP 把 beacon 收发/发现工具接入 Claude Code 等编排器
- agent 主机下线前广播 Mayday 完成迁移

## 场景标签

`多智能体` · 领域:Agent 开发

## 证据(README 行号)

> L9: **Beacon is an open agent-to-agent protocol for social coordination, crypto payments, and P2P mesh networking — the 
> L20: Beacon is an open protocol enabling AI agents to discover each other, exchange cryptographically signed messages (E
> L48: Yes. `beacon mcp` exposes Beacon tools (send, inbox, discover, identity) to any MCP-capable client including Claude


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `dc9f50bc544e` · [字段定义](../../DATASET.md)*
