# natexcvi/go-llm

⭐ 158 · Go · MIT · 推送 2026-11-25 · [GitHub](https://github.com/natexcvi/go-llm) · 个人维护

**Go 语言的 LLM agent 构建框架，提供任务编排与可恢复运行**

以 Go 库形式提供的 agent 构建框架：给 agent 一个工作区、任务与预算，框架负责任务拆解、子 agent 委派、上下文压缩、记忆与检查点恢复。应用侧持有工具定义、每次调用的授权决策与运行存储。内置 coder/researcher 预设、代码模式（WASM 内 Starlark REPL 调用工具）、MCP 集成、Chromium 浏览器交互，支持 OpenAI 与 Anthropic 的流式接口及模型回退。需要 Go 1.26+（示例可用 1.25.8+）与支持工具调用的模型。

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

- Planning/Compaction/Memory/Checkpointing 四种长任务机制，支持审批暂停与进程重启后恢复
- Options.Authorize 回调对每次工具调用（含委派调用）做授权决策
- 代码模式：WASM 内 Starlark REPL 批量调用 Go 工具，嵌套调用走父级授权
- models 包提供 OpenAI Chat Completions/Responses 与 Anthropic Messages 流式接入

## 适用场景

- 在 Go 应用中集成可暂停审批、可断点恢复的 agent 工作流
- 构建代码仓库调查/回归排查类 coding agent
- 需要子 agent 委派与共享工具调用预算的多步任务编排

## 场景标签

`Agent 框架` `编码 Agent` · 领域:Agent 开发

## 证据(README 行号)

> L3: **A Go harness for deep agents.** Give an agent a workspace, a task, and a budget. It can break the task into steps,
> L89: |models|Streaming OpenAI Chat Completions, OpenAI Responses, Anthropic Messages, and model fallback.|
> L91: |integrations|MCP tool discovery and execution, hosted service adapters, and search providers for research agents.|


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 high · 依据 README sha `5cff0ca12928` · [字段定义](../../DATASET.md)*
