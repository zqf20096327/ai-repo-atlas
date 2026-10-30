# tensorflow/mlir-hlo

⭐ 420 · MLIR · 推送 2026-02-24 · [GitHub](https://github.com/tensorflow/mlir-hlo) · 组织维护

**基于 MLIR 的 HLO 编译器项目（已弃用，迁移至 openxla/xla）**

实现受 XLA HLO IR 启发的线性代数运算集独立编译器，基于 MLIR 组件，提供不依赖 TensorFlow/XLA 单体仓库的端到端编译流程。定义 chlo、mhlo、lmhlo 三个方言支持 HLO 式编译管线，支持 CPU 与 GPU 并为其他加速器提供可复用构件。README 明确声明本仓库已弃用、将被删除，贡献与依赖应转向 openxla/xla 仓库，MHLO 用户应尽可能迁移到 StableHLO。构建需先克隆 LLVM/MLIR 仓库并以 CMake/Ninja 编译，另有 Python API 与外部项目 CMake 集成方式。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- chlo/mhlo/lmhlo 三个 MLIR 方言构成 HLO 式编译管线
- mhlo 方言支持动态形状并可独立于 XLA 演进
- 提供 CPU/GPU 编译及面向其他加速器的可复用构件
- 可通过 find_package(MHLO) 作为外部项目依赖集成

## 适用场景

- 在 XLA 单体仓库之外复用 HLO 编译组件
- 研究 MLIR 方言设计与 HLO 风格编译管线
- 将 HLO 程序编译降低到 LLVM IR/机器码

## 场景标签

 · 领域:编译器/机器学习基础设施

## 证据(README 行号)

> L19: This implements a self-contained compiler for a linear algebra set of operations
> L63: MLIR-HLO aims to provide an end-to-end compiler for CPU and GPU, as well as
> L106: This repository defines three dialects to support a HLO-like compilation

## 星数曲线

```mermaid
xychart-beta
    title "tensorflow/mlir-hlo 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-30"]
    y-axis "stars" 418 --> 421
    line [419, 420, 420]
```

2026-10-18 419 → 2026-10-30 420（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `2ea384c8c47a` · [字段定义](../../DATASET.md)*
