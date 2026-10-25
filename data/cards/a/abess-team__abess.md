# abess-team/abess

⭐ 468 · C++ · NOASSERTION · 推送 2026-03-15 · [GitHub](https://github.com/abess-team/abess) · [官网](https://abess.readthedocs.io/) · 组织维护

**面向科研的快速最优子集选择库（Python/R）**

abess 实现 Adaptive Best Subset Selection 通用算法框架，在稀疏建模中寻找最优预测变量子集，支持线性回归、二分类/多分类、计数响应（Poisson）、删失响应（Cox）、多任务学习、Ising 模型估计及群组子集选择、nuisance penalized regression 等变体；线性回归的（群组）最优子集选择时间复杂度为可证明的多项式级。核心框架用 C++ 编写，提供 Python（pip/conda）与 R（CRAN）接口，GPL-3 许可。方法发表于 PNAS、JMLR 等期刊。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 支持线性/逻辑/Poisson/Cox/多任务/Ising 等多种模型的最优子集选择
- 线性回归最优子集选择具有可证明的多项式时间复杂度
- C++ 核心框架，Python 与 R 双接口
- 配套 PNAS/JMLR/INFORMS/JASA 等论文方法实现

## 适用场景

- 高维数据中筛选少量关键预测变量做回归或分类
- 基因组表达数据中挑选与疾病相关的重要基因
- 统计建模中替代 L0 惩罚类方法做变量选择

## 场景标签

 · 领域:机器学习/统计计算

## 证据(README 行号)

> L25: `abess` (Adaptive BEst Subset Selection) library aims to solve general best subset selection, i.e.,
> L31: This framework now supports the detection of best subset under:
> L37: Ising model estimation, etc.

## 星数曲线

```mermaid
xychart-beta
    title "abess-team/abess 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-25"]
    y-axis "stars" 466 --> 469
    line [467, 468, 468]
```

2026-10-18 467 → 2026-10-25 468（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `af968ad8da67` · [字段定义](../../DATASET.md)*
