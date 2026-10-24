# traccia-ai/traccia-py

⭐ 127 · Python · Apache-2.0 · 推送 2026-10-21 · [GitHub](https://github.com/traccia-ai/traccia-py) · [官网](https://traccia.ai/) · 组织维护

**AI agent 可观测与治理 SDK：追踪、评测、运行时策略执行**

基于 OpenTelemetry 的 Python SDK，面向生产环境的 AI agent 与 LLM 应用：提供分布式追踪、token 与成本统计、guardrail 检测（三层：显式/提供商原生/启发式）、离线评测与 CI 质量门禁、提示词管理与 EU AI Act/HIPAA 导向的合规证据。运行时策略用 @govern 拒绝或改写 LLM/工具调用（如 Spend Cap、Model Boundary）。自动插桩 OpenAI/Anthropic/Gemini，并集成 LangChain、CrewAI、OpenAI Agents SDK；部分功能（提示词注册表、实验保存）依赖 Traccia 平台与 API key。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 基于 OpenTelemetry 的分布式追踪与 token/成本统计，OTLP 导出至 Grafana Tempo/Jaeger/Zipkin/SigNoz
- @govern 运行时策略（Spend Cap、Model Boundary、Loop Cap）可拒绝或改写 LLM/工具调用
- 三层 guardrail 检测：显式标注、提供商原生信号（OpenAI/Anthropic/Gemini 等）、启发式关键词
- traccia eval 在 CI 中以退出码作质量门禁，支持 pass-rate 与成本阈值

## 适用场景

- 生产环境 AI agent 的调用追踪、成本与延迟监控
- 在 CI 中对 agent 任务跑评测并设置质量门禁
- 按策略限制模型的支出上限与可用模型边界
- 生成面向 EU AI Act/HIPAA 的治理与合规证据

## 场景标签

`LLM 可观测性` `模型评测` · 领域:评测与运维

## 证据(README 行号)

> L5: Traccia is a production-ready Python SDK for **observing, evaluating, and enforcing policies on AI agents and LLM ap
> L7: Built on OpenTelemetry, Traccia provides distributed tracing, token and cost tracking, evaluation, governance eviden
> L9: Framework-agnostic and built for **OpenAI Agents, LangGraph, CrewAI, and LLM applications in production.**

## 星数曲线

```mermaid
xychart-beta
    title "traccia-ai/traccia-py 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 126 --> 128
    line [127, 127]
```

2026-10-18 127 → 2026-10-24 127（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `78ccc3e8ee32` · [字段定义](../../DATASET.md)*
