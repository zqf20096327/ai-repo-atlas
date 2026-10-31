# zycaskevin/Vault-Agent-Memory

⭐ 50 · Python · Apache-2.0 · 推送 2026-08-27 · [GitHub](https://github.com/zycaskevin/Vault-Agent-Memory) · [官网](https://zycaskevin.github.io/Vault-Agent-Memory/) · 个人维护 · 中文 README

**本地优先的 AI agent 记忆治理层：可共享、可审查、可审计**

面向已在构建或使用 agent 的开发者，为 Codex、Claude Code、Hermes、OpenClaw、n8n、Coze 等多个 agent 提供统一的受治理共享记忆库：候选提交→审查→晋升→检索→有界读取→回滚→审计的完整生命周期，含隐私、重复、质量与来源校验门，并生成每日人工审查报告。后端无关，本地 SQLite/Markdown 为事实源，可选自建中央主机或 Supabase 适配器；通过 CLI、MCP、Gateway 与 OpenAPI 适配器接入。v0.10.2 为 Public Beta / Developer Preview，pre-1.0，高级面需刻意启用并监控。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- propose→review→promote→search→bounded read→rollback→audit 记忆生命周期
- 本地 SQLite 为事实源，后端可换（自建/Supabase/未来托管云）
- 单机共享 + 多主机受治理同步：远程 agent 只能提交候选，受信主机晋升
- 通过 CLI/MCP/Gateway/OpenAPI 接入，兼容 Letta、mem0 等框架作为其后端

## 适用场景

- 让多个 agent（Codex/Claude Code 等）共享一份可审查的长期记忆
- 团队治理 agent 记忆：控制谁能读写、过期回滚、审计变更
- 让 agent 安全使用 Obsidian 笔记（来源区间与审查边界）

## 场景标签

`Agent 记忆` `多智能体` · 领域:Agent 开发

## 证据(README 行号)

> L7: Vault is a local-first, backend-agnostic memory governance layer for AI agents.
> L20: Vault works standalone, and it can also become the governed memory backend for
> L21: other agent memory frameworks. You can use Vault by itself with CLI, MCP,

## 星数曲线

```mermaid
xychart-beta
    title "zycaskevin/Vault-Agent-Memory 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 49 --> 51
    line [50, 50]
```

2026-10-18 50 → 2026-10-31 50（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `52e7cbe1ad85` · [字段定义](../../DATASET.md)*
