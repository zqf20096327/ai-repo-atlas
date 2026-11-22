# kvcache-ai/Mooncake

⭐ 7,101 · C++ · Apache-2.0 · 推送 2026-11-21 · [GitHub](https://github.com/kvcache-ai/Mooncake) · [官网](https://kvcache-ai.github.io/Mooncake/) · 组织维护 · 中文 README

**Kimi 背后的 LLM 推理/训练服务基础设施平台**

Mooncake 是面向大规模 LLM 推理与训练的基础设施项目，采用以 KVCache 为中心的分离式架构，将 prefill 与 decode 集群分离，并利用 GPU 集群中闲置的 CPU、DRAM 与 SSD 资源构建分布式 KV 缓存池。包含三个组件：跨异构网络与加速器进行低延迟数据传输的 Transfer Engine、管理分布式 KV 缓存与模型权重的 Mooncake Store，以及用于弹性 MoE 服务的 Mooncake EP & PG。以 PyPI 包分发（提供 CUDA/NPU/MUSA/ROCm 等多构建变体），与 SGLang、vLLM 等推理框架深度集成，FAST 2025 论文获最佳论文奖。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- KVCache 为中心的 prefill/decode 分离架构与分布式缓存池
- Transfer Engine 支持 RDMA 多网卡带宽聚合、拓扑感知路由与自动故障切换
- 以 PyPI 分发，提供 CUDA、Non-CUDA、NPU、MUSA、ROCm 多种构建
- 被 SGLang、vLLM、TensorRT-LLM、LMDeploy 等多个推理栈集成

## 适用场景

- 为多节点 LLM 推理集群搭建跨实例共享的 KV 缓存池
- 部署 prefill/decode 分离的分布式推理服务
- 分布式强化学习中在推理与训练节点间传输权重与隐状态

## 场景标签

`推理引擎` `强化学习` · 领域:训练与推理

## 证据(README 行号)

> L83: Mooncake is an infrastructure project for large-scale LLM inference and training. It features a KV cache-centric di
> L85: Mooncake includes a high-performance Transfer Engine for low-latency data movement across heterogeneous networks an

## 星数曲线

```mermaid
xychart-beta
    title "kvcache-ai/Mooncake 星数(近 26 点)"
    x-axis ["2026-10-19", "2026-10-23", "2026-10-24", "2026-10-25", "2026-10-26", "2026-10-27", "2026-10-28", "2026-10-29", "2026-10-30", "2026-10-31", "2026-11-01", "2026-11-02", "2026-11-06", "2026-11-08", "2026-11-10", "2026-11-11", "2026-11-12", "2026-11-13", "2026-11-14", "2026-11-15", "2026-11-16", "2026-11-18", "2026-11-19", "2026-11-20", "2026-11-21", "2026-11-22"]
    y-axis "stars" 6808 --> 7127
    line [6834, 6865, 6873, 6877, 6881, 6887, 6899, 6907, 6922, 6930, 6934, 6946, 6877, 7003, 7017, 7025, 7028, 7033, 7040, 7045, 7055, 7061, 7071, 7084, 7092, 7101]
```

2026-10-19 6,834 → 2026-11-22 7,101（+267）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-22 · 置信度 high · 依据 README sha `316e49ec2bab` · [字段定义](../../DATASET.md)*
