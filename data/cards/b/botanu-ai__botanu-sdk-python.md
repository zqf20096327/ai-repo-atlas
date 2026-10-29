# botanu-ai/botanu-sdk-python

⭐ 17 · Python · Apache-2.0 · 推送 2026-08-18 · [GitHub](https://github.com/botanu-ai/botanu-sdk-python) · 组织维护

**基于 OpenTelemetry 的 AI 工作流单事件成本归因 Python SDK**

面向 AI 公司的 Python SDK，构建在 OpenTelemetry 之上，对 AI 工作流做事件级成本归因：一个 event 对应一笔业务交易（如处理一张工单），其下多次 LLM 调用、HTTP 与 DB 调用通过 event_id 关联，实现按客户/按事件的成本与结果追踪。提供 with 块与装饰器两种 API，支持多阶段工作流、跨服务上下文传播、Kubernetes 零代码插桩、PII 清洗的内容捕获，兼容已有 OTel/Datadog 环境。需 Python 3.9+ 和 OpenTelemetry Collector（可自托管）。

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

- event_id 关联多次 LLM/HTTP/DB 调用实现单事件成本归因
- with 块与装饰器 API，支持 sync/async 与多阶段 step
- Kubernetes 零代码插桩与跨服务/队列上下文传播
- 兼容已有 OpenTelemetry / Datadog 部署

## 适用场景

- 按客户核算 AI 功能的真实单位成本
- 为按结果定价提供成本与结果数据支撑
- 在企业现有可观测性体系上叠加 AI 成本追踪

## 场景标签

`LLM 可观测性` · 领域:评测与运维

## 证据(README 行号)

> L5: botanu is platform that helps AI companies understand the real cost of their AI features per customer, enabling outc
> L6: This SDK is built on OpenTelemetry for event-level cost attribution for AI workflow. For more email- deborah@botanu.
> L10: An **event** is one business transaction — resolving a support ticket, processing an order, generating a report. Ea

## 星数曲线

```mermaid
xychart-beta
    title "botanu-ai/botanu-sdk-python 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-24", "2026-10-29"]
    y-axis "stars" 16 --> 19
    line [18, 17, 17]
```

2026-10-18 18 → 2026-10-29 17（-1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `d9fe19c5a300` · [字段定义](../../DATASET.md)*
