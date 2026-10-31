# BusySloths/mlox

⭐ 14 · Python · MIT · 推送 2026-10-30 · [GitHub](https://github.com/BusySloths/mlox) · [官网](https://busysloths.github.io/mlox/) · 组织维护

**自有服务器上部署管理 ML/AI 基础设施的一体化工具**

面向 solopreneur、初创与小团队的 ML/AI 基础设施管理工具：统一管理服务器，支持 Native、Docker、Kubernetes 三种执行后端，可部署 MLflow、Airflow、Milvus、LiteLLM、OpenBao 等自托管服务，集中存储 secrets 并连接服务间依赖，另可接入 BigQuery、GCP 等外部服务。提供 CLI、TUI 与 PyPI 包（busysloths-mlox），核心为配置驱动、状态可检查的 ProjectWorkspace API；项目存储加密，Streamlit Web UI 已弃用。项目已被 CAIN 2026 接收。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- Native、Docker、Kubernetes 统一执行后端
- 内置 MLflow/Airflow/Milvus/LiteLLM/OpenBao 等自托管服务目录
- 加密项目存储与集中 secrets 管理
- 提供 CLI、TUI 与 Python SDK（busysloths-mlox）

## 适用场景

- 在自己的服务器上统一部署和管理 ML 服务与数据库
- 小团队不自行拼装基础设施，直接部署配套服务并接入依赖
- 通过 CLI/TUI 管理多台服务器与单/多节点集群

## 场景标签

`MLOps` · 领域:训练与推理

## 证据(README 行号)

> L18: MLOX brings the infrastructure around your product into one connected system. It manages servers, sets up Docker an
> L20: Use the CLI or TUI to operate the same inspectable, configuration-driven core. MLOX is built for solopreneurs, star

## 星数曲线

```mermaid
xychart-beta
    title "BusySloths/mlox 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `88aba7cc9006` · [字段定义](../../DATASET.md)*
