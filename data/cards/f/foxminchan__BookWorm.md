# foxminchan/BookWorm

⭐ 507 · C# · MIT · 推送 2026-10-25 · [GitHub](https://github.com/foxminchan/BookWorm) · [官网](https://foxminchan.github.io/BookWorm/) · 个人维护

**展示 Aspire 云原生微服务与多 Agent AI 集成的参考架构项目**

基于 .NET Aspire 的云原生书店演示应用，采用 DDD、垂直切片架构与 CQRS，实现 gRPC 服务间通信、outbox/inbox、saga、事件溯源等微服务模式，用 Keycloak 做 AuthN/AuthZ、FusionCache 缓存。AI 部分：Microsoft Foundry 提供 LLM 与嵌入、Agent Framework 编排多 Agent 工作流、MCP 标准化工具、A2A/AG-UI/A2UI 协议支持及 Agent 治理。README 明确声明仅供演示、非生产可用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- Aspire 云原生微服务参考架构（DDD/VSA/CQRS/gRPC）
- Agent Framework 多 Agent 编排，MCP 标准化 AI 工具
- A2A、AG-UI 协议支持与 A2UI 生成交互式 UI
- Agent 治理：策略控制与监控

## 适用场景

- 学习 Aspire 云原生微服务与 agentic AI 的集成方式
- 参考 outbox/saga/事件溯源等微服务模式的实现
- 了解 MCP、A2A、AG-UI 协议在多 Agent 系统中的落地

## 场景标签

`多智能体` · 领域:Agent 开发

## 证据(README 行号)

> L23:  ⭐ BookWorm showcases Aspire in a cloud-native application with AI integration. Built with DDD and VSA, it features
> L45: - [x] Incorporated AI components:
> L47:  - [x] Orchestrated multi-agent workflows using Agent Framework

## 星数曲线

```mermaid
xychart-beta
    title "foxminchan/BookWorm 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 506 --> 508
    line [507, 507]
```

2026-10-18 507 → 2026-10-25 507（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `f54870fbfc52` · [字段定义](../../DATASET.md)*
