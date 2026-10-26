# zillow/quantile-forest

⭐ 255 · Python · Apache-2.0 · 推送 2026-10-14 · [GitHub](https://github.com/zillow/quantile-forest) · [官网](https://zillow.github.io/quantile-forest/) · 组织维护

**兼容 scikit-learn 的分位数回归森林 Python 库**

提供分位数回归森林（QRF）的 Python 实现：基于树的非参数集成方法，用于估计条件分位数，适用于高维数据与不确定性估计。Cython 优化的估计器扩展 scikit-learn 的森林回归器，可在预测时估计任意分位数而无需重训练，并提供袋外估计、分位数秩计算与邻近度计数方法；可作为 scikit-learn 森林回归器的替代品直接使用。通过 PyPI 与 conda-forge 安装，面向使用 scikit-learn 工作流的开发与科研用户。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 估计条件分位数，支持预测时任意分位数且无需重训练
- 提供袋外估计、分位数秩、邻近度计数方法
- 兼容并可替代 scikit-learn 森林回归器
- Cython 优化的实现

## 适用场景

- 为回归模型生成预测区间
- 高维数据的不确定性估计
- 在 scikit-learn 流水线中直接替换森林回归器做分位数预测

## 场景标签

 · 领域:机器学习/统计建模

## 证据(README 行号)

> L12: Quantile regression forests (QRF) are a non-parametric, tree-based ensemble method for estimating conditional quant
> L38: y_pred = qrf.predict(X, quantiles=[0.025, 0.5, 0.975])

## 星数曲线

```mermaid
xychart-beta
    title "zillow/quantile-forest 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 254 --> 256
    line [255, 255]
```

2026-10-18 255 → 2026-10-26 255（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `aa9407241edf` · [字段定义](../../DATASET.md)*
