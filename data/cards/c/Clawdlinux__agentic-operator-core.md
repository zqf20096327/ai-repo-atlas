# Clawdlinux/agentic-operator-core

⭐ 51 · Go · NOASSERTION · 推送 2026-10-23 · [GitHub](https://github.com/Clawdlinux/agentic-operator-core) · [官网](https://clawdlinux.org) · 组织维护

**Kubernetes 上 AI agent 的治理 operator：隔离、egress 策略、成本与审计**

Kubernetes operator，为 AI agent 工作负载提供集群内治理：通过 gVisor RuntimeClass 变异实现沙箱隔离、生成 default-deny 与白名单网络策略、按工作负载进行 token 与成本归因、HMAC 哈希链与 Ed25519 签名决策收据支持离线验证。注册三种运行时适配器（内置 CRD、kagent、自定义 pod），Argo Workflows 进行 DAG 编排，LiteLLM 做多供应商模型路由。提供 agentctl MCP 服务（六个工具）供外部编排 agent 使用。当前局限：决策模型仅 shadow 模式未经真实验证，审计链未完全接入控制器，企业功能在私有版。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- gVisor RuntimeClass 注入实现 pod 级沙箱隔离
- Default-deny 与白名单网络策略由已审核配置自动生成
- Ed25519 签名决策收据与 HMAC 哈希链审计，支持离线验证
- agentctl MCP 服务（六个工具，与 CRD 操作一一对应）

## 适用场景

- 平台团队在 Kubernetes 上运行 AI agent 时需要隔离、网络策略与成本控制
- 审计人员离线重放与验证 agent 行为证据
- 通过 Argo Workflows 编排 agent 步骤并管理多租户配额

## 场景标签

`网络安全` · 领域:学习与行业

## 证据(README 行号)

> L7:  In-cluster governance for AI agents on Kubernetes.
> L9:  Runtime-agnostic workload contracts, isolation and egress configuration, model-cost evidence, and offline-verifiabl
> L36: Clawdlinux is building the in-cluster governance boundary around those workloads. It does not replace the agent run

## 星数曲线

```mermaid
xychart-beta
    title "Clawdlinux/agentic-operator-core 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 50 --> 52
    line [51, 51]
```

2026-10-18 51 → 2026-10-24 51（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `a8edf25e0e68` · [字段定义](../../DATASET.md)*
