# InftyAI/llmaz

⭐ 315 · Go · Apache-2.0 · 推送 2026-08-27 · [GitHub](https://github.com/InftyAI/llmaz) · [官网](https://llmaz.inftyai.com) · 组织维护

**Kubernetes 上的大模型推理平台，简化 LLM 服务部署**

基于 Kubernetes Operator 模式的 LLM 推理平台：用户通过声明式 CRD（Model/Playground）以少量配置部署模型服务。后端支持 vLLM、TGI、SGLang、llama.cpp、TensorRT-LLM 等推理框架；模型源支持 HuggingFace、ModelScope、对象存储，自动处理模型下载加载。另提供分布式推理（配合 LWS）、HPA/Karpenter 弹性伸缩、Envoy AI Gateway 网关集成与 Open WebUI 聊天界面。项目自述处于 alpha 阶段，API 可能变更。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 声明式 CRD（Model/Playground）以最少配置部署 LLM 服务
- 支持 vLLM/TGI/SGLang/llama.cpp/TensorRT-LLM 等多推理后端
- 自动处理 HuggingFace/ModelScope/对象存储的模型加载
- 配合 LWS 的多主机分布式推理与 HPA/Karpenter 弹性伸缩

## 适用场景

- 在 Kubernetes 集群上快速部署和运行 LLM 推理服务
- 统一管理多种推理后端与模型来源
- 按负载弹性伸缩 LLM 服务副本与节点

## 场景标签

`推理引擎` · 领域:训练与推理

## 证据(README 行号)

> L9: **llmaz** (pronounced `/lima:z/`), aims to provide a **Production-Ready** inference platform for large language mode
> L24: - **Broad Backends Support**: llmaz supports a wide range of advanced inference backends for different scenarios, l

## 星数曲线

```mermaid
xychart-beta
    title "InftyAI/llmaz 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 314 --> 316
    line [315, 315]
```

2026-10-18 315 → 2026-10-24 315（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `abee523e4a53` · [字段定义](../../DATASET.md)*
