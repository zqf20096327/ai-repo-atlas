# dukesun99/Corpus2Skill

⭐ 96 · Python · MIT · 推送 2026-09-06 · [GitHub](https://github.com/dukesun99/Corpus2Skill) · [官网](https://arxiv.org/abs/2604.14572) · 个人维护

**把文档语料编译为可导航技能树供 LLM agent 查询**

EMNLP 2026 Findings 论文的官方实现：在编译期将 .txt/.md/.json/.jsonl 文档经嵌入、层次聚类与 LLM 摘要标注，生成 Anthropic Skills 格式的技能树（SKILL.md/INDEX.md）及 documents.json 全文库；服务期由 LLM agent 沿层级导航定位文档 ID 并经 get_document 工具取全文，不依赖向量库、检索索引或 BM25。面向做企业知识 QA/RAG 的研究者与开发者，编译与服务均需 Anthropic API key，评估套件含 Token F1、BLEU、ROUGE、BERTScore 与 LLM 裁决指标。当前为 v0.1 初始版本。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 编译期嵌入+层次聚类+LLM 摘要，产出可导航技能树
- 服务期仅层级导航与文档 ID 取回，无向量库/检索索引
- 默认 Anthropic prompt caching，附每查询 token 与成本核算
- 评估套件覆盖 BLEU/ROUGE/BERTScore 及 LLM 裁决的忠实度、幻觉率

## 适用场景

- 把企业知识库编译成 agent 可导航的技能树用于问答
- 复现论文中的 WixQA 编译-服务-评估实验
- 研究无向量检索服务的 agentic RAG 方案

## 场景标签

`RAG` · 领域:知识与检索

## 证据(README 行号)

> L11: Corpus2Skill converts a collection of documents into a structured tree of Anthropic Skills. At query time, the LLM 

## 星数曲线

```mermaid
xychart-beta
    title "dukesun99/Corpus2Skill 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-27"]
    y-axis "stars" 94 --> 97
    line [95, 96, 96]
```

2026-10-18 95 → 2026-10-27 96（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `da8fe15edc2b` · [字段定义](../../DATASET.md)*
