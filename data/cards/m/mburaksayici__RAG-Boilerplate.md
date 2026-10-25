# mburaksayici/RAG-Boilerplate

⭐ 80 · Python · 推送 2025-11-18 · [GitHub](https://github.com/mburaksayici/RAG-Boilerplate) · 个人维护

**面向开发者的 RAG 系统脚手架：检索增强问答全流程模板**

提供完整 RAG 流水线的样板工程：命题模型+后期分块的切块策略、基于 Qdrant 的混合检索（BM25+稠密）、LLM 重排与查询增强 agent、CrewAI 编排对话/检索 agent、Redis/MongoDB 会话存储、Celery 后台文档摄取、Gradio Web 界面，以及命中率/MRR 评测套件用于对比不同检索组合。通过 git clone + docker-compose 运行，附 EURLEX 法律文档数据预处理脚本。README 同时记录了大量技术选型说明（向量库、嵌入模型、技术栈替代方案）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 命题模型+后期分块与递归重叠切块的切块管线
- Qdrant 混合检索（BM25+稠密）+ LLM 重排 + 查询增强 agent
- Celery 后台摄取管道与 Redis/MongoDB 会话分层存储
- Hit-Rate/MRR 评测套件，可对比有无重排/查询增强的检索组合

## 适用场景

- 作为起点快速搭建可与自有数据对话的问答系统
- 实验不同检索组合（重排器/查询增强）并评测效果
- 学习 RAG 系统的工程结构与组件选型

## 场景标签

`RAG` · 领域:知识与检索

## 证据(README 行号)

> L9: A RAG system that is :
> L11: - Chunking with propositional model + late chunking, and simple recursive overlap retrieval
> L12: - Using Qdrant as a Vector DB, utilising its hybrid search (BM25 + Dense Search)

## 星数曲线

```mermaid
xychart-beta
    title "mburaksayici/RAG-Boilerplate 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 79 --> 81
    line [80, 80]
```

2026-10-18 80 → 2026-10-25 80（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 mid · 依据 README sha `fdb36c3d8ce0` · [字段定义](../../DATASET.md)*
