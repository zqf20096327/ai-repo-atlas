# skforecast/skforecast-datasets

⭐ 16 · Python · BSD-3-Clause · 推送 2026-10-28 · [GitHub](https://github.com/skforecast/skforecast-datasets) · [官网](https://skforecast.org) · 组织维护

**skforecast 时间序列预测库配套的示例数据集仓库**

收录 skforecast 库及其教程所用的时间序列数据集，涵盖药品支出、燃油消耗、空气质量、共享单车、电力需求、门店销售、M4 竞赛序列等 18 个数据集，每个条目提供 CSV/Parquet 下载地址、分隔符、索引列、时间格式、频率、描述与原始出处。可从仓库直接下载，或通过 skforecast 库的 fetch_dataset() 函数按名称加载。数据来源包括 fpp3、UCI、Kaggle、Monash 等公开渠道。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | BSD-3-Clause |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 18 个时间序列数据集，标注分隔符/索引列/频率/格式等加载元信息
- 每条数据集附描述与原始出处（fpp3、UCI、Kaggle、Monash 等）
- 支持 skforecast 库 fetch_dataset() 按名称加载

## 适用场景

- 学习或测试 skforecast 时获取标准示例数据
- 时间序列预测算法的基准实验数据
- 教程与文档编写时引用带出处的时间序列数据

## 场景标签

 · 领域:时间序列预测/数据集

## 证据(README 行号)

> L3: This repository contains datasets used in the skforecast library. It also contains datasets used in related tutorial
> L5: All datasets included have a sort description as well as the original source. They can be downloaded directly from t

## 星数曲线

```mermaid
xychart-beta
    title "skforecast/skforecast-datasets 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-31 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `6daecb5e3c1e` · [字段定义](../../DATASET.md)*
