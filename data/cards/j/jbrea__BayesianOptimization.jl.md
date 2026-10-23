# jbrea/BayesianOptimization.jl

⭐ 105 · Julia · NOASSERTION · 推送 2025-10-27 · [GitHub](https://github.com/jbrea/BayesianOptimization.jl) · 个人维护

**Julia 贝叶斯优化库：用高斯过程优化昂贵黑箱函数**

Julia 语言的贝叶斯优化软件包，基于 GaussianProcesses.jl 对带噪声的目标函数执行全局优化，支持 Min/Max 两种优化方向。提供 ExpectedImprovement、ProbabilityOfImprovement、UpperConfidenceBound、ThompsonSamplingSimple、MutualInformation 等采集函数，GP 超参数优化器（MAPGPOptimizer/NoModelOptimizer），以及 Sobol/LHS 序列初始化。支持通过多次调用 boptimize! 恢复/续跑优化，可用已知函数值跳过初始化做热启动。面向需要在 Julia 中调参或优化昂贵函数的用户。

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

- 多种采集函数（EI/PI/UCB/Thompson 采样/互信息）
- 支持断点续跑与已知函数值热启动
- Sobol/LHS 序列初始化与 GP 超参数 MAP 优化

## 适用场景

- 在 Julia 中优化计算昂贵的黑箱目标函数
- 机器学习超参数调优
- 利用已有评估结果热启动优化过程

## 场景标签

 · 领域:机器学习/优化

## 证据(README 行号)

> L11: using BayesianOptimization, GaussianProcesses, Distributions
> L43: * acquisition types: `ExpectedImprovement`, `ProbabilityOfImprovement`, `UpperConfidenceBound`, `ThompsonSamplingSi

## 星数曲线

```mermaid
xychart-beta
    title "jbrea/BayesianOptimization.jl 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-23"]
    y-axis "stars" 104 --> 106
    line [105, 105]
```

2026-10-18 105 → 2026-10-23 105（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `b46cd5581b8d` · [字段定义](../../DATASET.md)*
