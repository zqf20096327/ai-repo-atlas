# aiperceivable/apcore-python

⭐ 15 · Python · Apache-2.0 · 推送 2026-10-24 · [GitHub](https://github.com/aiperceivable/apcore-python) · [官网](https://aipartnerup.com/) · 组织维护

**面向 AI 可调用能力的受治理模块开发框架**

apcore 是一个 schema 驱动的 Python 模块开发与治理运行时：开发者用 Pydantic 或 JSON Schema 定义输入/输出契约，通过 @module 装饰器与 YAML 绑定注册模块，供代码或 AI 调用。每次调用经过完整执行管道：ACL 授权、可插拔审批门、中间件、输入输出验证与审计。内置可观测性（tracing/metrics/结构化日志、Prometheus 端点）、熔断器、异步任务管理与行为注解（readonly/destructive 等）。与 TypeScript/Rust SDK 保持契约对齐。

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

- Schema 驱动模块：Pydantic/JSON Schema 定义输入输出契约，供代码与 AI 调用
- 完整执行管道：ACL、可插拔审批门、中间件、双重验证与审计事件
- 内置可观测性：OTEL tracing、指标、Prometheus /metrics /healthz 端点
- 熔断器、调用深度限制、频率节流等安全防护与行为注解

## 适用场景

- 为 AI agent 暴露受 ACL 与审批控制的可调用能力
- 构建每次调用可验证、可审计的模块化服务
- 需要跨 Python/TypeScript/Rust 保持契约一致的多语言团队

## 场景标签

`Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L12: A governed runtime for agent-callable capabilities — schema, ACL, approval, and audit enforced at every call.
> L14: **apcore** is an AI-Perceivable module standard that makes every interface naturally perceivable and understandable

## 星数曲线

```mermaid
xychart-beta
    title "aiperceivable/apcore-python 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-30 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `99beb3a6160c` · [字段定义](../../DATASET.md)*
