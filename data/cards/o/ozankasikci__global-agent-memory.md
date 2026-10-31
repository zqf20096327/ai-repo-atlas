# ozankasikci/global-agent-memory

⭐ 14 · Python · MIT · 推送 2026-09-01 · [GitHub](https://github.com/ozankasikci/global-agent-memory) · [官网](https://github.com/ozankasikci/global-agent-memory/releases/latest) · 个人维护

**给多个编程 agent 共享的本地记忆 MCP 服务器，含人审面板**

面向 Claude Code、Codex 及其他 MCP 兼容 agent 的本地优先记忆层：以 Markdown 为唯一事实源（可直接在 Obsidian 中读写），通过混合本地 MCP 运行时（可无守护进程）向 agent 提供项目感知的上下文检索、候选记忆创建与生命周期操作；检索采用 SQLite FTS5 关键词搜索，可选 Ollama 嵌入加 sqlite-vec 做语义排序，Ollama 不可用时关键词搜索仍可用。agent 提交的记忆为候选状态，需在本地认证 dashboard 中由 owner 审批、编辑、分级（Standard/Protected/Sealed）后才生效。支持 macOS/Linux，要求 Python 3.12+ 与 uv，经 uv tool 从 PyPI 安装后运行 guided setup。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Claude Code、Codex 等多个 agent 共享同一记忆服务与不可变记忆 ID
- Markdown 为规范事实源，兼容 Obsidian（模板、Bases 视图、wikilinks）
- agent 提交候选、owner 经本地 dashboard 审批后记忆才持久化
- SQLite FTS5 关键词检索 + 可选 Ollama 语义排序，离线可用

## 适用场景

- 让多个编程 agent 跨会话、跨客户端共享项目决策与解决方案
- 在 Obsidian 中直接读写 agent 的长期记忆库
- 对 agent 记住的内容做人工审批与敏感信息保护

## 场景标签

`Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L3: > Local-first, project-aware, durable memory for Claude Code, Codex, and other
> L60: - **Shared across agents** — Claude Code, Codex, and other MCP clients use the same
> L99: |**MCP**|Claude Code, Codex, and other agents|Project-aware context, search, candidate creation, safe updates, life

## 星数曲线

```mermaid
xychart-beta
    title "ozankasikci/global-agent-memory 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `38c37ecf5858` · [字段定义](../../DATASET.md)*
