# miquido/draive

⭐ 111 · Python · MIT · 推送 2026-09-16 · [GitHub](https://github.com/miquido/draive) · [官网](https://www.miquido.com/) · 组织维护

**构建生产级 LLM agent 与工作流的 Python 框架**

由 Miquido 开发的 Python 框架，面向开发团队构建 GenAI 系统：提供类型化输出（State 模型）、工具编排（任意 Python 函数转为 LLM 可调用工具）、多模态内容处理、检索（内置 embeddings 与 VectorIndex）、评测、guardrails 与 OpenTelemetry 可观测性。执行模型基于 ctx.scope 提供状态管理与依赖生命周期控制。可选集成 OpenAI、Anthropic、Gemini、Mistral、Ollama、vLLM、Bedrock 等多种模型服务，以及 Postgres、Qdrant、SurrealDB、RabbitMQ 等。要求 Python 3.14 或更新版本，MIT 许可。

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

- 类型化结构化输出，生成经验证的 State 对象
- 任意 Python 函数可注解为 LLM 工具
- 内置评测、guardrails 与 OpenTelemetry 可观测性钩子
- 通过可选 extras 接入 OpenAI/Anthropic/Gemini/Mistral/Ollama/vLLM/Bedrock 等提供商

## 适用场景

- 构建自主 agent 或文档信息抽取应用
- 在不同模型提供商间切换而无需重写业务流程
- 为 LLM 应用搭建带评测与监控的 CI 流程
- 构建带检索（RAG）的工作流

## 场景标签

`Agent 框架` `RAG` · 领域:Agent 开发

## 证据(README 行号)

> L9: 🏎️ Build production-ready GenAI systems with strict typing, clean architecture, and fast iteration.
> L45: Draive is built for developers who want clarity, flexibility, and control when working with LLMs.
> L74: - **Model-Agnostic by Design**: Built-in support for major hosted and self-hosted providers.

## 星数曲线

```mermaid
xychart-beta
    title "miquido/draive 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 110 --> 112
    line [111, 111]
```

2026-10-18 111 → 2026-10-24 111（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `808deed7c317` · [字段定义](../../DATASET.md)*
