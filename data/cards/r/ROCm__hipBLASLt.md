# ROCm/hipBLASLt

⭐ 116 · Assembly · MIT · 推送 2026-10-26 · [GitHub](https://github.com/ROCm/hipBLASLt) · [官网](https://github.com/ROCm/rocm-libraries) · 组织维护

**AMD GPU 上的 GEMM 矩阵运算库（HIP 后端），已弃用迁库**

hipBLASLt 是 AMD ROCm 生态下提供通用矩阵-矩阵运算（GEMM）的库，通过 hipblasLtMatmul API 执行 D = Activation(alpha·op(A)·op(B) + beta·op(C) + bias) 运算，支持 GELU/ReLU/Swish 激活与 bias 广播。它以 HIP 编程语言编写，底层使用优化生成器作为后端内核提供者，支持灵活的矩阵布局、输入类型与计算类型。要求 gfx90a/gfx94x/gfx110x 显卡、ROCm 5.5+ 及 CMake 等软件。注意：本仓库已弃用，代码迁入 ROCm/rocm-libraries。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- hipblasLtMatmul API 支持 GEMM 加激活（GELU/ReLU/Swish）与 bias 广播
- 基于 HIP 语言，底层优化生成器作为后端内核提供者
- 支持灵活的矩阵数据布局、输入类型、计算类型与算法启发式
- 提供 install.sh 脚本构建及 hipblaslt-test/hipblaslt-bench 测试工具

## 适用场景

- 在 AMD GPU 上为深度学习或 HPC 应用执行 GEMM 运算
- 需要自定义矩阵布局与计算类型的矩阵乘法场景
- 作为 ROCm 生态中其他计算库的底层 BLASLt 依赖

## 场景标签

 · 领域:GPU 计算/线性代数库

## 证据(README 行号)

> L6: hipBLASLt is a library that provides general matrix-matrix operations. It has a flexible API that extends
> L13: hipBLASLt uses the HIP programming language with an underlying optimized generator as its backend
> L71: * AMD ROCm, version 5.5 or later

## 星数曲线

```mermaid
xychart-beta
    title "ROCm/hipBLASLt 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 115 --> 117
    line [116, 116]
```

2026-10-18 116 → 2026-10-28 116（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 mid · 依据 README sha `1eeba1acd536` · [字段定义](../../DATASET.md)*
