# tensorflow/fairness-indicators

⭐ 357 · Python · Apache-2.0 · 推送 2026-07-10 · [GitHub](https://github.com/tensorflow/fairness-indicators) · 组织维护

**评估二分类/多分类模型公平性指标的 TensorFlow 工具包**

TensorFlow 生态下的模型公平性评测与可视化工具：面向二分类与多分类分类器计算常用公平性指标，支持按用户群体切片评估模型表现、数据集分布评估、置信区间与多阈值评估，并可下钻到具体切片探查根因。pip 包内捆绑 TFDV、TFMA 与 What-If Tool，可在 TFX Evaluator 组件、TensorBoard 中使用，或以 TFMA 独立运行；Model Agnostic TFMA 支持基于任意模型输出计算。README 提供版本兼容表并维护 nightly 包源。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 计算二分类/多分类分类器的常用公平性指标
- 按用户群体切片评估模型性能，含置信区间与多阈值评估
- pip 包捆绑 TFDV、TFMA、What-If Tool
- Model Agnostic TFMA 支持基于任意模型输出计算

## 适用场景

- 上线前评估分类模型在不同用户群体上的表现差异
- 按切片下钻定位公平性问题的根因
- 在 TFX 或 TensorBoard 流程中集成公平性评估

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L17: Fairness Indicators enables easy computation of commonly-identified fairness metrics for **binary** and **multiclas
> L24: * Evaluate model performance, sliced across defined groups of users

## 星数曲线

```mermaid
xychart-beta
    title "tensorflow/fairness-indicators 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 356 --> 358
    line [357, 357]
```

2026-10-18 357 → 2026-10-24 357（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `54aa48e5440f` · [字段定义](../../DATASET.md)*
