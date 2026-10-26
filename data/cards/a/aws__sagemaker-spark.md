# aws/sagemaker-spark

⭐ 301 · Scala · Apache-2.0 · 推送 2026-08-06 · [GitHub](https://github.com/aws/sagemaker-spark) · [官网](https://aws.github.io/sagemaker-spark/) · 组织维护

**在 Spark 中调用 Amazon SageMaker 训练与托管模型的库**

面向 Spark 开发者的开源 Scala/Python 库（sagemaker-spark 与 sagemaker-pyspark-sdk），提供 SageMakerEstimator 与 SageMakerModel 等 Spark ML 组件，可将 Spark DataFrame 序列化上传 S3，发起 SageMaker 训练任务（内置 K-Means、XGBoost 适配类，也支持自定义算法 Docker 镜像），并通过托管 Endpoint 做推理。Scala 版经 Maven Central 分发，EMR 5.11.0 起预装；本地运行需自行构建带 Hadoop 2.8 的 Spark。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- SageMakerEstimator/SageMakerModel 作为 Spark ML Pipeline 阶段嵌入训练与推理流程
- 内置 K-Means、XGBoost 适配类，支持任意 SageMaker 算法镜像
- DataFrame 自动序列化上传 S3 并轮询训练/Endpoint 创建
- EMR 5.11.0 起预装，Maven Central 提供 Scala 构件

## 适用场景

- 在 Spark 数据管道中直接调用 SageMaker 托管算法训练模型
- 用自有算法 Docker 镜像在 Spark 规模数据上训练与推理
- 在 EMR 集群上运行混合 Spark ML 与 SageMaker 阶段的 Pipeline

## 场景标签

`MLOps` · 领域:训练与推理

## 证据(README 行号)

> L6: SageMaker Spark is an open source Spark library for Amazon SageMaker. With SageMaker Spark you construct Spark ML `P
> L210: The `SageMakerEstimator` is an `org.apache.spark.ml.Estimator` that trains a model on Amazon SageMaker.

## 星数曲线

```mermaid
xychart-beta
    title "aws/sagemaker-spark 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 300 --> 302
    line [301, 301]
```

2026-10-18 301 → 2026-10-26 301（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `2c3eedd5b1dc` · [字段定义](../../DATASET.md)*
