# Quantica-Foundation/quantica-lang

⭐ 16 · Rust · MIT · 推送 2026-04-25 · [GitHub](https://github.com/Quantica-Foundation/quantica-lang) · [官网](https://quantica-foundation.github.io/quantica-lang/) · 组织维护

**混合经典–量子编程语言，量子门为一级语法，可选 LLVM 编译**

Quantica 是一门用 Rust 实现的混合经典–量子编程语言：量子寄存器分配（quantum q[2]）、量子门操作（apply Hadamard）与测量直接作为语言原生语法，可与 if/while/函数等经典逻辑混合编写；任意门或线路支持 dagger、controlled 修饰符。运行方式包括解释器与经 LLVM 18 的 AOT 编译（JIT 为实验性），并内置 import/from 模块与包管理。提供 Windows 安装包，Linux/macOS 需 Rust 与 LLVM 18 从源码构建。README 明确声明语言仍处实验阶段，存在未完成特性（match 不完整、无 try/finally）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 量子寄存器与量子门为语言原生语法，可与经典控制流混合
- 任意门/线路可动态附加 dagger 与 controlled 修饰符
- LLVM 18 后端编译为原生机器码，另含解释器（JIT 实验性）
- 内置 import/from 模块与包管理

## 适用场景

- 编写混合经典逻辑与量子线路的算法程序
- 通过 AOT 编译获得原生机器码性能运行仿真负载
- 在语言层面直接实验量子门的受控与逆操作

## 场景标签

 · 领域:量子计算/编程语言

## 证据(README 行号)

> L11: **A Hybrid Classical–Quantum Programming Language with a Unified Execution Model**
> L15: Most quantum languages are just Python libraries. Quantica is a **Hybrid Classical–Quantum Programming Language** w

## 星数曲线

```mermaid
xychart-beta
    title "Quantica-Foundation/quantica-lang 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-30 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 mid · 依据 README sha `927a87bc93d7` · [字段定义](../../DATASET.md)*
