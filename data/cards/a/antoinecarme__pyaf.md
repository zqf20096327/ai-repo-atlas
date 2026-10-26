# antoinecarme/pyaf

⭐ 462 · Python · BSD-3-Clause · 推送 2026-10-04 · [GitHub](https://github.com/antoinecarme/pyaf) · 个人维护

**面向开发者的 Python 自动时间序列预测库**

基于 NumPy/SciPy/Pandas/scikit-learn 构建的开源 Python 库，以全自动方式训练模型预测时间序列未来值：将信号分解为趋势、周期与 AR 分量，通过多种信号变换与分解组合的竞争筛选最优模型，支持外生变量（ARX）、层级/分组预测（Bottom-Up、Top-Down、Middle-Out、最优组合）、预测区间与时间频率推断，模型经 scikit-learn 估计。提供简单 fit/predict API、Flask RESTful 服务与 Jupyter 演示。默认选项可快速建模，慢速模式探索全部模型。项目自 2016 年启动，自述功能仍在演进中。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | BSD-3-Clause |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 全自动信号分解：趋势+周期+AR 分量竞争式建模
- 外生数据支持（ARX 模型，任意类型变量）
- 层级与分组时间序列预测（4 种调和方法）
- 提供 Flask RESTful Web 服务与预测/置信区间

## 适用场景

- 我需要不手工调参就得到时间序列未来预测
- 我想利用相关外生变量改进预测（ARX）
- 我需要对层级/分组结构的销量等序列做一致预测

## 场景标签

`数据分析` · 领域:效率与自动化

## 证据(README 行号)

> L8: PyAF works as an automated process for predicting future values of a signal
> L36: PyAF statistical time series models are built/estimated/trained using scikit-learn.

## 星数曲线

```mermaid
xychart-beta
    title "antoinecarme/pyaf 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-26"]
    y-axis "stars" 460 --> 463
    line [461, 462, 462]
```

2026-10-18 461 → 2026-10-26 462（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `7cdfbf707a41` · [字段定义](../../DATASET.md)*
