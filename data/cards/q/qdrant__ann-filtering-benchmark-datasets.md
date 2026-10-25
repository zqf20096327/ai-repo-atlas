# qdrant/ann-filtering-benchmark-datasets

⭐ 65 · Python · 推送 2026-08-08 · [GitHub](https://github.com/qdrant/ann-filtering-benchmark-datasets) · [官网](https://qdrant.tech/benchmarks/#filtered-search-benchmark) · 组织维护

**带过滤条件的向量相似检索基准数据集集合**

由 Qdrant 维护的数据集仓库，用于评测带元数据过滤的向量相似检索：受 ann-benchmarks 启发，收录 11 个数据集，涵盖 MiniLM 编码的 ArXiv 标题、CLIP 编码的 LAION 样本、EfficientNet 编码的服装图像及合成随机向量，支持 match/range/geo 三类过滤条件。每个数据集含 vectors.npy 向量矩阵、payloads.jsonl 载荷和带期望结果的测试查询，数据来源包括随机生成脚本、Kaggle 与 Colab 生成流程。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 11 个数据集，规模 10 万至 213 万向量不等
- 三类过滤条件：match、range、geo
- 统一格式：vectors.npy + payloads.jsonl + 带期望结果的 tests.jsonl
- 提供随机数据生成脚本与嵌入生成 Colab

## 适用场景

- 评测向量数据库或 ANN 库的过滤检索性能与召回
- 对比不同过滤条件类型下的检索表现
- 为过滤式向量检索研究提供可复现的测试基准

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L3: This repo contains a collection of datasets, inspired by ann-benchmarks for searching for similar vectors with addit
> L30: |description|Num vectors|dim|distance|filters|link|

## 星数曲线

```mermaid
xychart-beta
    title "qdrant/ann-filtering-benchmark-datasets 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-25"]
    y-axis "stars" 63 --> 66
    line [64, 65, 65]
```

2026-10-18 64 → 2026-10-25 65（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `ef9c45bac6e6` · [字段定义](../../DATASET.md)*
