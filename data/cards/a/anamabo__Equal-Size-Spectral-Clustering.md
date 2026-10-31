# anamabo/Equal-Size-Spectral-Clustering

⭐ 26 · Python · MIT · 推送 2026-06-22 · [GitHub](https://github.com/anamabo/Equal-Size-Spectral-Clustering) · 个人维护

**约束簇大小的等规模谱聚类 Python 库（ELSARA）**

谱聚类算法的修改版本，在聚类过程中对簇大小施加约束，使各簇包含大致相等的点数。以 pip 包 elsara 提供，核心类 SpectralEqualSizeClustering 支持两种用法：直接给定 nclusters/nneighbors/equity_fraction 超参数，或指定目标簇大小范围由算法自动推导超参数。附带阿姆斯特丹餐厅位置与旅行距离的示例数据集及可视化函数。贡献流程基于 Poetry、Python 3.13 与 PR 版本号约定。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 对谱聚类施加簇规模约束，各簇约含 N/nclusters 个点
- 两种模式：固定超参数或从目标簇大小范围自动推导超参数
- 提供示例数据集（餐厅位置/旅行距离）与聚类可视化函数

## 适用场景

- 需要各簇规模均衡的聚类任务
- 地理点位（如城市设施）的等规模分组
- 指定簇大小范围自动求解可行超参数

## 场景标签

 · 领域:机器学习/聚类算法

## 证据(README 行号)

> L6: This is a modification of the spectral clustering algorithm that builds clusters balanced
> L38: from elsara import SpectralEqualSizeClustering, visualise_clusters

## 星数曲线

```mermaid
xychart-beta
    title "anamabo/Equal-Size-Spectral-Clustering 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 25 --> 27
    line [26, 26]
```

2026-10-18 26 → 2026-10-31 26（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `467c7d40388c` · [字段定义](../../DATASET.md)*
