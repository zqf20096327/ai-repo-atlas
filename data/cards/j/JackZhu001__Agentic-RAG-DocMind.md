# JackZhu001/Agentic-RAG-DocMind

⭐ 18 · Python · 推送 2025-12-29 · [GitHub](https://github.com/JackZhu001/Agentic-RAG-DocMind) · 个人维护 · 中文 README

**面向企业的 RAG 智能问答系统：混合检索+BGE重排+置信度过滤**

基于 Python 的 RAG 文档问答系统（CLI 形式）：三路混合检索（HyDE+语义重写+BM25）、BGE-M3 嵌入与 BGE-Reranker-v2-m3 重排、三级置信度过滤，LLM 通过 DeepSeek API 配置接入。内置评估体系（Recall/MRR/NDCG 与消融实验），文档以 PDF 等格式添加后交互问答。以源码方式提供，pip 安装依赖后运行 cli.py，MIT 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 三路混合检索：HyDE+语义重写+BM25
- BGE-M3 Embedding 与 BGE-Reranker-v2-m3
- 三级置信度过滤与完整评估体系（含消融实验）
- CLI 交互模式支持文档添加/知识库重置/检索日志

## 适用场景

- 对企业内部文档建知识库并做问答
- 对检索管线做评估与消融分析
- 验证混合检索与重排策略的增益

## 场景标签

`文档问答` `模型评测` · 领域:评测与运维

## 证据(README 行号)

> L1: # DocMind - 企业级 RAG 智能问答系统
> L10: - **三路混合检索**：HyDE + 语义重写 + BM25，Recall@3 达 93%+

## 星数曲线

```mermaid
xychart-beta
    title "JackZhu001/Agentic-RAG-DocMind 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 17 --> 19
    line [18, 18]
```

2026-10-18 18 → 2026-10-30 18（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `cb69f502f245` · [字段定义](../../DATASET.md)*
