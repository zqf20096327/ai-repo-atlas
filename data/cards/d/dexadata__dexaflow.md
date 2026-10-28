# dexadata/dexaflow

⭐ 50 · Go · Apache-2.0 · 推送 2026-10-27 · [GitHub](https://github.com/dexadata/dexaflow) · [官网](https://dexaflow.dexadata.ai/) · 组织维护

**Go 编写的 Airflow 兼容工作流编排器，单二进制控制平面**

用 Go 重写的容器原生工作流编排器：复用未经修改的 Apache Airflow 3.3 UI 与 REST API（/api/v2），每个任务以独立 Pod（或进程）执行，DAG 编译为不可变 dag.json 加容器镜像，通过 dexaflow.yaml 声明依赖并由 CLI 自动构建镜像。面向从 Airflow 迁移的数据/ML 工程团队，提供单机 Lite 版（一键安装脚本）与 Kubernetes Pro 版（Helm，需外部 Postgres 13+/Redis 6+）。含面向 ML 的原生 map-reduce 语法（列表推导式扇出）、XCom on Redis、JWT/RBAC 多租户与 Prometheus/OpenTelemetry 观测。自述为 pre-1.0 实验阶段，Pro 版尚未认证生产可用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- Go 单二进制控制平面复用原版 Airflow UI 与 /api/v2 REST API
- pod-per-task 任务隔离，每 DAG 独立容器镜像与依赖
- ML 场景原生 map-reduce：Python 列表推导式完成扇出与归并
- Lite 一条命令单机安装（含内嵌 Postgres），Pro 经 Helm 部署到 Kubernetes

## 适用场景

- 团队想沿用 Airflow UI 与 REST API 但换掉 Python 调度层
- 在 Kubernetes 上以 pod-per-task 隔离运行 ETL/dbt/ML 训练流水线
- 超参搜索、k-fold 交叉验证等并行 ML 任务的原生 map-reduce 编排

## 场景标签

`工作流自动化` `MLOps` · 领域:效率与自动化

## 证据(README 行号)

> L128: Dexaflow is a **GitOps-first, container-native workflow orchestrator** written in Go. Each phrase carries weight:
> L162: ## Native map-reduce for ML/AI
> L164: Hyperparameter search, k-fold cross-validation, ensemble training, batch

## 星数曲线

```mermaid
xychart-beta
    title "dexadata/dexaflow 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-28"]
    y-axis "stars" 47 --> 51
    line [48, 50, 50]
```

2026-10-18 48 → 2026-10-28 50（+2）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 low · 依据 README sha `0c7c295de9cb` · [字段定义](../../DATASET.md)*
