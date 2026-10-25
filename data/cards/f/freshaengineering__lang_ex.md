# freshaengineering/lang_ex

⭐ 45 · Elixir · MIT · 推送 2026-09-16 · [GitHub](https://github.com/freshaengineering/lang_ex) · [官网](https://hexdocs.pm/lang_ex) · 组织维护

**Elixir 的有状态 LLM agent 框架：图编排+检查点持久化**

运行于 BEAM 上的 LangGraph 风格 agent 框架：以函数为节点、路由为边编写图，compile 后 invoke 运行；通过检查点（内存/Redis/Postgres）实现崩溃恢复与 human-in-the-loop 中断续跑。支持 Anthropic/OpenAI/Gemini 三类模型（按模型字符串前缀选择，API key 从 opts/应用配置/环境变量解析）、流式输出、swarm/supervisor 多 agent 协作、中间件、子图、加密检查点与 OpenTelemetry。以 Hex 包形式安装，提供多数无需 API key 的示例脚本。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 图即数据：函数节点+compile/invoke，检查点支持崩溃恢复与人工中断续跑
- Memory/Redis/Postgres 三种检查点后端
- swarm 转交与 supervisor 委派两种多 agent 模式
- 流式 token/节点事件输出，可接入 LiveView/PubSub

## 适用场景

- 在 Elixir/Phoenix 应用中构建可恢复的 LLM agent 工作流
- 实现需要人工审批后继续执行的 agent 流程
- 搭建多 agent 协作（转交/委派）的对话系统

## 场景标签

`Agent 框架` `多智能体` · 领域:Agent 开发

## 证据(README 行号)

> L8: Stateful LLM agents for Elixir. You write functions, wire them into a graph, and the BEAM keeps the run alive — acro
> L19: Inspired by LangGraph. Built on functions, messages, and supervisors — not threads and async/await.
> L24: - **Checkpoints, not processes.** Memory, Redis, or Postgres. Crash mid-step, resume the thread. Pause for a human,

## 星数曲线

```mermaid
xychart-beta
    title "freshaengineering/lang_ex 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 44 --> 46
    line [45, 45]
```

2026-10-18 45 → 2026-10-25 45（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `5ddd39a19913` · [字段定义](../../DATASET.md)*
