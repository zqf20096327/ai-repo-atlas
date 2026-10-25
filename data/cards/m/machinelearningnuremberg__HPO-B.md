# machinelearningnuremberg/HPO-B

⭐ 42 · Python · MIT · 推送 2025-11-08 · [GitHub](https://github.com/machinelearningnuremberg/HPO-B) · 组织维护

**黑箱超参数优化算法评测基准与元数据集**

NeurIPS DBT 2021 提出的 HPO 评测基准：包含 176 个元数据集上不同搜索空间与数据集的精度评估，分 v1/v2/v3 三个版本，v3 划分训练/验证/测试。提供 HPOBHandler 类加载元数据集并评测新算法（实现 observe_and_suggest 方法），支持基于 XGBoost 代理模型的连续搜索空间评测，并附基准提取代码与绘图工具。需 Python 3.7，元数据集另行下载。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 176 个元数据集、三个版本（v1/v2/v3 train-val-test 划分）
- HPOBHandler 统一接口：实现 observe_and_suggest 即可评测任意 HPO 算法
- XGBoost 代理模型支持连续搜索空间评测
- 提供基准扩展代码与结果对比绘图工具（BenchmarkPlotter）

## 适用场景

- 为自己的 HPO 算法在统一基准上做可复现评测
- 在连续或离散搜索空间上对比优化方法性能
- 扩展元数据集、加入新的搜索空间与评估

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L2: HPO-B is a benchmark for assessing the performance of black-box HPO algorithms. This repo contains the code for easi
> L6: The meta-dataset contains evaluations of the accuracy for different search-spaces on different datasets. For more de

## 星数曲线

```mermaid
xychart-beta
    title "machinelearningnuremberg/HPO-B 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 41 --> 43
    line [42, 42]
```

2026-10-18 42 → 2026-10-25 42（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `97e40fefe3e5` · [字段定义](../../DATASET.md)*
