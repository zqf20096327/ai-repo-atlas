# tensorflow/tcav

⭐ 653 · Jupyter Notebook · Apache-2.0 · 推送 2026-07-22 · [GitHub](https://github.com/tensorflow/tcav) · 组织维护

**神经网络可解释性方法库：用概念激活向量量化概念对预测的重要性**

TensorFlow 团队的 TCAV（Testing with Concept Activation Vectors）实现：一种模型可解释性方法，通过少量正/反例学习高层概念（如颜色、性别、种族）的概念激活向量，量化这些概念对某一预测类别的重要性，提供类别级全局解释而非单样本特征归因。无需修改或重训已有网络。以 pip 包形式提供，附 Jupyter notebook 教程与离散数据（KDD99）示例。

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

- 以高层概念而非像素级权重解释模型预测
- 提供类别级全局解释，覆盖整类而非单张图
- 无需修改或重训练已有网络
- 支持离散/非图像数据模型（附 KDD99 示例）

## 适用场景

- 检查分类模型是否依赖性别、种族等敏感概念
- 为非 ML 背景的相关方生成可理解的概念级解释
- 在图像与离散数据模型上做全局归因分析

## 场景标签

 · 领域:机器学习可解释性

## 证据(README 行号)

> L10: Testing with Concept Activation Vectors (TCAV) is a new interpretability method
> L16: (e.g, pixel). TCAV instead shows importance of high level concepts (e.g., color,

## 星数曲线

```mermaid
xychart-beta
    title "tensorflow/tcav 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 653 --> 655
    line [654, 654]
```

2026-10-18 654 → 2026-10-28 654（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `5bc351d53fd0` · [字段定义](../../DATASET.md)*
