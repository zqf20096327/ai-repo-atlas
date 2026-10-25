# GBeurier/nirs4all

⭐ 42 · Python · AGPL-3.0 · 推送 2026-10-22 · [GitHub](https://github.com/GBeurier/nirs4all) · 组织维护

**近红外光谱机器学习分析库：数据加载到建模部署一站式**

面向近红外光谱（NIRS）研究者的 Python 库，覆盖数据加载、光谱预处理、模型训练与评估。提供 30 余种光谱变换（SNV/MSC/Savitzky-Golay 等）、15 余种 PLS 变体及 Kennard-Stone/SPXY 等划分方法，支持 scikit-learn、TensorFlow、PyTorch、JAX 多后端。采用声明式管道语法，集成 Optuna 调参、joblib 并行与 SHAP 解释，可导出 .n4a 模型包。另有桌面版 nirs4all Studio（独立仓库）。基于 Pinard 包重建，v0.9.0 起公共 API 稳定。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `dual` | AGPL-3.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 30+ 光谱预处理变换与 15+ PLS 变体（含自动算子选择）
- 多后端支持：scikit-learn / TensorFlow / PyTorch / JAX
- 声明式管道语法，joblib 并行执行与 Optuna 调参
- 导出 .n4a 可移植模型包，提供 sklearn 兼容封装

## 适用场景

- 对近红外光谱数据做回归/分类建模与交叉验证
- 批量试验预处理组合并自动选择最优管道
- 训练完成后导出模型包用于部署预测
- 用 SHAP 解释光谱模型的特征贡献

## 场景标签

 · 领域:科学计算/化学计量学

## 证据(README 行号)

> L7: **A comprehensive Python library for Near-Infrared Spectroscopy data analysis**
> L38: NIRS4ALL bridges the gap between spectroscopic data and machine learning by providing a unified framework for **dat

## 星数曲线

```mermaid
xychart-beta
    title "GBeurier/nirs4all 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-25"]
    y-axis "stars" 40 --> 43
    line [41, 42, 42]
```

2026-10-18 41 → 2026-10-25 42（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `ebac9e587b3c` · [字段定义](../../DATASET.md)*
