# abhinavralhan/kohonen-maps

⭐ 72 · Jupyter Notebook · MIT · 推送 2026-03-04 · [GitHub](https://github.com/abhinavralhan/kohonen-maps) · 个人维护

**SOM/GSOM/Neural Gas 聚类算法的 Python 实现与 notebook 集合**

以 Python 包 kohonen 和 Jupyter notebook 形式提供三种无监督聚类与降维算法：固定网格的 SOM、动态扩网格的 GSOM、自由放置神经元的 Neural Gas。包含 iris 基础示例与客户分群实际案例 notebook，支持 U-Matrix、Hit Map、Component Planes 可视化，并给出与 PCA/t-SNE/UMAP/K-Means 的特性对照表。通过 git clone 源码加 pip 安装依赖运行，直接调用包可在 sklearn 数据集上训练。算法原理、参数与选型指南在 README 中说明。

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

- SOM、GSOM、Neural Gas 三种算法的可复用 Python 包
- 含客户分群实际案例 notebook
- U-Matrix / Hit Map / Component Planes 三种可视化
- README 提供算法对照与选型指引

## 适用场景

- 对高维数据做聚类与 2D 拓扑可视化
- 按购买行为做客户分群
- 数据随时间增长时用 GSOM 做动态聚类

## 场景标签

 · 领域:机器学习/聚类算法

## 证据(README 行号)

> L3: Implementation of Self-Organizing Maps (SOM), Growing SOM (GSOM), and Neural Gas for unsupervised clustering and dim
> L38: from kohonen.som import SOM

## 星数曲线

```mermaid
xychart-beta
    title "abhinavralhan/kohonen-maps 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 71 --> 73
    line [72, 72]
```

2026-10-18 72 → 2026-10-29 72（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 mid · 依据 README sha `3af76569b0dc` · [字段定义](../../DATASET.md)*
