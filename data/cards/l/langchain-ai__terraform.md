# langchain-ai/terraform

⭐ 21 · HCL · Apache-2.0 · 推送 2026-10-27 · [GitHub](https://github.com/langchain-ai/terraform) · 组织维护

**在企业自有云上部署 LangSmith 自托管版的 Terraform 模块集**

LangChain 官方仓库，以可复用 Terraform 模块打包 LangSmith Self-Hosted 的云基础设施（网络/集群/数据库/缓存/对象存储/密钥/DNS）与 Helm 应用部署，覆盖 AWS EKS、Azure AKS、GCP GKE（GA）与 OpenShift（Preview），并提供 BYOC 客户侧 IAM/VPC 模块。面向在自有云账户运行 LangSmith 的企业客户，支持四档 sizing profile、企业功能开关（LangGraph Platform、Agent Builder、Insights、Polly）与 AWS 可选加固；部署需 Terraform ≥1.11、kubectl、helm 与云 CLI，首部署约 20–30 分钟，按全局 tag 发布并维护多条 chart 线。

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

- AWS/Azure/GCP/OpenShift 四云的 Terraform 基础设施 + Helm 两段式部署
- minimum/dev/production/production-large 四档 sizing profile 单变量切换
- 云厂商专属密钥流转（SSM/Key Vault/Secret Manager）
- 维护多条 chart 线（0.17/0.16/0.15）与维护分支的 tag 发布机制

## 适用场景

- 企业在我自己的云账户里搭建 LangSmith 自托管生产部署
- 为 LangSmith BYOC 场景配置客户侧 IAM 角色与 VPC
- 按 tag 固定版本做可复现的基础设施部署

## 场景标签

 · 领域:LLM 基础设施/DevOps

## 证据(README 行号)

> L3: Terraform modules for deploying **LangSmith Self-Hosted** on AWS, Azure, GCP, and OpenShift.
> L5: LangSmith is LangChain's observability, evaluation, and prompt-engineering platform. This repository packages the cl

## 星数曲线

```mermaid
xychart-beta
    title "langchain-ai/terraform 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-28"]
    y-axis "stars" 19 --> 22
    line [20, 21, 21]
```

2026-10-18 20 → 2026-10-28 21（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `76ca163ce55a` · [字段定义](../../DATASET.md)*
