# langfuse/langfuse-terraform-gcp

⭐ 33 · HCL · MIT · 推送 2026-10-27 · [GitHub](https://github.com/langfuse/langfuse-terraform-gcp) · 组织维护

**在 GCP 上部署 Langfuse 的 Terraform 模块**

由 Langfuse 官方维护的 Terraform 模块，将开源 LLM 可观测性平台 Langfuse（Helm chart v2 / 应用 v4）部署到 GCP。模块创建 VPC、GKE 集群、Cloud SQL PostgreSQL、Memorystore Redis、Cloud Storage、ClickHouse 集群（官方 operator 管理，或接入外部 ClickHouse Cloud）、TLS 证书与 Cloud DNS 等，提供约 40 个输入变量做尺寸与版本控制。要求 Terraform >= 1.3，采用两阶段 apply 的受支持安装流程；从 0.3.x 升级需在 Terraform 之外手动迁移数据。

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

- 基于 GCP 托管服务创建完整 Langfuse 栈（GKE/Cloud SQL/Redis/ClickHouse/DNS/TLS）
- 支持外部 ClickHouse（如 ClickHouse Cloud）替代集群内部署
- ClickHouse 副本数、存储、资源等可通过变量配置，默认 3 副本高可用
- Langfuse 应用版本通过 app_version 变量显式固定

## 适用场景

- 在 GCP 上以基础设施即代码方式部署 Langfuse
- 为 LLM 应用搭建带观测能力的生产环境
- 使用自有 ClickHouse Cloud 与自有 DNS 部署 Langfuse

## 场景标签

 · 领域:LLM 基础设施/云部署

## 证据(README 行号)

> L5: This repository contains a Terraform module for deploying Langfuse - the open-source LLM observability platform - on
> L79: This module creates a complete Langfuse stack with the following components:

## 星数曲线

```mermaid
xychart-beta
    title "langfuse/langfuse-terraform-gcp 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 32 --> 34
    line [33, 33]
```

2026-10-18 33 → 2026-10-28 33（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `275a1db676c4` · [字段定义](../../DATASET.md)*
