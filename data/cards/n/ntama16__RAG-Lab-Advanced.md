# ntama16/RAG-Lab-Advanced

⭐ 3 · Python · Apache-2.0 · 推送 2026-11-06 · [GitHub](https://github.com/ntama16/RAG-Lab-Advanced) · [官网](https://ntama16.github.io/raglab-tour/) · 个人维护

**本地 RAG 实验室：逐阶段追踪从查询到带引用答案的全流程**

本地运行的进阶 RAG 实验工具：以本地 Ollama、OpenAI 兼容服务、Anthropic 或 rerank API 为模型后端，覆盖分块、HNSW/BM25 索引、查询变换、融合、重排、Corrective RAG、上下文组装、生成与接地检查等十二个可切换阶段，每阶段展示输入、输出、耗时、提示词与原始模型响应。提供对比、参数扫描、评估（Recall@k/MRR/nDCG）与预设管理，附带两个示例语料库与引导实验。单用户设计，无认证，默认仅监听 127.0.0.1；Python 3.10+ 与 C++ 编译器为必需前置。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 十二个流水线阶段全部可追踪：输入、输出、耗时、提示词与原始响应
- HNSW 与 Okapi BM25 索引，HNSW recall 与精确搜索对照显示
- Compare/Sweeps/Evaluation 实验工具与分阶段指标（Recall@k/MRR/nDCG）
- RAGLAB_MOCK=1 确定性替身模式，供测试与 UI 开发

## 适用场景

- 逐阶段调试和比较 RAG 流水线的检索与生成效果
- 扫描 chunk 大小、ef_search、融合权重等参数并绘制指标曲线
- 用黄金集评估多种索引构建方式的召回与接地性
- 在没有模型服务器时用替身模式做界面与测试开发

## 场景标签

`RAG` `模型评测` · 领域:评测与运维

## 证据(README 行号)

> L3: A local lab for advanced RAG work. Every technique runs for real against real models (local Ollama,
> L34: The navigation follows the work: **Setup** (Models) → **Build** (Corpus, Chunking, Vector space) → **Run** (Normali
> L124: - **No LangChain / LlamaIndex.** In a lab the algorithm is the thing being studied. Each technique is a short,


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 high · 依据 README sha `b30c24ba73c5` · [字段定义](../../DATASET.md)*
