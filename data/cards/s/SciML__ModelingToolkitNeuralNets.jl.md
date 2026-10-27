# SciML/ModelingToolkitNeuralNets.jl

⭐ 41 · Julia · MIT · 推送 2026-10-25 · [GitHub](https://github.com/SciML/ModelingToolkitNeuralNets.jl) · [官网](https://docs.sciml.ai/ModelingToolkitNeuralNets/stable/) · 组织维护

**Julia 包：在 ODE 系统中嵌入神经网络块求解 UDE**

ModelingToolkitNeuralNets.jl 是 SciML 组织的 Julia 包，用于创建类似 ModelingToolkitStandardLibrary 组件的神经网络块，接入 ModelingToolkit 的 ODESystem 以求解 Universal Differential Equations（UDE）。通过 `inputs`/`outputs` 向量端口（v2 起替代 RealInputArray/RealOutputArray），可将神经网络嵌入方程的任意部分，为模型局部补充缺失物理项。v2 迁移至 ModelingToolkit v10 并移除对 StandardLibrary 的依赖。文档分稳定版与开发版两套。

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

- 创建类似 MTK StandardLibrary 组件的神经网络块
- 可将神经网络接入 ODESystem 方程的任意部分
- v2 改用 inputs/outputs 向量端口，移除 ModelingToolkitStandardLibrary 依赖
- v2 迁移至 ModelingToolkit v10

## 适用场景

- 在机理 ODE 模型的局部嵌入神经网络学习缺失物理项
- 构建 Universal Differential Equations 用于科学机器学习建模
- 复用 ModelingToolkit 符号建模流程做混合建模实验

## 场景标签

 · 领域:科学计算/SciML

## 证据(README 行号)

> L10: ModelingToolkitNeuralNets.jl is a package to create neural network blocks defined similar to MTKStandardLibrary com

## 星数曲线

```mermaid
xychart-beta
    title "SciML/ModelingToolkitNeuralNets.jl 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 40 --> 42
    line [41, 41]
```

2026-10-18 41 → 2026-10-27 41（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `d7a2c7b02661` · [字段定义](../../DATASET.md)*
