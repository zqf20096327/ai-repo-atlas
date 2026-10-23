# scverse/cellrank

⭐ 459 · Python · BSD-3-Clause · 推送 2026-10-14 · [GitHub](https://github.com/scverse/cellrank) · [官网](https://cellrank.readthedocs.io/en/latest/) · 组织维护

**单细胞多视图数据的细胞命运推断框架（马尔可夫态建模）**

CellRank 是研究细胞动力学的模块化框架，基于马尔可夫态建模处理多视图单细胞数据。支持从 RNA velocity、伪时间、实验时间点、代谢标记等多种生物先验估计分化方向，计算初始/终末/中间宏观态，推断命运概率与驱动基因，并可视化与聚类基因表达趋势。后端由 pyGPCCA 提供支持，兼容 scverse 生态。以 Python 包形式经 pip 安装，面向单细胞基因组学分析用户，附带论文与文档。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | BSD-3-Clause |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 基于多视图单细胞数据的马尔可夫态建模
- 支持 RNA velocity、伪时间、代谢标记等多种生物先验
- 计算宏观态、命运概率与驱动基因
- 后端由 pyGPCCA 驱动，兼容 scverse 生态

## 适用场景

- 推断细胞分化方向与终末命运
- 计算命运概率并识别驱动基因
- 可视化与聚类基因表达趋势

## 场景标签

`数据分析` · 领域:效率与自动化

## 证据(README 行号)

> L13: **CellRank** is a modular framework to study cellular dynamics based on Markov state modeling of
> L20: In the backend, it is powered by [pyGPCCA] ([Reuter et al. (2018)]). Feel

## 星数曲线

```mermaid
xychart-beta
    title "scverse/cellrank 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-23"]
    y-axis "stars" 458 --> 460
    line [459, 459]
```

2026-10-18 459 → 2026-10-23 459（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `abf7c8e6a2ee` · [字段定义](../../DATASET.md)*
