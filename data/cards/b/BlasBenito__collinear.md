# BlasBenito/collinear

⭐ 21 · R · NOASSERTION · 推送 2026-10-14 · [GitHub](https://github.com/BlasBenito/collinear) · [官网](https://blasbenito.github.io/collinear/) · 个人维护

**R 包：检测并过滤建模数据框中的多重共线性预测变量**

面向 R 用户的统计工具包，围绕主函数 collinear() 组织五个组件：目标编码（类别变量转数值以支持 VIF/相关分析）、按与响应变量单变量关联度的预测变量排序、统一相关框架（Pearson/目标编码/Cramer's V 处理混合变量类型）、自适应阈值与双策略过滤（成对相关+VIF）。提供 cor_df()、vif_df()、collinear_stats() 等诊断函数，输出选定的非共线预测变量、排序与建模公式，并可通过 step_collinear() 集成到 tidymodels。CRAN 可装，支持 future/progressr 并行（仅对含类别预测变量的大数据集有优势）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 混合变量类型的统一相关性计算（Pearson/目标编码/Cramer's V）
- 成对相关与 VIF 双重过滤，结合预测变量重要性排序
- 自适应阈值，可手动覆盖
- step_collinear() 集成 tidymodels recipes（不含目标编码）

## 适用场景

- 建模前自动筛选非冗余的预测变量集合
- 诊断数据框中预测变量的共线性程度
- 在 tidymodels 工作流中执行共线性过滤

## 场景标签

 · 领域:统计/数据预处理

## 证据(README 行号)

> L11: The R package `collinear` provides a comprehensive toolkit for smart
> L54:  Combines pairwise correlation and Variance Inflation Factor filtering
> L196: this case, it fits univariate models between the response and each

## 星数曲线

```mermaid
xychart-beta
    title "BlasBenito/collinear 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 20 --> 22
    line [21, 21]
```

2026-10-18 21 → 2026-10-28 21（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 mid · 依据 README sha `f8cb69c791dc` · [字段定义](../../DATASET.md)*
