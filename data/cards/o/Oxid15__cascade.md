# Oxid15/cascade

⭐ 21 · Python · Apache-2.0 · 推送 2026-10-17 · [GitHub](https://github.com/Oxid15/cascade) · [官网](https://oxid15.github.io/cascade/en/latest) · 个人维护

**本地优先的轻量 MLOps 库：用 Python 与文件系统跟踪实验/数据/模型**

面向不需要 MLOps 平台的小型项目，以 Python 库形式提供本地实验跟踪：无需跟踪服务器、云账号或复杂基础设施，直接用文件系统记录实验、数据集、模型与工件。核心机制包括 Datasets 包装器跟踪数据变换与血缘、Repo/Line 结构化保存与恢复模型及元数据、配置管理与实验结果查询；另提供独立 UI 包以本地仪表盘查看实验。附 Recipes 项目模板，文档含从 Aim/MLflow/W&B/ClearML 的迁移说明。

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

- 无跟踪服务器/云账号，文件系统本地跟踪实验、数据与模型
- Datasets 包装器实现数据变换版本化与血缘追踪
- Repo/Line 结构化保存模型及元数据，支持结果查询
- 独立 cascade-ui 包提供本地实验仪表盘

## 适用场景

- 个人或小团队项目本地跟踪实验与模型版本
- 排查模型回退是代码还是数据集变更导致
- 把现有 MLflow/W&B/ClearML 跟踪代码迁移到本地方案

## 场景标签

`MLOps` · 领域:训练与推理

## 证据(README 行号)

> L12: Track experiments, datasets, models and artifacts locally with Python and your filesystem. No tracking server, clou
> L72: Cascade provides a rich set of ML-experiment tracking tools.

## 星数曲线

```mermaid
xychart-beta
    title "Oxid15/cascade 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 20 --> 22
    line [21, 21]
```

2026-10-18 21 → 2026-10-28 21（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `6e0435ea3fb1` · [字段定义](../../DATASET.md)*
