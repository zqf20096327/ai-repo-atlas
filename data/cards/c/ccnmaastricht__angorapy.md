# ccnmaastricht/angorapy

⭐ 21 · Python · GPL-3.0 · 推送 2026-06-24 · [GitHub](https://github.com/ccnmaastricht/angorapy) · [官网](http://angorapy.org) · 组织维护

**供科研者用强化学习构建具身脑模型的开源库**

Python 建模库，用于在可定制的感知运动任务上构建并训练大脑的深度神经网络模型，采用强化学习（PPO 异步算法），通过 MPI 实现并行经验采集与优化，可在本地工作站或 SLURM HPC 集群上分布式运行。提供高级 API、内置模型与环境，同时保留自定义管线各环节的选项；附带 train/evaluate/observe/benchmark 等脚本与 Docker 镜像。依赖 Python 3.6+、swig 与 MPI 实现。由 Maastricht 大学团队维护，发表于 Frontiers in Neuroinformatics。

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

- 通过强化学习构建与训练具身脑模型的高级 API
- 基于 MPI 的分布式训练，支持本地工作站与 SLURM HPC 集群
- 内置 train/evaluate/observe/benchmark 脚本与监控链接
- 支持自定义模型、环境与超参数

## 适用场景

- 在感知运动任务上训练脑模型并评估
- 在 HPC 集群上分布式运行 PPO 实验
- 批量训练多配置 agent 并对比策略

## 场景标签

`科研工具` `强化学习` · 领域:学习与行业

## 证据(README 行号)

> L9: **AngoraPy** is an open source modeling library for buidling goal-driven embodied brain models. It provides an easy-
> L167:  Weidler, T., Goebel, R., & Senden, M. (2023). AngoraPy: A Python toolkit for modeling anthropomorphic goal-driven

## 星数曲线

```mermaid
xychart-beta
    title "ccnmaastricht/angorapy 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 20 --> 22
    line [21, 21]
```

2026-10-18 21 → 2026-10-30 21（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `d5cab4779cca` · [字段定义](../../DATASET.md)*
