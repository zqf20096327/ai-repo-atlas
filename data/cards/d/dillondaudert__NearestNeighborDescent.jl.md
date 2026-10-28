# dillondaudert/NearestNeighborDescent.jl

⭐ 49 · Julia · MIT · 推送 2026-09-19 · [GitHub](https://github.com/dillondaudert/NearestNeighborDescent.jl) · 个人维护

**Julia 实现的近似 kNN 图构建与搜索库**

Nearest Neighbor Descent（NNDescent）算法的 Julia 实现包，提供近似 K 近邻图构建、从图中取回 kNN 矩阵以及对新查询点做近似近邻搜索。支持任意相异度函数，经验复杂度 O(n^1.14)，仅需在近似 kNN 图上原地操作。算法基于'邻居的邻居也可能是邻居'的启发式。面向需要在 Julia 中做近似近邻图构建与搜索的开发者与科研用户，通过 Julia 包管理器安装。

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

- 支持任意相异度函数的近似 kNN 图构建
- 经验复杂度 O(n^1.14) 次两两比较
- 原地操作的近似 kNN 图即最终输出
- 支持对已构图的新查询点做近似搜索

## 适用场景

- 为数据集构建近似 K 近邻图用于下游机器学习流程
- 对新增查询点在已有图上做近似近邻检索

## 场景标签

 · 领域:机器学习/近邻搜索

## 证据(README 行号)

> L7: A Julia implementation of Nearest Neighbor Descent.
> L13: Nearest Neighbor Descent (NNDescent) is an approximate K-nearest neighbor graph construction algorithm that has

## 星数曲线

```mermaid
xychart-beta
    title "dillondaudert/NearestNeighborDescent.jl 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 48 --> 50
    line [49, 49]
```

2026-10-18 49 → 2026-10-28 49（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 mid · 依据 README sha `369af4d6ffc6` · [字段定义](../../DATASET.md)*
