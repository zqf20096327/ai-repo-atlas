# ArcadeData/arcadedb-python

⭐ 3 · Python · Apache-2.0 · 推送 2026-11-25 · [GitHub](https://github.com/ArcadeData/arcadedb-python) · [官网](https://docs.arcadedb.com/arcadedb-python/) · 组织维护

**ArcadeDB 多模型数据库的 Python 内嵌绑定库**

ArcadeDB 多模型数据库（图、文档、键值、向量、时间序列，SQL/openCypher 查询）的 Python 内嵌绑定：引擎以 GraalVM 编译的共享库或 JVM（JPype）形式直接运行在 Python 进程内，无需独立服务器与网络跳转。提供 native 与 jvm 两个包（同名导入、同一公开 API）、ACID 事务、CSV/XML/JSONL 导入、Arrow/DataFrame 列式输出、可选进程内 HTTP 服务器；状态为 beta，Python 3.11–3.14，四平台提供 wheel。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 引擎嵌入 Python 进程运行，无服务器无网络跳转
- 多模型：图/文档/键值/向量（JVector HNSW）/时间序列，SQL 与 openCypher 查询
- 两个包（native 默认 / jvm）同名导入且公开 API 相同
- 支持 to_arrow()/to_dataframe() 列式结果输出与类型标注（PEP 561）

## 适用场景

- 在脚本、notebook 或测试中直接内嵌使用多模型数据库
- 让 agent 自持数据，单进程内完成图/向量查询
- 从 CSV/XML 批量导入数据并用 SQL/openCypher 分析

## 场景标签

 · 领域:数据库/数据基础设施

## 证据(README 行号)

> L11: Python bindings for ArcadeDB, the multi-model database (graph, document, key/value, vector and time series, queried
> L66: - Graph, document, key/value, vector (JVector HNSW) and time series models; ACID transactions.
> L11: Python bindings for ArcadeDB, the multi-model database (graph, document, key/value, vector and time series, queried
> L65: - Embedded mode: the database is a directory, opened by one process at a time.


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 mid · 依据 README sha `014631f45c38` · [字段定义](../../DATASET.md)*
