# kedro-org/kedro

⭐ 11,064 · Python · NOASSERTION · 推送 2026-11-27 · [GitHub](https://github.com/kedro-org/kedro) · [官网](https://kedro.org) · 组织维护

**数据工程与数据科学流水线的工程化 Python 框架**

面向生产级数据工程与数据科学流水线的开源 Python 框架，由 LF AI & Data Foundation 托管。提供基于 Cookiecutter Data Science 的项目模板、跨本地/网络文件系统与云对象存储的 Data Catalog（含数据与模型版本控制）、纯 Python 函数间依赖的自动解析与 Kedro-Viz 可视化，以及 pytest/ruff/Sphinx 等工程规范集成；部署支持单机或分布式，并提供 Argo、Prefect、Kubeflow、AWS Batch、Databricks 的部署支持。通过 PyPI 或 conda 安装，要求 CPython 官方维护中的 Python 版本。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Data Catalog 支持多文件格式/文件系统的数据读写与版本控制
- Pipeline Abstraction 自动解析函数依赖并支持 Kedro-Viz 可视化
- 部署支持 Argo/Prefect/Kubeflow/AWS Batch/Databricks
- LF AI & Data Foundation 托管的开源 Python 框架

## 适用场景

- 把 notebook 和一次性脚本重构为可复现的模块化流水线
- 团队协作时统一数据科学项目的工程规范
- 构建的 ML 流水线需部署到 Kubeflow/AWS Batch 等平台
- 需要数据与模型版本管理的文件型数据管道

## 场景标签

`MLOps` · 领域:训练与推理

## 证据(README 行号)

> L20: Kedro is a toolbox for production-ready data engineering and data science pipelines. It uses software engineering b
> L22: Kedro is an open-source Python framework hosted by the LF AI & Data Foundation.
> L54: |Pipeline Abstraction|Automatic resolution of dependencies between pure Python functions and data pipeline visualis

## 星数曲线

```mermaid
xychart-beta
    title "kedro-org/kedro 星数(近 20 点)"
    x-axis ["2026-10-26", "2026-10-27", "2026-10-28", "2026-10-30", "2026-10-31", "2026-11-02", "2026-11-06", "2026-11-08", "2026-11-10", "2026-11-11", "2026-11-14", "2026-11-15", "2026-11-18", "2026-11-19", "2026-11-20", "2026-11-22", "2026-11-25", "2026-11-26", "2026-11-27", "2026-11-28"]
    y-axis "stars" 11030 --> 11067
    line [11034, 11035, 11036, 11037, 11038, 11040, 11033, 11047, 11050, 11052, 11051, 11052, 11054, 11056, 11057, 11059, 11060, 11062, 11064, 11064]
```

2026-10-26 11,034 → 2026-11-28 11,064（+30）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 high · 依据 README sha `563a4f99a49d` · [字段定义](../../DATASET.md)*
