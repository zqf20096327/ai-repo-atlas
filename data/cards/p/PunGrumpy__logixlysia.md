# PunGrumpy/logixlysia

⭐ 271 · TypeScript · MIT · 推送 2026-10-22 · [GitHub](https://github.com/PunGrumpy/logixlysia) · [官网](https://logixlysia.vercel.app) · 个人维护

**面向 ElysiaJS 的结构化日志库**

Logixlysia 是为 Bun 运行时上的 ElysiaJS 框架提供的日志库，以插件方式挂载到 Elysia 实例，为每个请求生成访问日志。功能包括：mergeContext 累积请求上下文字段、dev/prod/json 三种输出预设、按大小/时长/数量轮转的文件日志、九个内置输出目标（Axiom、Better Stack、ClickHouse、Datadog、HyperDX、Loki、OTLP、PostHog、Sentry）、头/尾采样控制、日志增补字段、HttpError 结构化错误、请求 ID 与 OpenTelemetry 追踪关联。AI 相关功能为可选的神经脱敏（logixlysia/desertant）与访问日志中的 AI 用量指标。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 九个内置日志输出适配器（Axiom、Datadog、Loki、OTLP 等）
- 按大小/时长/数量轮转的文件日志
- autoRedact 模式脱敏 PII，可选 logixlysia/desertant 神经脱敏
- OpenTelemetry 追踪关联与访问日志中的 AI 用量指标

## 适用场景

- 在 ElysiaJS 服务中接入结构化请求日志
- 将日志转发到 Datadog、Loki、ClickHouse 等观测平台
- 对请求日志中的 PII 做脱敏后落盘或外发

## 场景标签

 · 领域:后端可观测性/日志

## 证据(README 行号)

> L2:  Logixlysia is a logging library for ElysiaJS
> L28: - **Redaction**: `autoRedact` masks PII by pattern; `logixlysia/desertant` adds neural redaction. Config docs, Neur
> L31: - **OpenTelemetry**: trace correlation and AI usage metrics on the access log. Docs

## 星数曲线

```mermaid
xychart-beta
    title "PunGrumpy/logixlysia 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-22"]
    y-axis "stars" 270 --> 272
    line [271, 271]
```

2026-10-18 271 → 2026-10-22 271（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `4c4e024edbbb` · [字段定义](../../DATASET.md)*
