# amarodeabreu/claude-graph-memory

⭐ 18 · Shell · MIT · 推送 2026-01-06 · [GitHub](https://github.com/amarodeabreu/claude-graph-memory) · 个人维护

**给 Claude Code 提供本地知识图谱持久记忆的工具**

面向 Claude Code 用户的持久记忆层：通过 MCP 服务器与全局 hooks 在会话启动和文件编辑时自动索引 /docs 下 Markdown 与 Go/TypeScript/Python 代码结构，存入本地 Docker 容器中的 NornicDB（Neo4j 兼容图数据库）构成知识图谱；Claude 以 Cypher 查询按需检索项目上下文，并可存储跨会话记忆。数据全部留在本机，MCP 经 stdio 通信。安装依赖 Docker、Python 3.9+ 与 Claude Code CLI，经 install.sh 一键部署，附 claude-graph CLI 与 localhost:7474 图浏览器。限制：当前仅支持单机使用，语义向量检索仍在 Roadmap 未实现。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 会话启动与文件编辑时自动/增量索引文档与代码结构到知识图谱
- 100% 本地运行：NornicDB 本地 Docker 容器，数据不出机器
- Cypher 图查询按需检索项目上下文，避免全量加载上下文窗口
- 多项目按图标签隔离，支持跨会话存储决策与学习记忆

## 适用场景

- 跨会话延续 Claude Code 对项目架构与历史决策的记忆
- 查询哪些文档、决策和代码与某组件相关
- 在图浏览器中检视 Claude 回答所依赖的具体节点

## 场景标签

`知识图谱` `Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L8:  Persistent knowledge graph and RAG memory for Claude Code
> L141: 3. ✅ Configure MCP servers for Claude Code
> L35: A **100% local** knowledge graph that runs alongside Claude Code, automatically indexing your documentation and cod

## 星数曲线

```mermaid
xychart-beta
    title "amarodeabreu/claude-graph-memory 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 17 --> 19
    line [18, 18]
```

2026-10-18 18 → 2026-10-30 18（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `6ca6b1edec63` · [字段定义](../../DATASET.md)*
