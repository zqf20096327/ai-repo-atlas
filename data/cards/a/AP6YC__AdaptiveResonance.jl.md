# AP6YC/AdaptiveResonance.jl

⭐ 28 · Julia · MIT · 推送 2026-10-15 · [GitHub](https://github.com/AP6YC/AdaptiveResonance.jl) · [官网](https://AP6YC.github.io/AdaptiveResonance.jl) · 组织维护

**Julia 实现的自适应共振理论（ART）算法库，供科研与工程**

以 Julia 包形式提供自适应共振理论（ART）系列无监督与 ARTMAP 监督算法实现，包括 FuzzyART、HypersphereART、DVFA、DDVFA、SFAM、FAM 六个模块，并通过模块选项实现 Gamma-Normalized FuzzyART、Default ARTMAP 等文献变体；另附 ARTSCENE 多阶段滤波、分类精度计算与补码/线性归一化等辅助方法。训练与分类支持增量或批量数据，无监督模块可将内部类别映射为监督标签。通过 Julia 包管理器安装，2022 年发表于 JOSS。

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

- 实现 6 个 ART/ARTMAP 模块及多个文献变体
- train!/classify 支持增量与批量数据，行特征列样本
- 无监督模块可映射监督标签、支持完全失配时取最佳匹配单元
- 附 ARTSCENE 滤波、补码编码、线性归一化等辅助方法

## 适用场景

- 科研中复现和实验 ART/ARTMAP 系列聚类与分类算法
- 工程应用中做无监督/简单监督的模式学习
- 在 Julia 工作流中直接以包形式引入增量聚类算法

## 场景标签

`科研工具` · 领域:学习与行业

## 证据(README 行号)

> L21: This package provides implementations of many of these algorithms in Julia for both scientific research and enginee
> L107: This project has implementations of the following ART (unsupervised) and ARTMAP (supervised) modules:

## 星数曲线

```mermaid
xychart-beta
    title "AP6YC/AdaptiveResonance.jl 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 27 --> 29
    line [28, 28]
```

2026-10-18 28 → 2026-10-27 28（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `3aecbcbcda09` · [字段定义](../../DATASET.md)*
