# google/temporian

⭐ — · [GitHub]() · 组织维护

**面向机器学习的时序数据预处理与特征工程 Python 库**

Google 与 Tryolabs 合作开发的 Python 库，用于时序数据的预处理与特征工程，定位类似 Pandas 之于表格数据。支持多变量时间序列、非均匀采样、多索引与多源事件流；核心计算用 C++ 实现；通过 tp.leak 显式声明机制防止特征计算依赖未来数据（避免 future leakage）；不做模型训练，可将结果导出为 Pandas DataFrame 与任意 ML 库（PyTorch、Scikit-Learn、Jax、TensorFlow、XGBoost 等）配合使用。通过 pip 从 PyPI 安装，当前支持 Linux 与 macOS，Windows 支持开发中。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 支持均匀/非均匀采样、单/多变量、多索引与多源非同步事件流
- 核心计算以 C++ 实现
- 除非显式 tp.leak，特征计算不能依赖未来数据，防止 future leakage
- 不训练模型，可与 PyTorch/Scikit-Learn/Jax/TensorFlow/XGBoost 等集成

## 适用场景

- 为机器学习模型准备时序特征并防止数据泄漏
- 处理事件日志与多源非同步事件流
- 聚合与时序变换后导出 Pandas DataFrame 供下游 ML 库使用

## 场景标签

 · 领域:数据工程/机器学习

## 证据(README 行号)

> L9: **Temporian** is a library for **safe**, **simple** and **efficient** preprocessing and feature engineering of tempo
> L25: - **Easy to integrate into an existing ML ecosystem**: Temporian does not perform any ML model training - instead i

## 星数曲线

```mermaid
xychart-beta
    title "google/temporian 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 710 --> 712
    line [711, 711]
```

2026-10-18 711 → 2026-10-25 711（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `d610d15d5742` · [字段定义](../../DATASET.md)*
