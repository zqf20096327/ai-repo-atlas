# Tiramisu-Compiler/tiramisu

⭐ 963 · C++ · MIT · 推送 2026-07-21 · [GitHub](https://github.com/Tiramisu-Compiler/tiramisu) · [官网](http://tiramisu-compiler.org) · 组织维护

**多面体编译器：用 C++ API 表达并优化数据并行算法**

基于多面体模型的 C++ 编译器与库，开发者用 Tiramisu 表达式描述算法并声明循环优化与数据布局变换，编译器生成优化代码。后端覆盖多核 X86 CPU、Nvidia GPU、Xilinx FPGA（Vivado HLS）与 MPI 分布式机器，应用领域包括线性/张量代数、深度学习、图像处理与机器学习。提供 spack 安装或源码构建（依赖 CMake、LLVM、ISL、Halide），可选自动调度器与 Python 绑定。

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

- 基于多面体模型表达循环优化与数据布局变换
- 四种目标后端：X86 CPU、Nvidia GPU、Xilinx FPGA、MPI 分布式
- C++ API 声明式描述算法与优化策略
- 可选自动调度器模块与 Python 3.8+ 绑定

## 适用场景

- 为深度学习或张量代数算子生成多后端优化代码
- 对 stencil、图像处理等数据并行算法做循环级优化
- 针对 CPU/GPU/FPGA/分布式环境移植同一算法描述

## 场景标签

`代码生成` · 领域:编码与开发

## 证据(README 行号)

> L5: Tiramisu is a compiler for expressing fast and portable data parallel computations. It provides a simple C++ API for
> L7: The Tiramisu compiler is based on the polyhedral model thus it can express a large set of loop optimizations and dat

## 星数曲线

```mermaid
xychart-beta
    title "Tiramisu-Compiler/tiramisu 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-24", "2026-10-26"]
    y-axis "stars" 961 --> 964
    line [962, 963, 963]
```

2026-10-18 962 → 2026-10-26 963（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `31bd8c1bf9e6` · [字段定义](../../DATASET.md)*
