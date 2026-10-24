# omegaml/omegaml

⭐ 109 · Python · Apache-2.0 · 推送 2026-10-22 · [GitHub](https://github.com/omegaml/omegaml) · [官网](https://omegaml.github.io/omegaml/) · 组织维护

**一站式 MLOps 平台：从 Jupyter 部署模型、管道与 REST 服务**

omega-ml 提供 Python 库与集成平台，支持从 Jupyter Notebook 或任意代码中存储 Pandas 数据与模型对象、在纯 Python 计算集群上训练与缩放模型、通过 REST API 服务模型与数据，并共享数据科学工作区。开箱支持 scikit-learn、Keras、TensorFlow，可经扩展 API 接入其他框架、集群与数据源。通过 docker-compose 一键启动服务端（含 Jupyter 与 MongoDB），或 pip 安装客户端库。另有单独授权的 Commercial Edition，面向 Kubernetes 部署。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- om.models/om.datasets 透明存储与检索模型和数据
- 集成纯 Python 计算集群上运行 fit/predict/gridsearch
- REST API 服务模型与数据集
- 开箱支持 scikit-learn/Keras/TensorFlow，扩展 API 接入其他框架

## 适用场景

- 从 Jupyter 一行代码把模型部署到生产
- 团队共享数据、模型与 notebook 的数据科学协作
- 在共享集群上做核外计算与模型训练

## 场景标签

`MLOps` · 领域:训练与推理

## 证据(README 行号)

> L5: - deploy machine learning models straight from Jupyter Notebook (or any other code)
> L11: - scale model training on the included scalable pure-Python compute cluster, remote or locally
> L66: omega-ml currently supports scikit-learn, Keras and Tensorflow out of the box.
> L72: - deploy models to production with a single line of code

## 星数曲线

```mermaid
xychart-beta
    title "omegaml/omegaml 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-24"]
    y-axis "stars" 107 --> 110
    line [108, 109, 109]
```

2026-10-18 108 → 2026-10-24 109（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `45edc8a97d41` · [字段定义](../../DATASET.md)*
