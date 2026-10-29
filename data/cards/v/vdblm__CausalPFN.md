# vdblm/CausalPFN

⭐ 135 · Jupyter Notebook · Apache-2.0 · 推送 2026-09-27 · [GitHub](https://github.com/vdblm/CausalPFN) · 组织维护

**基于 Transformer 上下文学习的因果效应估计库**

Python 库，利用 transformer 架构的 in-context learning 实现摊销式因果效应估计：无需针对新场景重新训练即可快速估计 CATE/ATE，内置校准与置信区间的不确定性量化，支持 uplift 建模，GPU 上以 CUDA 加速。用于复现论文实验结果，提供多个 notebook 示例（因果效应估计、Hillstrom 营销、A/B 测试降本、校准分析），基线比较覆盖 IHDP/ACIC/Lalonde 共 310 个任务。依赖 Python 3.10+ 与 PyTorch 2.3+，经 PyPI 安装，Apache-2.0 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 摊销学习：无需重训练即可快速估计因果效应
- 内置校准与置信区间的不确定性量化
- 支持 uplift 建模与个性化决策
- 覆盖 IHDP/ACIC/Lalonde 310 个任务的基准比较

## 适用场景

- 在新数据上快速估计处理效应而无需重新训练
- 营销场景做 uplift 建模与 A/B 测试成本缩减
- 复现论文中的因果推断基准实验

## 场景标签

 · 领域:因果推断/机器学习

## 证据(README 行号)

> L19: **An easy-to-use library for causal effect estimation using transformer-based in-context learning**
> L27: CausalPFN leverages the power of transformer architectures for amortized causal effect estimation, enabling fast an
> L33: - **🚀 Fast Inference**: Amortized learning enables rapid causal effect estimation without retraining

## 星数曲线

```mermaid
xychart-beta
    title "vdblm/CausalPFN 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-29"]
    y-axis "stars" 133 --> 136
    line [134, 135, 135]
```

2026-10-18 134 → 2026-10-29 135（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `c5bce25a4211` · [字段定义](../../DATASET.md)*
