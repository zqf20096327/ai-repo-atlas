# salishforge/memforge

⭐ 14 · TypeScript · MIT · 推送 2026-10-26 · [GitHub](https://github.com/salishforge/memforge) · [官网](https://github.com/salishforge/memforge#readme) · 组织维护

**给 AI agent 的三层记忆系统：休眠周期改写强化知识**

面向 AI agent 的记忆管理服务：以 PostgreSQL 单库承担存储、全文检索、向量相似（pgvector）与图遍历；记忆分热/温/冷三层，后台 10 阶段休眠周期做评分、冲突解决、LLM 改写低置信记忆、反思与知识图谱维护，检索频次影响记忆强度。提供 MCP 服务器（30 工具）、TypeScript/Python SDK、Docker 独立镜像与 HTTP API；支持本地进程内嵌入（无需 OpenAI/Ollama）。自述 Beta，此前 LongMemEval 数字因评分器缺陷已撤回重测。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 热/温/冷三层记忆与 10 阶段休眠周期（改写、反思、知识图谱维护）
- 单 PostgreSQL 承担存储/全文/向量/图遍历，无需 Neo4j/Pinecone
- MCP 服务器 30 工具，接入 Claude Code、Cursor 等
- 本地进程内嵌入（bge-small-en-v1.5），无需外部嵌入服务

## 适用场景

- 为长期运行的 agent 提供可自我改写的记忆后端
- 通过 MCP 让 Claude Code/Cursor 等工具共享记忆
- 跨会话恢复 agent 上下文（resume 端点）

## 场景标签

`Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L13: Neuroscience-inspired memory system for AI agents. Sleep cycles consolidate, revise, and strengthen memories — just
> L15: MemForge manages agent memory across three tiers (hot → warm → cold) with vector search, a knowledge graph, LLM-dri
> L64: - **MCP Server** — 30 tools for Claude Code, Cursor, and MCP-compatible AI tools

## 星数曲线

```mermaid
xychart-beta
    title "salishforge/memforge 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `c8e9780234ac` · [字段定义](../../DATASET.md)*
