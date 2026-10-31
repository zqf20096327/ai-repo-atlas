# dapr/dapr-agents

⭐ 768 · Python · Apache-2.0 · 推送 2026-10-27 · [GitHub](https://github.com/dapr/dapr-agents) · [官网](https://docs.dapr.io/developing-applications/dapr-agents/) · 组织维护

**面向开发者的 Dapr 持久化 AI agent 构建框架**

构建在 Dapr 项目之上的 Python 开发者框架，用于编写可扩展、有状态的多 agent 系统：提供持久化工作流引擎（任务失败自动重试并从断点恢复）、虚拟 Actor 模型（单核运行数千 agent、Scale-To-Zero）、服务间调用、发布订阅与状态管理基础设施。支持多 LLM provider、结构化输出、上下文记忆、工具选择，以及零配置的 MCPServer 工具自动发现（经 Dapr sidecar 元数据 API）。面向需要在 Kubernetes 上部署生产级 agent 系统的开发者与平台团队，需安装 Dapr CLI、Python>=3.11 与 uv。Python SDK 处于开发中（Q2 2025），稳定版预计 Q4 2025。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 持久化工作流引擎：agentic 任务自动重试并从断点恢复状态
- 虚拟 Actor 模型：单核运行数千 agent，Scale-To-Zero 架构
- 零配置 MCP 集成：经 Dapr sidecar 自动发现 MCPServer 工具
- 内置消息与状态基础设施：服务调用、发布订阅、key-value 状态管理

## 适用场景

- 构建可在 Kubernetes 集群分布式运行的多 agent 工作流
- 开发需要长时运行、可从节点崩溃中恢复的研究型 agent 任务
- 平台团队以访问范围与声明式资源集成 agent 到现有系统

## 场景标签

`Agent 框架` `多智能体` · 领域:Agent 开发

## 证据(README 行号)

> L11: Dapr Agents is a developer framework designed to build production-grade resilient AI agent systems that operate at 
> L57: * 🔄 **Durable Workflow**: Defines long-running, persistent workflows that combine deterministic processes with LLM-

## 星数曲线

```mermaid
xychart-beta
    title "dapr/dapr-agents 星数(近 3 点)"
    x-axis ["2026-10-29", "2026-10-30", "2026-10-31"]
    y-axis "stars" 766 --> 769
    line [767, 768, 768]
```

2026-10-29 767 → 2026-10-31 768（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `5dc2e7f793d5` · [字段定义](../../DATASET.md)*
