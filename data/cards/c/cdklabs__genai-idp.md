# cdklabs/genai-idp

⭐ 14 · Python · Apache-2.0 · 推送 2026-10-19 · [GitHub](https://github.com/cdklabs/genai-idp) · [官网](https://cdklabs.github.io/genai-idp/) · 组织维护

**AWS CDK 版 GenAI 文档处理加速器：非结构化文档转结构化数据**

由 AWS CDK Labs 维护的智能文档处理（IDP）基础设施加速器，将非结构化文档大规模转换为结构化数据。以可组合的 CDK 包形式提供三种处理模式：Amazon Bedrock Data Automation、Bedrock 模型自定义抽取、SageMaker 端点专用处理。构建于 Lambda、Step Functions、SQS 等无服务技术之上，提供可选的 Web 界面与文档知识库自然语言查询。需 Node.js/yarn/Docker/rsync/Python/.NET/AWS CLI 等环境，从源码构建部署。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 三种预置文档处理模式（BDA / Bedrock LLM / SageMaker UDOP）
- 模块化 CDK 构造可组合为完整方案
- 基于 Lambda、Step Functions、SQS 的无服务架构
- 可选 Web 界面与文档知识库自然语言查询

## 适用场景

- 在 AWS 上部署可定制的大规模文档抽取流水线
- 处理贷款等金融文档并做结构化提取
- 对已处理文档建立自然语言查询知识库

## 场景标签

`文档解析` `文档问答` · 领域:知识与检索

## 证据(README 行号)

> L5: A modular AWS CDK implementation of the GenAI Intelligent Document Processing (IDP) Accelerator, designed to transfo
> L9: This project is a representation of the GenAI Intelligent Document Processing Accelerator as a set of composable AWS
> L29: - **AI-Powered Document Processing**: Leverages Amazon Bedrock, Textract, and other AWS AI services

## 星数曲线

```mermaid
xychart-beta
    title "cdklabs/genai-idp 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `55e5416d4206` · [字段定义](../../DATASET.md)*
