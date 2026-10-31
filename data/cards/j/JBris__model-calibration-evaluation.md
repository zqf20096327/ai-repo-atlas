# JBris/model-calibration-evaluation

⭐ 16 · Python · MIT · 推送 2026-09-14 · [GitHub](https://github.com/JBris/model-calibration-evaluation) · [官网](https://jbris.github.io/model-calibration-evaluation/) · 个人维护

**模型校准方法评测代码：面向灵敏度与贝叶斯推断等任务**

研究型代码仓库，对十余种模型校准方法进行评测比较，涵盖 Approximate Bayesian Computation - Sequential Monte Carlo、贝叶斯优化、BO Likelihood-Free Inference（BOLFI）、DREAM、高斯过程试验设计、流匹配后验估计、SNPE、多项式混沌展开等，应用于灵敏度分析、不确定性分析、优化与贝叶斯推断。真值仿真参数在 config.yaml 中给出。README 未提供安装运行说明，仅列出被评测方法清单。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 评测 15 种模型校准方法（ABC-SMC、贝叶斯优化、BOLFI、DREAM 等）
- 任务覆盖灵敏度分析、不确定性分析、优化与贝叶斯推断
- 真值仿真参数记录于 config.yaml

## 适用场景

- 比较不同模型校准方法在仿真任务上的表现
- 复现贝叶斯推断与灵敏度分析实验配置
- 了解似然无关推断方法的评测设置

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L6: Evaluating model calibration methods for sensitivity analysis, uncertainty analysis, optimisation, and Bayesian infe
> L10: The following model calibration methods have been evaluated.

## 星数曲线

```mermaid
xychart-beta
    title "JBris/model-calibration-evaluation 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-31 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 low · 依据 README sha `e8dcad3f0816` · [字段定义](../../DATASET.md)*
