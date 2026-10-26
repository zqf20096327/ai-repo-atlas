# FareedKhan-dev/rag-cookbook-2026

⭐ 30 · Jupyter Notebook · Apache-2.0 · 推送 2026-05-29 · [GitHub](https://github.com/FareedKhan-dev/rag-cookbook-2026) · [官网](https://fareedkhan-dev.github.io/rag-cookbook-2026/) · 个人维护

**40 章生产级 RAG 实战食谱集：含理论与评测的可运行教程**

面向 RAG 开发者的教学型代码食谱书：40 个自包含章节覆盖分块、查询变换、混合检索、重排、agentic 检索、图索引、多模态与评测（RAGAS/DeepEval/Phoenix 追踪）。默认运行于 Nebius AI Studio，可经单一环境变量切换到 OpenAI、Anthropic、Groq 等任意 OpenAI 兼容提供商；技术栈含 LiteLLM 抽象层、Qdrant 向量库（LanceDB/Chroma 亦封装）、LangGraph/DSPy。每章遵循六段结构（原理/搭建/构建/运行/讨论/评测），附四个公共领域语料库与可复现抓取脚本，Apache-2.0 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 40 个端到端可运行的 RAG 食谱，每章含评测 harness（RAGAS/DeepEval）
- 提供商可切换：Nebius AI Studio 默认，环境变量切换 OpenAI/Anthropic/Groq/OpenRouter/Together
- 覆盖 late chunking、contextual retrieval、ColBERT 晚交互、speculative RAG、GraphRAG、ColPali 等技术
- 四个公共语料库与 uv run fetch_corpus.py 可复现抓取

## 适用场景

- 系统学习并动手实践 2026 年生产级 RAG 技术全貌
- 为现有 RAG 系统选型嵌入模型与重排器（配对比较食谱）
- 为 RAG 流水线搭建评测与追踪（RAGAS/DeepEval/Phoenix）

## 场景标签

`RAG` `教程课程` `模型评测` · 领域:评测与运维

## 证据(README 行号)

> L3: > Recipes for production-grade retrieval — forty hands-on chapters covering the state of the art in retrieval-augmen
> L11: This cookbook teaches all of it. Forty self-contained recipes. Every recipe ships with theory, implementation, outp

## 星数曲线

```mermaid
xychart-beta
    title "FareedKhan-dev/rag-cookbook-2026 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 29 --> 31
    line [30, 30]
```

2026-10-18 30 → 2026-10-26 30（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `da0d815f1c92` · [字段定义](../../DATASET.md)*
