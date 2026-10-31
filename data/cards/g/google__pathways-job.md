# google/pathways-job

⭐ 23 · Go · Apache-2.0 · 推送 2026-07-09 · [GitHub](https://github.com/google/pathways-job) · [官网](https://github.com/google/pathways-job) · 组织维护

**Kubernetes 原生 API：在 GKE 上以 Pathways 部署 JAX 训练与批量推理**

PathwaysJob 是 Google 开源的 Kubernetes 原生 API（CRD + controller），用于在 GKE 上用 Pathways 系统部署 JAX 的 ML 训练与批量推理工作负载。它将 Pathways 资源管理器、代理服务器与用户工作负载容器打包为单一 pathways-head Pod，支持 ColocateHeadWithWorkers 与 Default 两种部署模式，前者面向低延迟批量推理，后者面向占用整片 TPU 的训练。注意：README 首行声明已废弃，改用直接 jobsets。安装需 go/kubectl/JobSet 等前置条件，支持 kubectl apply 安装发布版或从源码构建。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 将 Pathways RM、代理服务器与用户工作负载打包为 pathways-head Pod
- ColocateHeadWithWorkers 与 Default 两种部署模式
- 支持 dockerized 工作负载与 headless 交互式模式
- 已声明废弃，迁移至直接 jobsets 方案

## 适用场景

- 在 GKE 的 TPU 切片上运行 JAX 大规模训练工作负载
- 部署 Pathways 批量推理工作负载（低延迟场景）
- 通过 Vertex AI notebook 以 headless 模式连接交互式超算

## 场景标签

`模型训练` `推理引擎` · 领域:训练与推理

## 证据(README 行号)

> L5: PathwaysJob API is an OSS Kubernetes-native API, to deploy ML training and batch inference workloads, using Pathways
> L11: PathwaysJob is an API that provides an easy way to run JAX workloads using Pathways. A PathwaysJob instance bundles

## 星数曲线

```mermaid
xychart-beta
    title "google/pathways-job 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 22 --> 24
    line [23, 23]
```

2026-10-18 23 → 2026-10-31 23（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `9f92c7cbf508` · [字段定义](../../DATASET.md)*
