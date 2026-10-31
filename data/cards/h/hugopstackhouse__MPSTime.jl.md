# hugopstackhouse/MPSTime.jl

⭐ 25 · Julia · GPL-3.0 · 推送 2026-10-20 · [GitHub](https://github.com/hugopstackhouse/MPSTime.jl) · [官网](https://hugopstackhouse.github.io/MPSTime.jl/) · 组织维护

**用矩阵积态方法做时间序列分类与缺失填补的 Julia 库**

基于 ITensors.jl 的 Julia 包，用源自量子多体物理的矩阵积态（MPS）方法直接从数据学习时间序列的联合概率分布，提供统一的分类与填补（imputation）框架，可处理因传感器故障或例行维护导致的数据缺口。含分类、填补、编码与超参数教程文档。要求 Julia 1.11.1 及以上，从 Julia General registry 安装。方法发表于 Physical Review Research 2025 论文，GPL v3 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 用 MPS 学习时间序列联合概率分布
- 支持分类与缺失数据填补两类任务
- 基于 ITensors.jl 构建，附教程文档

## 适用场景

- 对未见时间序列做分类
- 填补因传感器故障产生的时序数据缺口
- 复现/扩展 MPS 时序机器学习方法

## 场景标签

 · 领域:科学计算/时间序列机器学习

## 证据(README 行号)

> L12: _MPSTime_ is a Julia package for learning the joint probability distribution of time series directly from data, usi
> L13: It provides a unified formalism for classifying unseen data and for imputing gaps in time-series data, which regula
> L14: The package is built on ITensors.jl and is described in Moore et al. (2025).

## 星数曲线

```mermaid
xychart-beta
    title "hugopstackhouse/MPSTime.jl 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 24 --> 26
    line [25, 25]
```

2026-10-18 25 → 2026-10-31 25（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `5f5b161968a6` · [字段定义](../../DATASET.md)*
