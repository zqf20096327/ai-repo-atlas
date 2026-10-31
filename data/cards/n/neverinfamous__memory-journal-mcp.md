# neverinfamous/memory-journal-mcp

⭐ 20 · TypeScript · MIT · 推送 2026-07-22 · [GitHub](https://github.com/neverinfamous/memory-journal-mcp) · [官网](https://search.adamic.tech/) · 个人维护

**为 AI 会话提供持久项目记忆与 GitHub 集成的 MCP 服务器**

面向使用 AI 编程助手的开发者，以 MCP 服务器形式提供跨会话的项目长期记忆：会话开始时通过 memory://briefing 交付约 350 token 的工作区上下文，会话结束时以 session-summary 交接。提供 73 个 MCP 工具（10 组）、19 个工作流提示词、46 个资源，覆盖条目 CRUD、FTS5+语义向量混合检索、知识图谱、Markdown/JSON 导入导出、18 个 GitHub 工具（Issues/PRs/Actions/Kanban）、28 个团队协作工具（共享数据库、Hush 标志）、沙箱化 Code Mode、备份与自动剪枝。安全方面支持 OAuth 2.1、审计日志与 token 计量。通过 npm 或 Docker（Alpine）部署。

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

- 73 个 MCP 工具 + 19 个工作流提示词 + 46 个资源
- FTS5 关键词与语义向量融合（RRF）的三重检索
- memory://briefing 会话简报与 session-summary 交接机制
- 18 个 GitHub 工具与 28 个团队协作工具（Hush 标志、共享团队库）

## 适用场景

- 让 AI 编程助手在新会话中自动获取项目历史与决策记录
- 通过自然语言操作 GitHub Issues、PR 与看板并留痕
- 团队多成员共享项目记忆与跨项目洞察
- 生成站会、回顾、周报等报告

## 场景标签

`Agent 记忆` `知识图谱` · 领域:Agent 开发

## 证据(README 行号)

> L18: 🎯 **AI Context + Project Intelligence:** Bridge disconnected AI sessions with persistent project memory and **autom
> L49: **73 MCP Tools** · **19 Workflow Prompts** · **46 Resources** · **10 Tool Groups** · **Code Mode** · **GitHub Comma
> L128: |`codemode`|1|Code Mode (sandboxed code execution) 🌟 **Recommended**|

## 星数曲线

```mermaid
xychart-beta
    title "neverinfamous/memory-journal-mcp 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 19 --> 21
    line [20, 20]
```

2026-10-18 20 → 2026-10-31 20（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `11994f28fd14` · [字段定义](../../DATASET.md)*
