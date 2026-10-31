# rhgs/crewai-go

⭐ 14 · Go · MIT · 推送 2026-09-23 · [GitHub](https://github.com/rhgs/crewai-go) · [官网](https://pkg.go.dev/github.com/rhgs/crewai-go) · 个人维护

**Go 语言多智能体编排框架，CrewAI 的惯用移植**

用 Go 标准库实现的多智能体协作编排框架，是 Python CrewAI 框架的移植。开发者以 Agent/Task/Crew/Tool/Flow 等类型组装智能体团队，支持 Sequential/Hierarchical/Staged 三种执行策略、异步任务波、可插拔 MemoryStore 记忆、带 JSON Schema 校验的结构化输出、Guardrails 输出拦截与带溯源的 Fact 类型。LLM 接入通过实现 LLM 接口完成，内置 OpenAI、Anthropic、Ollama、xAI 等提供方，工具调用支持 ReAct 与原生 function calling 两种模式。零外部依赖，需 Go 1.24+，通过 go get 安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 零外部依赖，仅用 Go 标准库实现
- Sequential/Hierarchical/Staged 三种编排策略与类型化 Flow[S] 事件驱动运行器
- 内置 OpenAI/Anthropic/Ollama/xAI 等提供方，支持 ReAct 与原生 function calling 双模式
- Fact 类型带完整溯源元数据，仅由确定性连接器工具填充
- Web 搜索结果经 SSRF 防护过滤（本地/私有 IP、DNS rebinding 防护）

## 适用场景

- 在 Go 项目中编排多智能体协作完成复杂任务
- 需要带结构化输出与业务规则校验的 LLM 工作流
- 接入 MCP 服务器将其工具暴露给智能体调用

## 场景标签

`Agent 框架` `多智能体` · 领域:Agent 开发

## 证据(README 行号)

> L17: **Orchestration of autonomous, collaborative AI agents in Go.**
> L19: `crewai-go` is an idiomatic Go port of the CrewAI framework. It lets you assemble teams (_crews_) of agents with di

## 星数曲线

```mermaid
xychart-beta
    title "rhgs/crewai-go 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-29", "2026-10-31"]
    y-axis "stars" 12 --> 15
    line [13, 14, 14]
```

2026-10-18 13 → 2026-10-31 14（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 mid · 依据 README sha `50d66cf84cea` · [字段定义](../../DATASET.md)*
