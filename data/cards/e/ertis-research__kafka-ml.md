# ertis-research/kafka-ml

⭐ 206 · Python · MIT · 推送 2026-09-08 · [GitHub](https://github.com/ertis-research/kafka-ml) · 组织维护

**在 Kubernetes 上管理 ML 模型流水线、数据流由 Kafka 接入的框架**

面向 TensorFlow/Keras 与 PyTorch(Ignite) 的机器学习流水线管理框架，部署于 Kubernetes：在 Web UI 中以源码定义模型，将模型编组为 configuration，部署到集群训练与推理；训练/推理数据通过 Apache Kafka 接入，可直接连接 IoT 等数据流。支持单模型与由 Edge-Fog-Cloud 子模型构成的分布式模型链，训练后可下载模型或部署推理，并在可视化页查看分类/回归指标与混淆矩阵。要求 Docker 与 Kubernetes≥v1.15.5，通过 kubectl apply -k 一键安装；有开放获取论文支撑。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Web UI 中定义 TF/Keras 与 PyTorch(Ignite) 模型，无需外部库执行
- 训练与推理数据经 Apache Kafka 流式接入，可连 IoT 数据流
- 支持 Edge-Fog-Cloud 层级式分布式模型的训练与推理部署
- kubectl apply -k 一键安装全部组件与 Kafka

## 适用场景

- 用 Kafka 数据流持续训练和推理我的深度学习模型
- 在 IoT 数据流上跑 MNIST 等模型的训练与预测
- 把模型按 Edge-Fog-Cloud 拆分做分布式训练与推理
- 在 Kubernetes 上比较一组模型的训练指标

## 场景标签

`MLOps` · 领域:训练与推理

## 证据(README 行号)

> L3: Kafka-ML is a framework to manage the pipeline of Tensorflow/Keras and PyTorch
> L5: design, training, and inference of ML models. The training and inference
> L6: datasets for the ML models can be fed through Apache Kafka, thus they can be

## 星数曲线

```mermaid
xychart-beta
    title "ertis-research/kafka-ml 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 205 --> 207
    line [206, 206]
```

2026-10-18 206 → 2026-10-26 206（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 mid · 依据 README sha `fe4b00328117` · [字段定义](../../DATASET.md)*
