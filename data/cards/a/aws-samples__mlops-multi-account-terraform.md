# aws-samples/mlops-multi-account-terraform

⭐ 49 · Jupyter Notebook · MIT-0 · 推送 2026-03-11 · [GitHub](https://github.com/aws-samples/mlops-multi-account-terraform) · 组织维护

**用 Terraform 与 GitHub 在 AWS 上构建企业级 MLOps 平台的参考方案**

AWS 官方示例仓库，演示如何用 Terraform 与 GitHub Actions 构建多账户安全 MLOps 基础设施，包含 SageMaker Studio、网络、权限与 SSM 参数的基础设施代码，以及四套可被 SageMaker Project 克隆的 GitHub 模板仓库（模型构建训练部署、跨环境流水线推广、单账户训练、LLM 构建训练评估）。部署需 AWS 账户（建议 dev/preprod/prod 三个）、GitHub 组织与 PAT，通过 CloudFormation 模板或 bash 脚本引导，配置 S3+DynamoDB 的 Terraform 后端与 OIDC 认证。面向需要在 AWS 上落地多账户 ML 生命周期的企业平台团队。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT-0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Terraform 基础设施代码覆盖 SageMaker Studio、网络、权限与 SSM 参数
- 四套 SageMaker Project GitHub 模板仓库（含 LLM 构建训练评估模板）
- GitHub Actions OIDC 短期凭证接入 AWS，避免长期 IAM 密钥
- 提供 bootstrap.yaml CloudFormation 模板与 bootstrap.sh 脚本两种引导方式

## 适用场景

- 在 AWS 多账户环境搭建 dev/preprod/prod 的 MLOps 基线设施
- 为数据科学家提供可克隆定制的 SageMaker 项目模板
- 以 GitHub Actions + Terraform 实现 ML 流水线的 CI/CD 与跨环境推广

## 场景标签

`MLOps` · 领域:训练与推理

## 证据(README 行号)

> L9: In this repository, we show how to use **Terraform** with **GitHub and GitHub Actions** to build a baseline infrastr
> L38: 1. **MLOps Template for Model Building, Training, and Deployment**: ML Ops pattern to train models using SageMaker 

## 星数曲线

```mermaid
xychart-beta
    title "aws-samples/mlops-multi-account-terraform 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 48 --> 50
    line [49, 49]
```

2026-10-18 49 → 2026-10-29 49（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `f1ed8d757e25` · [字段定义](../../DATASET.md)*
