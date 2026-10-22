# namkoong-lab/dro

⭐ 163 · Jupyter Notebook · MIT · 推送 2026-09-20 · [GitHub](https://github.com/namkoong-lab/dro) · [官网](https://python-dro.org/) · 组织维护

**分布鲁棒优化（DRO）机器学习方法的 Python 库，供研究者与开发者使用**

dro 是实现分布鲁棒优化（DRO）方法的 Python 包，面向监督学习任务（SVM、逻辑回归、线性回归及神经网络、树模型）。线性 DRO 模型基于 cvxpy 精确求解，默认调用 MOSEK（需许可证，也可切换 ECOS/SCS 等开源求解器）；神经网络 DRO 用 PyTorch 梯度下降求解，树模型基于 xgboost/lightgbm 函数逼近。内置多种散度/度量（chi-square、KL、CVaR、Wasserstein、MMD、Sinkhorn 等）、研究论文中的合成数据生成器及最坏分布、样本外性能评估等诊断接口。通过 pip 安装。

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

- 线性 DRO（chi2/KL/CVaR/TV/Wasserstein/MMD/Sinkhorn 等）经 cvxpy 精确求解
- 神经网络 DRO（PyTorch 梯度下降）与树模型 DRO（xgboost/lightgbm）
- 内置多篇论文的合成数据生成机制
- 提供最坏分布与样本外性能评估的诊断接口

## 适用场景

- 用 DRO 训练对分布偏移更稳健的监督学习模型
- 复现 DRO 研究论文中的实验设置与合成数据
- 评估模型的最坏情况与真实样本外性能

## 场景标签

`科研工具` · 领域:学习与行业

## 证据(README 行号)

> L10: `dro` is a python package that implements typical DRO methods on linear loss (SVM, logistic regression, and linear 
> L110: The models listed below are solved by exact solvers from ``cvxpy``.
> L176: The models listed below are solved by gradient descent (``Pytorch``).

## 星数曲线

```mermaid
xychart-beta
    title "namkoong-lab/dro 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-22"]
    y-axis "stars" 162 --> 164
    line [163, 163]
```

2026-10-18 163 → 2026-10-22 163（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `89d555c66d35` · [字段定义](../../DATASET.md)*
