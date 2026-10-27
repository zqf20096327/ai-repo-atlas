# stateful-y/kedro-dagster

⭐ 24 · Python · Apache-2.0 · 推送 2026-10-26 · [GitHub](https://github.com/stateful-y/kedro-dagster) · [官网](https://kedro-dagster.readthedocs.io/) · 组织维护

**将 Kedro 数据科学流水线接入 Dagster 编排的插件**

面向 Kedro 用户的 Python 插件：把 Kedro 流水线对象转换为 Dagster 的 jobs/assets 定义，通过 dagster.yml 按环境集中配置执行器、调度与流水线过滤，并用 kedro dagster dev 启动 Dagster UI 监控执行。保留 Kedro hooks 在执行周期中被调用，统一两边日志，支持配合 Kedro-MLflow 与 Dagster 的 MLflow 集成做实验跟踪。分区支持标注为实验性。支持 Kedro 0.19.x/1.x 与 Dagster 1.10-1.12。

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

- kedro dagster init 自动生成 Dagster definitions.py 与 dagster.yml
- Kedro hooks 在流水线执行中被保留调用
- 统一 Kedro 与 Dagster 日志到 Dagster UI
- 与 Kedro-MLflow 及 Dagster 的 MLflow 集成配合使用

## 适用场景

- 把已有 Kedro 项目部署到 Dagster 做编排与监控
- 为 Kedro 流水线配置定时调度与执行器
- 在 Dagster UI 中追踪 Kedro 节点日志与运行状态

## 场景标签

 · 领域:数据工程/MLOps 编排

## 证据(README 行号)

> L14: The Kedro-Dagster plugin enables seamless integration between Kedro, a framework for creating reproducible and main
> L25: - **MLflow compatibility:** Use Kedro-MLflow with Dagster’s MLflow integration to track experiments, log models, an

## 星数曲线

```mermaid
xychart-beta
    title "stateful-y/kedro-dagster 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 23 --> 25
    line [24, 24]
```

2026-10-18 24 → 2026-10-27 24（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `2feb0ca62db7` · [字段定义](../../DATASET.md)*
