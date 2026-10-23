# christopherkarani/Swarm

⭐ 584 · Swift · MIT · 推送 2026-10-02 · [GitHub](https://github.com/christopherkarani/Swarm) · [官网](https://christopherkarani.github.io/Swarm/) · 个人维护

**Swift 原生 AI agent 运行时：类型安全工具与多 agent 工作流**

面向 Swift 开发者的 agent 运行时库，用 Swift Package Manager 安装。提供编译期从 Swift 类型生成工具 schema 的 @Tool 宏、Workflow/Job 组合原语（串行、并行、路由、超时）、会话与多种记忆策略、guardrails、流式事件与 OpenTelemetry 追踪、MCP 桥接及检查点恢复。推理通过可插拔 InferenceProvider 接入 Apple Foundation Models（设备端）、Ollama、LM Studio、OpenAI 兼容 API 或自定义后端。支持 iOS/macOS 26.0+ 与 Ubuntu 22.04+，Apple 专属功能在 Linux 上不可用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- @Tool 宏在编译期从 Swift 类型生成工具 schema，Swift 6.2 严格并发检查
- Workflow/Job 支持串行、并行、路由、重复与超时的多 agent 组合
- 可插拔 InferenceProvider：Apple Foundation Models 设备端推理、Ollama、LM Studio、OpenAI 兼容 API
- 记忆、guardrails、重试/熔断、流式、MCP、检查点恢复与 OpenTelemetry 追踪

## 适用场景

- 在 iOS/macOS 应用中构建带设备端推理的 AI agent
- 组装串行/并行/路由的多 agent 工作流并做检查点恢复
- Swift 项目中接入 Ollama 或 OpenAI 兼容 API 构建本地/云端 agent
- 为 agent 输入输出与工具参数加校验 guardrails

## 场景标签

`Agent 框架` `多智能体` · 领域:Agent 开发

## 证据(README 行号)

> L5: Swarm is a Swift-native agent runtime for type-safe tools, on-device Apple
> L6: Foundation Models, composable workflows, memory, guardrails, and streaming.
> L105: Every agent uses a pluggable `InferenceProvider`. The agent loop stays the

## 星数曲线

```mermaid
xychart-beta
    title "christopherkarani/Swarm 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-23"]
    y-axis "stars" 583 --> 585
    line [584, 584]
```

2026-10-18 584 → 2026-10-23 584（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `e00fdee9b85e` · [字段定义](../../DATASET.md)*
