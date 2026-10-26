# botAGI/AGmind64

⭐ 28 · Python · Apache-2.0 · 推送 2026-09-27 · [GitHub](https://github.com/botAGI/AGmind64) · [官网](https://agmind.dev) · 组织维护

**单机自托管 LLM/RAG 平台：一条命令部署全套私有 AI 栈**

面向 AMD Strix Halo（gfx1151）或任意 x86_64 Linux 主机的自托管 AI 平台，通过 git clone 加 make setup 一键部署：llama.cpp 在 Vulkan/ROCm（含 CPU 回退）上提供 OpenAI 兼容的 LLM、嵌入与重排序端点，配合 Qdrant 向量库、Dify/RAGFlow RAG 应用、Docling 文档解析，可选 Open WebUI、Prometheus/Grafana 观测、Authelia SSO、n8n 等按 profile 组合。提供 agmind 运维 CLI（安装、诊断、备份恢复、TUI）。所有镜像按 digest 固定，治理检查禁止 NVIDIA/CUDA 路径。状态 pre-1.0，支持单节点 Docker Compose，多节点集群为实验性。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 单一 make setup 部署 LLM/嵌入/重排序/RAG/观测/SSO 全栈
- llama.cpp 以 Vulkan/ROCm 提供 OpenAI 兼容 HTTP 端点
- agmind CLI 覆盖安装、day-2 运维、备份恢复与诊断
- 全部服务镜像 digest 固定并有治理门禁

## 适用场景

- 在自有硬件上搭建不出网、不外发 API key 的私有 AI 平台
- 为团队提供带 RAG、观测与 SSO 的本地 LLM 服务
- AMD GPU（ROCm/Vulkan）环境下运行 MoE 模型推理

## 场景标签

`RAG` `推理引擎` · 领域:知识与检索

## 证据(README 行号)

> L13: AGmind turns an AMD Ryzen AI Max+ "Strix Halo" host (Radeon 8060S / gfx1151) — or
> L16: reranking, a RAG app, a vector store, edge auth, and a monitoring suite, all
> L21: - **Local inference** — llama.cpp serving LLM, embeddings and reranking on

## 星数曲线

```mermaid
xychart-beta
    title "botAGI/AGmind64 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 27 --> 29
    line [28, 28]
```

2026-10-18 28 → 2026-10-26 28（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 mid · 依据 README sha `4b30a24e0303` · [字段定义](../../DATASET.md)*
