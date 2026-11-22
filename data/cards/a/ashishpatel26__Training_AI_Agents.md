# ashishpatel26/Training_AI_Agents

⭐ 3 · Jupyter Notebook · 推送 2026-10-21 · [GitHub](https://github.com/ashishpatel26/Training_AI_Agents) · 个人维护

**用 LangChain/LangGraph 与本地模型学习 LLM Agent 的实操教程**

由 Ashish Patel 维护的教学仓库：11 个 Jupyter notebook 按从零到部署的顺序讲解 LLM Agent 构建，覆盖无框架的 agent loop、LangGraph 图结构、工具调用、持久化、MCP 工具，以及 RAG Agent 与研究 Agent 两个项目。模型通过 Ollama 本地运行（默认 qwen3.5-4b-16k），无需 OpenAI key，但联网搜索需要 Tavily API key。用 uv 管理依赖，另附可部署的 research agent demo（langgraph dev）与速查表、参考链接。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 11 个按序编排的 notebook，覆盖 agent loop、LangGraph 核心概念到部署
- 全部笔记本使用 Ollama 本地模型，无需 OpenAI key
- 附带可部署的 LangGraph research agent demo（本地服务端口 2024）
- 含自定义 MCP server（2.2 模块使用）

## 适用场景

- 系统学习用 LangChain/LangGraph 构建 LLM Agent
- 在没有云 API key 的本地环境练习 agent 开发
- 部署一个研究型 agent demo 作为项目起点

## 场景标签

 · 领域:AI 教育/开发教程

## 证据(README 行号)

> L3: Hands-on notebooks and a deployable demo for building LLM agents with LangChain and LangGraph — running on **local m
> L88: |#|Module|Notebook|What you'll learn|Colab|
> L90: |0.0|Foundations|Intro to LLM Agents from Scratch|Agent loop, tool calling and memory — no framework|Open In Colab|

## 星数曲线

```mermaid
xychart-beta
    title "ashishpatel26/Training_AI_Agents 星数(近 2 点)"
    x-axis ["2026-10-23", "2026-11-22"]
    y-axis "stars" 2 --> 4
    line [3, 3]
```

2026-10-23 3 → 2026-11-22 3（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-22 · 置信度 mid · 依据 README sha `da9e9afbc8a7` · [字段定义](../../DATASET.md)*
