# caranathunge/promor

⭐ 16 · R · LGPL-2.1 · 推送 2026-05-07 · [GitHub](https://github.com/caranathunge/promor) · [官网](https://caranathunge.github.io/promor/) · 个人维护

**蛋白质组学数据分析与机器学习建模的 R 语言包**

面向蛋白质组学研究者（label-free 定量）的 R 包：读取 MaxQuant 的 proteinGroups.txt 或标准制表符矩阵加实验设计文件，执行蛋白质水平的质量控制、归一化、差异表达分析，并用差异蛋白构建机器学习预测模型，输出火山图与 ROC 图等可视化。附带 R Shiny 网页版应用与分情境教程（有无技术重复、建模）。限制：输入需符合规定格式，模型构建依赖差异表达结果。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | LGPL-2.1 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- label-free 定量蛋白质组学差异表达分析流程
- 基于差异蛋白候选构建机器学习预测模型
- 读取 MaxQuant proteinGroups.txt 或标准矩阵输入
- 提供质量控制与可视化工具（火山图、ROC 图）及 R Shiny 网页版

## 适用场景

- 两组条件间筛选差异表达蛋白并绘制火山图
- 用差异蛋白数据训练模型预测疾病严重程度等结局
- 无编程基础者通过 Shiny App 使用分析流程

## 场景标签

 · 领域:生物信息学/蛋白质组学

## 证据(README 行号)

> L19: - `promor` streamlines differential expression analysis of **label-free
> L103: from differential expression analysis to build machine learning-based

## 星数曲线

```mermaid
xychart-beta
    title "caranathunge/promor 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-31 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `34de1a3432f4` · [字段定义](../../DATASET.md)*
