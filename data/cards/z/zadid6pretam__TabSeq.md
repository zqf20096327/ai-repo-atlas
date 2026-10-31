# zadid6pretam/TabSeq

⭐ 13 · Python · MIT · 推送 2026-08-21 · [GitHub](https://github.com/zadid6pretam/TabSeq) · [官网](https://link.springer.com/chapter/10.1007/978-3-031-78128-5_27) · 个人维护

**面向表格数据的深度学习框架：通过特征排序建模异构特征**

TabSeq 是一个用 Python 实现的表格数据深度学习框架，核心机制是通过特征排序（feature ordering）组织异构特征：利用聚类将相似特征分组，用 Multi-Head Attention 捕捉特征交互，并以 Denoising Autoencoder 降噪与重构输入。提供 binary.py 与 multiclass.py 分别覆盖二分类与多分类任务，依赖 numpy/pandas/scikit-learn/tensorflow/networkx，支持 pip 安装或源码安装。研究发表于 ICPR 2024（Springer, pp. 418–434），README 同时列举了作者团队的多项相关工作（GOTabPFN、iSyncTab 等）。

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

- 特征排序框架：聚类分组特征以最大化相关性与交互
- Multi-Head Attention 优先处理关键特征交互
- Denoising Autoencoder 降低冗余并重构噪声输入
- 提供二分类与多分类两种实现

## 适用场景

- 对表格数据做二分类或多分类预测
- 处理具有异构与序列特征的健康信息学、金融建模数据
- 作为研究复现：配合 ICPR 2024 论文使用

## 场景标签

 · 领域:机器学习/表格数据建模

## 证据(README 行号)

> L12: TabSeq is a cutting-edge framework designed to bridge the gap in applying deep learning to tabular datasets, which 
> L16: - Clustering to group features with similar characteristics in feature ordering.
> L26: - **binary.py**: Implementation for binary classification tasks.

## 星数曲线

```mermaid
xychart-beta
    title "zadid6pretam/TabSeq 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 12 --> 14
    line [13, 13]
```

2026-10-18 13 → 2026-10-31 13（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `c003e613a901` · [字段定义](../../DATASET.md)*
