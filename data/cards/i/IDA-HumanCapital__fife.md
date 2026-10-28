# IDA-HumanCapital/fife

⭐ 23 · Python · NOASSERTION · 推送 2026-03-27 · [GitHub](https://github.com/IDA-HumanCapital/fife) · 组织维护

**面向面板数据的离散时间生存分析与多变量时序预测库**

FIFE 是 Python 库，将离散时间生存分析（含竞争风险）与多变量时间序列预测统一在面板数据框架下：估计个体在未来各期仍被观测到的概率、未来特征取值以及退出情形。机制上支持梯度提升树（LightGBM）与神经网络（Keras）两类模型，通过 PanelDataProcessor 与 LGBSurvival/LGBState/LGBExit 等 Modeler 类组织建模流程，适用于非平衡面板数据。README 提供示例代码与真实数据示例 notebook（预测领导人失去权力的时间）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 统一生存分析与多变量时序预测，处理非平衡面板数据
- 支持 LightGBM 梯度提升树与 Keras 神经网络两类模型
- 可预测存续概率、未来状态值与退出情形（竞争风险）
- 提供带真实数据的引导式示例 notebook

## 适用场景

- 我有一个面板数据集，想预测各实体未来几年仍在数据中的概率
- 我想在预测时序特征值的同时考虑实体中途退出的可能
- 我想预测实体退出时属于哪种情形（竞争风险）

## 场景标签

`数据分析` · 领域:效率与自动化

## 证据(README 行号)

> L1: The Finite-Interval Forecasting Engine (FIFE) provides machine learning and other models for discrete-time survival 
> L31: FIFE unifies survival analysis (including competing risks) and multivariate time series analysis. Tools for the for

## 星数曲线

```mermaid
xychart-beta
    title "IDA-HumanCapital/fife 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 22 --> 24
    line [23, 23]
```

2026-10-18 23 → 2026-10-28 23（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `8bd062f85f1b` · [字段定义](../../DATASET.md)*
