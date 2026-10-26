# agentjido/jido_ai

⭐ 211 · Elixir · Apache-2.0 · 推送 2026-10-25 · [GitHub](https://github.com/agentjido/jido_ai) · [官网](https://jido.run/ecosystem/jido_ai) · 组织维护

**给 Elixir 开发者：为 Jido agent 提供 LLM 编排与推理策略的 AI 运行时层**

jido_ai 是 Jido 生态的核心包，为 Elixir 中的 tool-using agent 提供 AI 运行时：开发者以 Jido.Action 模块定义工具，以 Jido.AI.Agent 定义 agent，运行同步/异步请求，内置模型别名路由、重试与遥测。提供 ReAct、CoD、CoT、AoT、ToT、GoT、TRM、Adaptive 八种推理策略，以及不带 agent 进程的一次性生成助手（generate_text/ask/stream_text）。通过 req_llm 抽象接入 Anthropic、OpenAI、Google 等提供商；当前版本为 2.0.0-rc.0，许可 Apache-2.0。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 八种内置推理策略族（ReAct/CoD/CoT/AoT/ToT/GoT/TRM/Adaptive）
- 模型别名路由、重试与稳定遥测事件（Jido.AI.Observe）
- 策略无关的 Actions API，可经 Jido.Exec.run/3 直接运行
- 策略与配额插件可确定性地改写不安全或超预算请求

## 适用场景

- 在 Elixir 应用中构建带工具调用循环的长生命周期 agent
- 按任务选择不同推理策略（如数学逻辑用 CoT、复杂探索用 ToT/GoT）
- 把 LLM 调用嵌入现有工作流/作业而无需定义 agent 模块

## 场景标签

`Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L15: `jido_ai` is the AI runtime layer for Jido. You define tools and agents as Elixir modules, then run synchronous or 
> L26: `jido_ai` is a **core package** in the Jido ecosystem:

## 星数曲线

```mermaid
xychart-beta
    title "agentjido/jido_ai 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 210 --> 212
    line [211, 211]
```

2026-10-18 211 → 2026-10-26 211（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `375c540667b9` · [字段定义](../../DATASET.md)*
