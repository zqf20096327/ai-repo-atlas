# outerbounds/metaflow-tools

⭐ 68 · HCL · 推送 2025-11-12 · [GitHub](https://github.com/outerbounds/metaflow-tools) · 组织维护

**OSS Metaflow 生产部署运维工具集：AWS/Azure/K8s 配置模板**

Outerbounds 维护的开源 Metaflow（OSS）部署与运维工具仓库：提供 AWS CloudFormation 与 Terraform 模板（AWS Batch 计算、Step Functions 编排）、Azure Terraform 模板（AKS + Argo Workflows）、Nebius AI Cloud 模板，以及用于部署 Metaflow Metadata 服务与 UI 的 Helm charts（标注为 alpha），附带示例 flow 定义与部署辅助脚本。面向自建 Metaflow 基础设施的 MLOps/平台工程师，通过 IaC 模板与脚本交付，不含模型功能本身。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- AWS CloudFormation 与 Terraform 两种部署模板（Batch + Step Functions）
- Azure 与 Nebius AI Cloud 的 Terraform 端到端示例（AKS/托管 K8s + Argo Workflows）
- 部署 Metaflow Metadata 服务与 UI 的 Helm charts（alpha）
- 示例 flow 定义与部署/使用辅助脚本

## 适用场景

- 在 AWS/Azure/Nebius 云上搭建生产级 Metaflow 技术栈
- 在 Kubernetes 集群部署 Metaflow Metadata 服务与 UI
- 用示例 flow 测试自建 Metaflow 部署的端到端可用性

## 场景标签

`MLOps` · 领域:训练与推理

## 证据(README 行号)

> L6: This repository contains various configuration files, tools and utilities for operating OSS Metaflow in production. 
> L8: ## Metaflow on AWS (/aws)

## 星数曲线

```mermaid
xychart-beta
    title "outerbounds/metaflow-tools 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 67 --> 69
    line [68, 68]
```

2026-10-18 68 → 2026-10-30 68（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `dee5676dc1ff` · [字段定义](../../DATASET.md)*
