# rick12000/confopt

⭐ 106 · Python · MIT · 推送 2025-11-24 · [GitHub](https://github.com/rick12000/confopt) · [官网](https://confopt.readthedocs.io) · 个人维护

**基于保形预测的超参数优化（HPO）Python 库**

面向机器学习从业者的超参数调优库：通过保形不确定性量化与多种代理模型执行贝叶斯优化式搜索。用户以目标函数、IntRange/FloatRange/CategoricalRange 定义的搜索空间初始化 ConformalTuner，调用 tune 运行搜索并取回最优参数与分数。依赖精简，也适用于 HPO 研究方法实验。限制：自身不支持并行化、multi-fidelity 与多目标优化，这两项通过 Optuna 集成提供（multi-fidelity 部分为实验性）。实现了三篇保形 HPO 论文中的代理模型与采集函数。

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

- ConformalTuner API：定义搜索空间后单次调用 tune 执行保形超参数搜索
- 实现三篇论文（arXiv 2022/2023 PMLR/2025）的代理模型与采集函数
- 提供 Optuna 集成以补足并行化与 multi-fidelity 优化
- 依赖精简，支持 HPO 研究作为附加方法使用

## 适用场景

- 调优 RandomForest 等模型的超参数
- 作为 HPO 研究中的纯搜索方法基线或扩展
- 在需要并行或 multi-fidelity 时经 Optuna 集成使用

## 场景标签

 · 领域:机器学习/超参数优化

## 证据(README 行号)

> L9: Built for machine learning practitioners requiring flexible and robust hyperparameter tuning, **ConfOpt** delivers s
> L36: from confopt.tuning import ConformalTuner

## 星数曲线

```mermaid
xychart-beta
    title "rick12000/confopt 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 105 --> 107
    line [106, 106]
```

2026-10-18 106 → 2026-10-24 106（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `88806828a60b` · [字段定义](../../DATASET.md)*
