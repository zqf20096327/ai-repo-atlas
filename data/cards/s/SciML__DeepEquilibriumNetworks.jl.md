# SciML/DeepEquilibriumNetworks.jl

⭐ 59 · Julia · MIT · 推送 2026-10-28 · [GitHub](https://github.com/SciML/DeepEquilibriumNetworks.jl) · [官网](https://docs.sciml.ai/DeepEquilibriumNetworks/stable/) · 组织维护

**Julia 框架：训练与推理深度平衡网络（无限深神经网络）**

构建于 DifferentialEquations.jl 与 Lux.jl 之上的 Julia 框架，用于深度平衡网络（DEQ，无限深神经网络）的高效训练与推理，实现 O(1) 反向传播与加速收敛。提供 Pkg 安装方式与快速上手示例，示例中提及可选加载 LuxCUDA/LuxAMDGPU 以获得 GPU 支持。面向使用 Julia 进行神经网络研究开发的科研与工程用户，项目附论文引用信息与贡献指南。

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

- 基于 DifferentialEquations.jl 与 Lux.jl 构建的 DEQ 训练/推理框架
- O(1) 反向传播与加速收敛机制
- 支持通过 LuxCUDA/LuxAMDGPU 启用 GPU

## 适用场景

- 用 Julia 训练深度平衡网络模型
- 开展隐式深度学习方向的科研实验
- 复现与引用 Continuous Deep Equilibrium Models 论文工作

## 场景标签

 · 领域:机器学习框架/科学计算

## 证据(README 行号)

> L13: DeepEquilibriumNetworks.jl is a framework built on top of
> L15: Lux.jl enabling the efficient training and inference for
> L16: Deep Equilibrium Networks (Infinitely Deep Neural Networks).

## 星数曲线

```mermaid
xychart-beta
    title "SciML/DeepEquilibriumNetworks.jl 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 58 --> 60
    line [59, 59]
```

2026-10-18 59 → 2026-10-29 59（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `e0c5b819d54f` · [字段定义](../../DATASET.md)*
