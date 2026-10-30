# outerbounds/terraform-aws-metaflow

⭐ 70 · HCL · Apache-2.0 · 推送 2025-12-15 · [GitHub](https://github.com/outerbounds/terraform-aws-metaflow) · [官网](https://registry.terraform.io/modules/outerbounds/metaflow/aws/latest) · 组织维护

**在 AWS 上以 Terraform 部署 Metaflow 生产基础设施的模块**

Terraform 模块，用于在 AWS 上创建运行 Metaflow 所需的生产环境资源。由五个可单独使用的子模块组成：AWS Batch 计算集群（metaflow-computation）、S3 与元数据数据库（metaflow-datastore）、记录与查询历史执行的 API 服务（metaflow-metadata-service）、Step Functions 部署资源（metaflow-step-functions）与 Metaflow UI（metaflow-ui）。提供大量输入参数（Batch 计算类型 EC2/Fargate、RDS 实例类型、KMS 密钥轮换、IMDSv2 等）与输出（S3 路径、IAM 角色、profile JSON 等）。面向使用 Metaflow 与 AWS 的 MLOps 工程师，需自行提供 VPC、子网等前置资源。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 五个子模块可单独或整体使用（计算/存储/元数据服务/Step Functions/UI）
- 支持 AWS Batch（EC2 或 Fargate）与 Step Functions 两种执行后端
- 输出 metaflow_profile_json 可直接配置 Metaflow 客户端连接该栈
- 支持 KMS 加密、密钥轮换、API Gateway Basic Auth 与 IMDSv2 等配置

## 适用场景

- 用 Terraform 在 AWS 上一键创建 Metaflow 生产运行环境
- 为数据科学团队的 Metaflow 流水线提供计算与元数据基础设施
- 通过 Step Functions 编排 Metaflow 流程

## 场景标签

`MLOps` · 领域:训练与推理

## 证据(README 行号)

> L1: # Metaflow Terraform module
> L3: Terraform module that provisions AWS resources to run Metaflow in production.
> L7: - AWS Batch cluster to run Metaflow steps (`metaflow-computation`)

## 星数曲线

```mermaid
xychart-beta
    title "outerbounds/terraform-aws-metaflow 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 69 --> 71
    line [70, 70]
```

2026-10-18 70 → 2026-10-30 70（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `f4d2932ad336` · [字段定义](../../DATASET.md)*
