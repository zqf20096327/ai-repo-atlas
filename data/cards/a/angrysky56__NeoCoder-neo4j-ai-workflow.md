# angrysky56/NeoCoder-neo4j-ai-workflow

⭐ 21 · Python · MIT · 推送 2025-12-17 · [GitHub](https://github.com/angrysky56/NeoCoder-neo4j-ai-workflow) · 个人维护

**让 AI 助手以 Neo4j 知识图谱作为指令手册与记忆的 MCP 服务器**

面向 Claude 等 AI 助手的 MCP 服务器实现：将 Neo4j 知识图谱作为动态指令手册与项目长期记忆，结合 Qdrant 向量库做混合推理（结构化事实+语义检索），由 MCP 编排路由数据源并带引用溯源。提供多种'incarnation'运行模式，覆盖编码工作流、科研假设跟踪、决策分析、复杂系统建模、知识图谱管理与代码分析等场景。运行需自备 Neo4j、Qdrant 与 Python 3.10+，依赖项较多；部分 incarnation（如代码分析）仍在开发中。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- Neo4j 图 + Qdrant 向量的混合知识查询与智能路由
- 多 incarnation 模式：编码/科研/决策/建模/知识图谱/代码分析
- F-Contraction 合成：合并相似概念并保留来源归属与引用追踪
- 进程管理：信号处理、资源跟踪与孤儿实例清理

## 适用场景

- 为 Claude 等 MCP 客户端提供基于图谱的项目记忆与标准化工作流
- 科研场景中跟踪假设、实验与证据的因果脉络
- 知识管理中做跨数据库的引用式问答与冲突检测

## 场景标签

`Agent 记忆` `知识图谱` `科研工具` `RAG` · 领域:Agent 开发

## 证据(README 行号)

> L5: An MCP server implementation that enables AI assistants like Claude to use a Neo4j knowledge graph as their primary,
> L9: An advanced MCP server implementation that combines Neo4j knowledge graphs, Qdrant vector databases, and sophisticat
> L103: ## The MCP server runs the Python code, bridging the gap between the Neo4j graph and the AI assistant ( e.g. Claud

## 星数曲线

```mermaid
xychart-beta
    title "angrysky56/NeoCoder-neo4j-ai-workflow 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-30"]
    y-axis "stars" 19 --> 22
    line [20, 21, 21]
```

2026-10-18 20 → 2026-10-30 21（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 mid · 依据 README sha `a308025e3fae` · [字段定义](../../DATASET.md)*
