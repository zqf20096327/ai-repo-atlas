# samimhamza/crag-hybrid-retriever

⭐ 5 · Python · MIT · 推送 2026-11-04 · [GitHub](https://github.com/samimhamza/crag-hybrid-retriever) · 个人维护

**给开发者的 RAG 混合检索与纠错循环 Python 库**

以 Python 库形式提供的混合检索引擎：BM25 稀疏检索与稠密向量检索双路并行，用 RRF（k=60）融合排序，再经 FlashRank 的 ONNX 交叉编码器重排；内置 CRAG 自反思循环，按 CORRECT/AMBIGUOUS/INCORRECT 评估证据充分性并迭代改写查询。附带 P@K、Recall@K、MRR、NDCG@K 评测套件。作者称源自 AI 硕士论文工程后解耦开源，全类型化（Pydantic v2），内存运行、无云绑定，MIT 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- BM25 + 稠密向量双路检索与 RRF 融合排序
- FlashRank ONNX 交叉编码器重排（含多语 ms-marco-MultiBERT-L-12）
- CRAG 自反思循环：证据分级与最多 N 轮查询改写
- 内置 Precision@K/Recall@K/MRR/NDCG@K 评测

## 适用场景

- 为问答系统构建稀疏+稠密混合检索管线
- 对检索结果做交叉编码器重排提升候选质量
- 用标准 IR 指标对检索方案做基准评测
- 接入 CRAG 循环对证据做充分性校验

## 场景标签

`RAG` `模型评测` · 领域:评测与运维

## 证据(README 行号)

> L10: > **A production-grade, domain-agnostic Python library combining Dense Vector Search, Okapi BM25 Lexical Retrieval,
> L20: `crag-hybrid-retriever` solves both challenges by fusing sparse lexical precision with dense representation, follow
> L27: - **Self-Reflective CRAG Loop:** Evaluates candidate evidence sufficiency (`CORRECT`, `AMBIGUOUS`, `INCORRECT`), id

## 星数曲线

```mermaid
xychart-beta
    title "samimhamza/crag-hybrid-retriever 星数(近 2 点)"
    x-axis ["2026-11-02", "2026-11-24"]
    y-axis "stars" 4 --> 6
    line [5, 5]
```

2026-11-02 5 → 2026-11-24 5（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-21 · 置信度 high · 依据 README sha `8867e2829704` · [字段定义](../../DATASET.md)*
