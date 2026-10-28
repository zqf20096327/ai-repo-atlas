# hoangsonww/Agentic-AI-Pipeline

⭐ 86 · Python · Apache-2.0 · 推送 2026-09-27 · [GitHub](https://github.com/hoangsonww/Agentic-AI-Pipeline) · [官网](https://hoangsonww.github.io/Agentic-AI-Pipeline) · 个人维护

**多阶段研究外联 AI agent：规划-检索-推理后生成引用简报与邮件草稿**

基于 LangGraph 状态机（plan→decide→act→tools→reflect→finalize）的多阶段 agent，内置参考任务 DossierOutreachAgent：给定主题或公司，通过网页搜索、URL 抓取、计算器、知识库检索等工具链生成带引用的简报并可选起草外联邮件。记忆系统含 SQLite 会话存储与 ChromaDB 向量知识库（RAG）。附带 Agentic RAG 流水线（Gemini+FAISS）与自主编码流水线（GPT+Claude+Gemini QA）。模型支持 OpenAI 与 Anthropic，通过 MODEL_PROVIDER 切换。部署提供 Docker Compose、Terraform 多云模块与 Kubernetes 清单；安装走 Makefile/venv 或 Docker。

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

- LangGraph 状态机多阶段推理，单步原子动作（plan/decide/act/reflect/finalize）
- 双记忆系统：SQLite 会话存储 + ChromaDB 向量知识库
- 工具链：网页搜索、URL 抓取、计算器、文件写入、邮件草稿、知识库增查
- 附带 Agentic RAG 与自主编码两个子流水线及 MCP 控制面

## 适用场景

- 对指定公司或主题自动生成带引用的研究简报
- 自动起草个性化外联邮件草稿
- 搭建可扩展的 agentic 系统参考架构并二次开发

## 场景标签

`Agent 框架` `RAG` `科研工具` · 领域:Agent 开发

## 证据(README 行号)

> L55: A **full‑fledged, multi‑stage, agentic chatbot** that **plans → discovers → reasons → uses tools → learns**.
> L56: The reference task baked into this repo is a **Research & Outreach Agent** (“**DossierOutreachAgent**”): given a to
> L99: |Reasoning & Planning|`src/agentic_ai/layers/reasoning.py`, `graph.py`|

## 星数曲线

```mermaid
xychart-beta
    title "hoangsonww/Agentic-AI-Pipeline 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 85 --> 87
    line [86, 86]
```

2026-10-18 86 → 2026-10-28 86（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `a74f3d0328bc` · [字段定义](../../DATASET.md)*
