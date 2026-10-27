# cool-japan/numrs

⭐ 54 · Rust · Apache-2.0 · 推送 2026-09-12 · [GitHub](https://github.com/cool-japan/numrs) · [官网](https://github.com/cool-japan/numrs) · 个人维护

**Rust 高性能数值计算库，NumPy 的 Rust 原生替代**

面向 Rust 开发者与科研计算用户的数值计算库：提供 N 维数组（Arc 写时复制、O(1) 克隆）、BLAS/LAPACK 线性代数、稀疏矩阵、迭代求解器、数值优化、自动微分、FFT、随机数与统计分布等，通过 feature 开关可选 GPU（WGPU，无原生 CUDA/ROCm）、分布式 TCP 通信、Python 绑定（maturin wheel）、wasm 与多种 I/O 格式。0.4.1 版本标注核心路径已生产加固，quantum 与部分强化学习模块仍属实验性。以 Cargo 依赖方式安装，LAPACK 为默认 feature（OxiBLAS 纯 Rust 实现）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | `idea` | |

## 能力要点

- N 维数组 + BLAS/LAPACK 线性代数，NumPy 兼容广播与 API
- WGPU 后端可选 GPU 加速（Vulkan/Metal/DX12/WebGPU，无原生 CUDA/ROCm）
- distributed feature 提供点对点 TCP 传输的集合通信与分布式 TSQR/Cholesky
- 自动微分（前向/反向）、数值优化与 9 种 NumPy 分位数方法

## 适用场景

- 在 Rust 项目中做矩阵运算与科学计算，替代 Python/NumPy 工作流
- 通过 Python 绑定从 NumPy 生态迁移
- 需要跨平台 GPU 数值计算（WGPU 后端）的开发场景

## 场景标签

 · 领域:科学计算/数值库

## 证据(README 行号)

> L7: NumRS2 is a high-performance numerical computing library for Rust, designed as a Rust-native alternative to NumPy. I
> L33: - **N-dimensional arrays** with efficient memory layout, broadcasting, and `Arc`-backed
> L57: - **Automatic Differentiation**: Forward and reverse mode AD with higher-order derivatives

## 星数曲线

```mermaid
xychart-beta
    title "cool-japan/numrs 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-27"]
    y-axis "stars" 52 --> 55
    line [53, 54, 54]
```

2026-10-18 53 → 2026-10-27 54（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 mid · 依据 README sha `ebaf4a54b086` · [字段定义](../../DATASET.md)*
