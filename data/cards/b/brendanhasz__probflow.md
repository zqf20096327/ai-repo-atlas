# brendanhasz/probflow

⭐ 175 · Jupyter Notebook · MIT · 推送 2026-09-26 · [GitHub](https://github.com/brendanhasz/probflow) · [官网](http://probflow.readthedocs.io) · 个人维护

**构建贝叶斯概率模型的 Python 库，支持 TF/PyTorch/JAX 后端**

Python 概率建模库：提供参数与概率分布等底层构件和贝叶斯神经网络等高层模块，用随机变分推断拟合模型（一行 model.fit），支持预测、置信区间绘图、后验检查、预测区间覆盖率等不确定性评估，并内置线性回归、DenseRegression 等预置模型。可在 TensorFlow 2.0/TFP、PyTorch、JAX 三种后端上运行，也可与后端代码混用。面向需要构建和评估贝叶斯模型的开发者与科研用户。作者声明项目仍在开发中。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | `idea` | |

## 能力要点

- 以参数+分布为构件构建自定义贝叶斯模型，随机变分推断一行拟合
- 支持 TensorFlow 2.0/TFP、PyTorch、JAX 三种后端并可混用后端代码
- 提供预测区间覆盖率（coverage）等不确定性诊断指标
- 内置 LinearRegression、DenseRegression 等预置模型

## 适用场景

- 我要给回归/分类任务建贝叶斯模型并量化预测不确定性
- 我要检查模型后验分布与预测区间的覆盖率
- 我想在 TF/PyTorch/JAX 之间选择后端做概率建模

## 场景标签

 · 领域:机器学习/统计建模

## 证据(README 行号)

> L5: ProbFlow is a Python package for building probabilistic Bayesian models with TensorFlow 2.0 or PyTorch or JAX, perfo
> L62: >>> model.predict(x_test)

## 星数曲线

```mermaid
xychart-beta
    title "brendanhasz/probflow 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 174 --> 176
    line [175, 175]
```

2026-10-18 175 → 2026-10-28 175（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `a8ee98c22b24` · [字段定义](../../DATASET.md)*
