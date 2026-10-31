# erendikmenn/jev-rag-benchmark

⭐ 20 · Python · MIT · 推送 2026-10-29 · [GitHub](https://github.com/erendikmenn/jev-rag-benchmark) · 个人维护

**测量 Jev 重排在 RAG 中质量、延迟与成本的可复现基准**

面向 RAG 系统构建者的可复现评测项目：在 1,044 个土耳其语 XQuAD 问题上，对比 BM25、混合检索（BM25+bge-m3）、Jev 1.13 与 Cohere Rerank 3.5 的候选召回、Recall@5/nDCG@10、延迟与成本，并在冻结上下文下对比 Gemini 与 DeepSeek 生成器的端到端表现。模型与嵌入调用走 OpenRouter，不使用本地模型；附带 Jev 策略消融（逐点、集成、全语料分层等）。基于 LlamaIndex 的 MIT 许可示例应用改造，用 uv 管理运行，提供 CLI 与 FastAPI 接口；限制包括土耳其语结果不可外推、候选顺序影响 Jev 分数。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 1,044 个 XQuAD-TR 问题上对 Jev/Cohere/无重排的锁定候选对比，报告 Recall@5、nDCG@10、MRR@10 与成本
- 冻结上下文下 Gemini 与 DeepSeek 生成器的成对比较（含自助法置信区间）
- Jev 策略消融：逐点、3 序集成、多信号证据路由、全语料分层、引用验证
- 每次运行写出含 commit、依赖版本、数据集哈希、种子与提示版本的 JSONL/CSV/manifest

## 适用场景

- 评估是否在 RAG 流水线中引入 Jev 重排及其成本权衡
- 复现或审计检索-重排-生成各阶段的分离测量
- 比较不同重排器与生成器在同一冻结候选集上的表现

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L3: Reproducible, vendor-neutral experiments for measuring whether TypeSafe Jev improves a
> L37: Generation is disabled here, so the table isolates passage selection. All three rows use
> L104: - **Best measured quality/cost:** hybrid full-depth top-20 -> Jev batch top-5 -> DeepSeek

## 星数曲线

```mermaid
xychart-beta
    title "erendikmenn/jev-rag-benchmark 星数(近 4 点)"
    x-axis ["2026-10-18", "2026-10-24", "2026-10-30", "2026-10-31"]
    y-axis "stars" 17 --> 21
    line [18, 19, 20, 20]
```

2026-10-18 18 → 2026-10-31 20（+2）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `475e43f9a003` · [字段定义](../../DATASET.md)*
