# JuliaDecisionFocusedLearning/InferOpt.jl

⭐ 133 · Julia · MIT · 推送 2026-08-20 · [GitHub](https://github.com/JuliaDecisionFocusedLearning/InferOpt.jl) · [官网](https://juliadecisionfocusedlearning.github.io/InferOpt.jl/) · 组织维护

**Julia 工具箱：将组合优化算法封装为可微分层接入 ML 流水线**

InferOpt.jl 是 Julia 语言工具箱，用于在机器学习流水线中使用组合优化算法：对本身无可导导数的优化 oracle（如混合整数线性规划、图算法）构造可微分层，支持自动微分场景下的结构化学习。提供稳定版与开发版两种 Pkg 安装方式，附带 2022 年 Probabilistic Approach 论文供引用。README 另列出功能相近的相关库（ImplicitDifferentiation.jl、DiffOpt.jl、JAXopt）。

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

- 从无可导导数的优化 oracle 构造可微分层
- 典型适用对象包括混合整数线性规划与图算法
- 与 Julia 机器学习生态及自动微分配合使用

## 适用场景

- 在端到端可微流水线中嵌入组合优化求解步骤
- 决策聚焦学习/结构化学习研究与实验
- 对 MILP 或图算法做参数学习与梯度优化

## 场景标签

 · 领域:机器学习/组合优化

## 证据(README 行号)

> L12: InferOpt.jl is a toolbox for using combinatorial optimization algorithms within machine learning pipelines.
> L14: It allows you to create differentiable layers from optimization oracles that do not have meaningful derivatives.

## 星数曲线

```mermaid
xychart-beta
    title "JuliaDecisionFocusedLearning/InferOpt.jl 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-23"]
    y-axis "stars" 132 --> 134
    line [133, 133]
```

2026-10-18 133 → 2026-10-23 133（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `c2eeeb273872` · [字段定义](../../DATASET.md)*
