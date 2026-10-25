# IBM/AutoMLPipeline.jl

⭐ 371 · Julia · MIT · 推送 2026-10-18 · [GitHub](https://github.com/IBM/AutoMLPipeline.jl) · 组织维护

**Julia 机器学习流水线构建与评估包**

IBM 维护的 Julia 包，用管道组合算子（|>、+、*）把特征选择、PCA/ICA 降维、缩放、独热编码与多种学习器（RandomForest、PrunedTree、VoteEnsemble、StackEnsemble，及经 skoperator 调用的 sklearn 学习器）串成机器学习流水线，并提供 crossvalidate 交叉验证、score 评估、@pipeline 宏与 Distributed 并行评估，支持自动选择最优学习器。面向用 Julia 做数据挖掘与机器学习的开发者，配套论文含基准比较，通过 Julia pkg 安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 管道算子语法组合预处理、特征提取与学习器
- crossvalidate 十折交叉验证与 sklearn 性能指标
- Distributed 并行处理多学习器评估
- skoperator 接入 sklearn 学习器（PCA、SVC、MLP 等）

## 适用场景

- 组合降维、缩放与编码步骤搭建分类/回归流水线
- 并行交叉验证比较多个学习器性能
- 自动在候选学习器中选出最优模型

## 场景标签

`MLOps` · 领域:训练与推理

## 证据(README 行号)

> L1: ## AutoMLPipeline
> L20: #### Please read this [AutoMLPipeline Paper](https://doi.org/10.21105/jcon.00129) for benchmark comparisons.
> L80: rf = skoperator("RandomForestClassifier")

## 星数曲线

```mermaid
xychart-beta
    title "IBM/AutoMLPipeline.jl 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 370 --> 372
    line [371, 371]
```

2026-10-18 371 → 2026-10-25 371（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `64cbcb1e8d62` · [字段定义](../../DATASET.md)*
