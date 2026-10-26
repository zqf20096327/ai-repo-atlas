# JuliaAI/Imbalance.jl

⭐ 31 · Julia · MIT · 推送 2026-09-20 · [GitHub](https://github.com/JuliaAI/Imbalance.jl) · [官网](https://juliaai.github.io/Imbalance.jl/dev/) · 组织维护

**Julia 类别不平衡重采样工具箱，供分类任务前处理**

Julia 语言的机器学习工具包，提供 12 种以上类别不平衡重采样算法：随机过采样、SMOTE 及其变体（Borderline SMOTE1、SMOTE-N、SMOTE-NC）、ROSE、RWO、随机/聚类/EditedNearestNeighbors/Tomek Links 欠采样，以及经 MLJBalancing.jl 提供的 Balanced Bagging 分类器。支持多类别、名义与连续特征。除纯函数式 API 外，提供 MLJ 与 TableTransforms 两种接口，可与 MLJ 分类模型组成管道在训练前自动重采样。由 Google Summer of Code 项目创建，附 JOSS 论文可引用。

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

- 12+ 种过采样/欠采样算法（SMOTE 系列、ROSE、RWO、Tomek Links 等）
- 支持多类别与名义/连续特征，含自动名义特征编解码
- 提供 MLJ 与 TableTransforms 接口，可与 MLJ 分类器组管道
- 输入输出支持表格与矩阵格式

## 适用场景

- 分类训练前对少数类过采样或多数类欠采样
- 在 MLJ 流水线中自动完成训练前重采样
- 多类别且含类别特征的数据集做不平衡校正

## 场景标签

 · 领域:机器学习/数据预处理

## 证据(README 行号)

> L5: A Julia package with resampling methods to correct for class imbalance in a wide variety of classification settings.
> L65: All methods support the `MLJ` interface where instead of directly calling the method, one instantiates a model for 

## 星数曲线

```mermaid
xychart-beta
    title "JuliaAI/Imbalance.jl 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 30 --> 32
    line [31, 31]
```

2026-10-18 31 → 2026-10-26 31（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 mid · 依据 README sha `97db9fae4f11` · [字段定义](../../DATASET.md)*
