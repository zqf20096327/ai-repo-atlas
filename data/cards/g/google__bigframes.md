# google/bigframes

⭐ 297 · Python · NOASSERTION · 推送 2026-10-20 · [GitHub](https://github.com/google/bigframes) · [官网](https://dataframes.bigquery.dev/) · 组织维护

**给数据分析师/科学家：用 pandas 风格 API 在 BigQuery 上做大规模分析与 ML**

Google 开源的 Python DataFrame 库，将 pandas 风格代码转译为 SQL 在 BigQuery 分布式引擎上执行，避免本地拉取大数据。提供 pandas 兼容分析 API、scikit-learn 风格的 bigframes.ml，以及 bigframes.bigquery.ai 模块（由 Gemini 驱动的文本生成、向量嵌入、语义搜索、多模态处理）。使用需 Google Cloud 项目与 Application Default Credentials；GA 状态，Apache-2.0 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- pandas API 兼容，改少量 import 即可迁移工作负载
- bigframes.ml 提供 scikit-learn 风格 ML API
- bigframes.bigquery.ai 提供 Gemini 驱动的文本生成、向量嵌入与语义搜索
- 支持 partial ordering 模式与 to_pandas()/read_pandas() 混合本地/分布式处理

## 适用场景

- 在超本地内存的数据集上用熟悉的 pandas 操作做分析
- 通过 DataFrame 接口调用 Gemini 做文本生成与语义搜索
- 在企业 BigQuery 安全边界内完成分析与 ML 流程

## 场景标签

`数据分析` `语义搜索` · 领域:效率与自动化

## 证据(README 行号)

> L5: BigQuery DataFrames (also known as BigFrames) provides a Pythonic DataFrame
> L6: and machine learning (ML) API powered by the BigQuery engine. It provides modules
> L12: * `bigframes.bigquery.ai <https://dataframes.bigquery.dev/reference/api/bigframes.bigquery.ai.html>`_
> L13:  provides powerful AI functions, text generation, vector embeddings, and semantic search powered by Gemini.

## 星数曲线

```mermaid
xychart-beta
    title "google/bigframes 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-22"]
    y-axis "stars" 296 --> 298
    line [297, 297]
```

2026-10-18 297 → 2026-10-22 297（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `6833f26bbec7` · [字段定义](../../DATASET.md)*
