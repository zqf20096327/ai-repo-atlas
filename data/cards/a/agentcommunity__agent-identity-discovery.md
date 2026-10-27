# agentcommunity/agent-identity-discovery

⭐ 48 · TypeScript · NOASSERTION · 推送 2026-10-02 · [GitHub](https://github.com/agentcommunity/agent-identity-discovery) · [官网](https://aid.agentcommunity.org/) · 组织维护

**基于 DNS TXT 记录的 agent 服务发现开放标准与多语言库**

Agent Identity & Discovery (AID) 是一个开放标准：在域名下发布一条 DNS TXT 记录（_agent.<domain>），即可声明该域名的 agent 服务入口及其协议（MCP、A2A、OpenAPI、gRPC 等），并提供 HTTPS .well-known JSON 回退。v2.1 含 Ed25519 PKA 端点证明（RFC 9421）、key 别名、多语言库（TypeScript/Python/Go/Rust/.NET/Java）与 CLI 工具 aid-doctor。采用 PNPM/Turborepo monorepo 结构。面向构建 agent 客户端与服务发布的开发者与标准采纳者。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 单条 DNS TXT 记录声明 agent 服务入口与协议，.well-known HTTPS 回退
- v2 PKA 端点证明：Ed25519 RFC 9421 签名、nonce、created/expires
- TypeScript/Python/Go/Rust/.NET/Java 多语言 SDK 与 aid-doctor CLI
- 去中心化：控制域名即可发布 AID 记录，无中心注册表

## 适用场景

- 让我的 agent 客户端通过域名自动发现对方的 MCP/A2A 服务入口
- 为我的 agent 服务域名发布 AID 记录供他方发现
- 校验域名 agent 身份的 PKA 端点证明

## 场景标签

 · 领域:agent 基础设施/协议标准

## 证据(README 行号)

> L27: AID is a minimal, open standard that answers one question: **"Given a domain name, where does its agent interaction
> L29: It uses a single DNS `TXT` record to make any agent service—whether it speaks MCP, A2A, or another protocol—instant
> L80: - **Protocol-Agnostic:** Discover agents speaking MCP, A2A, OpenAPI, or even local protocols running in Docker.

## 星数曲线

```mermaid
xychart-beta
    title "agentcommunity/agent-identity-discovery 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 47 --> 49
    line [48, 48]
```

2026-10-18 48 → 2026-10-27 48（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `75920ec711d8` · [字段定义](../../DATASET.md)*
