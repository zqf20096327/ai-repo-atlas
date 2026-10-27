# sagents-ai/sagents_live_debugger

⭐ 30 · Elixir · NOASSERTION · 推送 2026-10-24 · [GitHub](https://github.com/sagents-ai/sagents_live_debugger) · [官网](https://hexdocs.pm/sagents_live_debugger/) · 组织维护

**给 Elixir Sagents 开发者的实时 agent 调试监控面板**

基于 Phoenix LiveView 的调试仪表盘，面向使用 Sagents 框架构建 agent 的 Elixir 开发者。通过 Phoenix Presence 实时发现运行中的 agent（无轮询），提供消息历史（含工具调用与 thinking 块）、事件流（LLM 调用、中间件动作、工具执行）、todo 跟踪与子 agent 全生命周期监控。以 Hex 依赖安装，挂载到 Phoenix 路由即可使用；自包含插件设计，宿主应用无需编译 JS/CSS。浏览器时区显示需配置 Calendar.TimeZoneDatabase，否则回退 UTC。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Phoenix Presence 实时 agent 发现，无轮询
- 完整消息历史：工具调用、结果与 thinking 块
- 子 agent 生命周期、配置、消息与工具的监控
- 自包含插件设计，宿主无需编译 JS/CSS，支持 CSP nonce

## 适用场景

- 开发时实时查看 agent 对话、工具调用与事件流
- 排查子 agent 委派任务的指令与响应
- 生产环境通过过滤器选择并跟踪特定 agent

## 场景标签

`LLM 可观测性` · 领域:评测与运维

## 证据(README 行号)

> L3: A Phoenix LiveView dashboard for debugging and monitoring Sagents agents in real-time. Provides visibility into agen
> L12: - **Event Stream**: Live feed of agent events (LLM calls, middleware actions, tool executions)

## 星数曲线

```mermaid
xychart-beta
    title "sagents-ai/sagents_live_debugger 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 29 --> 31
    line [30, 30]
```

2026-10-18 30 → 2026-10-27 30（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `9e3fd89fd7dc` · [字段定义](../../DATASET.md)*
