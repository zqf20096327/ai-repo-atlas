# SmartTensors/NMFk.jl

⭐ 20 · HTML · GPL-3.0 · 推送 2026-10-05 · [GitHub](https://github.com/SmartTensors/NMFk.jl) · [官网](https://smarttensors.github.io/NMFk.jl/stable/) · 组织维护

**自动估计特征数的非负矩阵分解无监督机器学习库**

SmartTensors 框架的 Julia 模块，实现带 k-means 聚类与物理约束的非负矩阵分解（NMF），可自动估计数据中的最优特征数 k（经典 NMF 不支持）。支持盲源分离、特征提取、异常检测、缺失数据填补、代理模型构建等任务；通过 Shared/Distributed Arrays 支持并行计算，GPU/TPU 加速经由现有 Julia 包提供。提供数据可视化与前后处理工具，附示例、测试与 Jupyter notebook。曾获 2021 R&D100 奖。要求 Julia 1.12+。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- k-means 聚类+正则化约束自动估计最优特征数 k
- 支持特征提取、盲源分离、异常检测、数据补缺等任务
- Shared/Distributed Arrays 并行计算，GPU/TPU 经由 Julia 包加速
- 提供 Docker 镜像、示例、测试与 Jupyter notebooks

## 适用场景

- 从混合观测数据中盲分离源信号并确定源数量
- 地球科学/环境数据（地下水、气候、污染物传输）的无监督分析
- 构建降阶/代理模型与数据集自动标注

## 场景标签

`数据分析` · 领域:效率与自动化

## 证据(README 行号)

> L12: **NMFk** is a novel unsupervised machine learning methodology that allows for the automatic identification of the o
> L16: **NMFk** estimates the number of features `k` through *k*-means clustering coupled with regularization constraints 
> L36: **NMFk** provides high-performance computing capabilities to solve problems in parallel using Shared and Distribute

## 星数曲线

```mermaid
xychart-beta
    title "SmartTensors/NMFk.jl 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 19 --> 21
    line [20, 20]
```

2026-10-18 20 → 2026-10-29 20（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `d69f91306bf3` · [字段定义](../../DATASET.md)*
