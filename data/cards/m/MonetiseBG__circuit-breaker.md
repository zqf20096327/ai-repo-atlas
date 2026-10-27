# MonetiseBG/circuit-breaker

⭐ 30 · TypeScript · Apache-2.0 · 推送 2026-06-23 · [GitHub](https://github.com/MonetiseBG/circuit-breaker) · [官网](https://circuitbreaker.dev) · 组织维护

**给 AI agent 开发者：用一层包装实现预算上限与熔断的执行治理**

一个 npm 安装的 TypeScript 库，为自主 AI agent 的运行提供经济性治理：以 withCircuitBreaker 包装已支持的 agent，在跨过限额时提前截断运行。提供三种模式——budget-guard（默认，输入/输出 token 累计上限）、loop-killer（同状态重复超限即停）、worth-it（按步计成本并预测总开销，在预算耗尽前熔断）。适配 LangChain.js、OpenAI Agents SDK、Claude Agent SDK、Vercel AI SDK、LangGraph Platform SDK，默认零配置（10k/10k token 上限），发出类型化事件与错误。要求 Node ≥ 22，Apache-2.0 许可。

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

- 三种模式：budget-guard / loop-killer / worth-it（成本预测熔断）
- 一个包装函数接入，默认 10k/10k token 上限，零配置
- 五种框架适配器（LangChain.js、OpenAI Agents SDK、Claude Agent SDK、Vercel AI SDK、LangGraph）
- 类型化 CircuitBreakerError 与可订阅的 CircuitBreakerEvent 事件流

## 适用场景

- 给生产环境的自主 agent 加 token 花费硬上限
- 拦截陷入重复循环的 agent 运行
- 在预算耗尽前收到预测告警并提前熔断

## 场景标签

`Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L12: **Circuit Breaker is the one wrapper that stops it.** Wrap any supported agent,
> L67: Shipped adapters, each a drop-in wrapper around the framework you already use:

## 星数曲线

```mermaid
xychart-beta
    title "MonetiseBG/circuit-breaker 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 29 --> 31
    line [30, 30]
```

2026-10-18 30 → 2026-10-27 30（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `a7a11eba6880` · [字段定义](../../DATASET.md)*
