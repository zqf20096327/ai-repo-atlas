# raamana/kernelmethods

⭐ 45 · Python · NOASSERTION · 推送 2026-04-04 · [GitHub](https://github.com/raamana/kernelmethods) · [官网](https://raamana.github.io/kernelmethods/) · 个人维护

**Python 核方法库：提供核矩阵与多种核函数的模块化实现**

纯 Python 的核方法（kernel methods）基础库，面向机器学习开发与科研用户。核心是 KernelMatrix 类，衔接输入数据与核学习算法，支持核矩阵的归一化、中心化、乘积、对齐评估、线性组合与排序等操作；提供 KernelSet/KernelBucket 管理大规模核集合，用于自动核选择与 Multiple Kernel Learning。除高斯、多项式等数值核外，设计上支持类别、字符串、图等非数值核的扩展开发，并提供兼容 scikit-learn 的 KernelMachine（SVM）与 OptimalKernelSVR 估计器。README 自述软件处于 beta 阶段。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- KernelMatrix 类支持归一化、中心化、对齐评估、线性组合等核操作
- KernelSet/KernelBucket 管理核集合，用于自动核选择与 MKL
- 兼容 scikit-learn 的 KernelMachine（SVM）与 OptimalKernelSVR 估计器
- 支持类别、字符串、图等非数值核的扩展框架

## 适用场景

- 在机器学习流程中自定义或扩展核函数
- 进行 Multiple Kernel Learning 与自动核选择实验
- 以 scikit-learn 估计器形式使用核 SVM

## 场景标签

 · 领域:机器学习/模式分析

## 证据(README 行号)

> L34: ``kernelmethods`` is a pure python library defining modular classes that provides basic kernel methods as well as a
> L46: Moreover, drop-in ``Estimator`` classes are provided, called ``KernelMachine``, offering the power of ``SVM`` for s

## 星数曲线

```mermaid
xychart-beta
    title "raamana/kernelmethods 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 44 --> 46
    line [45, 45]
```

2026-10-18 45 → 2026-10-30 45（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `9158775d6496` · [字段定义](../../DATASET.md)*
