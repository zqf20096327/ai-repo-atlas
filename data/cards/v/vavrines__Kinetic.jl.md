# vavrines/Kinetic.jl

⭐ 150 · Julia · MIT · 推送 2026-06-07 · [GitHub](https://github.com/vavrines/Kinetic.jl) · [官网](https://xiaotianbai.com/Kinetic.jl/dev) · 个人维护

**Julia 编写的计算流体力学工具箱，融合机器学习建模**

以 Julia 编写的计算流体力学（CFD）工具箱，面向从粒子输运视角模拟流体问题：基于可微编程框架，将力学模型与神经网络模型融合统一求解，支持 CPU 与 GPU 上的 1-3 维数值模拟。物理模型覆盖 Boltzmann 方程、辐射输运、Fokker-Planck-Landau、DSMC、Euler、Navier-Stokes、磁流体力学等。生态按模块化拆分为 KitBase（物理与数值格式）、KitML（神经网络方法）、KitFort（可选 Fortran 后端）、FluxReconstruction、KitAMR 等，另有基于 pyjulia 的 Python 接口。以 Julia 注册包形式经包管理器安装，已发表于 JOSS。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 基于可微编程将力学模型与神经网络模型统一求解
- 支持 Boltzmann、辐射输运、Fokker-Planck-Landau、Euler、Navier-Stokes、磁流体力学等模型
- CPU/GPU 上进行 1-3 维数值模拟
- 模块化生态：KitBase/KitML/KitFort/FluxReconstruction/Langevin/KitAMR 等组件

## 适用场景

- 从动理学理论（Boltzmann 方程）到连续介质力学的跨尺度数值模拟
- 用神经网络与物理模型融合的方式求解输运问题
- 开展等离子体、稀薄气体等粒子输运相关的科研计算

## 场景标签

`科研工具` · 领域:学习与行业

## 证据(README 行号)

> L13: **Kinetic** is a computational fluid dynamics toolbox written in Julia.
> L15: Based on differentiable programming, mechanical and neural network models are fused and solved in a unified framewo
> L21: - KitBase: physical models and numerical schemes

## 星数曲线

```mermaid
xychart-beta
    title "vavrines/Kinetic.jl 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 149 --> 151
    line [150, 150]
```

2026-10-18 150 → 2026-10-29 150（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 mid · 依据 README sha `6095331051c3` · [字段定义](../../DATASET.md)*
