# TensoriumCore/Tensorium_lib

⭐ 25 · C++ · MIT · 推送 2026-10-29 · [GitHub](https://github.com/TensoriumCore/Tensorium_lib) · 组织维护

**面向数值相对论的 C++17 张量与网格核 HPC 库**

在 CPU 上演化解算爱因斯坦方程动力学时空的 C++17 科学计算库：提供 SIMD（SSE/AVX/AVX2/AVX-512/Arm NEON）向量化的 Vector/Matrix/Tensor 稠密线性代数容器、BSSN/Z4c 数值相对论演化栈（4/6 阶有限差分、RK4 时间积分、Kreis-Oliger 耗散）、约束监测与移动穿刺黑洞并合模拟。支持 OpenMP 多线程，MPI 域分解与 CUDA 后端处于实验/脚手架阶段，另有可选 LLVM/MLIR 编译器插件和 pybind11 Python 绑定。面向数值相对论与 HPC 研究开发者，需从源码用 CMake 编译。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `high` | 编译与系统依赖俱全 |
| 成熟度 | `idea` | |

## 能力要点

- BSSN/Z4c 数值相对论演化栈：单 Schwarzschild 穿刺到双黑洞并合
- SIMD（SSE 至 AVX-512/NEON）向量化线性代数核与 OpenMP 并行
- FMR 网格细化与移动穿刺跟踪（puncture tracker）
- pybind11 Python 绑定暴露张量代数、度规/曲率与 Z4c 初始数据构造

## 适用场景

- 构建并演化黑洞时空（单穿刺/双黑洞并合）数值模拟
- 监控 Hamiltonian/动量约束与数值收敛性
- 从 Python 使用张量代数与微分几何工具做数值相对论研究

## 场景标签

 · 领域:科学计算/数值相对论

## 证据(README 行号)

> L4: Tensorium_lib is a C++17 scientific computing library for high-performance numerical relativity on CPUs. It provides
> L8: Its low-level kernels are designed around explicit memory layouts, SIMD vectorization, multithreading, memory cache 

## 星数曲线

```mermaid
xychart-beta
    title "TensoriumCore/Tensorium_lib 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 24 --> 26
    line [25, 25]
```

2026-10-18 25 → 2026-10-31 25（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 low · 依据 README sha `6a4041c57db4` · [字段定义](../../DATASET.md)*
