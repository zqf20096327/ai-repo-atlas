# Galileo-Galilei/kedro-mlflow

⭐ 236 · Python · Apache-2.0 · 推送 2026-05-10 · [GitHub](https://github.com/Galileo-Galilei/kedro-mlflow) · [官网](https://kedro-mlflow.readthedocs.io/) · 组织维护

**Kedro 插件：在 Kedro 项目中集成 MLflow 实验追踪与模型打包**

面向使用 Kedro 框架构建机器学习流水线的开发者提供的插件：在 Kedro 运行中以少量配置自动注册参数与数据集到 MLflow Tracking，供事后在 MLflow UI 中浏览检索；并通过 pipeline_ml_factory 等 API 将 Kedro 流水线（含预处理、后处理与训练产物）转换为 MLflow 模型，可一行命令打包并以 API 形式部署。要求 kedro>=0.16.0、mlflow>=1.0.0；当前 2.0.3 版本仅兼容 mlflow 3.x。经 pip、conda-forge 与 GitHub 源码安装，遵循 SemVer。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Kedro 运行中自动注册参数与数据集到 MLflow Tracking
- 将 Kedro 流水线打包为自包含 MLflow 模型（含预处理/后处理）并可作为 API 部署
- MlflowArtifactDataset / MlflowMetricsHistoryDataset 自动记录文件与指标
- 提供 pip、conda-forge、GitHub 源码三种安装途径

## 适用场景

- 在 Kedro 项目里做实验追踪与参数/数据集版本记录
- 把 Kedro 流水线打包成 MLflow 模型用于生产部署与共享
- 通过 MLflow UI 浏览和检索历史运行

## 场景标签

`MLOps` · 领域:训练与推理

## 证据(README 行号)

> L24: ``kedro-mlflow`` is a kedro-plugin for lightweight and portable integration of mlflow capabilities inside kedro pro
> L26: - **experiment tracking**: `kedro-mlflow` intends to enhance reproducibility for machine learning experimentation. 
> L27: - **pipeline as model**: ``kedro-mlflow`` intends to be be an agnostic machine learning framework for people who wa

## 星数曲线

```mermaid
xychart-beta
    title "Galileo-Galilei/kedro-mlflow 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 235 --> 237
    line [236, 236]
```

2026-10-18 236 → 2026-10-26 236（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `5277f4ad28af` · [字段定义](../../DATASET.md)*
