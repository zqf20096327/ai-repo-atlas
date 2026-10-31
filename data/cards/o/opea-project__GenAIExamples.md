# opea-project/GenAIExamples

⭐ 739 · Shell · Apache-2.0 · 推送 2026-10-29 · [GitHub](https://github.com/opea-project/GenAIExamples) · [官网](https://opea.dev) · 组织维护

**面向开发者的企业级 GenAI 应用示例集，展示 OPEA 流水线部署**

OPEA 项目旗下的生成式 AI 示例合集，收录 ChatQnA（RAG 问答）、DocSum（文档摘要）、CodeGen、Text2Image、VisualQnA 等十余个用例，由 GenAIComps 微服务组件（llm/embedding/reranking 等）构建，通过 GenAIInfra 实现容器化与云原生部署，GenAIEval 负责吞吐/时延/精度评测。支持 Docker Compose、Kubernetes（Helm/GMC）与 Python 三种启动方式，覆盖 Xeon、Gaudi、AMD EPYC/Instinct、NVIDIA GPU 等硬件；各用例在部分硬件/部署方式上存在 Not Supported 限制。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | `gpu-24g` | |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 十余个微服务化 GenAI 示例（RAG 问答、摘要、代码生成、文生图、多模态问答等）
- Docker Compose / Kubernetes（Helm、GMC）/ Python 三种部署方式
- 覆盖 Xeon、Gaudi、AMD EPYC、AMD Instinct 等硬件并给出参考配置
- 配套 GenAIEval 按硬件配置对比吞吐、时延与精度

## 适用场景

- 快速部署一套企业级 RAG 问答或文档摘要服务
- 在不同硬件（Xeon/Gaudi/AMD）上验证 GenAI 应用部署方案
- 参考示例学习 OPEA 微服务组件的组装方式

## 场景标签

`RAG` `代码生成` `图像生成` `多模态` · 领域:编码与开发

## 证据(README 行号)

> L5: GenAIExamples are designed to give developers an easy entry into generative AI, featuring microservice-based samples
> L9: GenAIComps is a service-based tool that includes microservice components such as llm, embedding, reranking, and so o
> L11: GenAIInfra is part of the OPEA containerization and cloud-native suite and enables quick and efficient deployment o

## 星数曲线

```mermaid
xychart-beta
    title "opea-project/GenAIExamples 星数(近 4 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-27", "2026-10-31"]
    y-axis "stars" 737 --> 740
    line [739, 738, 739, 739]
```

2026-10-18 739 → 2026-10-31 739（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `3561a4f5a477` · [字段定义](../../DATASET.md)*
