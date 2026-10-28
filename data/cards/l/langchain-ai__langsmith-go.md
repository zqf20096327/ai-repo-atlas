# langchain-ai/langsmith-go

⭐ 34 · Go · MIT · 推送 2026-10-28 · [GitHub](https://github.com/langchain-ai/langsmith-go) · 组织维护

**LangSmith 官方 Go SDK：在 Go 应用中访问其 REST API**

由 langchain-ai 维护、经 Stainless 生成的 Go 语言 SDK，为 LangSmith REST API 提供 Go 客户端：配置通过环境变量（LANGSMITH_API_KEY/TENANT_ID/ENDPOINT）或 NewClient 选项完成。功能包括运行查询与自动分页、数据集管理、实验与 Prompt 版本管理、OpenTelemetry 追踪上报（含 OpenAI/Anthropic 调用包装示例）以及沙箱 trace 元数据标注。请求参数用泛型 Field 类型区分零值与 null，支持重试（默认 2 次）、中间件、超时与未公开端点访问。要求 Go 1.22+。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 运行查询、数据集管理、实验记录与 Prompt 仓库管理的 API 封装
- OpenTelemetry 追踪上报，含 OpenAI/Anthropic 客户端包装示例
- 泛型 Field 参数类型区分零值/null/省略，自动重试（默认 2 次）与中间件支持
- 可访问未公开端点、参数与响应字段（ExtraFields/RawJSON）

## 适用场景

- 在 Go 服务中把 LLM 应用的追踪与评测数据上报到 LangSmith
- 用 Go 管理数据集、实验与 Prompt 版本
- 为 OpenAI/Anthropic 的 Go 调用接入自动 OpenTelemetry 追踪

## 场景标签

`LLM 可观测性` · 领域:评测与运维

## 证据(README 行号)

> L5: The LangChain Go library provides convenient access to the LangChain REST API
> L64: - **E2E Evaluation** - Run OpenAI experiments with automatic OpenTelemetry tracing linked to dataset examples

## 星数曲线

```mermaid
xychart-beta
    title "langchain-ai/langsmith-go 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-26", "2026-10-28"]
    y-axis "stars" 32 --> 35
    line [33, 34, 34]
```

2026-10-18 33 → 2026-10-28 34（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `b1d5fb7e5f3d` · [字段定义](../../DATASET.md)*
