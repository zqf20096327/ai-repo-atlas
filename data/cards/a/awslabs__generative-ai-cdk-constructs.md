# awslabs/generative-ai-cdk-constructs

⭐ 544 · TypeScript · Apache-2.0 · 推送 2026-10-29 · [GitHub](https://github.com/awslabs/generative-ai-cdk-constructs) · [官网](https://awslabs.github.io/generative-ai-cdk-constructs/) · 组织维护

**AWS CDK 的生成式 AI 基础设施模式库：用代码定义可复用架构**

AWS CDK 的开源扩展库，为生成式 AI 场景提供多服务、高层抽象的 constructs 模式：SageMaker 基础模型部署（JumpStart/Hugging Face/S3 自定义）、Bedrock 批量推理与数据自动化、OpenSearch 向量集合与索引、Aurora DSQL、S3 Vectors 等。面向在 AWS 上用基础设施即代码构建生成式 AI 应用的开发者，以 npm/PyPI/NuGet/Go/Maven 多语言分发。README 标注 Experimental，所有类可能发生非向后兼容变更或移除；Bedrock L2 constructs 已声明弃用并迁移至 aws-cdk 核心仓库。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | `idea` | |

## 动量与使用信号

- 安装:github 包 `release-assets` 月下载无数据

## 能力要点

- L3 constructs 覆盖 SageMaker 模型部署与 Bedrock 批量推理/数据自动化
- L2 constructs 覆盖 OpenSearch 向量集合/索引、Aurora DSQL、S3 Vectors
- 五种语言分发：TypeScript/Python/C#/Go/Java
- 附 Terraform 版 Bedrock/OpenSearch/SageMaker/Streamlit 模块

## 适用场景

- 用 CDK 代码快速定义生成式 AI 基础设施并保持可重复部署
- 部署 SageMaker 端点承载基础模型
- 为 RAG 应用创建 OpenSearch 向量检索基础设施

## 场景标签

 · 领域:云基础设施/生成式 AI

## 证据(README 行号)

> L26: The AWS Generative AI Constructs Library is an open-source extension of the AWS Cloud Development Kit (AWS CDK) tha
> L28: The patterns defined in AWS Generative AI CDK Constructs are high level, multi-service abstractions of AWS CDK cons

## 星数曲线

```mermaid
xychart-beta
    title "awslabs/generative-ai-cdk-constructs 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 543 --> 545
    line [544, 544]
```

2026-10-18 544 → 2026-10-30 544（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-18 · 置信度 high · 依据 README sha `bd1d12ce9063` · [字段定义](../../DATASET.md)*
