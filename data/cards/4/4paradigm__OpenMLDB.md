# 4paradigm/OpenMLDB

⭐ 1,715 · C++ · Apache-2.0 · 推送 2026-10-23 · [GitHub](https://github.com/4paradigm/OpenMLDB) · [官网](https://openmldb.ai) · 组织维护 · 中文 README

**面向机器学习应用的特性计算数据库，训练与推理特性一致**

由第四范式开源的机器学习数据库，定位为 ML 应用的特性平台，以 SQL 作为统一编程语言完成离线特性开发，一条命令即可上线部署，通过统一执行计划生成器桥接批式（基于定制 Spark）与实时 SQL 引擎，保证训练与推理特性一致。实时引擎针对时序数据优化，可在毫秒级延迟产出在线特性，并提供分布式存储计算、故障恢复、高可用等企业级能力。也包含一个时序数据库能力，应用于金融、IoT 等领域。

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

- SQL 定义特性，Development as Deployment 三步完成训练到在线推理
- 统一执行计划生成器保证离线训练与在线推理特性一致
- 实时 SQL 引擎毫秒级延迟产出在线特性，针对时序数据优化
- 提供 Kafka/Pulsar/RocketMQ 连接器与 Airflow/DolphinScheduler 集成

## 适用场景

- 为实时推荐、风控等 ML 应用构建低延迟在线特性平台
- 离线特性脚本与在线推理之间保证数据一致性，避免数据泄漏
- 作为时序数据库用于金融、IoT 场景

## 场景标签

`MLOps` · 领域:训练与推理

## 证据(README 行号)

> L32: ### OpenMLDB is an open-source machine learning database that provides a feature platform computing consistent feat
> L38: OpenMLDB is an open-source machine learning database that is committed to solving the data and feature challenges. 
> L44: OpenMLDB is particularly designed as a feature platform for ML applications to accomplish the mission of **Developm

## 星数曲线

```mermaid
xychart-beta
    title "4paradigm/OpenMLDB 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 1714 --> 1716
    line [1715, 1715]
```

2026-10-18 1,715 → 2026-10-25 1,715（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 mid · 依据 README sha `cd5fbab3aa80` · [字段定义](../../DATASET.md)*
