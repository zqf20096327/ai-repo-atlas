# Cre4T3Tiv3/jetson-orin-matmul-analysis

⭐ 22 · Python · MIT · 推送 2026-04-02 · [GitHub](https://github.com/Cre4T3Tiv3/jetson-orin-matmul-analysis) · [官网](https://bytestacklabs.com) · 个人维护

**Jetson Orin Nano 上 CUDA 矩阵乘法的基准测试框架**

面向 NVIDIA Jetson Orin Nano 的科学基准测试框架：对四种 CUDA 矩阵乘法实现（naive、cache 分块、cuBLAS、Tensor Core WMMA/TF32）在三种功率模式（15W/25W/MAXN）与五种矩阵规模下测吞吐。每个结果与 NumPy 参考计算比对，强制 99.5% 精度阈值校验，并对照理论硬件限值与实时 GPU 频率。C++/CUDA 与 Python 编写，需 JetPack 6.x 与 CUDA Toolkit 12.6+，通过 make 构建运行。

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

- 四种 CUDA 实现（naive/分块/cuBLAS/Tensor Core WMMA）跨三种功率模式基准测试
- 结果经 NumPy 参考计算逐元素校验，强制 99.5% 精度阈值
- 60 个校验数据点，含实时 GPU 频率测量与理论峰值对照
- CI 强制 Ruff/mypy/pytest/clang-format 等全部 linter

## 适用场景

- 在 Jetson Orin Nano 上评估不同功率模式的性能与能效
- 比较 cuBLAS 与 Tensor Core 实现的 ML 推理吞吐
- 学习 CUDA 优化策略的量化效果（分块、Tensor Core）

## 场景标签

 · 领域:边缘计算/GPU 性能基准

## 证据(README 行号)

> L1: Scientific benchmarking framework for CUDA matrix multiplication on NVIDIA Jetson Orin Nano. Four implementations, t
> L22: Matrix multiplication is the computational primitive underlying neural network inference, training, and linear alge
> L24: The four implementations span the optimization spectrum: naive element-wise computation, cache-blocked tiling for m

## 星数曲线

```mermaid
xychart-beta
    title "Cre4T3Tiv3/jetson-orin-matmul-analysis 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 21 --> 23
    line [22, 22]
```

2026-10-18 22 → 2026-10-31 22（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `0ca9e5c47f2f` · [字段定义](../../DATASET.md)*
