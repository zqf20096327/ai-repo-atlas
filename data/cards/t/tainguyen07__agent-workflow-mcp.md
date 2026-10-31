# tainguyen07/agent-workflow-mcp

⭐ 15 · Python · MIT · 推送 2026-08-21 · [GitHub](https://github.com/tainguyen07/agent-workflow-mcp) · 个人维护

**面向开发者的 MCP 多智能体工作流编排框架**

基于 Model Context Protocol 的多智能体工作流编排器：Planner/Executor/Critic 三层 agent 将目标分解为类型化计划，经有界重试与 schema 校验的工具调用循环执行，通过 stdio/WebSocket 的 MCP 客户端/服务端发现并调用工具。每一步与中间消息追加到可回放/可恢复的事件日志，支持崩溃后断点续跑，附 OpenTelemetry 风格追踪。内置 Anthropic 适配器并提供 Provider 协议接入其他后端，Pydantic v2 类型化配置，CLI 含 serve/run/replay/trace 子命令。以 Python 3.11+ 源码方式安装。

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

- Planner/Executor/Critic agent 栈与类型化工具调用循环
- MCP 客户端/服务端（stdio/WebSocket，JSON-RPC 2.0）
- 持久化运行状态：事件日志可回放、崩溃后可续跑
- 内置 Anthropic 适配器，Provider 协议可插拔其他后端

## 适用场景

- 编排需要长时间无人值守运行的多步 agent 任务
- 通过 MCP 工具服务端扩展 agent 的可调用工具
- 回放与审计 agent 运行轨迹和 token 消耗

## 场景标签

`多智能体` `Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L10: Production-grade multi-agent workflow orchestrator built on the **Model Context Protocol (MCP)**. A planner/executo
> L24: - **Pluggable providers**: built-in Anthropic adapter with a clean `Provider` protocol for OpenAI, Bedrock, or loca

## 星数曲线

```mermaid
xychart-beta
    title "tainguyen07/agent-workflow-mcp 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-31 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 mid · 依据 README sha `90726bd7ec72` · [字段定义](../../DATASET.md)*
