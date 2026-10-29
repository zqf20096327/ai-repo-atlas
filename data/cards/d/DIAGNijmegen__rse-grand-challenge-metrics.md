# DIAGNijmegen/rse-grand-challenge-metrics

⭐ 23 · Python · MIT · 推送 2026-10-01 · [GitHub](https://github.com/DIAGNijmegen/rse-grand-challenge-metrics) · [官网](https://grand-challenge.org) · 组织维护

**医学影像机器学习评估指标计算库**

由 DIAG Nijmegen（拉德堡德大学医学中心）维护的 Python 库，提供医学影像场景下机器学习模型评估所需指标的计算：边界框 Jaccard 指数、自助法 ROC 曲线、检测任务评分，以及混淆矩阵、Dice 分数、Hausdorff 距离、绝对/相对体积差异等。与 grand-challenge.org 平台的评估扩展场景配套，支持 SimpleITK 图像读取。要求 Python 3.10 以上，经 pip 安装，MIT 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 边界框标注与 Jaccard 指数计算
- 自助法（bootstrapped）ROC 曲线计算与检测任务评分
- 混淆矩阵、Dice、Hausdorff 距离、体积差异等指标的高效计算

## 适用场景

- 为医学影像分割/检测任务计算评估指标
- 构建 grand-challenge.org 的评估扩展
- 在论文或竞赛中计算 Dice 与 Hausdorff 等指标

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L9: Grand Challenge Metrics contains useful functions for evaluating machine learning models in the context of medical i
> L16:  - Bounding box annotations with Jaccard Index calculations

## 星数曲线

```mermaid
xychart-beta
    title "DIAGNijmegen/rse-grand-challenge-metrics 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 22 --> 24
    line [23, 23]
```

2026-10-18 23 → 2026-10-29 23（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `beb0f0ee6245` · [字段定义](../../DATASET.md)*
