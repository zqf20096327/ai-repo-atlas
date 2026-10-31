# NatLabRockies/nsrdb

⭐ 15 · Python · BSD-3-Clause · 推送 2026-06-08 · [GitHub](https://github.com/NatLabRockies/nsrdb) · [官网](https://natlabrockies.github.io/nsrdb/) · 组织维护

**美国国家太阳辐射数据库的辐照度数据处理流水线软件**

提供 NSRDB 全套辐照度数据处理方法：PXS All-Sky 物理模型计算地表辐照度，Data Model 框架负责数据采集、处理与准备，接入 MLClouds 模型预测缺失云属性（Gap Fill）。含命令行接口与版本化数据发布记录（GOES/Meteosat 卫星数据）。由 NREL（美国国家可再生能源实验室）维护，面向太阳能资源分析师与开发者，通过 pip 安装。机器学习仅用于云属性填补模块，主体为物理模型驱动。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | BSD-3-Clause |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- PXS All-Sky 物理模型计算地表辐照度
- Data Model 数据聚合框架负责采集与预处理
- 接入 MLClouds 模型预测缺失云属性（Gap Fill）
- 提供 CLI 与 conda/pixi/pip 安装途径

## 适用场景

- 处理卫星数据生成太阳辐照度数据集
- 对缺失云属性进行机器学习填补
- 构建辐射传输建模与太阳能资源分析流水线

## 场景标签

 · 领域:可再生能源/气象数据科学

## 证据(README 行号)

> L29: The National Solar Radiation Database (NSRDB) software includes all the methods
> L54: The `MLClouds Model <https://github.com/NatLabRockies/mlclouds.git>`_ is used to predict

## 星数曲线

```mermaid
xychart-beta
    title "NatLabRockies/nsrdb 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-31 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `297fcd9ae181` · [字段定义](../../DATASET.md)*
