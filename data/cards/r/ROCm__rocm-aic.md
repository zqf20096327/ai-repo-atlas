# ROCm/rocm-aic

⭐ 19 · Shell · MIT · 推送 2026-10-28 · [GitHub](https://github.com/ROCm/rocm-aic) · [官网](https://rocm.github.io/rocm-aic/) · 组织维护

**AMD Instinct GPU 上的分离式 KV Cache LLM 推理栈**

ROCm 官方维护的分布式 KV-cache 推理栈：将 LLM 服务框架（源码构建的 vLLM + AITER + FlashAttention）与 KV Cache 块管理器结合，把 KV 张量卸载到 GPU VRAM、CPU DRAM、本地 NVMe 与 NFS-over-RDMA 的分层内存层级，支持约千卡规模共享访问，实现长上下文服务免重算。仓库提供 Docker 镜像构建、测试与基准测试 harness 及 Slurm/Spur 自动化。声明为早期访问技术预览，不建议生产负载。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- KV 张量跨 GPU/DRAM/NVMe/NFS-over-RDMA 分层卸载
- 支持 O(1000) GPU 共享访问的低延迟 KV Cache
- 集成源码构建的 vLLM、AITER、FlashAttention、LMCache、NIXL
- 提供 Docker 构建、基准与 Slurm/Spur 集群自动化

## 适用场景

- AMD Instinct GPU 集群上部署长上下文 LLM 服务
- 跨节点共享 KV Cache 避免预填充重算
- 构建和测试分层内存 KV 卸载的推理平台

## 场景标签

`推理引擎` · 领域:训练与推理

## 证据(README 行号)

> L32: ROCm(tm) AMD Infinity Context (AIC) is a disaggregated KV-cache inference stack
> L34: framework with a KV Cache block manager to offload KV tensors across a tiered

## 星数曲线

```mermaid
xychart-beta
    title "ROCm/rocm-aic 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-27", "2026-10-29"]
    y-axis "stars" 17 --> 20
    line [18, 19, 19]
```

2026-10-18 18 → 2026-10-29 19（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `6f9f4e5a84f4` · [字段定义](../../DATASET.md)*
