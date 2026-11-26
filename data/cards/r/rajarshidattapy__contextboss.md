# rajarshidattapy/contextboss

⭐ 4 · Python · MIT · 推送 2026-11-25 · [GitHub](https://github.com/rajarshidattapy/contextboss) · [官网](https://contextboss.vercel.app) · 个人维护

**为 agent 管理上下文窗口预算的 Python 库与 MCP 服务器**

ContextBoss 将上下文窗口当作预算管理：把 system、task、memory、retrieval、tools 五类候选块按预算分层注入 agent 提示词，超限时依次压缩、摘要、丢弃，并用 tiktoken 做真实 token 计数与最终校验。每个注入/裁剪决策连同原因写入 ctx.decisions 供检查。提供 pip 安装的核心库、REST API、dashboard，以及可接入 Claude Code、Codex、ChatGPT 的 MCP 服务器；持久化层用 SQLite（WAL+FTS5）保存命名空间与版本历史。MIT 许可。

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

- 五层 tier 预算分配与 system>task>memory>retrieval>tools 固定注入顺序
- 每个注入/压缩/丢弃决策记录 tokens 与原因（ctx.decisions）
- MCP 服务器接入 Claude Code、Codex、ChatGPT
- SQLite 持久化上下文：命名空间、标签、pinned 标志与完整版本历史

## 适用场景

- 为多轮 agent 会话控制提示词不超过上下文窗口
- 在预算内对记忆与检索片段做优先级排序注入
- 通过 MCP 让 Claude Code 等客户端共享统一上下文存储

## 场景标签

`Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L6: One SQLite store that budgets, ranks and injects context for agents.
> L21: contextboss treats the window as a budget. Hand it every candidate block (system prompt, task,
> L27:  **MCP server** for Claude Code, Codex and ChatGPT:


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 high · 依据 README sha `07f3ab3960bd` · [字段定义](../../DATASET.md)*
