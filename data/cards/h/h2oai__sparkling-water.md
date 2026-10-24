# h2oai/sparkling-water

⭐ 982 · Scala · Apache-2.0 · 推送 2025-11-05 · [GitHub](https://github.com/h2oai/sparkling-water) · [官网](https://docs.h2o.ai/sparkling-water/3.3/latest-stable/doc/index.html) · 组织维护

**将 H2O-3 机器学习引擎集成进 Spark 集群的库**

Sparkling Water 将 H2O-3 机器学习引擎与 Apache Spark 集成：提供 Spark 数据结构（RDD/DataFrame/Dataset）与 H2O 帧之间的互转工具、以 Spark 数据为 H2O 算法输入的 DSL、构建 ML 应用的基础组件，以及从 PySpark 直接使用的 Python 接口。以 Spark 应用库、zip 发行包和 Maven Central 多个 artifact 形式发布，支持 Spark 2.3 至 3.5 版本，有 internal/external 两种后端部署模式。面向使用 Scala/Python 的 Spark 开发者。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Spark 数据结构与 H2O-3 帧的双向转换工具
- PySparkling 提供 PySpark 内直接使用的 Python 接口
- 发布至 Maven Central 的多模块 artifact（训练/评分/REPL 等）
- 支持 Spark 2.3–3.5 与 internal/external 两种后端模式

## 适用场景

- 在 Spark 集群上运行 H2O-3 的机器学习算法
- 在 Spark 与 H2O 数据结构之间转换并构建 ML 应用
- 通过 PySpark 使用 H2O-3 功能

## 场景标签

 · 领域:机器学习/大数据集成

## 证据(README 行号)

> L5: Sparkling Water integrates `H2O-3 <https://github.com/h2oai/h2o-3/>`__, a fast scalable machine learning engine with
> L42: Sparkling Water is distributed as a Spark application library which can be used by any Spark application.

## 星数曲线

```mermaid
xychart-beta
    title "h2oai/sparkling-water 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 981 --> 983
    line [982, 982]
```

2026-10-18 982 → 2026-10-24 982（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `af5387cec4ba` · [字段定义](../../DATASET.md)*
