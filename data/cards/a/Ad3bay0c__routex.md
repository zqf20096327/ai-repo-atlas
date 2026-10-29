# Ad3bay0c/routex

⭐ 25 · Go · MIT · 推送 2026-07-06 · [GitHub](https://github.com/Ad3bay0c/routex) · 个人维护

**Go 语言多智能体运行时：YAML 定义 crews，运行时调度与监督**

面向 Go 开发者的轻量 AI agent 运行时：用 goroutine 与 channel 实现 agent，支持以 YAML 或纯 Go 代码定义多智能体 crew。调度器对依赖关系做拓扑排序并行执行，Supervisor 借鉴 Erlang/OTP 提供三种重启策略与重启预算。支持 Anthropic/OpenAI/Ollama/Gemini 四种 LLM 提供商及按 agent 指定不同模型，内置 11 个工具，可接入任意 MCP 工具服务器，内存后端默认为 inmem、可选 Redis 持久化。提供 CLI 与 Go 库两种使用方式。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- YAML 或纯 Go 定义 crew，调度器按 DAG 拓扑排序并行执行
- Erlang/OTP 风格 Supervisor，三种重启策略与重启预算
- 支持 Anthropic/OpenAI/Ollama/Gemini，可按 agent 指定不同 LLM
- 接入任意 MCP 工具服务器，启动时自动发现工具

## 适用场景

- 在 Go 服务中编排多智能体工作流，不引入 Python 运行时
- 为不同任务分配不同 LLM 模型
- 通过 CLI 快速运行 YAML 定义的多智能体任务

## 场景标签

`多智能体` `Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L15: **A lightweight AI agent runtime for Go.**
> L17: Routex lets you build, run, and supervise multi-agent AI crews using the primitives Go developers already know — go

## 星数曲线

```mermaid
xychart-beta
    title "Ad3bay0c/routex 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 24 --> 26
    line [25, 25]
```

2026-10-18 25 → 2026-10-29 25（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 mid · 依据 README sha `db7588eb339a` · [字段定义](../../DATASET.md)*
