# vornicx/Midas

⭐ 15 · Python · MIT · 推送 2026-07-28 · [GitHub](https://github.com/vornicx/Midas) · [官网](https://midas.archic.es/) · 个人维护

**本地优先的长期 agent 记忆层：MCP 服务器 + Python SDK**

为跨会话长期运行的 AI agent 提供本地记忆存储：以 Python SDK 与标准 MCP 服务器形式发布，摄取与查询阶段均不调用 LLM，记忆逐条溯源到原始对话轮次。机制包括类型化信念修订、选择性遗忘、来源防护（阻止基于记忆的外部/破坏性动作除非用户确认）、memory_state/memory_diff 查询，以及可复现基准评测。单一 SQLite 文件被 Claude Code、Cursor 等多个客户端共享，支持从 CLAUDE.md/Mem0/Zep 等导入。限制：不做整段对话聚合/摘要（文档声明的设计取舍）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 摄取与查询零 LLM 调用，$0 每消息，数据不出本机
- 召回返回逐字源对话轮次，可溯源到来源
- 信念修订 + 选择性遗忘 + provenance 防护（阻止未确认的记忆驱动破坏性动作）
- 单一 SQLite 文件被 Claude Code/Cursor 等 10 个 MCP 客户端共享

## 适用场景

- 让编码 agent 记住数个会话前的决策、约定与 bug
- 多个 IDE/聊天客户端共享同一份本地记忆
- 需要可审计、可复现记忆行为的 agent 系统
- 从 CLAUDE.md/Cursor 规则/Mem0 导出迁移既有记忆

## 场景标签

`Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L3:  The local memory layer for long-horizon AI agents — remembers across sessions, keeps what's current, and won't act 
> L161: Midas is a standard MCP server: point any client at the **`midas-mcp`** command. It uses the shared store

## 星数曲线

```mermaid
xychart-beta
    title "vornicx/Midas 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-30 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `48f25176a3b4` · [字段定义](../../DATASET.md)*
