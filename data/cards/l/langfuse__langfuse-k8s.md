# langfuse/langfuse-k8s

⭐ 288 · Go Template · MIT · 推送 2026-11-27 · [GitHub](https://github.com/langfuse/langfuse-k8s) · [官网](https://langfuse.com/self-hosting/deployment/kubernetes-helm) · 组织维护

**在 Kubernetes 上部署 Langfuse 的社区维护 Helm chart**

社区维护的仓库，提供在 Kubernetes 上部署 Langfuse 的资源与 Helm chart。chart 默认打包 Langfuse v4，捆绑 Postgres、ClickHouse（经 clickhouse-operator）、Valkey、SeaweedFS 子 chart，首次安装自动生成凭证 Secret 并通过 lookup 跨升级持久化；支持 helm repo 或 OCI 安装、v1 Bitnami chart 迁移路径与 ArgoCD/GitOps 注意事项。v2.0.0 起以 OSS 许可镜像替换 Bitnami 子 chart，AI gateway 为 Beta 值，不纳入 SemVer 保证。

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

- Helm chart 部署 Langfuse v4 及配套数据存储子 chart
- 首次安装自动生成并持久化凭证 Secret
- 提供 v1 Bitnami chart 到 v2 的迁移路径与空卷升级防护
- 可选部署 AI gateway（Deployment/Service/Ingress/HPA）

## 适用场景

- 在 Kubernetes 集群自托管 Langfuse
- 通过 GitOps/ArgoCD 流水线管理 Langfuse 部署
- 为 Langfuse v4 准备 ClickHouse/Postgres/Redis 等依赖组件

## 场景标签

 · 领域:LLM 基础设施/部署运维

## 证据(README 行号)

> L7: This is a community-maintained repository that contains resources for deploying Langfuse on Kubernetes.
> L61: We provide a Helm chart that helps you deploy Langfuse on Kubernetes.

## 星数曲线

```mermaid
xychart-beta
    title "langfuse/langfuse-k8s 星数(近 12 点)"
    x-axis ["2026-10-26", "2026-10-27", "2026-10-28", "2026-11-06", "2026-11-08", "2026-11-10", "2026-11-11", "2026-11-12", "2026-11-14", "2026-11-19", "2026-11-20", "2026-11-28"]
    y-axis "stars" 279 --> 289
    line [280, 281, 282, 280, 283, 285, 287, 286, 285, 286, 288, 288]
```

2026-10-26 280 → 2026-11-28 288（+8）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-27 · 置信度 high · 依据 README sha `1580dae88368` · [字段定义](../../DATASET.md)*
