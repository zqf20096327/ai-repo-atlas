# ArthurMangussi/pymdatagen

⭐ 15 · Python · MIT · 推送 2026-10-13 · [GitHub](https://github.com/ArthurMangussi/pymdatagen) · [官网](https://arthurmangussi.github.io/pymdatagen/) · 组织维护

**给机器学习研究者的缺失数据人工生成 Python 库**

mdatagen（missing-data-generator）是一个用于人工生成缺失数据的 Python 库，实现 Santos et al. (2019) 综述中的多种缺失机制，覆盖单变量与多变量场景下的 MCAR、MAR、MNAR 三类机制，用于模拟含缺失观测的现实数据。库设计为与现有 Python 数据分析工作流集成，兼容 scikit-learn，可搭配 missingno 做可视化，并提供直方图绘图与基于 MSE 的插补质量评估示例。由巴西航空技术研究所与葡萄牙科英布拉大学的研究者合作开发，通过 pip 安装，相关论文发表于 Neurocomputing。

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

- 实现 MCAR、MAR、MNAR 三类缺失数据生成机制
- 支持单变量与多变量场景，含新型 MNAR 多变量机制
- 提供直方图可视化与基于 MSE 的插补质量评估示例
- 与 scikit-learn 工作流集成，可搭配 missingno 使用

## 适用场景

- 为缺失数据插补方法研究构造可控的实验数据
- 在机器学习流程中模拟不同缺失机制下的真实场景
- 评估和比较插补算法的质量

## 场景标签

 · 领域:机器学习/数据预处理

## 证据(README 行号)

> L10: This package has been developed to address a gap in machine learning research, specifically the artificial generati
> L12: This Python package is a collaboration between researchers at the Aeronautics Institute of Technologies (Brazil) an

## 星数曲线

```mermaid
xychart-beta
    title "ArthurMangussi/pymdatagen 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-31 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `3be4833130eb` · [字段定义](../../DATASET.md)*
