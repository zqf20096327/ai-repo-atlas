# libxsmm/libxsmm

⭐ 980 · C · BSD-3-Clause · 推送 2026-09-28 · [GitHub](https://github.com/libxsmm/libxsmm) · [官网](https://libxsmm.readthedocs.io/) · 组织维护

**小规模稠密/稀疏矩阵运算与深度学习原语的高性能库**

面向深度学习与 HPC 工作负载的 C/C++/Fortran 线性代数库，提供小矩阵乘法（GEMM/BRGEMM）、逐元素原语与稀疏运算，并作为 Tensor Processing Primitives（TPP）的参考实现。核心机制为 JIT 代码特化生成，支持 FP64 到 int1 等多种数据类型，覆盖 Intel SSE/AVX/AVX-512/AMX、AArch64、RISC-V、POWER10 等架构，实现一次构建到处部署。2.0 版将深度学习算子、PyTorch 集成等移至伴生仓库，本仓库保留核心库、JIT 后端与 TPP 前端。限制：GEMM 仅支持 Alpha=1、Beta∈{0,1}、TransA='N'，适合 (MNK)^(1/3)≤64 的小矩阵规模。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | BSD-3-Clause |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 小稠密/稀疏矩阵乘与逐元素原语，TPP 参考实现
- 基于 JIT 代码特化，无需目标平台编译标志
- 支持 FP64~int1 共 17+ 种数据类型
- 覆盖 x86（AVX-512/AMX）、AArch64、RISC-V、POWER10 架构

## 适用场景

- 为深度学习框架/HPC 应用提供小 GEMM 与张量原语后端
- 构建可跨架构移植的高性能算子（卷积、全连接、归一化）
- 在 Fortran 或 C 代码中加速小规模矩阵运算

## 场景标签

 · 领域:HPC/深度学习基础库

## 证据(README 行号)

> L9: LIBXSMM is high performance library for small dense and sparse linear algebra opertions incl. GEMM and elementwise p
> L65: Common operators in deep learning applications (GEMM with activation function fusion, Convolutions with activation 

## 星数曲线

```mermaid
xychart-beta
    title "libxsmm/libxsmm 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-23"]
    y-axis "stars" 979 --> 981
    line [980, 980]
```

2026-10-18 980 → 2026-10-23 980（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `727a487bd6be` · [字段定义](../../DATASET.md)*
