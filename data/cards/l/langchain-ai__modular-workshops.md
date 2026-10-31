# langchain-ai/modular-workshops

⭐ 14 · Jupyter Notebook · 推送 2026-10-29 · [GitHub](https://github.com/langchain-ai/modular-workshops) · 组织维护

**LangChain/LangGraph/DeepAgents 实操教程仓库（模块化工作坊）**

LangChain 官方团队维护的动手教程仓库，是 LangChain Academy 的精简版，设计为在 LangChain 工程师带讲的工作坊场景中运行。内容覆盖 LangChain、LangGraph 与 Deep Agents，含 5 个模块：默认使用 OpenAI 模型（可经 utils/models.py 一行切换供应商）、经 LangSmith Gateway 做部署治理（PII/密钥脱敏、langgraph CLI 部署）、以及读取生产 trace 聚类故障并提议 GitHub PR 修复的 LangSmith Engine 演示。需要 Python 3.11+、uv（或 pip）、多个 API key，在 Jupyter 中运行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 5 个模块覆盖模型切换、Gateway 治理、部署与 Engine 故障分析
- utils/models.py 单行切换模型供应商，无需改动 notebook
- langgraph CLI 部署 agent 到 LangSmith，网关统一策略
- Engine 演示：从生产 trace 聚类故障并提议修复 PR

## 适用场景

- 参加 LangChain 工程师带讲的实操工作坊
- 学习 Deep Agents 与 LangGraph 部署、治理流程
- 了解 LangSmith Gateway 与 Engine 的使用方式

## 场景标签

`教程课程` · 领域:学习与行业

## 证据(README 行号)

> L3: This repository contains hands-on tutorials for learning LangChain, LangGraph, and Deep Agents.
> L5: This is a condensed version of LangChain Academy, intended to be run in a session with a LangChain engineer. If you'

## 星数曲线

```mermaid
xychart-beta
    title "langchain-ai/modular-workshops 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `9e9c7ea03867` · [字段定义](../../DATASET.md)*
