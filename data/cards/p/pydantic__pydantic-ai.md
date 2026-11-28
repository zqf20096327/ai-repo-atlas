# pydantic/pydantic-ai

⭐ 21,431 · Python · MIT · 推送 2026-11-27 · [GitHub](https://github.com/pydantic/pydantic-ai) · [官网](https://pydantic.dev/pydantic-ai) · 组织维护

**Python AI SDK：类型化构建与运行 AI Agent**

Pydantic AI 是一个 Python AI SDK，提供类型化的 Agent 循环，支持模型以字符串切换与失败回退。同一 Agent 定义可运行在 Web 前端、终端、语音通话、后台队列、GitHub Actions 等多种接口；随包提供图像生成与 embeddings。配套 Pydantic AI Harness 以能力（capability）形式提供记忆、护栏、子 Agent、规划、持久化等组件；Pydantic Evals 用于评测 Agent 输出与工具调用轨迹；经 OpenTelemetry 原生插桩接入任意后端。安装通过 uv/pypi，内置 'test' 模型可在无 API key 情况下起步。

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

## 动量与使用信号

- 维护:`active` — 距上次 push 0.7 天,年发版 100,475 位贡献者
- 涨星:近 1 天 **+25**(自 20261016 起算)
- 平台:— · 协议:MCP / OLLAMA

## 能力要点

- 任意模型以字符串切换，提供 failover 机制
- 端到端类型化：结构化输出、类型化依赖注入与工具
- 实时语音会话（OpenAI Realtime、Gemini Live、Azure、xAI Grok Voice）
- 九种持久执行引擎（Temporal、DBOS、Prefect 等）

## 适用场景

- 用 Python 构建带结构化输出的 LLM Agent
- 搭建可在终端或 Web 界面运行的编码 Agent
- 在后台队列中运行需要跨重启存续的长时 Agent 任务
- 为 Agent 运行接入追踪与成本监控

## 场景标签

`Agent 框架` `模型评测` · 领域:Agent 开发

## 证据(README 行号)

> L16:  Agents, realtime voice, image generation, embeddings. Every model, every interface, typed end to end.
> L18: **Pydantic AI** is the Python AI SDK: a typed, extensible agent loop with every model a string swap away, and anoth
> L158: - **Any model, one Python API.** Virtually every model and provider (OpenAI, Anthropic, Google, Bedrock, Azure AI 

## 星数曲线

```mermaid
xychart-beta
    title "pydantic/pydantic-ai 星数(近 27 点)"
    x-axis ["2026-10-26", "2026-10-27", "2026-10-28", "2026-10-29", "2026-10-30", "2026-10-31", "2026-11-01", "2026-11-02", "2026-11-06", "2026-11-08", "2026-11-10", "2026-11-11", "2026-11-12", "2026-11-13", "2026-11-14", "2026-11-15", "2026-11-16", "2026-11-18", "2026-11-19", "2026-11-20", "2026-11-21", "2026-11-22", "2026-11-23", "2026-11-25", "2026-11-26", "2026-11-27", "2026-11-28"]
    y-axis "stars" 20779 --> 21490
    line [20862, 20886, 20905, 20929, 20947, 20959, 20969, 20981, 20838, 21089, 21125, 21145, 21173, 21194, 21209, 21224, 21247, 21261, 21278, 21295, 21316, 21328, 21337, 21357, 21388, 21415, 21431]
```

2026-10-26 20,862 → 2026-11-28 21,431（+569）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-27 · 置信度 high · 依据 README sha `3a9f0f7d0b8e` · [字段定义](../../DATASET.md)*
