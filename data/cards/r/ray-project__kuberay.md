# ray-project/kuberay

⭐ — · [GitHub]() · 组织维护

**在 Kubernetes 上部署与管理 Ray 应用的运维工具集**

Apache 许可的开源 Kubernetes operator，通过 RayCluster、RayJob、RayService 三个自定义资源管理 Ray 应用的集群生命周期、自动扩缩容、作业提交与容错；RayService 由 RayCluster 加 Ray Serve 部署图构成，提供零停机升级与高可用。可选生态组件包括 kubectl ray 插件、APIServer 与 Dashboard。面向在 Kubernetes 上运行 Ray 训练与 LLM 推理等负载的工程团队，用户文档与示例托管在 Ray 官方文档站。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- RayCluster/RayJob/RayService 三种自定义资源管理 Ray 负载
- 集群自动扩缩容、容错与 RayService 零停机升级
- 可选组件：kubectl ray 插件、APIServer、Dashboard
- 与 Prometheus、Grafana、Volcano、Kueue 等 Kubernetes 生态集成

## 适用场景

- 在 Kubernetes 集群上运行 Ray 训练与 LLM 在线/批量推理
- 以 RayJob 方式提交作业并按需创建/回收集群
- 通过 kubectl 插件或 Dashboard 管理 KubeRay 资源

## 场景标签

`MLOps` · 领域:训练与推理

## 证据(README 行号)

> L7: KubeRay is a powerful, open-source Kubernetes operator that simplifies the deployment and management of Ray applicat
> L9: **KubeRay core**: This is the official, fully-maintained component of KubeRay that provides three custom resource de
> L43: Examples span a wide range of use cases, including training, LLM online inference, batch inference, and more.

## 星数曲线

```mermaid
xychart-beta
    title "ray-project/kuberay 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-21"]
    y-axis "stars" 2730 --> 2738
    line [2731, 2737, 2737]
```

2026-10-18 2,731 → 2026-10-21 2,737（+6）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `a8a735eb5586` · [字段定义](../../DATASET.md)*
