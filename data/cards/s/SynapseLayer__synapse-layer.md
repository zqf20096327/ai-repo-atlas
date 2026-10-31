# SynapseLayer/synapse-layer

⭐ 13 · Python · Apache-2.0 · 推送 2026-10-22 · [GitHub](https://github.com/SynapseLayer/synapse-layer) · [官网](https://synapselayer.org) · 组织维护

**给 AI agent 的持久记忆基础设施：加密存储与语义检索**

面向 AI agent 与助手的持久记忆基础设施：记忆以 AES-256-GCM 加密存储，经 pgvector HNSW 索引做语义召回，通过 MCP JSON-RPC 暴露给 Claude、GPT、Gemini 及任意 MCP 兼容客户端，支持跨 agent 记忆（如 ChatGPT 保存、Claude 召回）。提供 13 个 MCP 工具（save/recall/search/agent handoff 等）、Trust Quotient 置信度排序。部署分 Python SDK 与 Forge 云 API 两种模式，需在 forge.synapselayer.org 获取 Connect Token。Apache 2.0 许可。

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

- AES-256-GCM 静态加密 + HMAC-SHA-256 完整性校验，租户隔离存储
- pgvector HNSW 语义索引与检索
- 13 个 MCP 工具：记忆存取、语义召回、反馈、agent 交接、可观测性
- 跨 agent 记忆连续性与 Trust Quotient 置信度排序

## 适用场景

- 让助手跨会话记住用户偏好与历史决策
- 在 ChatGPT 保存上下文、在 Claude 中召回的跨 agent 协作
- 为 Claude Desktop/Cursor 等 MCP 客户端接入治理型记忆层
- 生产 agent 团队维护结构化、可审计的运营记忆

## 场景标签

`Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L7: Synapse Layer is open-source persistent memory infrastructure for AI agents and assistants. Memories are encrypted a
> L107: Synapse Layer currently exposes 13 MCP tools for persistent memory workflows:

## 星数曲线

```mermaid
xychart-beta
    title "SynapseLayer/synapse-layer 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 12 --> 14
    line [13, 13]
```

2026-10-18 13 → 2026-10-31 13（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `b1ba9d5e9bf7` · [字段定义](../../DATASET.md)*
