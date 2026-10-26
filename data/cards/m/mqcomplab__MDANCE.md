# mqcomplab/MDANCE

⭐ 147 · Python · MIT · 推送 2026-10-23 · [GitHub](https://github.com/mqcomplab/MDANCE) · [官网](https://mdance.readthedocs.io) · 组织维护

**分子动力学轨迹分析工具包：提供9种线性复杂度聚类算法**

面向分子动力学模拟数据分析的 Python 库，基于 n-ary 相似度框架提供 9 个算法模块：NANI 确定性 k-means 初始化、HELM 层次聚类、DIVINE 分裂聚类、mdBIRCH 在线流式聚类、SHINE 通路分析、PRISM 通路表征聚类、eQual 线性聚类、CADENCE 密度聚类、PRIME 天然结构预测（在 2Å RMSD 内识别实验结构）。各算法将 O(N²) 复杂度降为 O(N)，避免成对距离矩阵。供科研人员使用，方法经同行评审论文支撑，由 NIH 资助项目维护。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 9 个算法模块覆盖初始化、层次/分裂/在线/密度聚类与通路分析
- 声称将 O(N²) 复杂度降至 O(N)，避免成对距离矩阵
- PRIME 模块用于从模拟数据预测天然蛋白结构
- 提供 pip 安装与各算法教程

## 适用场景

- 对百万帧级 MD 轨迹做快速聚类与构象分析
- 从增强采样数据中识别主导生物通路
- 将计算模型结构与实验结构对照验证
- 流式处理在线产生的 MD 帧

## 场景标签

`科研工具` · 领域:学习与行业

## 证据(README 行号)

> L1: # MDANCE: Molecular Dynamics Analysis with *N*-ary Clustering Ensembles
> L26: MDANCE introduces a novel *n*-ary similarity framework that transforms how we analyze MD trajectories. Our algorith
> L165: - NANI: J. Chem. Theory Comput. 2024; J. Chem. Inf. Model. 2025

## 星数曲线

```mermaid
xychart-beta
    title "mqcomplab/MDANCE 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 146 --> 148
    line [147, 147]
```

2026-10-18 147 → 2026-10-26 147（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `634d725cc2da` · [字段定义](../../DATASET.md)*
