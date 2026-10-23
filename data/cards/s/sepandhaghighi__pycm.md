# sepandhaghighi/pycm

⭐ 1,509 · Python · MIT · 推送 2026-10-05 · [GitHub](https://github.com/sepandhaghighi/pycm) · [官网](http://pycm.io) · 个人维护

**多分类混淆矩阵 Python 库：分类模型评估指标计算**

面向数据科学家的分类模型评估库：接收实际/预测向量或直接输入矩阵，生成多分类混淆矩阵及各类与整体统计参数。支持样本权重、矩阵转置、重命名、合并（适用于 mini-batch 学习）、ROC/PR/Precision/Recall/F1 曲线（One-vs-Rest 扩展到多分类）、最优阈值计算，并根据数据集平衡性推荐评估参数。通过 pip、源码或 conda 安装，可结合 MATLAB 调用。

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

- 同时支持输入向量与直接矩阵两种构建方式
- ROC/PR/Precision/Recall/F1 曲线以 One-vs-Rest 扩展到多分类
- combine 方法合并混淆矩阵，适用于 mini-batch 学习
- 根据数据集平衡/多分类特征推荐评估参数

## 适用场景

- 分类器训练后计算混淆矩阵与大量统计指标
- 比较多分类器的性能并选最优阈值
- mini-batch 场景下增量合并混淆矩阵

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L13: PyCM is a multi-class confusion matrix library written in Python that supports both input data vectors and direct m
> L14: PyCM is the swiss-army knife of confusion matrices, targeted mainly at data scientists that need a broad array of m

## 星数曲线

```mermaid
xychart-beta
    title "sepandhaghighi/pycm 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-23"]
    y-axis "stars" 1508 --> 1510
    line [1509, 1509]
```

2026-10-18 1,509 → 2026-10-23 1,509（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `15f4d49caf10` · [字段定义](../../DATASET.md)*
