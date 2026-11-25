# langfuse/langfuse-k8s

⭐ 288 · Go Template · MIT · 推送 2026-11-23 · [GitHub](https://github.com/langfuse/langfuse-k8s) · [官网](https://langfuse.com/self-hosting/deployment/kubernetes-helm)

**为开发者在 Kubernetes 上部署自托管 Langfuse 提供的社区 Helm chart**

社区维护的仓库，包含在 Kubernetes 上部署 Langfuse 所需的资源：charts/langfuse 提供 Helm chart，examples 目录提供示例 yaml。chart 默认捆绑部署 Postgres、ClickHouse（经 clickhouse-operator）、Valkey 和 SeaweedFS，首次安装自动生成并持久化凭据 Secrets；支持外部数据存储、Secret 引用/External Secrets Operator、AI gateway（beta）与内置 AI 功能配置，提供 v1→v2 迁移路径。要求 Helm ≥3.17、Kubernetes ≥1.28。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Helm chart 一键部署 Langfuse 及捆绑的 Postgres/ClickHouse/Valkey/SeaweedFS
- 首次安装自动生成凭据 Secrets，跨升级持久化，支持 secretKeyRef/existingSecret
- 支持外部 ClickHouse/Postgres 部署与 v1→v2 迁移示例
- 可开启 beta 版 AI gateway（独立 Deployment/Service/Ingress/HPA）

## 适用场景

- 在自管 Kubernetes 集群上自托管 Langfuse
- 用 GitOps/ArgoCD 管理语言追踪平台的部署
- 为生产环境配置外部 ClickHouse 与资源限额

## 场景标签

`LLM 可观测性` · 领域:评测与运维

## 证据(README 行号)

> L7: This is a community-maintained repository that contains resources for deploying Langfuse on Kubernetes.
> L61: We provide a Helm chart that helps you deploy Langfuse on Kubernetes.

## 星数曲线

```mermaid
xychart-beta
    title "langfuse/langfuse-k8s 星数(近 13 点)"
    x-axis ["2026-10-23", "2026-10-25", "2026-10-27", "2026-10-28", "2026-11-06", "2026-11-08", "2026-11-10", "2026-11-11", "2026-11-12", "2026-11-14", "2026-11-19", "2026-11-20", "2026-11-25"]
    y-axis "stars" 279 --> 289
    line [282, 280, 281, 282, 280, 283, 285, 287, 286, 285, 286, 288, 288]
```

2026-10-23 282 → 2026-11-25 288（+6）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-25 · 置信度 high · 依据 README sha `8e9b600d97fb` · [字段定义](../../DATASET.md)*
