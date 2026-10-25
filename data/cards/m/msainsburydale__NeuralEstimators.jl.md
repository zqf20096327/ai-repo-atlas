# msainsburydale/NeuralEstimators.jl

⭐ 60 · Julia · MIT · 推送 2026-10-21 · [GitHub](https://github.com/msainsburydale/NeuralEstimators.jl) · 个人维护

**面向似然不可解场景的 Julia 神经网络仿真推断包**

Julia 语言包，提供基于神经网络的仿真式（似然无关）参数推断：神经后验估计（NPE）直接学习后验分布、神经比率估计（NRE）近似似然比以支持频率派或贝叶斯推断、神经贝叶斯估计（NBE）估计后验的点概括量。方法为摊销式：在模拟数据上训练后可对任意多组观测数据快速推断。神经网络后端支持 Flux.jl 或 Lux.jl。面向统计建模与科研用户，通过 Julia Pkg 安装，另有 CRAN 上的 R 接口。开发于学术研究背景下，README 附 BibTeX 引用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 支持 NPE/NRE/NBE 三类仿真式推断方法
- 摊销式训练，训练后可对多组观测数据快速推断
- 神经网络后端可选 Flux.jl 或 Lux.jl
- 提供 CRAN 上的 R 接口

## 适用场景

- 似然不可解或 MCMC 代价高的模型做参数估计
- 对大量观测数据集重复快速推断
- R 用户通过 CRAN 接口使用仿真式推断

## 场景标签

 · 领域:统计推断/科学计算

## 证据(README 行号)

> L7: `NeuralEstimators` is a Julia package for **fast simulation-based inference** using neural networks. It is designed 
> L9: - Neural posterior estimation (NPE): directly learn the posterior distribution
> L10: - Neural ratio estimation (NRE): approximate likelihood ratios for flexible frequentist or Bayesian inference

## 星数曲线

```mermaid
xychart-beta
    title "msainsburydale/NeuralEstimators.jl 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 59 --> 61
    line [60, 60]
```

2026-10-18 60 → 2026-10-25 60（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `0948e09eb88c` · [字段定义](../../DATASET.md)*
