# yzhao062/SUOD

⭐ 395 · Python · BSD-2-Clause · 推送 2026-09-08 · [GitHub](https://github.com/yzhao062/SUOD) · [官网](https://www.andrew.cmu.edu/user/yuezhao2/papers/20-preprint-suod.pdf) · 个人维护

**大规模无监督异构异常检测加速框架（MLSys'21）**

面向高维大数据集上大量异构无监督异常检测器集成训练的可扩展性问题，SUOD 提供三方面加速：随机投影降维、复杂模型近似、负载均衡并行调度，同时控制检测性能损失。以 Python 库形式发布（依赖 PyOD，兼容其模型），使用 numba JIT 与 joblib 并行化，各模块可开关或替换，支持模型持久化。论文发表于 MLSys 2021，已被 PyOD 集成，README 自述用于学术研究与 IQVIA 医疗索赔分析等行业场景。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | BSD-2-Clause |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 三模块加速：随机投影降维、模型近似、均衡并行调度
- 与 PyOD 模型完全兼容，可组合 LOF/IForest/KNN 等检测器
- numba JIT 与 joblib 并行化，模块可开关或自定义替换
- joblib/pickle 模型保存与加载

## 适用场景

- 在高维大数据集上并行训练并组合大量异构异常检测器
- 通过 PyOD 调用 SUOD 做集成异常检测
- 需要对检测结果做标签/分数/概率输出的无监督异常检测任务

## 场景标签

 · 领域:机器学习/数据挖掘

## 证据(README 行号)

> L66: **SUOD** (**S**\calable **U**\nsupervised **O**\utlier **D**\etection) is an **acceleration framework for large-sca
> L113:  model.fit(X_train) # fit all models with X

## 星数曲线

```mermaid
xychart-beta
    title "yzhao062/SUOD 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-22"]
    y-axis "stars" 394 --> 396
    line [395, 395]
```

2026-10-18 395 → 2026-10-22 395（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `283728d16008` · [字段定义](../../DATASET.md)*
