# JuliaAI/DecisionTree.jl

⭐ 364 · Julia · NOASSERTION · 推送 2025-11-09 · [GitHub](https://github.com/JuliaAI/DecisionTree.jl) · 组织维护

**Julia 决策树（CART）与随机森林算法实现库**

用 Julia 编写的决策树（CART）与随机森林机器学习库，支持分类与回归：预剪枝/后剪枝、多线程 bagging 随机森林、SAMME 自适应提升决策桩、n 折交叉验证。提供原生 API 与 ScikitLearn.jl、MLJ.jl 两套接口，模型可经 JLD2.jl 保存加载，并提供不纯度/分割/置换三种特征重要性与 print_tree 可视化。通过 Julia 包管理器安装，供使用 Julia 的机器学习开发者使用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 分类与回归的决策树、随机森林、AdaBoost 决策桩实现
- 提供原生 API 及 ScikitLearn.jl、MLJ.jl 两套接口
- impurity/split/permutation 三种特征重要性度量
- 模型可经 JLD2.jl 保存与加载

## 适用场景

- 在 Julia 中训练决策树/随机森林做分类或回归
- 通过 MLJ.jl 或 ScikitLearn.jl 流水线使用树模型
- 查看特征重要性与树结构可视化

## 场景标签

 · 领域:机器学习/算法库

## 证据(README 行号)

> L8: Julia implementation of Decision Tree (CART) and Random Forest algorithms
> L19: ## Classification

## 星数曲线

```mermaid
xychart-beta
    title "JuliaAI/DecisionTree.jl 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-22"]
    y-axis "stars" 363 --> 365
    line [364, 364]
```

2026-10-18 364 → 2026-10-22 364（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `933bf439c9d8` · [字段定义](../../DATASET.md)*
