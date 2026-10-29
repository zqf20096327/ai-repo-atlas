# alvertogit/bigdata_docker

⭐ 19 · Python · 推送 2026-10-25 · [GitHub](https://github.com/alvertogit/bigdata_docker) · 个人维护

**用 Docker Compose 构建 Spark/HDFS 大数据与数据科学集群**

提供构建容器化大数据集群所需的全部组件：基于 Apache Spark 4.x、Hadoop HDFS 与 Docker Compose 搭建一主一从（可扩展）集群，主节点内置 Maven 与 Python 虚拟环境（TensorFlow、scikit-learn、XGBoost、TPOT 等）。工作流为 Scala Spark 应用处理大数据文件，Python 数据科学应用训练预测模型，另支持在主节点远程运行 Jupyter Lab 做数据分析与建模。面向需要可扩展数据处理与机器学习开发环境的开发者和数据科学工作者。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Docker Compose 一键构建 Spark master/worker 集群与 HDFS 存储
- 主节点预装 Python 3.12 数据科学环境（TensorFlow/scikit-learn/XGBoost/TPOT 等）
- 提供 Scala（Maven 编译）与 Python 示例应用及 Jupyter Notebook
- worker 节点数量可通过修改 docker-compose 文件增加

## 适用场景

- 搭建容器化 Spark+HDFS 集群跑大数据处理作业
- 在集群环境中做数据处理与机器学习模型训练
- 通过浏览器远程使用主节点上的 Jupyter Lab 做数据分析

## 场景标签

`数据分析` · 领域:效率与自动化

## 证据(README 行号)

> L3: This repository stores all the required components to build a containerized cluster for [Big Data] and [Data Science
> L87: 1. Containerized [Big Data] cluster: It shall be the base of the system and it can allow to run large files process
> L89: 3. [Python] [Data Science] applications: It shall employ [Python] [Data Science] libraries to use [machine learning

## 星数曲线

```mermaid
xychart-beta
    title "alvertogit/bigdata_docker 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 18 --> 20
    line [19, 19]
```

2026-10-18 19 → 2026-10-29 19（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `5eb2bf4f4110` · [字段定义](../../DATASET.md)*
