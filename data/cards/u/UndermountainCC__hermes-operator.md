# UndermountainCC/hermes-operator

⭐ 26 · Go · Apache-2.0 · 推送 2026-09-01 · [GitHub](https://github.com/UndermountainCC/hermes-operator) · [官网](https://undermountain.cc/labs/hermes-operator) · 组织维护

**K8s operator：用 CRD 声明式部署管理 Hermes AI agent 实例**

为 Hermes AI agent 提供的 Kubernetes operator：用户创建 HermesAgent 自定义资源，operator 负责调和 Deployment、PVC、Service、ServiceAccount、RBAC、环境变量组装与逐网关就绪状态，将每 agent 的多对象管理收敛为单个 CR。状态为 v1alpha1、面向内部 alpha 使用，公开 API 可能变更。安装方式为 Helm chart（OCI 仓库）或 kustomize，需 cert-manager 前置。提供 E2E 测试套件与文档站。

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

- HermesAgent CRD 声明式定义 agent，operator 自动创建 Deployment/PVC/RBAC 等资源
- status 中报告逐网关（Discord/Telegram/WhatsApp）就绪状态
- 支持 Helm（OCI chart）与 kustomize 两种安装方式
- 针对真实 Kind 集群的 E2E 测试套件

## 适用场景

- 在 Kubernetes 上以声明式方式运行多个 Hermes agent
- 为每个 agent 统一管理持久存储、凭据与 RBAC
- 通过 Helm/kustomize 将 operator 纳入集群运维流程

## 场景标签

 · 领域:云原生/AI agent 运维

## 证据(README 行号)

> L13: A Kubernetes operator for deploying and managing Hermes AI agent instances. Define an agent declaratively via a `He
> L17: Hermes is stateful: each agent has a persistent home directory, paired credentials (Discord/Telegram/WhatsApp token

## 星数曲线

```mermaid
xychart-beta
    title "UndermountainCC/hermes-operator 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 25 --> 27
    line [26, 26]
```

2026-10-18 26 → 2026-10-28 26（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `faf3b90d1139` · [字段定义](../../DATASET.md)*
