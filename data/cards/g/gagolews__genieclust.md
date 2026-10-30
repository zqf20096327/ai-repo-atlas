# gagolews/genieclust

⭐ 75 · C++ · NOASSERTION · 推送 2026-06-18 · [GitHub](https://github.com/gagolews/genieclust) · [官网](https://genieclust.gagolewski.com/) · 个人维护

**R/Python 双语言的鲁棒层次聚类算法库**

实现 Genie 层次聚类算法的 R 与 Python 包：基于欧几里得最小生成树，通过在合并时平衡簇大小来避免极端不平衡的划分，可在分钟级完成百万级数据点的完整聚类层级；支持互可达距离聚类（可作为 HDBSCAN 的替代且无需设置 eps 参数），配合 Deadwood 可作离群点检测。另附不平等度量（Gini 等）、外部与内部聚类有效性指标。核心为 header-only C++ 实现，Python 版提供 scikit-learn 风格 API，R 版兼容 stats::hclust()。

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

- 基于最小生成树的 Genie 层次聚类，处理百万级数据点
- 互可达距离聚类可作为 HDBSCAN 替代，无需设置 eps 参数
- 附 Gini/Bonferroni 不平等度量与多种内外部聚类有效性指标
- 核心为 header-only C++ 库，R 接口兼容 stats::hclust()

## 适用场景

- 对大规模、含离群点的数据做稳健的层次聚类
- 在 Python/R 中需要确定簇数的聚类分析
- 评估与比较不同聚类结果的有效性

## 场景标签

 · 领域:机器学习/数据科学

## 证据(README 行号)

> L16: *Genie* is a robust hierarchical clustering algorithm
> L95: The Python language version of **genieclust** has a **scikit-learn**-like API:

## 星数曲线

```mermaid
xychart-beta
    title "gagolews/genieclust 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 74 --> 76
    line [75, 75]
```

2026-10-18 75 → 2026-10-30 75（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `235b8f3a5df9` · [字段定义](../../DATASET.md)*
