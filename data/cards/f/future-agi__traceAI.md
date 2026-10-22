# future-agi/traceAI

⭐ 224 · Python · Apache-2.0 · 推送 2026-10-21 · [GitHub](https://github.com/future-agi/traceAI) · [官网](https://app.futureagi.com) · 组织维护

**面向 AI 应用的 OpenTelemetry 埋点追踪框架**

基于 OpenTelemetry 的开源 AI 可观测性框架，面向构建 LLM 应用与 agent 的开发者：以 drop-in 埋点方式捕获每次 LLM 调用、prompt、token 用量、检索步骤、工具调用与 agent 决策，生成结构化 OTel trace，发送到 Datadog、Grafana、Jaeger、Future AGI 等任意 OTel 兼容后端。提供 Python、TypeScript、Java、C# 四语言一致的 API，覆盖 50+ 框架集成（LLM 提供商、agent 框架、向量数据库）。限制：需接入 OTel 兼容后端存储与查看 trace。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 捕获 prompt、补全、token、模型参数、工具调用、流式分块与错误上下文
- 50+ AI 框架集成，覆盖 Python/TypeScript/Java/C# 四语言
- OpenTelemetry 原生，支持任意 OTel 兼容后端（OTLP HTTP/gRPC）
- 3 行代码 drop-in 埋点，无需重构现有代码

## 适用场景

- 为生产环境 LLM 应用与 agent 做调用链追踪与排障
- 定位回答出错时具体是哪个检索、工具或 prompt 环节失效
- 在现有 Datadog/Grafana/Jaeger 体系中统一观测 AI 工作流

## 场景标签

 · 领域:AI 可观测性/LLM 基础设施

## 证据(README 行号)

> L5: **Open-source observability for AI applications - trace every LLM call, prompt, token, retrieval step, and agent dec
> L7: Built on OpenTelemetry, traceAI sends structured traces to any OTel-compatible backend (Datadog, Grafana, Jaeger, Fu
> L30: - **Drop-in instrumentation** for 50+ AI frameworks across 4 languages

## 星数曲线

```mermaid
xychart-beta
    title "future-agi/traceAI 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-22"]
    y-axis "stars" 222 --> 225
    line [223, 224, 224]
```

2026-10-18 223 → 2026-10-22 224（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `f024477e2dc0` · [字段定义](../../DATASET.md)*
