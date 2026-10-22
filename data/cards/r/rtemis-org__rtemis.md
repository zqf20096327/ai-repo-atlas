# rtemis-org/rtemis

⭐ 150 · R · NOASSERTION · 推送 2026-10-21 · [GitHub](https://github.com/rtemis-org/rtemis) · [官网](https://docs.rtemis.org/r/ml) · 个人维护

**R 语言机器学习与可视化工具包，Schema 驱动建模流程**

面向 R 用户的机器学习与可视化包：以 S7 类型化配置（setup_* 函数，发布为 JSON Schema）驱动从数据预处理、重采样、调参到训练的完整流程；train()/cluster()/decomp() 一次调用完成监督学习、聚类与分解，单个 train() 覆盖预处理、分解、超参调优、stacking 与嵌套重采样。内建 SuperLearner、RuleFit、线性加性树等算法，提供 Shapley 解释、校准与保形预测，输出记录每个解析值及来源并可用 writeup() 生成溯源的方法与结果文档。经 CRAN 与 r-universe 安装。

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

- setup_* 类型化配置并发布为 JSON Schema，可在 R、CLI 与 rtemislive 间迁移
- train() 单次调用完成预处理、调参、stacking 与嵌套重采样
- Shapley 值解释、校准与保形预测
- 输出可审计：记录每个值来源，writeup() 生成可溯源报告

## 适用场景

- 在 R 中一站式完成监督学习、聚类与降维建模
- 需要可审计、可复现配置的机器学习流程
- 为训练好的模型生成解释与不确定性评估

## 场景标签

`数据分析` · 领域:效率与自动化

## 证据(README 行号)

> L11: - **Functional API**: `train()`, `cluster()`, and `decomp()` provide one-call supervised learning, clustering, and 
> L14: - **Algorithms**: a broad set of supervised learners, including native SuperLearner, RuleFit, and Linear Additive T

## 星数曲线

```mermaid
xychart-beta
    title "rtemis-org/rtemis 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-22"]
    y-axis "stars" 149 --> 151
    line [150, 150]
```

2026-10-18 150 → 2026-10-22 150（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `3419b181a951` · [字段定义](../../DATASET.md)*
