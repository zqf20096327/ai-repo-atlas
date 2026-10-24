# libxsmm/tpp-mlir

⭐ 166 · MLIR · NOASSERTION · 推送 2026-10-20 · [GitHub](https://github.com/libxsmm/tpp-mlir) · [官网](https://arxiv.org/abs/2404.15204) · 组织维护

**基于 MLIR 的线性代数 TPP 编译器实验，自动选择最优微内核**

libxsmm 组织维护的 out-of-tree MLIR 方言项目：用 MLIR 自动为线性代数运算选择最优 Tensor Processing Primitives（TPP），提供 opt 类编译工具与 runner 类内核执行/基准工具，并通过 recipes 在 MLIR 内调用 LIBXSMM，供其他工具驱动其编译 pass。构建需先编译 LLVM/MLIR，依赖 libxsmm 与 libxsmm-dnn 由构建系统自动拉取，可选 OpenMP，支持 Linux/macOS，提供 Conda 环境方案。前身为 tpp-sandbox。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | `idea` | |

## 能力要点

- MLIR 方言 + opt 类工具，自动选择线性代数最优 TPP
- runner 类工具执行与基准测试 MLIR 内核
- recipes 支持从 MLIR 内部调用 LIBXSMM
- 提供 Conda 最小环境与多平台 CI（含 Arm Graviton 3）

## 适用场景

- 为线性代数/HPC 内核生成优化的 CPU 微内核
- 研究 MLIR 编译 pass 与 TPP 抽象的实验平台
- 对 MLIR 内核做执行与性能基准测试

## 场景标签

 · 领域:AI 编译器/HPC

## 证据(README 行号)

> L3: This is an experiment in using MLIR to automatically select the best Tensor Processing Primitives for linear algebra
> L5: This repository contains an out-of-tree MLIR dialect as well as an `opt`-like tool to operate on that dialect and a 
> L7: It also contains the recipes to use LIBXSMM from inside MLIR and can be used by other tools to drive our passes.

## 星数曲线

```mermaid
xychart-beta
    title "libxsmm/tpp-mlir 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-24"]
    y-axis "stars" 164 --> 167
    line [165, 166, 166]
```

2026-10-18 165 → 2026-10-24 166（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `a1c4ce57caa4` · [字段定义](../../DATASET.md)*
