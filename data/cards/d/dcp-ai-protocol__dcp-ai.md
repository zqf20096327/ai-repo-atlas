# dcp-ai-protocol/dcp-ai

⭐ 23 · TypeScript · Apache-2.0 · 推送 2026-10-30 · [GitHub](https://github.com/dcp-ai-protocol/dcp-ai) · [官网](https://dcp-ai.org) · 组织维护 · 中文 README

**AI agent 问责协议：身份绑定、意图声明与可验证审计**

定义开放网络上 AI agent 的便携问责层：通过责任主体绑定、Agent Passport、意图声明、策略决定与哈希链审计证据，使任意验证者可核验 agent 的责任归属与行为记录。协议由 DCP Core、Profiles（含 A2A、治理、混合后量子加密）与可选服务组成；V2 对 RPR、passport、intent 等分别签名，无需中心化验证服务。提供 TypeScript/Python/Go/Rust/WASM 五种 SDK 与 Express、FastAPI、LangChain、CrewAI、OpenAI、MCP 等框架集成。CLI 向导与 playground 为演示用途，签名是模拟的。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 责任主体绑定、意图声明、哈希链审计与 Merkle 证明构成的可验证问责层
- V2 支持混合后量子签名与 4 级安全分级（Routine 到 Maximum）
- TypeScript/Python/Go/Rust/WASM 五语言 SDK
- 覆盖 LangChain、CrewAI、OpenAI、Anthropic MCP、Google A2A 等框架集成

## 适用场景

- 为自主 AI agent 建立可验证的身份与责任归属
- 在跨组织 agent 通信中执行意图声明与策略分级验证
- 为 agent 行为生成防篡改的审计证据链以满足合规需求

## 场景标签

 · 领域:AI 安全/Agent 基础设施

## 证据(README 行号)

> L24: The **Digital Citizenship Protocol (DCP)** defines a portable accountability layer for AI agents, allowing any veri
> L48: - **Responsible Principal Binding** — links every agent to a human or legal entity that assumes accountability

## 星数曲线

```mermaid
xychart-beta
    title "dcp-ai-protocol/dcp-ai 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 22 --> 24
    line [23, 23]
```

2026-10-18 23 → 2026-10-31 23（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `128db96f8948` · [字段定义](../../DATASET.md)*
