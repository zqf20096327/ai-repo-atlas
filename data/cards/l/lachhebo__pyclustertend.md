# lachhebo/pyclustertend

⭐ 50 · Python · BSD-3-Clause · 推送 2026-10-17 · [GitHub](https://github.com/lachhebo/pyclustertend) · [官网](https://pyclustertend.readthedocs.io/en/master/index.html) · 个人维护

**评估数据集聚类倾向的 Python 统计库**

pyclustertend 是专注聚类倾向评估的 Python 包：判断对给定数据集做聚类是否有意义。实现 Hopkins 统计量、VAT、iVAT 三种聚类倾向方法，以及基于 KMeans 估计器指标的评估（Silhouette、Calinski-Harabasz、Davies-Bouldin）。以 Python 库形式经 PyPi 提供，示例基于 sklearn 的 iris 数据集演示各方法调用。README 注明使用 hopkins/vat 前建议先对数据缩放，且 vat/ivat 不适合海量数据库，可先采样。

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

- Hopkins 统计量评估聚类倾向
- VAT 与 iVAT 可视化方法
- 基于 KMeans 的 Silhouette/Calinski-Harabasz/Davies-Bouldin 指标评估
- 依赖 scikit-learn，接口以数据矩阵为输入

## 适用场景

- 在跑聚类算法前判断数据是否具有聚类结构
- 聚类分析流程中的前探性统计检验
- 对比不同数据集的聚类可适用性

## 场景标签

 · 领域:数据科学/统计

## 证据(README 行号)

> L6: pyclustertend is a Python package specialized in cluster tendency. Cluster tendency consist to assess if clustering 
> L8: Three methods for assessing cluster tendency are currently implemented and one additional method based on metrics ob

## 星数曲线

```mermaid
xychart-beta
    title "lachhebo/pyclustertend 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 49 --> 51
    line [50, 50]
```

2026-10-18 50 → 2026-10-24 50（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `894904839b67` · [字段定义](../../DATASET.md)*
