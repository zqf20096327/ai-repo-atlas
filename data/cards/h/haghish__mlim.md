# haghish/mlim

⭐ 34 · R · NOASSERTION · 推送 2026-10-24 · [GitHub](https://github.com/haghish/mlim) · 个人维护

**面向 R/Stata 的自动机器学习缺失数据插补包**

R 包（另有 Stata 版本），对含 NA 的数据框执行单次或多次插补：先以均值/众数等填充初始化，再为每个变量自动微调机器学习模型（ELNET 默认，可选 RF/GBM/XGBoost/DL/Stacked Ensemble）。支持连续、二分类、多分类与有序变量，自动处理类别不平衡与变量交互，通过 10 折交叉验证报告插补误差，可用 mlim.mids() 转为 mice 兼容的 mids 对象。自称处于 Beta 阶段，GBM 微调对内存需求高。面向社会科学研究者与数据分析人员。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 逐变量自动微调模型参数，无需手工指定
- 支持 ELNET/RF/GBM/XGBoost/DL/Stacked Ensemble 多算法
- 单次与多次插补，并提供交叉验证插补误差估计（mlim.error()）
- 多次插补结果可转为 mice 兼容的 mids 对象

## 适用场景

- 社会调查数据中填补缺失值并控制类别不平衡带来的偏差
- 用多次插补生成 m 个数据集做后续统计分析
- 在大数据集上选择 ELNET 做快速插补

## 场景标签

 · 领域:统计/数据预处理

## 证据(README 行号)

> L1: **`mlim`** : Single and Multiple Imputation for `R` and `Stata` with Automated Machine Learning
> L6: **`mlim`** is the first missing data imputation software to implement automated machine learning for performing _mul

## 星数曲线

```mermaid
xychart-beta
    title "haghish/mlim 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 33 --> 35
    line [34, 34]
```

2026-10-18 34 → 2026-10-31 34（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `83b82883942b` · [字段定义](../../DATASET.md)*
