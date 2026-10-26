# bodo-ai/Bodo

⭐ 383 · Python · Apache-2.0 · 推送 2026-10-24 · [GitHub](https://github.com/bodo-ai/Bodo) · [官网](https://docs.bodo.ai) · 组织维护

**面向大规模数据与 AI 工作流的 Pandas 替代型高性能 DataFrame 库**

Bodo DataFrames 是一个 Python DataFrame 库，定位为 Pandas 的 drop-in 替换：将 import pandas 改为 import bodo.pandas 即可加速和扩展工作流。机制上依赖基于 MPI 的 HPC 技术、JIT 编译器、C++ 运行时与集成 SQL 引擎，支持流式处理超内存数据集，I/O 支持 Iceberg、Snowflake、Parquet、CSV、JSON，并对 Pandas/Numpy/Scikit-learn 提供原生 JIT 支持。需 Python 3.10+，通过 pip 或 conda 安装；平台支持 Linux x86、Mac x86/ARM 与 Windows，Linux ARM 暂未支持。

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

- 单行 import 改动即可作为 Pandas 替换，未支持部分自动回退到原生 Pandas
- MPI 并行执行、C++ 运行时与 JIT 编译加速自定义变换
- 集成 SQL 引擎与流式执行，可处理超内存数据集
- I/O 支持 Iceberg、Snowflake、Parquet、CSV、JSON 并带过滤下推与列裁剪

## 适用场景

- 在笔记本或多节点集群上加速现有 Pandas 数据处理代码
- 处理超出内存的大规模数据集
- 在同一 Python 工作流中结合 SQL 查询与 DataFrame 操作
- 对 Scikit-learn 等 AI/ML 工作流做数据侧加速

## 场景标签

 · 领域:数据工程/分布式计算

## 证据(README 行号)

> L11: Bodo DataFrames is a high performance DataFrame library for large scale Python data processing, AI/ML use cases.
> L45: - Intuitive APIs for simplifying and scaling AI workloads.
> L50: - Just in time (JIT) compilation with native support for Pandas, Numpy and Scikit-learn

## 星数曲线

```mermaid
xychart-beta
    title "bodo-ai/Bodo 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 382 --> 384
    line [383, 383]
```

2026-10-18 383 → 2026-10-26 383（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `f75e5e5da989` · [字段定义](../../DATASET.md)*
