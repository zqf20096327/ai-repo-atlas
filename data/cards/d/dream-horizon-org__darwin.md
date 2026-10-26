# dream-horizon-org/darwin

⭐ 62 · Python · MIT · 推送 2026-03-23 · [GitHub](https://github.com/dream-horizon-org/darwin) · [官网](https://darwin.dreamhorizon.org/) · 组织维护

**Dream11 的企业级端到端 ML 平台，覆盖训练到推理全生命周期**

面向生产规模 AI/ML 工作负载的统一平台，由 Dream11 组织维护。包含 11 个组件：基于 Kubernetes/Ray 的分布式计算编排（darwin-compute）、Go 编写的集群管理服务、Cassandra/Kafka 后端的低延迟特征存储（<10ms 在线取数）、模型部署服务（FastAPI/Ray Serve）、MLflow 实验跟踪、事件血缘追踪（Chronos）、数据目录、Airflow 工作流编排与统一 CLI。部署依赖 Kubernetes、Helm 3.8+、Docker、Python 3.9.7+，通过 init.sh 脚本按 Training/Inference 预设或服务粒度安装。提供 Python SDK。

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

- Ray 2.37.0 集群的创建/伸缩/自动终止与成本监控
- 特征存储：Cassandra 在线服务、Point-in-time 正确性、Kafka 实时物化
- MLflow 2.12.2 实验跟踪与自定义 FastAPI 鉴权层、模型注册
- Airflow DAG 编排 + Ray 集群自动供给的多步 ML 流水线

## 适用场景

- 数据科学家在 Ray 集群上做分布式训练并用 MLflow 跟踪实验
- ML 工程师将模型部署为多环境实时推理端点并配置自动扩缩
- 数据工程师构建 Spark 特征流水线并发布到 Kafka 实时物化
- 平台工程师通过 Helm 在 EKS 上部署并管理多租户与 RBAC

## 场景标签

`MLOps` · 领域:训练与推理

## 证据(README 行号)

> L5: **Darwin** is an enterprise-grade, end-to-end machine learning platform designed for production-scale AI/ML workload
> L12: - **Production-Grade Scalability**: Built on Kubernetes and Ray for elastic, distributed compute at scale

## 星数曲线

```mermaid
xychart-beta
    title "dream-horizon-org/darwin 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-26"]
    y-axis "stars" 60 --> 63
    line [61, 62, 62]
```

2026-10-18 61 → 2026-10-26 62（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 mid · 依据 README sha `736437ed9658` · [字段定义](../../DATASET.md)*
