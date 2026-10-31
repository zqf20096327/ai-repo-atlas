# truvaagents/truva-g3

⭐ 13 · Go · Apache-2.0 · 推送 2026-10-30 · [GitHub](https://github.com/truvaagents/truva-g3) · [官网](https://truvag3.dev) · 组织维护

**Go 微代理框架：agent/工具经共享注册表动态发现、去中心化协作**

TruvaG3 是 microagents 架构的开源参考实现：专用 agent 与工具作为独立服务在运行时向共享注册表（默认 Redis/Valkey，可插拔）注册能力，调用方按逻辑能力名解析到端点，经集群内 HTTP/REST 直接互调，无中央控制面。框架层提供厂商中立的 AI 客户端（OpenAI/Anthropic/Gemini/Bedrock 等及 OpenAI 兼容端点）、DAG 执行与迭代重规划、断路器与语义重试、OpenTelemetry 埋点、双层记忆与人工审批。面向在 Kubernetes 上自托管运行大规模、多团队 agent 网络的开发者；Go 实现，容器约 15-44MB、运行时内存约 6-45MB。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 能力级服务发现：按逻辑名在运行时解析 agent/工具端点（默认 Redis/Valkey）
- DAG 执行计划 + 迭代重规划的编排器，LLM 按发现到的能力动态选工具
- 厂商中立 AI 客户端，覆盖 OpenAI/Anthropic/Gemini/Azure/Bedrock/OpenRouter 及 OpenAI 兼容端点
- 断路器、语义重试、OpenTelemetry 分布式追踪与双层记忆、人审节点

## 适用场景

- 在 Kubernetes 上自托管运行由多个独立部署的 agent 与工具组成的网络
- 合规隔离或离线环境中运行无外部 SaaS 依赖的 agent 系统
- 按团队/部门命名空间隔离各自的 agent 生态并逐步扩展到数百个参与者
- 让平台团队用现有 K8s/OTEL 运维体系直接管理 agent 工作负载

## 场景标签

`Agent 框架` `多智能体` `Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L8: > **About this framework.** TruvaG3 is the open-source reference implementation of the microagents architecture desc
> L6: > **A different way to wire agents and tools.** Specialized agents and tools register their capabilities with a shar
> L102: ## What Makes TruvaG3 Unique: Dynamic Agent Discovery, Vendor-Agnostic, Microservice-Native AI

## 星数曲线

```mermaid
xychart-beta
    title "truvaagents/truva-g3 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 12 --> 14
    line [13, 13]
```

2026-10-18 13 → 2026-10-31 13（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `5f77f9679566` · [字段定义](../../DATASET.md)*
