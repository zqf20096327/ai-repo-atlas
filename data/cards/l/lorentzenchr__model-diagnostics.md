# lorentzenchr/model-diagnostics

⭐ 45 · Python · MIT · 推送 2026-04-26 · [GitHub](https://github.com/lorentzenchr/model-diagnostics) · [官网](https://lorentzenchr.github.io/model-diagnostics/) · 个人维护

**Python 库：机器学习模型的校准诊断与性能评估**

面向开发者和科研人员的 Python 库，提供机器学习模型诊断工具：覆盖均值、中位数、分位数、期望分位的点预测校准评估（compute_bias、compute_marginal、识别函数），生成 reliability diagram、bias plot、marginal plot 等图形，并将评分分解为失准、区分度与不确定性三部分；内部实现保序分位数/期望分位回归以支持分位数与期望分位的 reliability diagram。绘图后端可在 matplotlib 与 plotly 间选择。MIT 许可，经 pip 安装。

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

- 支持均值/中位数/分位数/期望分位预测的校准评估
- 评分分解为 miscalibration、discrimination、uncertainty
- reliability diagram、bias plot、marginal plot 图形诊断
- matplotlib 与 plotly 双绘图后端

## 适用场景

- 检查回归或概率预测模型的校准情况
- 用图形工具定位模型的条件偏差
- 将预测得分分解以分析性能来源

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L10: **Tools for diagnostics and assessment of (machine learning) models**
> L15: - Assess model calibration with identification functions (generalized residuals), compute_bias and compute_marginal

## 星数曲线

```mermaid
xychart-beta
    title "lorentzenchr/model-diagnostics 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 44 --> 46
    line [45, 45]
```

2026-10-18 45 → 2026-10-29 45（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `c851acc7c14a` · [字段定义](../../DATASET.md)*
