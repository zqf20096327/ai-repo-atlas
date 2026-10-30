# enriquegit/multiviewstacking

⭐ 30 · Python · MIT · 推送 2026-07-02 · [GitHub](https://github.com/enriquegit/multiviewstacking) · [官网](https://pypi.org/project/multiviewstacking/) · 个人维护

**多视图堆叠分类器的 Python 实现：多视角数据训练分类模型**

基于 Stacked Generalization 方法的 Python 包：对每个表示视图独立训练任意数量的 first-level-learner（可用任意 scikit-learn 分类器或实现 fit/predict/predict_proba 的自定义模型），再以这些模型的类别与分数预测作为特征训练 meta-learner。支持组合不同类型的一级学习器，视图数量上限为内存限制。内置一个含音频与加速度计两视图的活动识别测试数据集，并提供适合多视图学习的公开数据集列表。面向使用 Python 做多视图学习的研究者与开发者。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 每个视图独立训练 first-level-learner，元学习器融合预测
- 任意 scikit-learn 分类器或实现 fit/predict/predict_proba 的自定义模型可用
- 支持任意数量视图与不同类型一级学习器组合
- 内置两视图活动识别示例数据集

## 适用场景

- 对图像/音频/文本等多表示视图数据训练分类模型
- 避免拼接各视图特征，按视图分别建模再融合
- 活动识别等多传感器数据的分类实验

## 场景标签

 · 领域:机器学习/分类算法

## 证据(README 行号)

> L5: In machine learning, Multi-View learning algorithms aim to learn from different representational views. For example,
> L9: * Train Multi-View Stacking classifiers.

## 星数曲线

```mermaid
xychart-beta
    title "enriquegit/multiviewstacking 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 29 --> 31
    line [30, 30]
```

2026-10-18 30 → 2026-10-30 30（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `bcfd37492013` · [字段定义](../../DATASET.md)*
