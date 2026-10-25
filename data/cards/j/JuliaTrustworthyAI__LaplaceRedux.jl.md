# JuliaTrustworthyAI/LaplaceRedux.jl

⭐ 49 · Julia · MIT · 推送 2026-02-05 · [GitHub](https://github.com/JuliaTrustworthyAI/LaplaceRedux.jl) · [官网](https://www.taija.org/LaplaceRedux.jl/) · 组织维护

**Julia 库：对 Flux.jl 神经网络做拉普拉斯近似贝叶斯深度学习**

纯 Julia 编写的贝叶斯深度学习库，通过对训练后的 Flux.jl 神经网络做拉普拉斯近似（LA），为回归和分类模型提供预测不确定性估计（如 95% 置信区间、后验预测分布）。用法为对预训练模型调用 Laplace 构造器并 fit!、optimize_prior!。开发灵感来自 Python 库 laplace-redux 及其论文（Daxberger et al. 2021）。面向 Julia 深度学习开发者，通过 Pkg 安装，提供稳定版与开发版两种途径。

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

- 对 Flux.jl 训练的神经网络做拉普拉斯近似
- 支持回归与（二）分类任务的预测不确定性估计
- 提供 optimize_prior! 等先验调优接口与可视化绘图

## 适用场景

- 为已训练的 Flux.jl 模型添加不确定性量化
- 回归任务中可视化预测置信区间
- 对比 Plugin 近似与拉普拉斯近似的后验预测分布

## 场景标签

 · 领域:机器学习/不确定性量化

## 证据(README 行号)

> L5: `LaplaceRedux.jl` is a library written in pure Julia that can be used for effortless Bayesian Deep Learning through 
> L29: `LaplaceRedux.jl` can be used for any neural network trained in `Flux.jl`. Below we show basic usage examples invol

## 星数曲线

```mermaid
xychart-beta
    title "JuliaTrustworthyAI/LaplaceRedux.jl 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 48 --> 50
    line [49, 49]
```

2026-10-18 49 → 2026-10-25 49（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `9f884f0fcdd0` · [字段定义](../../DATASET.md)*
