# LYAKAKOY/Hermes-Codex-Plugin

⭐ 19 · Python · 推送 2026-06-05 · [GitHub](https://github.com/LYAKAKOY/Hermes-Codex-Plugin) · 个人维护

**给 Codex 开发者的本地记忆与技能演化插件**

为 Codex agent 提供跨会话持久记忆的本地优先插件：以 SQLite FTS5 全文检索存储项目规则、任务摘要与聊天记录，通过 Codex 生命周期钩子（SessionStart/UserPromptSubmit 等）在请求前注入最小相关上下文以减少 token 消耗；附带 MCP 服务器（搜索/写入/删除/统计/技能草稿八个工具）与 Python CLI。支持从重复规则起草 SKILL.md 技能文件。不使用嵌入与后台守护进程，敏感值入库前做遮蔽。技能生成为启发式，需人工审核。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- SQLite FTS5 全文记忆存储，LIKE 回退，无需嵌入服务
- Codex 生命周期钩子自动捕获与召回记忆
- MCP 服务器提供 8 个记忆与技能工具
- 从重复规则起草 SKILL.md，含多语言工作流规则

## 适用场景

- 跨 Codex 会话记住项目架构规则与编码约定
- 搜索历史对话而不必手动粘贴上下文
- 从重复项目规则生成可复用技能文件
- 在本地检查记忆库内容与统计

## 场景标签

`Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L12: Hermes Codex Plugin is a local-first Codex plugin that gives Codex durable memory across chats,
> L25: - MCP tools for search, write, delete, stats, and skill drafts;

## 星数曲线

```mermaid
xychart-beta
    title "LYAKAKOY/Hermes-Codex-Plugin 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 18 --> 20
    line [19, 19]
```

2026-10-18 19 → 2026-10-30 19（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `db7a48728fb2` · [字段定义](../../DATASET.md)*
