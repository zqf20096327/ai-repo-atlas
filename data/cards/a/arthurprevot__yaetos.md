# arthurprevot/yaetos

⭐ 36 · Python · Apache-2.0 · 推送 2026-03-31 · [GitHub](https://github.com/arthurprevot/yaetos) · 个人维护

**基于 Pandas/Spark 的数据管道框架，可本地或 AWS 运行**

用 SQL、Python（Pandas/Spark）编写 ETL 与数据管道并部署到 AWS（S3 数据集、EMR 集群）的框架，同名 pip 包 yaetos 提供 CLI（setup/run_dockerized/launch_docker_jupyter）。支持跨作业依赖、增量作业与幂等、按需自动创建并回收 EMR 集群、py.test 单元测试；同一作业本地与云端无改动运行，Docker 环境内置 python 和 spark。SQL-only 管道面向 BI 用户，Python 管道可接入任意机器学习库。

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

- 同一作业本地与 AWS EMR 集群无改动运行，集群按需创建并自动回收
- 支持作业间依赖与增量作业（含幂等）
- 简单场景纯 SQL 文件即可，复杂场景可接入 Pandas/Spark/RDD 与任意 Python 库
- 按参数在 Spark、DuckDB+Pandas、Pandas 间切换执行引擎

## 适用场景

- 编写 SQL/Python ETL 管道并部署到 AWS EMR 运行
- 在 Jupyter 中探索和开发管道，单元测试业务逻辑
- 用 Panel 在 notebook 中定义并发布仪表盘
- 构建拉取外部数据、微调小模型并推理的数据管道

## 场景标签

 · 领域:数据工程/ETL

## 证据(README 行号)

> L9: Yaetos is a framework to write data pipelines on top of Pandas and Spark, and deploy them to Amazon Web Services (AW
> L11:  - In more complex cases, pipelines consist of python files, giving access to Pandas, Spark dataframes, RDDs and an
> L29:  * The ability to integrate any python library in the process (ex: machine learning libraries).

## 星数曲线

```mermaid
xychart-beta
    title "arthurprevot/yaetos 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 35 --> 37
    line [36, 36]
```

2026-10-18 36 → 2026-10-26 36（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `5416908a67c9` · [字段定义](../../DATASET.md)*
