# qdrant/laion-400m-benchmark

⭐ 15 · Python · 推送 2026-06-23 · [GitHub](https://github.com/qdrant/laion-400m-benchmark) · 组织维护

**LAION 400M 向量数据集在 Qdrant 中的上传与检索基准评测脚本**

提供将 LAION 400M 数据集（4 亿条 512 维 CLIP 嵌入向量）分块下载并上传至 Qdrant 向量数据库的脚本，以及基于全量扫描生成的参考真值数据，用于对比检索结果与测量检索延迟。上传脚本在客户端不持久化中间数据；评测可通过 rescore_limit 参数在精度与速度间权衡。README 给出最低可用硬件配置（64Gb 内存、8 核 CPU、1Tb 磁盘），并提示启用异步 IO 可获得更好性能。面向评估向量检索系统的研究与工程人员。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 分块下载并上传 4 亿条 512 维 CLIP 向量至 Qdrant，客户端不持久化中间数据
- 附全量扫描生成的参考真值数据（expected.py）
- 评测脚本对比检索结果并测量延迟，rescore_limit 可调
- 给出最低硬件配置：64Gb 内存、8 核 CPU、1Tb 磁盘，交互检索延迟低于 1 秒

## 适用场景

- 将 LAION 400M 数据集导入 Qdrant 做大规模图像相似检索
- 评测向量检索系统的召回率与延迟表现
- 测试不同资源配置下的相似检索性能

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L3: This repository provides scripts for uploading and benchmarking the Laion 400M dataset in Qdrant.
> L7: Laion 400M dataset is a dataset of 400M vectors with 512d CLIP embeddings.
> L44: python eval.py --rescore_limit 1000

## 星数曲线

```mermaid
xychart-beta
    title "qdrant/laion-400m-benchmark 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-31 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `fcf63fd3c0c4` · [字段定义](../../DATASET.md)*
