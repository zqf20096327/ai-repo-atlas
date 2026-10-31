# RAZZULLIX/fast_topk_batched

⭐ 18 · C · MIT · 推送 2026-03-20 · [GitHub](https://github.com/RAZZULLIX/fast_topk_batched) · 个人维护

**CPU 批量 Top-K 选择 C 库：加速 LLM 采样环节**

用 C 实现的高性能批量 Top-K 选择库，面向 CPU 推理中的 LLM 采样负载，供 Python 经 ctypes 调用。README 给出与 PyTorch CPU/CUDA 的延迟基准数据，声称小批量下与 CUDA 相当。实现机制包括自适应采样加最小堆跟踪、AVX2 SIMD 8 路并行比较、缓存优化的块扫描，以及对有序/常量输入的快速路径。安装方式为从源码用 gcc 编译为共享库（Windows/Linux/macOS 各有命令），MIT 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `high` | 编译与系统依赖俱全 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- C 语言实现，经 ctypes 供 Python 调用
- AVX2 SIMD 8 路并行比较与最小堆跟踪
- README 提供与 PyTorch CPU/CUDA 的延迟基准表
- 对有序/常量输入提供快速路径

## 适用场景

- CPU 上做 LLM 采样时替换 PyTorch Top-K 以降低延迟
- 小批量推理场景减少采样环节开销
- 无 GPU 环境下加速推理采样步骤

## 场景标签

`推理引擎` · 领域:训练与推理

## 证据(README 行号)

> L3: High-performance batched Top-K selection for CPU inference. Optimized for LLM sampling workloads.
> L7: **Up to 80x faster than PyTorch CPU, competitive with CUDA for small batches.**

## 星数曲线

```mermaid
xychart-beta
    title "RAZZULLIX/fast_topk_batched 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 17 --> 19
    line [18, 18]
```

2026-10-18 18 → 2026-10-31 18（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `8a4fbfe9100f` · [字段定义](../../DATASET.md)*
