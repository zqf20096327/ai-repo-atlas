# langfuse/langfuse-terraform-aws

⭐ 64 · HCL · MIT · 推送 2026-10-26 · [GitHub](https://github.com/langfuse/langfuse-terraform-aws) · 组织维护

**在 AWS 上部署 Langfuse 的 Terraform 模块**

由 Langfuse 官方维护的 Terraform 模块，将开源 LLM 可观测平台 Langfuse 部署到 AWS，尽量使用托管服务：EKS Fargate、Route53、S3、EFS，含 ClickHouse 与 Keeper。支持复用已有 VPC、容器资源配额配置、基于代码的评估执行器（租户隔离 Lambda）与 AI 功能（Ask AI / 内置 agent，可接 Bedrock/Anthropic/OpenAI，默认关闭）。使用方式为配置 Terraform 模块后 terraform apply，需自备域名与 DNS 委派；首次安装存在已知的调度竞态问题。

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

- 在 AWS EKS Fargate 上部署 Langfuse 全栈（含 ClickHouse/Keeper）
- 可选启用基于代码的评估执行器：租户隔离 Lambda + 无出网隔离 VPC
- 可选 AI 功能与 Agent 沙箱（Lambda MicroVM，需自行构建镜像）
- 支持复用已有 VPC 并自动打 Kubernetes 所需子网标签

## 适用场景

- 在自有 AWS 账号中用 Terraform 声明式部署 Langfuse
- 以生产配置运行 Langfuse 的代码评估与 Agent 功能
- 在已有 VPC 内复用网络部署 Langfuse

## 场景标签

 · 领域:LLM 基础设施/云部署

## 证据(README 行号)

> L5: This repository contains a Terraform module for deploying Langfuse - the open-source LLM observability platform - on
> L6: This module aims to provide a production-ready, secure, and scalable deployment using managed services whenever poss

## 星数曲线

```mermaid
xychart-beta
    title "langfuse/langfuse-terraform-aws 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 63 --> 65
    line [64, 64]
```

2026-10-18 64 → 2026-10-27 64（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `fed7813779ea` · [字段定义](../../DATASET.md)*
