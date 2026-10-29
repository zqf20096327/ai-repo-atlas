# aws-controllers-k8s/sagemaker-controller

⭐ 53 · Python · Apache-2.0 · 推送 2026-10-26 · [GitHub](https://github.com/aws-controllers-k8s/sagemaker-controller) · [官网](https://aws-controllers-k8s.github.io/community/docs/tutorials/sagemaker-example/) · 组织维护

**Kubernetes 控制器：用 CRD 管理 Amazon SageMaker 资源**

AWS Controllers for Kubernetes（ACK）项目中针对 Amazon SageMaker 的服务控制器：在 Kubernetes 集群内通过自定义资源（CRD）与 kubectl 创建和管理 SageMaker 资源，如 Endpoint 等；配合 Application Auto Scaling 控制器可为 SageMaker 工作负载扩缩容，并支持跨区域、跨 AWS 账号资源管理与采用（adopt）集群外已有资源。提供 Helm Chart 与控制器镜像（Amazon ECR Public Gallery），含从旧版 SageMaker Operators for Kubernetes 迁移的说明与示例目录。面向在 Kubernetes 上运维 AWS 机器学习资源的开发与运维人员。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 通过 CRD 与 kubectl 在集群内管理 SageMaker 资源
- 支持采用（adopt）非 ACK 创建的已有资源
- 支持跨区域与跨 AWS 账号资源管理
- 提供 Helm Chart 与控制器镜像（ECR Public Gallery）

## 适用场景

- 在 Kubernetes 中以声明式方式创建和运维 SageMaker Endpoint 等资源
- 为 SageMaker 工作负载配置自动扩缩容
- 把已有的 SageMaker 资源纳管进集群管理

## 场景标签

`MLOps` · 领域:训练与推理

## 证据(README 行号)

> L1: # ACK service controller for Amazon SageMaker
> L3: This repository contains source code for the AWS Controllers for Kubernetes
> L4: (ACK) service controller for Amazon SageMaker.

## 星数曲线

```mermaid
xychart-beta
    title "aws-controllers-k8s/sagemaker-controller 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 52 --> 54
    line [53, 53]
```

2026-10-18 53 → 2026-10-29 53（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `b9bd20201663` · [字段定义](../../DATASET.md)*
