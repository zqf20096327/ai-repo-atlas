# Koldim2001/MLflow_tracking

⭐ 32 · Jupyter Notebook · 推送 2025-12-25 · [GitHub](https://github.com/Koldim2001/MLflow_tracking) · 个人维护

**用 Docker Compose 部署 MLflow 追踪服务的示例仓库**

演示如何搭建 MLflow 实验追踪服务的配置仓库：通过 docker-compose 一并启动 MLflow Tracking Server、PostgreSQL 数据库与 MinIO 对象存储，用 .env 文件配置环境变量；main 分支为第 3 种方案（含存储与数据库），local_mlflow 分支提供本地开发的最简方案（第 1 种）。仓库附带 Jupyter Notebook，分别示例 PyTorch 与 Sklearn 实验的参数、指标、模型记录，以及通过 MinIO S3 读写数据的用法。面向使用 PyTorch/Sklearn 的开发者和研究人员。

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

- docker-compose 一键启动 MLflow + PostgreSQL + MinIO
- 支持将参数、指标与模型工件保存到数据库与对象存储
- 提供 PyTorch 与 Sklearn 的追踪示例 Notebook（另有 local_mlflow 本地分支）
- 含 MinIO S3 读写示例

## 适用场景

- 为 PyTorch/Sklearn 实验搭建可持久化的 MLflow 追踪服务
- 想了解 MLflow 配合 Postgres 与 MinIO 存储后端的部署方式
- 本地开发时用最简配置跑通 MLflow 追踪

## 场景标签

`MLOps` · 领域:训练与推理

## 证据(README 行号)

> L3: MLflow - это инструмент для управления жизненным циклом машинного обучения, который предоставляет разработчикам и ис
> L14: ## Запуск MLFlow + Postgres + MinIO

## 星数曲线

```mermaid
xychart-beta
    title "Koldim2001/MLflow_tracking 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 31 --> 33
    line [32, 32]
```

2026-10-18 32 → 2026-10-27 32（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `65c8e189022f` · [字段定义](../../DATASET.md)*
