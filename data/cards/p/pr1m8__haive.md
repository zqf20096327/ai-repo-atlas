# pr1m8/haive

⭐ 24 · Python · MIT · 推送 2026-04-29 · [GitHub](https://github.com/pr1m8/haive) · [官网](https://github.com/pr1m8/haive) · 个人维护

**构建 LLM Agent 的 Python 框架：53+ 现成 Agent、RAG 与记忆**

基于 LangGraph/LangChain 之上的 Python 多包 monorepo 框架，以 9 个 PyPI 包分发，覆盖 Agent 模式（Simple/React/Multi/Memory）、22+ 种 RAG 变体、推理与规划 Agent、持久记忆（PostgreSQL+pgvector）与知识图谱抽取（Neo4j）。提供自动工具路由、状态 schema、MCP 动态工具接入（1,960+ 服务器）、Docker Compose 基础设施与 80+ 可运行 demo。面向需要生产级多 Agent 管线的开发者，各包可按需单独安装。

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

- 53+ 生产级 Agent 实现与 22+ RAG 变体
- 持久记忆 + 从对话自动抽取知识图谱（PostgreSQL/Neo4j）
- 以 9 个 PyPI 包按需安装的 monorepo 结构
- MCP 动态工具集成（1,960+ 服务器）

## 适用场景

- 用现成 Agent 模式快速搭建带记忆与 RAG 的多 Agent 管线
- 在 PostgreSQL+Neo4j 上做带知识图谱的长期记忆 Agent
- 通过 MCP 在运行时接入外部工具生态

## 场景标签

`Agent 框架` `多智能体` `Agent 记忆` `知识图谱` · 领域:Agent 开发

## 证据(README 行号)

> L7: **Production-ready Python framework for building LLM-powered agents.** From simple chatbots to complex multi-agent p
> L13: Haive is a production-grade framework built on top of LangGraph and LangChain. It fills the gap between raw state m
> L15: The framework is organized as a monorepo with **9 published PyPI packages**, each focused on a specific concern. Yo

## 星数曲线

```mermaid
xychart-beta
    title "pr1m8/haive 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 23 --> 25
    line [24, 24]
```

2026-10-18 24 → 2026-10-31 24（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 mid · 依据 README sha `40b333a9ebe4` · [字段定义](../../DATASET.md)*
