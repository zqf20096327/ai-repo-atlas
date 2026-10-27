# ARM-software/mango

⭐ 418 · Jupyter Notebook · Apache-2.0 · 推送 2026-03-11 · [GitHub](https://github.com/ARM-software/mango) · 组织维护

**面向机器学习分类器的并行超参数调优 Python 库**

Mango 是 ARM 软件团队维护的 Python 超参数优化库：定义兼容 scikit-learn 的连续/离散/类别搜索空间，用基于高斯过程的梯度无关优化器寻找最优超参数，并支持将目标函数调度到本地、集群或云端并行执行（内置 serial/parallel 调度器，可自定义接入 Celery 或 Kubernetes）。提供早停、参数约束、自定义初始点、失败评估容错、CASH 分类器选择与优化、神经架构搜索等能力；配套两篇论文（ICASSP 2020、CogMI 2021）。以 pip 安装为主，源码安装亦可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 兼容 scikit-learn 参数空间定义（连续/离散/类别/分布）
- 本地/集群/云端模块化并行调度（serial/parallel/custom 调度器）
- 早停、参数约束、自定义初始点等配置项
- CASH 联合分类器选择与优化、神经架构搜索

## 适用场景

- 为 KNN、SVM、XGBoost 等模型调优超参数
- 在 Celery 或 Kubernetes 集群上并行评估目标函数
- 在多次运行之间复用调优结果作为初始点继续优化

## 场景标签

`MLOps` · 领域:训练与推理

## 证据(README 行号)

> L3: **Mango** is a python library to find the optimal hyperparameters for machine learning classifiers.
> L148: Mango is designed to take advantage of distributed computing. The objective function can be scheduled to

## 星数曲线

```mermaid
xychart-beta
    title "ARM-software/mango 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 417 --> 419
    line [418, 418]
```

2026-10-18 418 → 2026-10-27 418（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `4a0afdb00e29` · [字段定义](../../DATASET.md)*
