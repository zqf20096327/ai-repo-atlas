# awslabs/aiops-modules

⭐ 103 · Python · Apache-2.0 · 推送 2026-05-11 · [GitHub](https://github.com/awslabs/aiops-modules) · 组织维护

**AWS 上 ML/LLM/GenAI 开发运维的可复用 IaC 模块集**

awslabs 维护的基础设施即代码模块集合，配合 SeedFarmer CLI 使用，模块间解耦、可经 GitOps 清单聚合部署。覆盖 SageMaker 环境/HyperPod/端点/模型监控与 CI-CD、Bedrock 微调、JumpStart 与 Hugging Face 基础模型端点、Mlflow 跟踪服务器与 AI 网关、Ray on EKS 分布式训练、MWAA 编排、Step Functions MLOps、AppSync RAG 问答、Strands Agent 等，用于在 AWS 上搭建 MLOps/FMOps/LLMOps 环境。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 配合 SeedFarmer CLI 与 GitOps 清单聚合部署的解耦 IaC 模块
- 覆盖 SageMaker、Bedrock、Mlflow、Ray/EKS、MWAA、Step Functions 的模块目录
- 提供端到端示例清单（GPT-J 微调、DeepSeek R1 部署、RAG 问答、天气 Agent 等）
- 兼容 Industry Data Framework (IDF) 与 Autonomous Driving Data Framework (ADDF) 模块

## 适用场景

- 在 AWS 上搭建含 Studio/HyperPod 的 SageMaker MLOps 环境
- 部署 Mlflow 跟踪服务器与模型注册表
- 用 Ray on EKS 运行 LLM 微调与分布式训练
- 部署基础模型端点与 Bedrock 微调流水线

## 场景标签

`MLOps` · 领域:训练与推理

## 证据(README 行号)

> L3: AIOps modules is a collection of reusable Infrastructure as Code (IAC) modules that works with SeedFarmer CLI. Pleas
> L5: The modules in this repository are decoupled from each other and can be aggregated together using GitOps (manifest f
> L9: The modules in this repository are / must be generic for reuse without affiliation to any one particular project in 

## 星数曲线

```mermaid
xychart-beta
    title "awslabs/aiops-modules 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-25", "2026-10-27"]
    y-axis "stars" 102 --> 105
    line [104, 103, 103]
```

2026-10-18 104 → 2026-10-27 103（-1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 mid · 依据 README sha `385bb3ed246f` · [字段定义](../../DATASET.md)*
