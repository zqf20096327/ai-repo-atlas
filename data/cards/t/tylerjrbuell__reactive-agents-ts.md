# tylerjrbuell/reactive-agents-ts

⭐ 31 · TypeScript · MIT · 推送 2026-10-28 · [GitHub](https://github.com/tylerjrbuell/reactive-agents-ts) · [官网](https://docs.reactiveagents.dev) · 个人维护

**TypeScript agent 框架：可控执行与可观测的 agent 运行构建**

基于 Effect-TS 的开源 TypeScript agent 构建框架（harness）：提供 12 阶段确定性执行引擎、8 种推理策略、4 层记忆、8 个 LLM 提供商接入（含本地 Ollama 与 LiteLLM），支持工具调用修复、崩溃恢复、验证与签名证据回执。可观测性包括类型化事件、OTLP 分布式追踪、SSE 流式输出与本地 Cortex Studio 调试界面。能力以 .with() 构建器逐层 opt-in 组合，面向需要在本地小模型与前沿 API 上以同一代码运行 agent 循环的开发者。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 12 阶段确定性执行引擎，每阶段带 before/after/on-error 钩子
- 8 个 LLM 提供商接入，含 Ollama 本地模型与 LiteLLM
- 工具调用修复管道、模型自适应上下文与崩溃恢复
- 每次运行返回签名 receipt 与证据账本

## 适用场景

- 用 TypeScript 构建可在本地模型与前沿 API 上运行的 agent
- 对 agent 执行过程做逐步追踪、回放与调试
- 构建带护栏、成本路由与验证的生产级 agent 流水线

## 场景标签

`Agent 框架` `LLM 可观测性` · 领域:Agent 开发

## 证据(README 行号)

> L5: The transparent, composable harness for TypeScript agents. The same code runs the full agent loop on a local 4B mode
> L21: - 🛡️ **Reliable on every model tier.** Model-adaptive context profiles, tool-call healing, output verification, dur
> L30: |**8 LLM providers**|Anthropic, OpenAI, Gemini, Groq, xAI, Ollama (local), LiteLLM (40+ models), Test|

## 星数曲线

```mermaid
xychart-beta
    title "tylerjrbuell/reactive-agents-ts 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-28"]
    y-axis "stars" 29 --> 32
    line [30, 31, 31]
```

2026-10-18 30 → 2026-10-28 31（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `cafef93bb5e2` · [字段定义](../../DATASET.md)*
