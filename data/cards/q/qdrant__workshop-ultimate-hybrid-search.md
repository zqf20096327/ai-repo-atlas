# qdrant/workshop-ultimate-hybrid-search

⭐ 50 · Jupyter Notebook · 推送 2026-09-02 · [GitHub](https://github.com/qdrant/workshop-ultimate-hybrid-search) · 组织维护

**Qdrant 混合检索实战教程：用 Query API 构建并评测混合搜索**

一个 hands-on 线下研讨会的配套材料仓库：演示如何使用 Qdrant 1.10 引入的 Query API 组合多种检索方式（不同向量方法结合）以提升搜索质量。流程分为两个 Jupyter notebook——先用三种方法索引文档，再组合检索结果并做效果评测。使用 BeIR 基准中的 SciFact 数据集（5.18k 文档、1.11k 查询），依赖 Python 3.10+ 与 poetry，模型全部为开源模型、CPU 可运行；需自备 Qdrant 实例（本地或 Qdrant Cloud 免费层）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 基于 Qdrant 1.10 Query API 构建混合检索的步骤化教程
- 用三种方法索引文档并组合检索结果做数据驱动评测
- 使用 BeIR/SciFact 数据集（5.18k 文档、1.11k 查询）
- 仅用开源模型，CPU 可运行

## 适用场景

- 学习如何组合多种检索方法构建混合搜索
- 跟着 notebook 实践 Qdrant Query API 的索引与检索
- 对自己的检索方案做量化效果评测

## 场景标签

`教程课程` `语义搜索` `模型评测` · 领域:评测与运维

## 证据(README 行号)

> L3: This repository contains the materials for the hands-on webinar "[How to Build the Ultimate Hybrid Search with
> L4: Qdrant](https://www.youtube.com/watch?v=LAZOxqzceEU)". It is a step-by-step guide on how to utilize the new Query AP
> L32: Building and evaluating a search system are two different tasks. We will start by indexing all the available docume

## 星数曲线

```mermaid
xychart-beta
    title "qdrant/workshop-ultimate-hybrid-search 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 49 --> 51
    line [50, 50]
```

2026-10-18 50 → 2026-10-29 50（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `91746e17feee` · [字段定义](../../DATASET.md)*
