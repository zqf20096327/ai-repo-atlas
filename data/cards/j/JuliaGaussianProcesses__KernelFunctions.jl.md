# JuliaGaussianProcesses/KernelFunctions.jl

⭐ 276 · Julia · MIT · 推送 2026-10-11 · [GitHub](https://github.com/JuliaGaussianProcesses/KernelFunctions.jl) · [官网](https://juliagaussianprocesses.github.io/KernelFunctions.jl/stable/) · 组织维护

**Julia 机器学习核函数库：灵活构建与组合各类核函数**

Julia 生态的通用核函数包，提供创建与操作核函数的框架及大量实现。设计目标为：核间运算灵活且 API 友好；模型无关、可即插即用，与 ParameterHandling.jl、Funiors.jl 等参数处理包互操作；核函数与 ForwardDiff.jl、Zygote.jl 等自动微分包兼容。它取代已停止维护的 MLKernels.jl，吸收 GaussianProcesses.jl 等包的实现，被 AbstractGPs.jl、ApproximateGPs.jl、Stheno.jl 等下游包使用。面向 Julia 机器学习与高斯过程开发者。

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

- 提供核函数创建、运算与组合的通用框架及大量实现
- 模型无关设计，与参数处理包互操作
- 核函数支持自动微分（ForwardDiff.jl / Zygote.jl）
- 被 AbstractGPs.jl、ApproximateGPs.jl、Stheno.jl 等下游包使用

## 适用场景

- 在 Julia 中为高斯过程模型构建与组合核函数
- 为机器学习模型提供可微分的核函数实现
- 作为下游 GP 包的核函数基础设施

## 场景标签

 · 领域:机器学习/高斯过程

## 证据(README 行号)

> L13: **KernelFunctions.jl** is a general purpose kernel package.
> L31: This package replaces the now-defunct MLKernels.jl. It incorporates lots of excellent existing work from packages s

## 星数曲线

```mermaid
xychart-beta
    title "JuliaGaussianProcesses/KernelFunctions.jl 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 275 --> 277
    line [276, 276]
```

2026-10-18 276 → 2026-10-31 276（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `d5920292d115` · [字段定义](../../DATASET.md)*
