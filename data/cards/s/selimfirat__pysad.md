# selimfirat/pysad

⭐ 322 · Python · BSD-3-Clause · 推送 2026-11-26 · [GitHub](https://github.com/selimfirat/pysad) · [官网](https://pysad.readthedocs.io/en/stable/) · 个人维护

**面向 Python 开发者的流式异常检测库：50+ 在线检测器逐点评分**

PySAD 是 Python 流式（在线）异常检测库，覆盖多元与单元数据流，每到达一个点即通过 fit_partial/score_partial 评分并学习，无需完整数据集。内置 50+ 来自已发表研究的检测器（LODA、RRCF、Half-Space Trees、xStream、DAMP、SAND、MIDAS 等）、10 个漂移监测器、conformal/极值/Gaussian 尾部三种分数校准器与阈值过滤器、逐点更新的 prequential 评估工具，以及用 `|`、`&` 组合的管道语法和 LODA 特征归因解释。提供 PyPI/conda 安装、可选 Rust 内核扩展、MCP 服务器与终端实时仪表盘，纯 NumPy/SciPy 实现、核心无需 JVM。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | BSD-3-Clause |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 50+ 在线检测器与 10 个漂移监测器，逐点 fit/score 接口
- conformal、SPOT、Gaussian 尾部三种分数校准，输出 [0,1] 概率与二值告警
- 管道组合（`|`/`&`）与 LODA.explain_partial() 特征归因
- 可与 PyOD、River、scikit-learn、CapyMoa 集成，并提供 MCP 服务器

## 适用场景

- 对传感器/日志数据流逐点做异常检测与告警
- 信用卡欺诈、入侵检测等带概念漂移的在线监测场景
- 在不加载全量数据的情况下对 ODDS/NAB 等数据集做 prequential 评估
- 通过 MCP 客户端调用检测器与解释工具

## 场景标签

`网络安全` · 领域:学习与行业

## 证据(README 行号)

> L7:  Streaming anomaly detection in Python for multivariate and univariate data streams.
> L8:  PySAD scores and learns from each point as it arrives, with calibrated alerts, drift handling, and prequential eval
> L50: Every detector learns from and scores one point at a time with `fit_partial`, `score_partial` and `fit_score_partia

## 星数曲线

```mermaid
xychart-beta
    title "selimfirat/pysad 星数(近 11 点)"
    x-axis ["2026-10-25", "2026-10-28", "2026-11-06", "2026-11-08", "2026-11-10", "2026-11-15", "2026-11-16", "2026-11-19", "2026-11-20", "2026-11-25", "2026-11-27"]
    y-axis "stars" 313 --> 323
    line [314, 315, 314, 318, 319, 320, 321, 322, 321, 322, 322]
```

2026-10-25 314 → 2026-11-27 322（+8）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-27 · 置信度 high · 依据 README sha `a669c89a5fd8` · [字段定义](../../DATASET.md)*
