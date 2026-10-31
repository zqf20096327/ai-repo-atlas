# fh6312/kubeflow-pipeline-forge

⭐ 53 · HTML · 推送 2026-10-30 · [GitHub](https://github.com/fh6312/kubeflow-pipeline-forge) · 个人维护

**面向 Kubernetes 的 AI 工作负载编排系统（概念性 README）**

自称 KubePilot：在 Kubernetes 之上提供 AI 工作负载（训练、推理、批处理管道）的编排层。核心概念为四个原语：Mission（意图编译为资源 DAG）、Convoy（共享生命周期的任务组）、Anchor（GPU/镜像/权重的暖池）、Beacon（遥测事件面）。支持多集群联邦、抢占式调度、OpenTelemetry/Prometheus 遥测、短时工作负载身份与策略即代码。README 自述为 Kubeflow 的互补而非替代。面向平台团队与 ML 工程师。注意：README 未提供任何安装命令或代码入口，多数功能列为 2026 年路线图，成熟度无法核验。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- Mission 意图描述编译为 Kubernetes 资源 DAG
- Anchor 暖池回收 GPU、镜像与模型权重以降低冷启动
- OpenTelemetry spans 与 Prometheus 指标开箱输出
- 多集群联邦与按 Convoy 的多租户隔离

## 适用场景

- 在 Kubernetes 集群上编排训练与推理工作负载
- 通过暖池复用降低 GPU 冷启动延迟
- 跨本地、云与边缘集群提交统一工作负载

## 场景标签

`MLOps` `模型训练` · 领域:训练与推理

## 证据(README 行号)

> L6: A next-generation orchestration companion that turns Kubernetes into a self-aware stage for AI workloads — training 
> L30: 1. **Missions** — a description of an AI workload's intent, constraints, and success criteria. A Mission compiles i
> L60: - **Scheduler Adapter** — Bridges KubePilot's predictive scoring into the upstream Kubernetes scheduler.

## 星数曲线

```mermaid
xychart-beta
    title "fh6312/kubeflow-pipeline-forge 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 52 --> 54
    line [53, 53]
```

2026-10-18 53 → 2026-10-31 53（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 mid · 依据 README sha `5f2bd718a1bf` · [字段定义](../../DATASET.md)*
