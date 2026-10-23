# GaeaRuiW/kube-llmops

⭐ 103 · Go · Apache-2.0 · 推送 2026-06-12 · [GitHub](https://github.com/GaeaRuiW/kube-llmops) · 个人维护 · 中文 README

**Kubernetes 原生 LLMOps 平台：一条命令部署整套 LLM 运维栈**

以 Helm chart + Go Operator 形式在 Kubernetes 上部署完整 LLM 运维栈：模型服务按格式自动选择 vLLM/llama.cpp/TEI；LiteLLM 网关提供统一 OpenAI 兼容 API、密钥与预算管理；Prometheus/Grafana/Langfuse 构成可观测体系；KEDA 基于 TTFT/TPOT 指标自动伸缩并支持缩到零；集成 Keycloak SSO、Dify RAG、LLaMA-Factory 微调管道。配套 kubectl 插件（15+ 命令）与 Headlamp 仪表盘，提供 CI/最小/团队/生产四种部署配置。面向需要在 K8s 上运行和治理 LLM 基础设施的团队，Apache 2.0 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 按模型格式自动选择 vLLM/llama.cpp/TEI 推理引擎
- LiteLLM 网关：密钥管理、限流、预算控制
- KEDA 基于 TTFT P95/TPOT P95 的自动伸缩与缩到零
- kubectl-llmops CLI 提供 15+ 命令，含 canary/finetune/rag

## 适用场景

- 在 Kubernetes 集群上部署并让多团队共享一个 LLM，附带 token 预算限制
- 追踪每个 LLM 请求的完整 prompt、token、成本与延迟
- 统计各团队的 GPU 时长消耗
- 同一 API 后面同时服务 GGUF（llama.cpp）与全精度（vLLM）模型

## 场景标签

`MLOps` `推理引擎` `模型网关` `LLM 可观测性` · 领域:Agent 开发

## 证据(README 行号)

> L22: `kube-llmops` is an opinionated, batteries-included Helm chart that deploys a complete LLM operations stack on Kube
> L26: - **AI Gateway** -- LiteLLM for unified OpenAI-compatible API, key management, rate limiting, budget control
> L29: - **Autoscaling** -- KEDA scales vLLM pods based on queue depth, TTFT P95, and TPOT P95; supports scale-to-zero wit

## 星数曲线

```mermaid
xychart-beta
    title "GaeaRuiW/kube-llmops 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-23"]
    y-axis "stars" 101 --> 104
    line [102, 103, 103]
```

2026-10-18 102 → 2026-10-23 103（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `59dd07f721fa` · [字段定义](../../DATASET.md)*
