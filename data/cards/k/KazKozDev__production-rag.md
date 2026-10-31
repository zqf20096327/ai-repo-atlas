# KazKozDev/production-rag

⭐ 25 · Python · MIT · 推送 2025-11-04 · [GitHub](https://github.com/KazKozDev/production-rag) · 个人维护

**多策略 RAG 检索与评测框架：混合检索+重排+指标评估**

Python 实现的 RAG 检索系统库，提供 Semantic、BM25、Hybrid（RRF 融合）三种检索策略，统一 BaseRetriever 接口可互换。流水线串联查询分析→查询优化（扩展/重写/停用词/意图检测）→检索→cross-encoder 重排。配套 Evaluator 模块计算 Precision@K、Recall@K、MRR、NDCG@K、MAP 五类指标，可系统对比检索策略。依赖 Python 3.8+ 与 numpy，通过 git clone 源码运行；HNSW/ANN、DPR、多跳推理等列为未实现项。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Semantic/BM25/Hybrid（RRF）三种可互换检索策略
- 查询优化四步：扩展、重写、停用词移除、意图检测
- cross-encoder 重排在 100+ 候选中精选 top-k
- 内置五类评测指标（P@K/R@K/MRR/NDCG@K/MAP）的策略对比

## 适用场景

- 为问答系统搭建混合检索并对比各策略效果
- 用标准指标评估检索器质量
- 基于可插拔流水线扩展查询优化与重排组件

## 场景标签

`RAG` `模型评测` · 领域:评测与运维

## 证据(README 行号)

> L12: A complete implementation of enterprise-grade RAG retrieval systems that:
> L83: from rag import HybridRetriever

## 星数曲线

```mermaid
xychart-beta
    title "KazKozDev/production-rag 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-26", "2026-10-31"]
    y-axis "stars" 23 --> 26
    line [24, 25, 25]
```

2026-10-18 24 → 2026-10-31 25（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `ae56fdf337b9` · [字段定义](../../DATASET.md)*
