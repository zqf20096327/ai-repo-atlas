# RumbleDB/rumble

⭐ 249 · Java · NOASSERTION · 推送 2026-10-23 · [GitHub](https://github.com/RumbleDB/rumble) · [官网](http://rumbledb.org/) · 组织维护

**基于 Apache Spark 的 JSONiq 查询引擎，查询大规模嵌套异构数据**

RumbleDB 是构建在 Apache Spark 之上的查询引擎，以 JSONiq 查询语言（而非 DataFrame API）访问 JSON、CSV、Parquet、Avro、LibSVM、文本等嵌套异构数据格式，可原地查询本地文件系统或数据湖（Azure blob、Amazon S3、HDFS）。附带 RumbleDB ML 模块，用于数据准备、清洗、校验后接入机器学习流程。项目 2017 年起源于 ETH Zurich 的硕士论文，由 Ghislain Fourny 的学生团队持续贡献。提供 Jupyter notebook 入门教程与文档。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 以 JSONiq 查询语言访问多种嵌套异构数据格式
- 可原地查询 Azure blob、Amazon S3、HDFS 等数据湖
- RumbleDB ML 支持数据准备/清洗/校验并接入机器学习流程
- 起源于 ETH Zurich，由学生团队持续开发

## 适用场景

- 对不适合 DataFrame 模型的大规模嵌套数据做查询
- 在数据湖上原地查询 JSON/Parquet/CSV 等混合格式数据
- 清洗校验数据后送入机器学习管道

## 场景标签

 · 领域:大数据/数据工程

## 证据(README 行号)

> L3: With RumbleDB, you can query with ease a lot of different nested, heterogeneous data formats like JSON, CSV, Parquet
> L9: You can prepare, clean up, validate your data and put it right into your machine learning pipelines with RumbleDB ML
> L17: RumbleDB was started in February 2017 at ETH Zurich as the Master's thesis of Stefan Irimescu, under the supervisio

## 星数曲线

```mermaid
xychart-beta
    title "RumbleDB/rumble 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 248 --> 250
    line [249, 249]
```

2026-10-18 249 → 2026-10-26 249（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 mid · 依据 README sha `7e0ea1abe634` · [字段定义](../../DATASET.md)*
