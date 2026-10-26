# Mangaba-ai/mangaba_ai

⭐ 207 · Python · MIT · 推送 2026-10-18 · [GitHub](https://github.com/Mangaba-ai/mangaba_ai) · [官网](https://www.mangaba.ia.br) · 组织维护

**Python 多智能体编排框架：Crews、事件流、ReAct、RAG、MCP/A2A**

面向开发者的多智能体编排 Python 框架，自称 CrewAI + LangChain 的轻量替代方案。核心机制：Crew（Sequential/Hierarchical/Parallel/Consensual 四种流程）与事件驱动的 Flow（@start/@listen/@router、Pydantic 类型化状态、SQLite 持久化可 resume/fork）、ReAct 推理循环与原生 function calling、RAG 管线与知识库（PDF/DOCX/CSV/URL）、统一 Memory（相似度+新近度+重要性召回）、7 类 LLM 提供商互操作与 OpenRouter 动态路由、MCP 工具接入与 A2A 开放协议。附 CLI（create/run/train/test）、guardrails、human-in-the-loop、OpenTelemetry/Langfuse/MLflow 观测。要求 Python 3.10+。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 4 种 Crew 流程 + 事件驱动 Flow（持久化可 resume/fork）
- 7 类 LLM 提供商互操作，OpenRouter 动态路由与自动 fallback
- MCP 外部工具接入（stdio/HTTP）与 A2A 开放协议互操作
- CLI 覆盖 create/run/test/train，项目以 agents.yaml/tasks.yaml 声明

## 适用场景

- 用 Python 编排多智能体协作完成研究、分析类任务
- 搭建带文档知识库（RAG）与持久记忆的智能体应用
- 混合使用多家 LLM 提供商并在其之间做 fallback
- 通过事件流编排带断点恢复的多步骤工作流

## 场景标签

`Agent 框架` `多智能体` `RAG` · 领域:Agent 开发

## 证据(README 行号)

> L13: Framework profissional de orquestração multi-agente com ReAct reasoning, function calling nativo, RAG, memória pers
> L24: Alternativa leve e completa a CrewAI + LangChain em um único pacote, com interoperabilidade real entre provedores, 
> L58: - **7 Provedores LLM** — Google Gemini, OpenAI GPT, Anthropic Claude, HuggingFace, OpenRouter, Ollama e servidores 

## 星数曲线

```mermaid
xychart-beta
    title "Mangaba-ai/mangaba_ai 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-26"]
    y-axis "stars" 206 --> 209
    line [208, 207, 207]
```

2026-10-18 208 → 2026-10-26 207（-1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `198f90be05f3` · [字段定义](../../DATASET.md)*
