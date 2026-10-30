# jenasuraj/Ai_agents

⭐ 15 · Python · 推送 2026-06-10 · [GitHub](https://github.com/jenasuraj/Ai_agents) · 个人维护

**基于 LangGraph/MCP 的多智能体实验集合（10 个 agent）**

个人维护的多智能体实验仓库：包含网页抓取、播客生成、股票分析、GitHub 自动化、Notion Copilot、Agentic RAG、监督者编排等 10 个 agent，均基于 LangGraph 图式控制流与 LangChain 编排构建，通过 MCP SDK 接入外部工具，调用 Tavily/Firecrawl/ElevenLabs/OpenRouter 等外部 API。仓库正从脚本集合重构为 agent 平台：实验 agent 位于 projects/，共享代码位于 src/ai_agents/。通过 git clone、pip 安装依赖并设置 .env 中的 API key 运行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 10 个面向具体工作流的实验 agent（抓取/播客/股票/GitHub/Notion/RAG 等）
- 监督者-工作者图式编排，经 ToolNode 路由工具调用并合成最终回答
- MCP（Model Context Protocol）支持接入外部工具
- 共享平台层 src/ai_agents/ 提供基类、注册表与配置约定

## 适用场景

- 学习 LangGraph 监督者-工作者与工具调用路由的构建方式
- 参考具体工作流 agent（抓取、播客、RAG）的实现结构
- 按模板新增自己的 agent 到平台结构中

## 场景标签

`多智能体` · 领域:Agent 开发

## 证据(README 行号)

> L12:  A modular AI agent experimentation hub built with LangGraph, LangChain, MCP, and Python.
> L16: **AI Agents with MCP and LangGraph** is a multi-agent experimentation hub where each agent is designed around a spe
> L137: - **LangChain**: LLM application framework

## 星数曲线

```mermaid
xychart-beta
    title "jenasuraj/Ai_agents 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-30 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `7b2b7669c299` · [字段定义](../../DATASET.md)*
