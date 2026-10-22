# ROCm/Tensile

⭐ 262 · Python · MIT · 推送 2026-10-14 · [GitHub](https://github.com/ROCm/Tensile) · [官网](https://github.com/ROCm/rocm-libraries) · 组织维护

**已弃用：GPU 上 GEMM/张量收缩基准驱动后端库生成工具**

Tensile 用于创建面向 GPU 的基准驱动后端库，覆盖 GEMM、类 GEMM 问题（如批量 GEMM）与一般 N 维张量收缩；主要作为 rocBLAS 的后端库，为运行在 AMD GPU 上的计算类应用提供性能基础。本仓库已退役，README 声明代码迁移至 ROCm/rocm-libraries 仓库，文档源位于 Tensile/docs/src。仓库不再提供本体的安装与维护说明。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 生成 GEMM/批量 GEMM/N 维张量收缩的基准驱动后端库
- 主要作为 rocBLAS 的后端库使用
- 仓库已退役，迁移至 ROCm/rocm-libraries

## 适用场景

- 了解 rocBLAS 的后端实现来源
- 查阅历史文档了解 Tensile 机制

## 场景标签

 · 领域:GPU 计算库/BLAS

## 证据(README 行号)

> L6: Tensile is a tool for creating benchmark-driven backend libraries for GEMMs, GEMM-like problems (such as batched GEM
> L7: The Tensile library is mainly used as a backend library for rocBLAS.

## 星数曲线

```mermaid
xychart-beta
    title "ROCm/Tensile 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-22"]
    y-axis "stars" 261 --> 263
    line [262, 262]
```

2026-10-18 262 → 2026-10-22 262（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `f78133912f73` · [字段定义](../../DATASET.md)*
