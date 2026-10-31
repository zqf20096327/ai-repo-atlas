# amirhosssein0/ai-platform-lab

⭐ 14 · Python · MIT · 推送 2026-09-25 · [GitHub](https://github.com/amirhosssein0/ai-platform-lab) · 个人维护

**单节点本地 K8s 集群上自建的 AI 平台工程实验仓**

在单节点裸金属 k3s 集群上完整搭建 AI 平台基础设施的实验仓库：GitOps（ArgoCD App-of-Apps）、Vault 密钥管理、Kyverno 镜像准入、Falco 运行时安全、Velero 备份、Prometheus/Grafana/OTel/ELK 全链路可观测性；AI 侧以 llama.cpp（CUDA 构建）自托管模型服务，LiteLLM 作模型网关，应用层为 FastAPI 后端与 Next.js 聊天前端，数据层用 Postgres 与 Qdrant（RAG）。所有组件经 kubectl + ArgoCD 从零引导，无云依赖。作者声明为亲手逐项构建与验证的学习实验，非模板脚手架产物。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- ArgoCD App-of-Apps 一条命令引导整个平台（应用/安全/可观测/GPU 栈）
- 供应链安全链路：Trivy + Checkov + Cosign 无密钥签名 + Syft SBOM + Kyverno verifyImages 准入
- llama.cpp 自托管 GPU 推理 + LiteLLM 网关 + Presidio PII 检测护栏
- LLM 专属指标（请求/token/成本/PII 检出）与 SRE 风格多窗口燃尽率 SLO 告警

## 适用场景

- 学习在本地 K8s 上从零搭建生产化 AI 平台的完整工程实践
- 参考 GitOps + 密钥管理 + 镜像签名准入的供应链安全方案
- 搭建带 RAG、可观测性与护栏的自托管 LLM 服务参考架构

## 场景标签

`模型网关` `LLM 可观测性` `RAG` `推理引擎` · 领域:Agent 开发

## 证据(README 行号)

> L3: > A production-grade, security-first AI platform built entirely on a single local Kubernetes cluster — from containe
> L11: This is a hands-on lab built to go deep on **AI Platform Engineering** from the DevOps/Platform side — not the ML s
> L41: |**Model Gateway**|LiteLLM Proxy|

## 星数曲线

```mermaid
xychart-beta
    title "amirhosssein0/ai-platform-lab 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `3483ff0e17f6` · [字段定义](../../DATASET.md)*
