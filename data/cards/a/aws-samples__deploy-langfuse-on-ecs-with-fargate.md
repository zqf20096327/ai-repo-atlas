# aws-samples/deploy-langfuse-on-ecs-with-fargate

⭐ 79 · Python · MIT-0 · 推送 2026-07-28 · [GitHub](https://github.com/aws-samples/deploy-langfuse-on-ecs-with-fargate) · 组织维护

**用 CDK Python 在 AWS ECS/Fargate 上自托管 Langfuse 的部署代码**

aws-samples 仓库，提供 AWS CDK Python 代码，将开源 LLM 工程平台 Langfuse 部署到 Amazon ECS（Fargate）并使用 ECR 存放镜像，覆盖 langfuse-v2 与 langfuse-v3 两套架构。面向需要在 AWS 上自托管 Langfuse 以调试、分析、迭代 LLM 应用的团队。README 仅含架构图链接、参考文档与安全说明，未给出安装运行步骤细节；许可为 MIT-0。

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

- 提供 Langfuse v2 与 v3 两套架构的 CDK Python 部署代码
- 使用 Amazon ECR 与 ECS（Fargate）承载 Langfuse 应用

## 适用场景

- 在自有 AWS 账号中自托管 Langfuse 平台
- 以基础设施即代码方式复用 Langfuse 的 ECS/Fargate 部署

## 场景标签

`LLM 可观测性` · 领域:评测与运维

## 证据(README 行号)

> L3: This repository contains the AWS CDK Python code for deploying the Langfuse application using Amazon Elastic Contain
> L5: Langfuse is an open-source LLM engineering platform that helps teams collaboratively debug, analyze, and iterate on 

## 星数曲线

```mermaid
xychart-beta
    title "aws-samples/deploy-langfuse-on-ecs-with-fargate 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 78 --> 80
    line [79, 79]
```

2026-10-18 79 → 2026-10-31 79（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 mid · 依据 README sha `022a2a8b17a4` · [字段定义](../../DATASET.md)*
