# aws-samples/sample-genai-on-eks-starter-kit

⭐ 95 · JavaScript · MIT-0 · 推送 2026-10-23 · [GitHub](https://github.com/aws-samples/sample-genai-on-eks-starter-kit) · [官网](https://aws-samples.github.io/sample-genai-on-eks-starter-kit/) · 组织维护

**在 Amazon EKS 上一键部署生成式 AI 基础设施的启动套件**

面向在 AWS 上自托管 LLM 与 AI 工作负载的团队的生产级启动套件：通过单一 CLI 在 Amazon EKS 上部署 LLM 推理引擎（vLLM、SGLang、Ollama）、AI 网关（LiteLLM、Kong）、向量数据库（Qdrant、Chroma、Milvus）、嵌入模型（TEI）、可观测性（Langfuse、Phoenix）、AI Agent 框架等组件。基础设施由 Terraform 配置，支持 demo 一键部署与交互式选装，并提供模型配置、NVIDIA Dynamo 平台、Neuron/Inferentia2 支持与清理命令。需 AWS CLI、Terraform、kubectl、Helm、Docker 等前置工具。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT-0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 单一 CLI 部署 LLM 服务、AI 网关、向量库、可观测性等 10 类组件
- Terraform 管理 EKS 基础设施，支持 demo 快速部署与交互式选装
- 支持 NVIDIA Dynamo 平台与 AWS Neuron/Inferentia 2 推理
- 提供模型级配置/更新/移除命令与一键清理

## 适用场景

- 团队在 AWS 上自建生产级 LLM 推理与 AI 网关基础设施
- 按需在 EKS 上选装向量数据库、可观测性与 Agent 框架组件
- 使用 GPU（g6e/g6/g5g）或 Inferentia 2 实例运行模型

## 场景标签

 · 领域:云基础设施/LLM 部署

## 证据(README 行号)

> L6: A production-ready starter kit for deploying **generative AI infrastructure** on **Amazon EKS** (Elastic Kubernetes 
> L10: - AI Gateway - LiteLLM, Kong AI Gateway OSS
> L11: - LLM Model - vLLM, SGLang, Ollama

## 星数曲线

```mermaid
xychart-beta
    title "aws-samples/sample-genai-on-eks-starter-kit 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 94 --> 97
    line [96, 95]
```

2026-10-18 96 → 2026-10-24 95（-1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 mid · 依据 README sha `62e5ac4b8e70` · [字段定义](../../DATASET.md)*
