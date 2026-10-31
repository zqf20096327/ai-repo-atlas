# HASHIRU-AI/HASHIRU

⭐ 20 · Python · NOASSERTION · 推送 2026-10-30 · [GitHub](https://github.com/HASHIRU-AI/HASHIRU) · 组织维护

**带预算管理的企业级多智能体框架：CEO agent 调度 agent 与工具**

提供创建与管理 AI agent 和工具的框架：架构为层级系统，CEO agent 管理一组员工 agent 与工具，两者均可由 CEO 自主创建、调用和删除。内置 BudgetManager 追踪资源与开销预算并强制限额，本地模型（Ollama）成本可回收、云模型（Gemini/Groq/Lambda）不可回收。支持多种语言模型接入，提供 Gradio Web 界面，默认经 Auth0 认证、可 --no-auth 跳过。附 HASHIRUBench 基准（另仓库）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- CEO agent 层级管理员工 agent 与工具，可自主创建/调用/删除
- BudgetManager 追踪并强制资源与开销预算限额
- 支持 Ollama/Gemini/Groq/Lambda 多模型接入
- 内置预定义工具与 agent，Gradio Web 界面交互

## 适用场景

- 搭建需要预算控制的多 agent 协作系统
- 在本地与云模型之间按成本管理 agent 调用
- 通过 Web 界面与自建工具的 agent 交互

## 场景标签

`多智能体` `Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L17: This project provides a framework for creating and managing AI agents and tools. It includes features for managing 
> L19: The architecture consists of a hierarchical system where a CEO agent manages a set of employee agents and tools. Bo

## 星数曲线

```mermaid
xychart-beta
    title "HASHIRU-AI/HASHIRU 星数(近 2 点)"
    x-axis ["2026-10-30", "2026-10-31"]
    y-axis "stars" 19 --> 21
    line [20, 20]
```

2026-10-30 20 → 2026-10-31 20（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 mid · 依据 README sha `17af596517b5` · [字段定义](../../DATASET.md)*
