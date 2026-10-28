# microsoft/CBM

⭐ 63 · Jupyter Notebook · MIT · 推送 2026-10-26 · [GitHub](https://github.com/microsoft/CBM) · 组织维护

**可解释的计数数据预测库：Cyclic Boosting 的 scikit-learn 兼容实现**

微软开源的 Cyclic Boosting 机器学习算法 Python 实现，专用于计数数据（如销量、需求）的可解释监督预测。预测方式为全局均值乘以各特征分箱的权重估计，权重可解读为相对全局均值的百分比增减。针对类别特征优化，连续特征用 pandas.qcut 离散化，支持日期自动展开（星期+月份）、特征重要性可视化及基于 RMSE/L1/SMAPE 的训练停止指标。通过 PyPI 以 pip install cyclicbm 安装，接口兼容 scikit-learn。

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

- 预测结果可解释：权重表示相对全局均值的百分比变化
- 针对类别特征优化，连续特征经 pandas.qcut 离散化
- 特征重要性图：类别、连续及交互作用
- 支持 RMSE/L1/SMAPE 指标控制训练停止

## 适用场景

- 预测销量、需求等计数型目标变量
- 需要向业务方解释各特征对预测影响的分析场景
- 在 scikit-learn 工作流中接入可解释回归模型

## 场景标签

 · 领域:机器学习/需求预测

## 证据(README 行号)

> L10: This is an efficient and Scikit-learn compatible implementation of the machine learning algorithm Cyclic Boosting -
> L22: The CBM model predicts by multiplying the global mean with each weight estimate for each bin and feature. Thus the 

## 星数曲线

```mermaid
xychart-beta
    title "microsoft/CBM 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 62 --> 64
    line [63, 63]
```

2026-10-18 63 → 2026-10-28 63（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `c9868766601f` · [字段定义](../../DATASET.md)*
