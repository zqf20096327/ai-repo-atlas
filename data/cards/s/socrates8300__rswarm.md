# socrates8300/rswarm

⭐ 14 · Rust · MIT · 推送 2026-10-05 · [GitHub](https://github.com/socrates8300/rswarm) · 个人维护

**Rust 库：为生产后端构建多轮 Agent 式 LLM 工作流**

面向 Rust 生产后端团队的 LLM agent 工作流库：提供多轮 Swarm::run 对话、基于 Tool trait 的函数/工具调用（JSON Schema 校验、串行或并行执行）、流式输出、XML 定义执行步骤、SQLite/PostgreSQL 持久化、事件订阅、断路器、升级策略与内容护栏、OpenTelemetry 追踪等能力。通过 OpenAI 兼容的 chat-completions 端点通信。限制：仅支持 Rust；需 OpenAI 兼容端点；持久化向量后端（Qdrant、sqlite-vec）尚未实现，当前仅有内存向量存储。

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

- 多轮对话与 agent 间 handoff、上下文更新的工具调用标记约定
- JSON Schema 校验的工具参数与串行/并行工具执行
- SQLite/PostgreSQL 持久化（会话、事件、检查点、记忆记录）
- 断路器、升级策略、内容护栏与 OpenTelemetry 追踪等生产加固配置

## 适用场景

- 在 Rust 后端服务中实现多 agent 路由与工具调用逻辑
- 为 LLM 工作流添加持久会话历史与事件审计
- 通过断路器与护栏对 provider 和工具故障做生产加固

## 场景标签

`Agent 框架` `多智能体` · 领域:Agent 开发

## 证据(README 行号)

> L3: `rswarm` is a Rust library for agent-style LLM workflows: multi-turn conversations, function and tool calling, strea
> L24: **The mental model:** rswarm sits between "call the OpenAI API yourself" and "use a full LLM application framework.

## 星数曲线

```mermaid
xychart-beta
    title "socrates8300/rswarm 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `538a8ba384fe` · [字段定义](../../DATASET.md)*
