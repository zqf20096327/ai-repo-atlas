# python-adaptive/adaptive

⭐ 1,231 · Python · BSD-3-Clause · 推送 2026-10-26 · [GitHub](https://github.com/python-adaptive/adaptive) · [官网](http://adaptive.readthedocs.io/) · 组织维护

**数学函数的自适应并行采样/主动学习 Python 库**

用户提供目标函数与参数范围，库在参数空间中选择信息量最大的点进行评估，而非稠密网格全采样。实现 Learner1D/2D/ND、AverageLearner、IntegratorLearner 等学习器，损失函数可替换或自定义；通过 concurrent.futures、mpi4py、loky、ipyparallel、distributed 在多核或多机上并行执行，支持 Jupyter 实时绘图与 DataFrame 导出。适用于单次评估约 ≥50ms、参数维度较低的函数；高维时 LearnerND 效率下降。面向科学与数值计算场景，需 Python 3.11+。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | BSD-3-Clause |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 7 种学习器与 2 种元学习器，覆盖 1D/2D/ND、随机变量与积分场景
- 多执行器并行：concurrent.futures/mpi4py/loky/ipyparallel/distributed
- 可选 Rust 三角剖分后端加速 LearnerND，无需改代码自动启用
- Jupyter 实时绘图与 to_dataframe() 数据导出

## 适用场景

- 对计算昂贵的仿真函数做自适应采样，替代均匀网格
- 在集群上并行评估函数并实时监控采样过程
- 对 1D 函数做自适应数值积分

## 场景标签

 · 领域:科学计算/机器学习工具库

## 证据(README 行号)

> L13: `adaptive` is an open-source Python library for adaptive parallel function evaluation.
> L14: You supply a function and its bounds, and `adaptive` evaluates it at the "best" points in parameter space, instead 
> L52: The core concept in `adaptive` is the *learner*.

## 星数曲线

```mermaid
xychart-beta
    title "python-adaptive/adaptive 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-25", "2026-10-30"]
    y-axis "stars" 1228 --> 1232
    line [1229, 1230, 1231]
```

2026-10-18 1,229 → 2026-10-30 1,231（+2）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 mid · 依据 README sha `31f6fd5c0a93` · [字段定义](../../DATASET.md)*
