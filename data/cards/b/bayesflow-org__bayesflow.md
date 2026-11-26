# bayesflow-org/bayesflow

⭐ 790 · Python · MIT · 推送 2026-11-25 · [GitHub](https://github.com/bayesflow-org/bayesflow) · [官网](https://bayesflow.org/) · 组织维护

**给科研人员做仿真推断的深度学习贝叶斯库**

基于深度学习的仿真推断（SBI）Python 库，围绕摊销贝叶斯工作流组织：先从任意仿真器生成数据，再定义神经后验/似然/比率/点估计器并训练，配套诊断工具验证结果。通过 Keras 3 支持 PyTorch、TensorFlow、JAX 三种后端，可与 PyMC 集成，支持层级模型、集成与组合估计器。安装需 Python 3.12/3.13，且必须另装一个后端方可运行。

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

- 摊销贝叶斯工作流的高层 API（BasicWorkflow）
- 经 Keras 3 支持 PyTorch/TensorFlow/JAX 多后端
- 内置扩散与一致性模型等生成模型与诊断套件
- 提供 19 个教程笔记本与 PyMC 集成路径

## 适用场景

- 用仿真器数据训练神经后验估计器做参数推断
- 对 SIR 等科学计算模型做摊销贝叶斯推断
- 结合 MCMC 或 PyMC 做神经似然/比率估计
- 科研实验设计中的自适应序贯实验

## 场景标签

`科研工具` · 领域:学习与行业

## 证据(README 行号)

> L9: BayesFlow is a Python library for simulation-based inference (SBI) with deep learning.
> L12: - A user-friendly API for amortized Bayesian workflows
> L14: - Multi-backend support via Keras 3: You can use PyTorch, TensorFlow, or JAX

## 星数曲线

```mermaid
xychart-beta
    title "bayesflow-org/bayesflow 星数(近 10 点)"
    x-axis ["2026-10-24", "2026-10-29", "2026-11-06", "2026-11-08", "2026-11-10", "2026-11-13", "2026-11-15", "2026-11-20", "2026-11-21", "2026-11-26"]
    y-axis "stars" 781 --> 791
    line [782, 783, 782, 784, 785, 786, 787, 788, 790, 790]
```

2026-10-24 782 → 2026-11-26 790（+8）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 high · 依据 README sha `bb24183b9115` · [字段定义](../../DATASET.md)*
