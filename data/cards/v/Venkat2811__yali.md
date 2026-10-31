# Venkat2811/yali

⭐ 13 · Cuda · MIT · 推送 2026-04-08 · [GitHub](https://github.com/Venkat2811/yali) · [官网](https://venkat-systems.bearblog.dev/yali-vs-nvidia-nccl/) · 个人维护

**2-GPU NVLink AllReduce CUDA 库：低延迟集合通信原语**

面向 2 卡 NVLink 配置（A100/H100/B200）的 CUDA AllReduce 库，为分布式深度学习训练提供集合通信原语。采用静态调度、预取与预分配设计，提供 Flash（≤64MB，cp.async 三级预取）与 Stream（>64MB，128 lane 环形缓冲）两种内核模式，支持 FP32/FP16/BF16 与单进程/MPI 多进程。以 Bazel 从源码构建，含基准测试与 NCCL 对比工具；限制为仅支持 2 GPU、单节点、需 NVLink 直连。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Flash 与 Stream 两种内核模式覆盖不同消息大小
- 支持 FP32/FP16/BF16，单进程与 MPI 多进程
- 提供与 NCCL 的基准对比测试与自动化 sweep 脚本
- 通过环境变量（YALI_KERNEL_MODE 等）控制内核与调优参数

## 适用场景

- 双 GPU NVLink 服务器上替代 NCCL 执行 AllReduce 通信
- 小消息延迟敏感的分布式训练场景降低尾延迟
- 测量并对比自有 NVLink 带宽基线与集合通信性能

## 场景标签

`模型训练` · 领域:训练与推理

## 证据(README 行号)

> L7: YALI is a 2-GPU NVLink AllReduce library that outperforms NVIDIA NCCL across the entire message size range (1.2x-2.4
> L55: - **1.2x-2.4x faster than NCCL** across all sizes

## 星数曲线

```mermaid
xychart-beta
    title "Venkat2811/yali 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-26", "2026-10-31"]
    y-axis "stars" 11 --> 14
    line [12, 13, 13]
```

2026-10-18 12 → 2026-10-31 13（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `399512494853` · [字段定义](../../DATASET.md)*
