# builtbyahnaf/Project-Nirqoba

⭐ 3 · C++ · NOASSERTION · 推送 2026-11-26 · [GitHub](https://github.com/builtbyahnaf/Project-Nirqoba) · 个人维护

**静态类型通用编程语言，统一系统/数值/AI 开发**

由个人开发者构建的静态类型编译型语言，通过 MLIR 与 LLVM 生成原生机器代码。核心机制为混合内存模型：默认所有权与借用检查，可选的代际增量垃圾回收器，以及可插拔的显式分配器（arena/pool/slab 等）。编译管线为 Lexer→Parser→AST→TypeChecker→TIR→MLIR→LLVM IR，支持 O0-O3 优化、SIMD 向量化与逃逸分析栈提升。当前版本 0.621-beta，面向 Windows x64 MSVC；张量、自动微分与 GPU 执行等能力标注为 Planned。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | `idea` | |

## 能力要点

- 默认所有权/借用 + 可选代际增量 GC 的混合内存模型
- 经 MLIR/LLVM 编译到原生机器码，含逃逸分析与 SIMD 向量化
- 8 种可插拔显式分配器，支持按线程或按操作绑定
- 直接互操作 C/C++ ABI 与 DirectX/DXGI

## 适用场景

- 编写需要精细内存控制的系统程序
- 数值计算与科学计算开发
- 在一门语言中混合高级抽象与底层硬件控制

## 场景标签

 · 领域:编程语言/编译器基础设施

## 证据(README 行号)

> L9: **Nirqoba** is an ambitious, statically typed, high-performance systems and scientific programming language built by
> L40: |**Numerical & AI (Planned)**|First-class tensors, computational graphs, automatic differentiation, reduced precisi
> L94: The language is actively progressing through its architectural milestones. Current active version: **`0.621-beta`**


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-28 · 置信度 high · 依据 README sha `cc9700dfe8e4` · [字段定义](../../DATASET.md)*
