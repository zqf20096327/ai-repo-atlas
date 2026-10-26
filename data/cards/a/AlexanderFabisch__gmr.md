# AlexanderFabisch/gmr

⭐ 201 · Python · BSD-3-Clause · 推送 2026-01-12 · [GitHub](https://github.com/AlexanderFabisch/gmr) · [官网](https://alexanderfabisch.github.io/gmr/) · 个人维护

**Python 高斯混合模型库：用 GMM 做聚类与回归预测**

纯 Python 实现的高斯混合模型（GMM）库，支持从样本估计 GMM、从 GMM 采样以及基于条件分布做回归预测；提供对角/满协方差选项、可选的 sklearn 回归器接口，并可直接从 sklearn 的 GaussianMixture 初始化。作者说明回归功能难以融入 sklearn 接口故独立成库。不内置模型存储函数，但可用 pickle 或导出 priors/means/covariances 属性持久化。面向机器人学/机器学习研究者的传统监督学习场景，附 JOSS 论文与 Google Colab 示例。

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

- GMM 聚类与基于条件分布的回归预测
- 支持从 sklearn GaussianMixture 初始化
- 提供可选的 sklearn 回归器接口用于模型选择
- 纯 Python 实现，可通过属性导出跨库持久化模型

## 适用场景

- 从带噪声的样本数据拟合 GMM 并做条件回归预测
- 生成轨迹与从置信区间采样的运动建模
- 在 sklearn 工作流中用回归器接口做模型选择

## 场景标签

 · 领域:机器学习/统计建模

## 证据(README 行号)

> L3: > Gaussian Mixture Models (GMMs) for clustering and regression in Python.
> L43: Estimate GMM from samples, sample from GMM, and make predictions:

## 星数曲线

```mermaid
xychart-beta
    title "AlexanderFabisch/gmr 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 200 --> 202
    line [201, 201]
```

2026-10-18 201 → 2026-10-26 201（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `afe97c3be2cd` · [字段定义](../../DATASET.md)*
