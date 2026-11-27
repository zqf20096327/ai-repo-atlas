# kvcache-ai/Mooncake

⭐ 7,142 · C++ · Apache-2.0 · 推送 2026-11-26 · [GitHub](https://github.com/kvcache-ai/Mooncake) · [官网](https://kvcache-ai.github.io/Mooncake/) · 组织维护 · 中文 README

**为 Kimi 提供服务的 KVCache 为中心 LLM 推理部署平台**

面向大规模 LLM 推理与训练的基础设施项目，核心是以 KVCache 为中心的分离式架构：将 prefill 与 decode 集群分离，并利用 GPU 集群中闲置的 CPU、DRAM 与 SSD 资源构建分布式 KVCache 池。包含三个组件：提供多协议、拓扑感知路由与自动故障切换的 Transfer Engine；分布式 KV cache 与模型权重管理 Store；面向弹性 MoE 服务的 Mooncake EP & PG。与 SGLang、vLLM 等推理框架集成，通过 PyPI 提供 CUDA/NPU/ROCm 等多种构建。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `high` | 编译与系统依赖俱全 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Transfer Engine：支持 TCP/RDMA/EFA/NVLink 等多种传输协议与多网卡带宽聚合
- Mooncake Store：分布式 KV cache 与模型权重管理
- Mooncake EP & PG 支持弹性 MoE 推理
- 已集成进 SGLang、vLLM、TensorRT-LLM、LMDeploy 等推理栈

## 适用场景

- 为大规模 LLM 推理搭建 PD 分离部署
- 在多节点 GPU 集群间高速传输 KV cache 与模型权重
- 构建跨实例共享的分布式 KV cache 池
- 分布式 RL 训练中在 rollout 与训练间同步权重与张量

## 场景标签

`推理引擎` `强化学习` · 领域:训练与推理

## 证据(README 行号)

> L83: Mooncake is an infrastructure project for large-scale LLM inference and training. It features a KV cache-centric di
> L85: Mooncake includes a high-performance Transfer Engine for low-latency data movement across heterogeneous networks an
> L105: - **Widely adopted across the LLM ecosystem.** TE is used in production inference stacks such as SGLang, vLLM, Ten

## 星数曲线

```mermaid
xychart-beta
    title "kvcache-ai/Mooncake 星数(近 27 点)"
    x-axis ["2026-10-25", "2026-10-26", "2026-10-27", "2026-10-28", "2026-10-29", "2026-10-30", "2026-10-31", "2026-11-01", "2026-11-02", "2026-11-06", "2026-11-08", "2026-11-10", "2026-11-11", "2026-11-12", "2026-11-13", "2026-11-14", "2026-11-15", "2026-11-16", "2026-11-18", "2026-11-19", "2026-11-20", "2026-11-21", "2026-11-22", "2026-11-23", "2026-11-25", "2026-11-26", "2026-11-27"]
    y-axis "stars" 6851 --> 7168
    line [6877, 6881, 6887, 6899, 6907, 6922, 6930, 6934, 6946, 6877, 7003, 7017, 7025, 7028, 7033, 7040, 7045, 7055, 7061, 7071, 7084, 7092, 7101, 7107, 7119, 7131, 7142]
```

2026-10-25 6,877 → 2026-11-27 7,142（+265）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-24 · 置信度 high · 依据 README sha `0064bdf66f1e` · [字段定义](../../DATASET.md)*
