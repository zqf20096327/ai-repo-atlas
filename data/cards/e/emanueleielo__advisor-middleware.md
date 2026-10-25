# emanueleielo/advisor-middleware

⭐ 45 · Python · MIT · 推送 2026-10-05 · [GitHub](https://github.com/emanueleielo/advisor-middleware) · [官网](https://pypi.org/project/advisor-middleware/) · 个人维护

**把 Anthropic Advisor 策略做成 DeepAgents 即插中间件**

开源 Python 中间件，在 LangChain DeepAgents 框架上实现 Anthropic 的 Advisor 策略：小模型作为 executor 端到端执行，强模型仅在关键决策时被咨询。提供双模式：Anthropic executor 下注入原生 advisor_20260301 服务端工具（零额外往返），其他 provider 走直接 LLM 调用的 fallback 模式。含成本护栏（每轮/每会话调用上限）、上下文裁剪配置与用量内省接口，由个人作者以 MIT 许可维护，经 pip 发布。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 原生模式注入 advisor_20260301 服务端工具，零额外往返
- fallback 模式支持任意 executor/advisor 模型组合
- 成本护栏：max_uses_per_turn / max_uses_per_session 上限
- ContextCurationConfig 控制转发给 advisor 的上下文预算

## 适用场景

- DeepAgents 项目中用便宜模型执行、贵模型按需把关以控制成本
- 跨 provider 场景下给任意 executor 挂接指定 advisor 模型
- 追踪 agent 运行中 advisor 的实际调用次数与开销

## 场景标签

`Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L3:  Anthropic's Advisor Strategy as a drop-in DeepAgents middleware.
> L20: **advisor-middleware** makes this a single import for DeepAgents. It handles provider detection, native API routing
> L42: The middleware operates in **two modes** depending on the executor's provider:

## 星数曲线

```mermaid
xychart-beta
    title "emanueleielo/advisor-middleware 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 44 --> 46
    line [45, 45]
```

2026-10-18 45 → 2026-10-25 45（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `8015a8248181` · [字段定义](../../DATASET.md)*
