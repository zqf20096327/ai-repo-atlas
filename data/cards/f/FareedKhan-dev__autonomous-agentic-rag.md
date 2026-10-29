# FareedKhan-dev/autonomous-agentic-rag

⭐ 227 · Jupyter Notebook · MIT · 推送 2025-11-13 · [GitHub](https://github.com/FareedKhan-dev/autonomous-agentic-rag) · [官网](https://medium.com/@fareedkhandev/building-self-improving-rag-agentic-system-to-improve-rag-pipeline-f55003af44c4) · 个人维护

**教程/博文：构建自我改进的 Agentic RAG 流水线（医疗领域）**

以博客教程形式逐步讲解如何搭建端到端、可自我改进的 Agentic RAG 系统，面向医疗（临床试验设计）场景：多个专职 agent 协作生成文档，多维评估体系打分，诊断 agent 定位弱点，SOP 架构 agent 提出改进，最终以 Pareto 前沿供人类决策。技术栈为 LangChain/LangGraph 编排，Ollama 本地运行多档开源模型（8B 至 70B 按角色分配），知识库来自 PubMed、FDA 指南、MIMIC-III 等，索引至 FAISS 与 DuckDB，并用 LangSmith 做追踪。仓库以教学讲解为主，非可安装的库。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 多 agent 协作 + 多维评估 + SOP 进化的自我改进闭环
- 按角色分配本地模型（Qwen2 7B / Llama 3.1 8B / Llama 3 70B，经 Ollama 服务）
- 多源医疗知识库（PubMed/FDA/MIMIC-III）索引到 FAISS 与 DuckDB
- LangSmith 全程追踪 agent 交互

## 适用场景

- 学习如何构建自我改进的 Agentic RAG 架构
- 参考医疗领域多 agent RAG 的数据源与模型分配方案
- 了解本地 LLM 分级部署与可观测性配置做法

## 场景标签

`教程课程` `RAG` `多智能体` · 领域:Agent 开发

## 证据(README 行号)

> L5: **A better approach is to let the system learn how to optimize itself**. A typical Agentic RAG pipeline that **evolv
> L19: > We will build a complete end-to-end, self-improving Agentic RAG pipeline that generates different design patterns
> L35: * **Install the Open-Source Stack:** We will set up our environment with all the necessary libraries, focusing on a

## 星数曲线

```mermaid
xychart-beta
    title "FareedKhan-dev/autonomous-agentic-rag 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-24", "2026-10-29"]
    y-axis "stars" 226 --> 229
    line [228, 227, 227]
```

2026-10-18 228 → 2026-10-29 227（-1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 mid · 依据 README sha `b1ef5520312b` · [字段定义](../../DATASET.md)*
