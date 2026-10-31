# microsoft/Accera

⭐ 119 · C++ · MIT · 推送 2026-10-26 · [GitHub](https://github.com/microsoft/Accera) · [官网](https://microsoft.github.io/Accera) · 组织维护

**面向计算密集循环的跨平台优化编译器（Python 库）**

Accera 是微软研究院开源的编译器，以 Python 库形式提供，让开发者无需手写汇编即可实验循环优化（融合、调度、展开等），支持交叉编译到多种处理器目标。工作机制：将定义循环调度与算法的 Python 代码转换为 MLIR 中间表示，经多条 MLIR 管线变换后生成带 C 头文件的二进制库（HAT 格式），可用 hatlib 做基准测试。面向编写 AI/数值算法高性能内核的开发者；运行需本机装有编译器（Windows 的 MSVC 或 Linux/macOS 的 gcc），要求 Python 3.7-3.10；自述为研究中的平台。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- Python 定义算法与循环调度，生成优化二进制库与 C 头文件
- 基于 MLIR 中间表示的编译管线
- 支持交叉编译到多种处理器目标
- 提供 Binder 浏览器内运行 quickstart，无需本地安装

## 适用场景

- 为 matmul+ReLU 等机器学习算子生成优化实现并对比基准
- 实验不同循环变换（融合/调度/展开）对性能的影响
- 交叉编译计算密集内核到多种处理器目标

## 场景标签

 · 领域:编译器/高性能计算

## 证据(README 行号)

> L10: Accera is a compiler that enables you to experiment with loop optimizations without hand-writing Assembly code. Wit
> L97: In a nutshell, Accera takes the Python code that defines the loop schedule and algorithm while converting it into M

## 星数曲线

```mermaid
xychart-beta
    title "microsoft/Accera 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-31"]
    y-axis "stars" 117 --> 120
    line [118, 119, 119]
```

2026-10-18 118 → 2026-10-31 119（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `d3cda1bc835e` · [字段定义](../../DATASET.md)*
