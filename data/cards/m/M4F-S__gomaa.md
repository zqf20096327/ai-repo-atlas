# M4F-S/gomaa

⭐ 34 · Python · Apache-2.0 · 推送 2026-10-14 · [GitHub](https://github.com/M4F-S/gomaa) · 个人维护

**给 AI agent 的持久记忆系统：Obsidian 笔记库+混合检索+MCP 服务**

面向自主 AI agent（Claude Desktop、Cursor、Hermes、CrewAI 等）的本地优先分层记忆引擎：以 Obsidian Markdown 笔记库为人类可读载体，存储采用 PostgreSQL+pgvector 或零配置 SQLite WAL。机制包括 4 象限认知架构（情景/语义/程序/工作记忆）、HippoRAG 2 个性化 PageRank 与 5 路 RRF 混合检索、3 阶段睡眠巩固命令（gomaa sleep）、Ebbinghaus 时间衰减与置顶免疫、Wing/Room 作用域隔离、跨 agent 舰队共享记忆。以 MCP 服务器（13 个工具）形式接入各类客户端，提供 pip 安装、一键安装脚本与 Docker Compose 部署，含 LangChain/LangGraph/CrewAI 适配器。

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

- MCP 服务器形式提供 13 个工具，接入 Claude Desktop/Cursor/Windsurf 等客户端
- 4 象限认知存储与 HippoRAG 2 PPR + 5 路 RRF 混合检索
- 语义记忆为 Obsidian 人类可读 Markdown 笔记（YAML frontmatter + Wiki Links）
- gomaa sleep 三阶段离线巩固：情景→语义结晶、跨 agent 技能共享、ATMS 冲突消解

## 适用场景

- 给 Claude Desktop / Cursor 等 MCP 客户端挂上跨会话长期记忆
- 多 agent 舰队共享高成功率程序性技能而隔离私有库
- 在 Obsidian 中人工审计、修正和组织 agent 学到的知识

## 场景标签

`Agent 记忆` `多智能体` · 领域:Agent 开发

## 证据(README 行号)

> L12: Gomaa equips AI agents (Hermes, OpenClaw, Claude Desktop, Cursor, Windsurf, CrewAI, LangChain) with permanent, huma
> L108: |**🤖 MCP Native (v2024-11-05)**|Standardized stdio JSON-RPC protocol server (13 tools)|Seamless drop-in for Claude

## 星数曲线

```mermaid
xychart-beta
    title "M4F-S/gomaa 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-24", "2026-10-29"]
    y-axis "stars" 32 --> 35
    line [33, 34, 34]
```

2026-10-18 33 → 2026-10-29 34（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `43db8ac9f622` · [字段定义](../../DATASET.md)*
