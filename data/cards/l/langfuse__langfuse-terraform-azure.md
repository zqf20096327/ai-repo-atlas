# langfuse/langfuse-terraform-azure

⭐ 36 · HCL · MIT · 推送 2026-10-19 · [GitHub](https://github.com/langfuse/langfuse-terraform-azure) · 组织维护

**在 Azure 上部署 Langfuse 的 Terraform 模块**

由 Langfuse 维护的 Terraform 模块，将开源 LLM 可观测性平台 Langfuse（Helm chart v2 / Langfuse v4）部署到 Azure 托管服务上：创建 AKS 集群、PostgreSQL Flexible Server、Azure Managed Redis、Storage、Key Vault、DNS Zone 与带 WAF 的 Application Gateway，并通过 ClickHouse operator 部署集群内 ClickHouse（也可接入外部 ClickHouse Cloud）。安装需两阶段 terraform apply，运行 terraform 的身份需 Owner 或 User Access Administrator 角色；从 0.4.x 升级到 1.x 需自行迁移数据。

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

- 在 Azure 上创建完整 Langfuse 栈（AKS/PostgreSQL/Redis/Storage/Key Vault/Application Gateway）
- 通过 cert-manager 与 ClickHouse operator 部署集群内 ClickHouse，支持外部 ClickHouse Cloud
- Key Vault 用 Azure RBAC 保护，可选 LLM API 凭证加密密钥与 DDoS Protection
- 应用版本通过 app_version 变量显式固定（默认 4.63.0）

## 适用场景

- 用 Terraform 在 Azure 上搭建生产可用的 Langfuse 自托管实例
- 以基础设施即代码方式管理 Langfuse 部署与升级
- 接入自有 ClickHouse Cloud 或外部 ClickHouse 部署 Langfuse

## 场景标签

 · 领域:LLM 基础设施/可观测性部署

## 证据(README 行号)

> L5: This repository contains a Terraform module for deploying Langfuse - the open-source LLM observability platform - on

## 星数曲线

```mermaid
xychart-beta
    title "langfuse/langfuse-terraform-azure 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 35 --> 37
    line [36, 36]
```

2026-10-18 36 → 2026-10-25 36（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `f57ef8c145aa` · [字段定义](../../DATASET.md)*
