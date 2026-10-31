# raamana/neuropredict

⭐ 105 · Python · Apache-2.0 · 推送 2026-01-19 · [GitHub](https://github.com/raamana/neuropredict) · [官网](https://raamana.github.io/neuropredict/) · 个人维护

**神经影像生物标记的机器学习预测分析工具，产出分类/回归评估报告**

面向神经影像与生物标记研究者（含结构 MRI、功能连接等特征）的预测建模工具：在嵌套交叉验证框架下运行机器学习工作流，支持分类与（v0.6 起）连续目标回归，可在嵌套 CV 内回归掉协变量/混杂因素，支持缺失值插补（遵循 CV 划分避免数据泄漏），内置多种分类器（含 XGBoost、决策树），并通过 CVResults 类管理与输出结果，目标是标准化、可复现的预测能力评估。以 Python 包形式提供，配套文档站点。

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

- 嵌套交叉验证下的分类与回归（连续目标）预测
- 在嵌套 CV 内回归掉协变量/混杂因素，遵循最佳实践
- 缺失值插补遵循 CV 划分、避免数据泄漏
- CVResults 类管理与输出分类/回归工作流结果

## 适用场景

- 我想评估神经影像特征对疾病分类的预测能力
- 需要在 CV 框架内控制年龄等协变量后做回归预测
- 希望获得标准化、可复现的生物标记预测分析报告

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L11: - As of ``v0.6``, **neuropredict now supports regression applications**
> L13:  classes), as well as allow you to **regress out covariates /
> L60: - Major feature: Ability to predict continuous variables (regression)

## 星数曲线

```mermaid
xychart-beta
    title "raamana/neuropredict 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 104 --> 106
    line [105, 105]
```

2026-10-18 105 → 2026-10-31 105（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `979d525f49e1` · [字段定义](../../DATASET.md)*
