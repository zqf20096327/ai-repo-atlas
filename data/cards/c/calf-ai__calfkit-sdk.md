# calf-ai/calfkit-sdk

⭐ 150 · JavaScript · Apache-2.0 · 推送 2026-08-31 · [GitHub](https://github.com/calf-ai/calfkit-sdk) · 组织维护

**构建分布式事件驱动多 agent 系统的 Python SDK**

Calfkit 提供一个 Python SDK，用于构建多 agent 系统：各 agent 作为独立事件驱动微服务运行，在自动发现的数据流 mesh 网络上互相通信、移交任务，无需显式编排。mesh 与 Kafka 兼容，可部署到生产流式基础设施；本地开发可用 [mesh] extra 附带的零配置内存 broker（ck dev 命令）。模型客户端示例使用 OpenAIResponsesModelClient。面向构建多 agent 工作流的开发者，当前为重写阶段，0.13 版本文档位于 legacy/0.13 分支。

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

- agent 运行时自动发现与任务移交（Handoff/Messaging）
- 每个 agent 作为独立事件驱动微服务运行与扩展
- mesh 与 Kafka 兼容，可接入生产流式基础设施
- ck dev 提供零配置本地内存 mesh 与聊天终端

## 适用场景

- 构建互相发现、协作的多 agent 团队
- 让 agent 对实时数据流（行情/日志/工单队列）做出响应
- 在既有 Kafka 基础设施上运行与扩展 agent 集群

## 场景标签

`多智能体` `Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L3:  Build agents that discover each other at runtime, choreograph work, and scale as independent, event-driven services
> L12: Calfkit agents find each other and choreograph work over a **mesh** — a highly-connected data streaming network the
> L16: - **Dynamic agent-to-agent discovery and collaboration.** Agents find each other at runtime and work together — mes

## 星数曲线

```mermaid
xychart-beta
    title "calf-ai/calfkit-sdk 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-26", "2026-10-31"]
    y-axis "stars" 148 --> 151
    line [149, 150, 150]
```

2026-10-18 149 → 2026-10-31 150（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `9f0909e81e89` · [字段定义](../../DATASET.md)*
