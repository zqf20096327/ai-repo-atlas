# EtzionR/Clustering-by-Silhouette

⭐ 18 · Python · MIT · 推送 2026-05-31 · [GitHub](https://github.com/EtzionR/Clustering-by-Silhouette) · 个人维护

**自动用轮廓系数选取最优聚类参数的 Python 脚本**

提供 scluster.py：对给定 pandas dataframe，在指定参数范围内遍历运行 KMeans、MeanShift、HDBSCAN 三种聚类算法，以轮廓系数（含针对 label=-1 噪声点的调整 silhouette ∙ (M/N)）比较结果，仅返回轮廓系数最高的聚类标签。内置应对 silhouette MemoryError 的机制：出错时将 sample_size 按 5% 递减直至可计算。支持 stp 步长参数与多维数据，依赖 sklearn、hdbscan、pandas。以 MIT 许可发布，含示例实现与 3D 可视化输出文档。

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

- 按轮廓系数自动搜索 KMeans/MeanShift/HDBSCAN 的最优参数
- 针对噪声点（label=-1）的调整轮廓系数 silhouette ∙ (M/N)
- MemoryError 时 sample_size 自动按 5% 递减直至可运行
- 支持多维数据与 stp 步长参数

## 适用场景

- 不知道选多少聚类数时自动确定最优 K
- 对比多种聚类算法在数据上的最优划分结果
- 高维数据集上自动做聚类参数调优

## 场景标签

 · 领域:机器学习/聚类分析

## 证据(README 行号)

> L2: Create the optimal clustering by the measure of Silhouette Score automatically.
> L38: The **scluster.py** code based on this logic demonstrated in the case we have saw. The code uses three different ty

## 星数曲线

```mermaid
xychart-beta
    title "EtzionR/Clustering-by-Silhouette 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 17 --> 19
    line [18, 18]
```

2026-10-18 18 → 2026-10-29 18（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `0c1806f1a641` · [字段定义](../../DATASET.md)*
