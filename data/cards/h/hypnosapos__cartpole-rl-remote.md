# hypnosapos/cartpole-rl-remote

⭐ 25 · Python · MIT · 推送 2026-01-12 · [GitHub](https://github.com/hypnosapos/cartpole-rl-remote) · 组织维护

**CartPole 强化学习示例项目：从自定义训练到 Kubernetes 部署推理**

基于 QLearning 与 Keras 神经网络的 CartPole 游戏强化学习实验项目，展示从本地训练到生产化部署的完整路径。本地场景用 Make/Docker 运行训练器，通过 Visdom、EFK（fluentd/Elasticsearch/Kibana）或 ModelDB 收集实验指标；进阶场景在 Kubernetes 上用 Polyaxon 做多实验训练，用 Seldon 部署模型推理，支持 model/abtest/router 三种部署图与 epsilon greedy 流量路由。面向希望参考开源 MLOps 流水线的开发者。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- QLearning + Keras 神经网络的 CartPole 训练器，输出 h5 最优模型
- Visdom / EFK / ModelDB 三种指标采集与实验跟踪方式
- Polyaxon on Kubernetes 上的多实验训练编排
- Seldon 部署推理，支持 model/abtest/router 图与 epsilon greedy 流量路由

## 适用场景

- 学习从训练到推理的容器化 RL 流水线
- 参考 Docker Compose 与 Kubernetes 上的 ML 实验编排
- 体验 Seldon 多模型路由与 A/B 测试部署

## 场景标签

`MLOps` `强化学习` · 领域:训练与推理

## 证据(README 行号)

> L12: This project is intended to play with `CartPole <https://gym.openai.com/envs/CartPole-v0/>`_ game using Reinforceme
> L15: The model is divided basically in three parts: Neural network model, QLearning algorithm and application runner.
> L17: We want to show you a journey from custom training of models to a productive platform based on open source (trainin

## 星数曲线

```mermaid
xychart-beta
    title "hypnosapos/cartpole-rl-remote 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 24 --> 26
    line [25, 25]
```

2026-10-18 25 → 2026-10-31 25（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 mid · 依据 README sha `b94e97ed2617` · [字段定义](../../DATASET.md)*
