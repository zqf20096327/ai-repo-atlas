# awslabs/gen-ai-evaluation-toolkit-on-aws

⭐ 21 · TypeScript · Apache-2.0 · 推送 2026-10-30 · [GitHub](https://github.com/awslabs/gen-ai-evaluation-toolkit-on-aws) · [官网](https://awslabs.github.io/gen-ai-evaluation-toolkit-on-aws/) · 组织维护

**AWS 上的生成式 AI 应用评测工具包：测试用例生成与质量评估**

部署到用户自有 AWS 账号的云原生评测加速器：提供测试用例生成与版本管理、基于指标与 LLM 的质量评估（LLM-as-Judge、RAGAS、DeepEval、FMEval、PyRIT 等）及实验结果可视化，采用插件化可扩展架构，支持 Evaluator SDK 用 Python 编写自定义评估器。计算可运行于 AWS Lambda 或 ECS。通过 AWS CDK 或 Terraform 以基础设施即代码方式部署，提供 REST API、生成的 TypeScript/Python 客户端与 CLI。源码以 Apache-2.0 分发。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 插件化评估：内置 LLM-as-Judge、RAGAS、DeepEval、Amazon Bedrock AgentCore 等评估器
- Python Evaluator SDK 编写自定义评估器
- AWS Lambda 或 ECS 灵活计算
- AWS CDK 与 Terraform 双部署路径，附 REST API/客户端/CLI

## 适用场景

- 评估模型在准确率、毒性、鲁棒性等指标上的质量
- 评估 RAG 管线与 agentic 系统
- 将评测加入 CI/CD 流水线

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L3: Gen AI Evaluation Toolkit on AWS is a flexible, cloud-native accelerator built on
> L7: generation and version management, both metrics- and LLM-based quality
> L14: - **Pluggable evaluation.** Run LLM-as-Judge, RAGAS, DeepEval, and Amazon Bedrock

## 星数曲线

```mermaid
xychart-beta
    title "awslabs/gen-ai-evaluation-toolkit-on-aws 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 19 --> 22
    line [20, 21]
```

2026-10-18 20 → 2026-10-31 21（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `1d872de76627` · [字段定义](../../DATASET.md)*
