# strict-lang/Strict

⭐ 15 · MLIR · MIT · 推送 2026-10-30 · [GitHub](https://github.com/strict-lang/Strict) · [官网](https://strict.dev) · 组织维护

**面向 AI 编写的低级编程语言：自举、强校验、原生代码生成**

Strict 是一门定位为'AI 能可靠读、写、修改'的小型低级编程语言：每个类型一个文件、每个方法自带内联测试、值不可变、每个问题只有一种解法，`strict check` 与测试可在数秒内验证生成代码。仓库内含编译器、Strict VM、标准库与基于 MLIR/LLVM 的原生代码生成，支持 SIMD、多核、NVIDIA GPU kernel（无需 CUDA 工具链）、HIP、Metal（实验性）与 WebAssembly；已用 Strict 实现 GPT-2 与 Qwen3 推理、神经网络训练等负载。面向开发者，需 LLVM 22 工具链（缺失时可自动安装），非通用语言，网站/数据库等需外部代码互操作。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 自举：解析器、类型推断、VM、MLIR/LLVM 原生代码生成器均用 Strict 编写
- 每方法自带内联测试，`strict check` 数秒内校验生成代码
- 原生代码生成支持 SIMD、多核、NVIDIA GPU（无需 CUDA 工具链）、HIP、WebAssembly
- 已用 Strict 实现 GPT-2 与 Qwen3 推理及神经网络训练

## 适用场景

- 让 AI 生成可被测试与校验快速验证的低层代码
- 编写高性能数值/GPU kernel 并编译到原生代码或 WebAssembly
- 作为程序的可验证'DNA'底层，上层语言在其上生成与演化代码

## 场景标签

 · 领域:编程语言/开发工具

## 证据(README 行号)

> L11: Strict is a small programming language that AI can write, read and change as reliably as people can. Every type is 
> L16: - **Self-hosted**: parser, type inference, validators, the Strict VM and the native code generator (MLIR and LLVM) 

## 星数曲线

```mermaid
xychart-beta
    title "strict-lang/Strict 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-31 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `6bfc3207e517` · [字段定义](../../DATASET.md)*
