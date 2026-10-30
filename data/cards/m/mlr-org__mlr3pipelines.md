# mlr-org/mlr3pipelines

⭐ 149 · R · LGPL-3.0 · 推送 2026-10-26 · [GitHub](https://github.com/mlr-org/mlr3pipelines) · [官网](https://mlr3pipelines.mlr-org.com/) · 组织维护

**R 语言机器学习数据流（流水线）构建工具包**

基于 mlr3 包的 R 语言数据流编程工具包：将预处理、模型拟合、集成学习等步骤表示为 PipeOps，以有向 Graph 连接组成机器学习流水线，并可包装为 GraphLearner 用于重采样、基准测试与调参；支持 PCA、特征过滤、路径分支（同时/可选）、预测聚合等操作。面向使用 mlr3 生态的 R 数据科学与机器学习用户。范围仍在扩展中，功能覆盖以当前文档所列为准。发表于 JMLR 2021。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `viral` | LGPL-3.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 以 PipeOps + 有向 Graph 组合机器学习流水线
- GraphLearner 包装后可用于重采样、基准测试与调参
- 支持同时/可选路径分支与预测的集成聚合
- 可与 mlr3tuning 联合优化多个处理单元的参数

## 适用场景

- 在 R 中组合预处理与建模步骤构建机器学习流水线
- 构建 stacking/bagging 等集成学习流程
- 对流水线整体做重采样评估与超参数调优

## 场景标签

`MLOps` · 领域:训练与推理

## 证据(README 行号)

> L22: **`mlr3pipelines`** is a [dataflow
> L26: workflows can be written as directed “Graphs” that represent data flows
> L29: **mlr3tuning** package, it is

## 星数曲线

```mermaid
xychart-beta
    title "mlr-org/mlr3pipelines 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 148 --> 150
    line [149, 149]
```

2026-10-18 149 → 2026-10-30 149（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `0b4c2c709b82` · [字段定义](../../DATASET.md)*
