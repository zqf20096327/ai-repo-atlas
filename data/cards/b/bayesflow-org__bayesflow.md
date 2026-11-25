# bayesflow-org/bayesflow

⭐ 790 · Python · MIT · 推送 2026-11-24 · [GitHub](https://github.com/bayesflow-org/bayesflow) · [官网](https://bayesflow.org/) · 组织维护

**面向科研人员的深度学习仿真推断（SBI）Python 库**

基于深度学习的仿真推断（SBI）Python 库：用户用任意模拟器生成数据，通过 Keras 3 生态定义神经后验/似然/比值/点估计器，训练摊销化贝叶斯推断模型并配套诊断套件；支持 PyTorch/TensorFlow/JAX 多后端，可与 PyMC 集成，需自行安装后端才能运行。提供 PyPI 与源码安装，附 19 个教程笔记本、书籍示例与视频资源，另有供 AI agent 使用的 Baygent Skills。

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

- 摊销化贝叶斯工作流的用户友好 API（神经后验/似然/比值估计器）
- 经 Keras 3 支持 PyTorch/TensorFlow/JAX 三后端
- 内置扩散到一致性模型等生成模型与诊断功能
- 提供 PyMC 集成与 19 个教程笔记本

## 适用场景

- 从模拟器数据摊销化估计后验分布
- 用神经似然接入 PyMC/MCMC 采样流程
- 分层贝叶斯模型与贝叶斯模型比较
- 用后验不确定性做模型预测控制或自适应实验设计

## 场景标签

`科研工具` `教程课程` · 领域:学习与行业

## 证据(README 行号)

> L9: BayesFlow is a Python library for simulation-based inference (SBI) with deep learning.
> L20: BayesFlow is a flexible framework for Bayesian inference with deep learning—from idea to results in just a few line
> L46: To use BayesFlow, you will also need to install one of the following machine learning backends.

## 星数曲线

```mermaid
xychart-beta
    title "bayesflow-org/bayesflow 星数(近 10 点)"
    x-axis ["2026-10-23", "2026-10-29", "2026-11-06", "2026-11-08", "2026-11-10", "2026-11-13", "2026-11-15", "2026-11-20", "2026-11-21", "2026-11-25"]
    y-axis "stars" 781 --> 791
    line [782, 783, 782, 784, 785, 786, 787, 788, 790, 790]
```

2026-10-23 782 → 2026-11-25 790（+8）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-25 · 置信度 high · 依据 README sha `c3125ecb76f5` · [字段定义](../../DATASET.md)*
