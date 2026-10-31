# reggiebernardo/cosmo_learn

⭐ 14 · Jupyter Notebook · MIT · 推送 2026-08-02 · [GitHub](https://github.com/reggiebernardo/cosmo_learn) · 个人维护

**宇宙学参数推断工具包：模拟观测数据并用统计与机器学习方法约束**

面向宇宙学研究者的 Python 包，通过统一的 CosmoLearn 类覆盖五类观测探针（宇宙计时器、Pantheon+超新星、DESI BAO、RSD、LISA 亮并合源）：基于平坦 wCDM 宇宙生成含真实噪声的模拟数据，训练 GP/BRR/ANN 等模型在红移空间重构可观测量（不预设宇宙学模型），并可用 MCMC、遗传算法+Fisher 矩阵做参数推断，附带可视化与多指标方法评分。要求 Python 3.10，提供 conda 与 pip 安装，配套 arXiv 论文。

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

- 五类观测探针的模拟数据生成（含真实观测噪声）
- GP/BRR/ANN/遗传算法重构宇宙学可观测量，不预设宇宙学模型
- MCMC 与 GA+Fisher 矩阵推断平坦 wCDM 参数
- 多指标定量评分模块对比各方法

## 适用场景

- 生成多探针模拟宇宙学数据集用于方法测试
- 比较不同机器学习与统计方法重构宇宙学观测量的表现
- 约束 H0、Om0、w0、s8 等宇宙学参数

## 场景标签

`科研工具` · 领域:学习与行业

## 证据(README 行号)

> L3: `cosmo-learn` is a Python package for learning cosmology using a combination of statistical inference and machine le
> L21: - **Train machine learning models** (Gaussian Processes, Bayesian Ridge Regression, Artificial Neural Networks) to 

## 星数曲线

```mermaid
xychart-beta
    title "reggiebernardo/cosmo_learn 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `72f9d5c9c53d` · [字段定义](../../DATASET.md)*
