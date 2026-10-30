# ctlab/ITMO_FS

⭐ 148 · Python · BSD-3-Clause · 推送 2026-07-21 · [GitHub](https://github.com/ctlab/ITMO_FS) · 组织维护

**Python 特征选择工具箱：统一接口实现数十种算法**

由 ITMO 大学 ctlab 开发的开源特征选择库，在统一接口下实现监督/无监督过滤器、包裹式、嵌入式、混合与集成方法，共数十种经典与现代算法，暴露 fit/transform/fit_transform 的 scikit-learn 兼容 API，可嵌入 sklearn pipeline。支持 NumPy 数组、pandas DataFrame 与 SciPy 稀疏矩阵；过滤器由 measure 与 cutting rule 组件组合构成。适用场景包括高维数据降维、传统 ML 模型预处理、研究中的特征排序与算法基准对比。经 PyPI 或源码安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | BSD-3-Clause |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 监督/无监督/包裹式/嵌入式/混合/集成方法统一接口
- scikit-learn 兼容 API（fit/transform/fit_transform），可接入 sklearn pipeline
- 可组合过滤器：measure 与 cutting rule 分离，支持自定义策略
- 支持 NumPy/pandas/SciPy 稀疏矩阵的稠密与稀疏数据

## 适用场景

- 为高维数据集做降维与特征筛选
- 在 SVM、逻辑回归、树模型等 ML 流水线前做特征预处理
- 研究项目中做特征排序与探索性分析
- 对比与基准测试不同特征选择算法

## 场景标签

 · 领域:机器学习/数据预处理

## 证据(README 行号)

> L6:  Supervised, unsupervised, wrapper, embedded and hybrid methods under a unified interface.
> L23: ITMO_FS is an open-source feature selection toolbox developed at ITMO University.

## 星数曲线

```mermaid
xychart-beta
    title "ctlab/ITMO_FS 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 147 --> 149
    line [148, 148]
```

2026-10-18 148 → 2026-10-30 148（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `8d345c065513` · [字段定义](../../DATASET.md)*
