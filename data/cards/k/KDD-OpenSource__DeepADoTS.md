# KDD-OpenSource/DeepADoTS

⭐ 601 · Python · MIT · 推送 2026-04-13 · [GitHub](https://github.com/KDD-OpenSource/DeepADoTS) · 组织维护

**时间序列深度异常检测方法的基准评测流水线**

论文配套仓库，提供时间序列异常检测的基准评测流水线，实现 LSTM-AD、LSTM-ED、Autoencoder、Donut、REBM、DAGMM 等 7 种深度学习方法。各模型遵循 scikit-learn 接口，fit(X) 以无监督方式估计数据分布，predict(X) 返回每个样本的异常分数，用 ROC AUC 比较方法性能。基于 PyTorch/TensorFlow 实现，支持 git clone 源码安装与 Docker 部署，以 MNIST 演示用法。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 实现 7 种深度异常检测算法（LSTM-AD/Donut/DAGMM/REBM 等）
- 遵循 scikit-learn API（fit/predict），输出逐样本异常分数
- 以 ROC AUC 统一比较各方法性能
- 提供 Docker 构建与运行命令

## 适用场景

- 在自有时序数据上跑多种深度异常检测方法并对比
- 复现论文中的系统性基准评测
- 以 scikit-learn 风格接口快速试用 LSTM-AD 或 DAGMM 等模型

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L3: The goal of this repository is to provide a benchmarking pipeline for anomaly detection on time series data for mult
> L28: We follow the scikit-learn API by offering the interface methods `fit(X)` and `predict(X)`. The former estimates th

## 星数曲线

```mermaid
xychart-beta
    title "KDD-OpenSource/DeepADoTS 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 600 --> 602
    line [601, 601]
```

2026-10-18 601 → 2026-10-30 601（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 mid · 依据 README sha `611973459135` · [字段定义](../../DATASET.md)*
