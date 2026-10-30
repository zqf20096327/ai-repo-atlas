# Karim-53/pdll

⭐ 23 · Python · Apache-2.0 · 推送 2026-10-25 · [GitHub](https://github.com/Karim-53/pdll) · 个人维护

**scikit-learn 兼容的元估计器：把多分类转为点对同异二分类**

Pairwise Difference Learning（pdll）是 scikit-learn 兼容的元估计器，包裹任意分类器或回归器，将多分类问题改写为『两点是否同类』的二分类：基模型从全部训练点对中学习，预测时将新点与已知标签的锚点比较后按后验聚合，n 行数据产生 n² 训练样本。保留 fit/predict/predict_proba API，可直接用于 Pipeline、GridSearchCV。面向小规模表格数据（约 2000 行以内）与树模型基学习器，实现了 Discovery Science 2024 论文（Belaid 等）。默认设置下典型数据集需约 1GB 内存，131 个真实数据集峰值内存不超过 2.6GB。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 把多分类转为点对同/异二分类，n 行产生 n² 训练对
- 兼容 scikit-learn API，可在 Pipeline/GridSearchCV/cross_val_score 中直接替换
- 直接接收 pandas/polars/pyarrow 原始 DataFrame，自动编码字符串/类别/缺失值
- 在 131 个真实数据集上默认设置无崩溃，峰值内存不超过 2.6GB

## 适用场景

- 小样本表格数据（约 2000 行以内）上提升树模型分类效果
- 在不改动 sklearn 工作流的前提下尝试 PDL 方法
- 复现 Discovery Science 2024 论文的 OpenML 基准实验

## 场景标签

 · 领域:机器学习/表格数据分类

## 证据(README 行号)

> L13: **Pairwise Difference Learning (PDL)** turns a multiclass problem into a binary one. Instead of asking *"what class
> L15: `pdll` wraps any scikit-learn classifier (or regressor) and keeps the usual `fit` / `predict` / `predict_proba` / `

## 星数曲线

```mermaid
xychart-beta
    title "Karim-53/pdll 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 22 --> 24
    line [23, 23]
```

2026-10-18 23 → 2026-10-30 23（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `732a74036c20` · [字段定义](../../DATASET.md)*
