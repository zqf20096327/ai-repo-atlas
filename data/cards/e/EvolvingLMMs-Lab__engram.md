# EvolvingLMMs-Lab/engram

⭐ 23 · TypeScript · NOASSERTION · 推送 2026-06-12 · [GitHub](https://github.com/EvolvingLMMs-Lab/engram) · 组织维护

**端到端加密的本地优先 AI 记忆层，经 MCP 接入各类 AI 客户端**

面向 AI 助手的记忆层 MCP 服务：在本地设备存储会话记忆，提供向量相似性语义检索、加密的密钥/凭证存储与可选的零知识多设备同步。加密采用 AES-256-GCM、PBKDF2 密钥派生与 24 词 BIP39 恢复短语，密钥不离开设备。支持 Claude Desktop、Claude Code、Cursor 及任意 MCP 兼容客户端，并可经生命周期钩子将 Claude Code Agent Teams 的团队记忆整合为结构化摘要。通过 npx 初始化。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 本地默认存储，AES-256-GCM 端到端加密，密钥不出设备
- 跨会话语义记忆（向量相似性检索）与加密凭证保管
- 可选零知识多设备同步，服务端仅见密文
- Claude Code Agent Teams 钩子自动整合团队记忆为结构化摘要

## 适用场景

- 让 Claude/Cursor 等 AI 客户端跨会话记住我的上下文
- 在多设备间同步 AI 记忆且不让服务端看到明文
- 对 AI 记忆数据做本地加密与自主掌控

## 场景标签

`Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L16: An **end-to-end encrypted** memory layer for AI assistants.
> L26: Works with Claude Desktop, Claude Code, Cursor, and any MCP-compatible client.

## 星数曲线

```mermaid
xychart-beta
    title "EvolvingLMMs-Lab/engram 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 22 --> 24
    line [23, 23]
```

2026-10-18 23 → 2026-10-29 23（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `18d2699c682b` · [字段定义](../../DATASET.md)*
