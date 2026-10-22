# nebius/soperator

⭐ 453 · Go · Apache-2.0 · 推送 2026-10-22 · [GitHub](https://github.com/nebius/soperator) · 组织维护

**在 Kubernetes 上运行 Slurm 集群的开源 operator，面向 AI 训练与 HPC**

Nebius 维护的 Kubernetes operator：将单个 SlurmCluster 自定义资源转为可用的 Slurm 集群，包含控制器、登录/工作节点、CUDA/NCCL 栈、共享根文件系统（jail）、健康检查与记账。面向需要提供 Slurm 而无需逐节点手工运维的平台团队，也适用于从裸机迁移到 Kubernetes 化 Slurm 的团队。特性包括临时节点自动伸缩、InfiniBand 拓扑感知、故障节点自动排水与替换。限制：节点镜像固定 Ubuntu 24.04，存在单分区、GPU-only 或 CPU-only 集群约束；另有 Nebius 托管与 Soperator Pro 商业服务路径。

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

- 单个 SlurmCluster 资源声明式部署与维护 Slurm 集群
- 共享根文件系统（jail）使节点软件配置保持一致
- 被动/主动健康检查与故障节点自动排水替换
- 镜像预装 NVIDIA 驱动、CUDA、NCCL 训练栈

## 适用场景

- 平台团队在自有 Kubernetes 上交付 Slurm AI 训练集群
- 从裸机 Slurm 迁移到 Kubernetes 化部署
- 跨云或本地环境运行 GPU 训练并自动恢复故障节点

## 场景标签

`模型训练` · 领域:训练与推理

## 证据(README 行号)

> L5: Soperator is an open-source Kubernetes operator for running Slurm clusters for AI training and high-performance comp
> L24: Slurm is a common scheduler for AI training and HPC workloads. Soperator is a Kubernetes operator that turns a `Slu
> L26: It is intended for platform teams and engineers who need to provide Slurm without managing each part of the cluster

## 星数曲线

```mermaid
xychart-beta
    title "nebius/soperator 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-22"]
    y-axis "stars" 447 --> 452
    line [448, 451, 451]
```

2026-10-18 448 → 2026-10-22 451（+3）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `efa640e7d647` · [字段定义](../../DATASET.md)*
