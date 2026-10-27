# Prismer-AI/signet

⭐ 40 · Rust · Apache-2.0 · 推送 2026-09-24 · [GitHub](https://github.com/Prismer-AI/signet) · [官网](https://signet-auth.vercel.app/) · 组织维护 · 中文 README

**为 AI agent 工具调用提供密码学签名与授权凭证的信任层**

Signet 为 AI agent 的每次工具调用生成 Ed25519 签名凭证，写入 SHA-256 哈希链审计日志，可离线验证，不依赖托管平台或日志厂商。0.11 起授权本身携带凭证：委托链证明谁允许 agent 行动，YAML 策略满足时在凭证中嵌入签名 PolicyAttestation，另含撤销机制与调用限额。提供 signet proxy 透明包装任意 MCP server、CLI、Python/TypeScript SDK，并为 Claude Code、Codex CLI、LangChain、CrewAI、Vercel AI SDK 等框架提供接入路径。面向 MCP 构建者、安全合规团队与企业 agent 平台，合规映射覆盖 SOC 2、ISO 27001、EU AI Act Art.12 等。限制：README 自称是工具而非认证，合规态势取决于部署与配置。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Ed25519 签名 + SHA-256 哈希链的防篡改审计日志，仅需公钥即可离线验证
- 委托链证明授权来源（权限只可收窄），YAML 策略签名为 PolicyAttestation
- signet proxy 无需改动代码即可包装任意 MCP server 并签名 tools/call
- 支持双边 co-signing、撤销记录与调用次数/花费限额

## 适用场景

- 审计或事故后证明 agent 具体执行了什么操作、谁授权的
- 给 MCP server 加执行边界验证，在运行前拒绝被篡改的请求
- 满足 SOC 2 / ISO 27001 / EU AI Act 的记录留存与可追溯要求
- 多步工作流通过 trace_id 与 parent_receipt_id 追踪 agent 行为链

## 场景标签

`网络安全` `LLM 可观测性` · 领域:评测与运维

## 证据(README 行号)

> L64: - **MCP builders** — wrap any MCP server with `signet proxy`, sign every `tools/call`, no code changes
> L67: - **Framework users** — LangChain, CrewAI, Claude Code, Codex, OpenAI Agents, Vercel AI SDK — all supported
> L86: - **Proxy** any MCP server transparently — sign requests without touching agent or server code, with local bilatera

## 星数曲线

```mermaid
xychart-beta
    title "Prismer-AI/signet 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 39 --> 41
    line [40, 40]
```

2026-10-18 40 → 2026-10-27 40（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `f9187cb93c5a` · [字段定义](../../DATASET.md)*
