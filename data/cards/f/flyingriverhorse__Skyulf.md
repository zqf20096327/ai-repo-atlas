# flyingriverhorse/Skyulf

⭐ 47 · Python · AGPL-3.0 · 推送 2026-10-27 · [GitHub](https://github.com/flyingriverhorse/Skyulf) · [官网](https://www.skyulf.com/) · 个人维护

**自托管可视化 MLOps 平台：从数据到训练、部署与漂移监控**

由两部分组成：Kayra 自托管 Web 应用（上传数据、画布式构建流水线、后台训练调参、模型注册与 REST 服务、漂移监控）与 skyulf-core Python 库（Apache 2.0，PyPI 发布），共享同一引擎。支持 34 种模型类型（scikit-learn/XGBoost/LightGBM），训练任务经 Celery+Redis 或线程后台执行，可关闭 Celery 仅用 SQLite 单机运行。模型可导出为不含 Kayra 依赖的独立 FastAPI 服务与批处理项目，或通过 Databricks Asset Bundle 模板在 Databricks 上以 MLflow 跟踪与注册。后端/前端为 AGPL-3.0，库为 Apache-2.0 的拆分许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `viral` | AGPL-3.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 节点式画布构建预处理与建模流水线，多分支画布并行运行
- 训练完成的模型可导出为独立 FastAPI 服务与 CSV/Parquet 批处理项目
- Databricks Asset Bundle 模板覆盖训练、审批、批处理与 Model Serving，配合 MLflow
- skyulf-core 以 Python 库形式提供相同流水线与 EDA 能力，可选 extras 安装

## 适用场景

- 在自己服务器上完成数据探索、训练到部署监控的完整流程
- 把训练好的模型导出为脱离平台独立运行的 API 服务
- 在 Databricks 上以 MLflow 跟踪并注册同一套流水线模型

## 场景标签

`MLOps` · 领域:训练与推理

## 证据(README 行号)

> L29: Skyulf has two parts that share one engine:
> L31: - **Kayra** — a self-hosted web application. Upload data, explore it, build a pipeline on a
> L34: - **`skyulf-core`** — the standalone Python library behind Kayra (Apache 2.0, on PyPI). Use the
> L52: |**Registry & serving**|Versioned model registry. Promote a version and it is served behind a REST endpoint; the fu

## 星数曲线

```mermaid
xychart-beta
    title "flyingriverhorse/Skyulf 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 46 --> 48
    line [47, 47]
```

2026-10-18 47 → 2026-10-31 47（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `6c18eac11024` · [字段定义](../../DATASET.md)*
