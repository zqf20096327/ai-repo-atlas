# RubixML/Iris

⭐ 35 · PHP · MIT · 推送 2026-10-08 · [GitHub](https://github.com/RubixML/Iris) · [官网](https://rubixml.github.io/ML) · 组织维护

**用 Iris 数据集与 KNN 分类器的 Rubix ML 入门教程项目**

面向 PHP 开发者的机器学习入门示例工程：基于鸢尾花（Iris）数据集演示 Rubix ML 库的完整流程——从 CSV 提取数据与类型转换、划分训练/测试集、实例化并训练 K 近邻分类器、用 predict() 做预测，到用 Accuracy 指标交叉验证评分。附带 explore.php 脚本用 t-SNE 将数据嵌入二维并输出 embeddings.csv（结果非确定性）。通过 composer create-project 安装，要求 PHP 8.3 及以上，命令行运行 train.php / explore.php。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 覆盖数据提取→训练→预测→Accuracy 交叉验证评分的完整示例
- KNN 超参数 k 的配置与更换距离核（Euclidean/Manhattan/Minkowski）的指引
- explore.php 用 t-SNE 做二维数据可视化探索

## 适用场景

- PHP 开发者跟随教程首次学习 Rubix ML 与机器学习基础
- 作为 Rubix ML 项目结构的学习模板（train.php/explore.php）
- 了解 KNN 分类与交叉验证指标的工作方式

## 场景标签

`教程课程` · 领域:学习与行业

## 证据(README 行号)

> L3: A lightweight introduction to machine learning in Rubix ML using the famous Iris dataset and the K Nearest Neighbors
> L111: Congratulations on completing the introduction to machine learning in PHP with Rubix ML using the Iris dataset. No

## 星数曲线

```mermaid
xychart-beta
    title "RubixML/Iris 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 34 --> 36
    line [35, 35]
```

2026-10-18 35 → 2026-10-31 35（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `085e7e763e8c` · [字段定义](../../DATASET.md)*
