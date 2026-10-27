# Core-Bioinformatics/ClustAssess

⭐ 34 · R · NOASSERTION · 推送 2026-09-27 · [GitHub](https://github.com/Core-Bioinformatics/ClustAssess) · [官网](https://core-bioinformatics.github.io/ClustAssess/) · 组织维护

**评估聚类稳健性的 R 包，面向单细胞 RNA-seq 分析**

R 语言包，提供单细胞聚类结果稳健性评估工具集：基于元素中心相似度（ECS，通过带重启随机游走/个性化 PageRank 度量）比较两个或多个聚类及其与真实划分的一致性；marker_overlap 比较不同聚类下的标志基因集；PAC 共识聚类（Rcpp 优化）判定最优簇数 k；并评估特征集、参数选择对聚类稳定性的影响。附带 Shiny 交互应用，可无 R 基础完成稳定性评估与下游分析（UMAP、marker 基因、富集分析）。大数据集建议几何素描降采样。可从 CRAN 或 GitHub 安装，另有 Python 实现 ClustAssessPy。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- ECS 元素级聚类相似度（支持 flat、重叠与层级聚类）
- PAC 共识聚类评估簇数 k 的稳定性（Rcpp 实现，含收敛诊断）
- 参数/特征集稳定性评估（跨随机种子计算 ECC）
- 内置 Shiny 应用：交互式稳定性评估与下游分析（UMAP/marker/富集）

## 适用场景

- 单细胞聚类结果稳健性检验与不同方法结果比较
- 选择稳定的最优簇数 k 与特征集
- 评估聚类参数选择对最终结果的影响
- 无需 R 基础的交互式下游分析（marker、富集）

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L10: This repo contains the ClustAssess R package, which provides a set of tools
> L58: The most common clustering pipeline for single-cell data consists of
> L62: ClustAssess provides several methods to assess the stability of parameter

## 星数曲线

```mermaid
xychart-beta
    title "Core-Bioinformatics/ClustAssess 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 33 --> 35
    line [34, 34]
```

2026-10-18 34 → 2026-10-27 34（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `28b83aa993fc` · [字段定义](../../DATASET.md)*
