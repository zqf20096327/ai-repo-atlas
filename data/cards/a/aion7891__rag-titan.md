# aion7891/rag-titan

⭐ 3 · Python · MIT · 推送 2026-11-22 · [GitHub](https://github.com/aion7891/rag-titan) · [官网](https://aion7891.github.io/rag-titan/) · 个人维护

**统一 Python API 的多类型 RAG 库，可本地运行**

以 Python 库和 CLI 形式提供的 RAG 工具包：提供 7 种 RAG 类型（simple/adaptive/parent_child/hyde/rag_fusion/corrective/iterative），8 种分块器，支持 SQLite/Chroma/Qdrant 向量存储，混合检索融合向量与 BM25。默认经 Ollama 本地运行，也可用 ANTHROPIC_API_KEY 接入 Claude。附带端到端评估（recall/MRR/nDCG）与对任意 RAG 管线的分阶段诊断（70+ 指标、无 LLM judge）。需要 Python 3.10+ 与 Ollama。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 7 种 RAG 类型，一个 rag_type 参数切换
- 混合检索（RRF 融合向量与 BM25）
- 对任意 RAG 系统的分阶段评估与根因定位（无 LLM judge）
- 浏览器内 RAG playground（Pyodide）可视化每一步

## 适用场景

- 对本地文档做带引用的问答
- 比较不同分块器与 RAG 类型在自己问题集上的效果
- 诊断已有 RAG 管线中失败的具体阶段

## 场景标签

`RAG` `模型评测` · 领域:评测与运维

## 证据(README 行号)

> L19: - **Many RAG types, one API.** Two today (`simple`, `adaptive`), with more on the way. Switch with one word: `rag_t
> L28: - **Find the stage that fails, in any RAG system.** Pass the logged outputs of your pipeline (rag-titan or not) and


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-23 · 置信度 high · 依据 README sha `e955c0664cf1` · [字段定义](../../DATASET.md)*
