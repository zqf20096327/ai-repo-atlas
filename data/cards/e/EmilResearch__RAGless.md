# EmilResearch/RAGless

⭐ 19 · Python · MIT · 推送 2026-08-14 · [GitHub](https://github.com/EmilResearch/RAGless) · 个人维护

**面向文档问答的检索式 QA 系统：运行时零 LLM 调用**

由三个脚本组成的三段式流水线：prepare_data.py 在准备阶段用 Gemini（经 LiteLLM 调用，JSON 模式）从 .pdf/.txt/.md 源文档抽取自包含 Q&A 块（可选 --judge 二次 LLM 校验），ingest_to_qdrant.py 用非对称 Gemini 嵌入写入本地嵌入式 Qdrant 向量库（无需 Docker/服务器），chatbot.py 提供 CLI 问答，运行时纯向量检索。核心机制是 answer_id 聚合：同一答案的多个问题变体得分求和，配合双阈值判定。限制：无法合成新答案，覆盖范围受抽取阶段约束，更新需重跑全流程。AGPLv3 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 运行时零 LLM 调用，纯向量检索返回预生成答案
- answer_id 聚合：多问题变体得分求和提升 Q-Q 匹配稳定性
- 嵌入式 Qdrant 本地存储，无需 Docker 服务器
- 可选 --judge 二次 LLM 校验与确定性 UUID5 幂等入库

## 适用场景

- 为产品文档/FAQ 搭建确定性问答，运行时无 API 成本
- 需要可审计答案（含 source_quote 出处）的高风险领域问答
- 在低配 CPU 硬件上本地运行文档问答，数据不出机器

## 场景标签

`文档问答` `语义搜索` · 领域:知识与检索

## 证据(README 行号)

> L3: **RAGless** is a retrieval-only question-answering system with **zero LLM calls at runtime**.
> L18: |`prepare_data.py`|Extracts Q&A blocks from source documents using Gemini in JSON mode|
> L20: |`chatbot.py`|CLI chatbot that retrieves the most relevant answers for a user query|

## 星数曲线

```mermaid
xychart-beta
    title "EmilResearch/RAGless 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 18 --> 20
    line [19, 19]
```

2026-10-18 19 → 2026-10-29 19（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `aeb1e7b0c928` · [字段定义](../../DATASET.md)*
