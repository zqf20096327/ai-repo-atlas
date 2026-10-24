# ekimetrics/adaptive-chunking

⭐ 397 · Python · MIT · 推送 2026-07-06 · [GitHub](https://github.com/ekimetrics/adaptive-chunking) · 组织维护

**为 RAG 逐文档自动选出最优分块策略的库（LREC 2026 论文实现）**

论文《Adaptive Chunking: Optimizing Chunking-Method Selection for RAG》（LREC 2026）的官方实现。核心机制：对每份文档并行评估多种分块方法（递归切分、按页切分、LLM regex 等），用 5 项无需 ground-truth 的内在质量指标（尺寸合规、块内凝聚、上下文连贯、结构块完整、指代链断裂）打分并自动选最优策略。方法与指标均可注册自定义。提供 3 种 PDF 解析后端（Docling 默认/PyMuPDF/Azure）与 Excel 支持，附带论文复现流程（含 CLAIR 语料 33 篇文档与 RAG 评测）。面向 RAG 管线开发者与研究者，Python 3.11+。部分指标需下载 spaCy 模型，复现 RAG 评测需 OpenAI API 调用与 GPU。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 按文档自动选择分块策略：多方法 × 5 项内在质量指标打分
- 方法与指标均模块化，可注册自定义切分器与打分函数
- 3 种 PDF 解析后端（Docling/PyMuPDF/Azure）+ Excel 支持
- 附带 CLAIR 语料与完整论文复现脚本（表 1–5）

## 适用场景

- RAG 管线中为不同类型文档自动选分块策略
- 研究者复现或扩展分块质量评估指标
- 技术/法律/可持续报告等多领域文档的分块评测

## 场景标签

`RAG` · 领域:知识与检索

## 证据(README 行号)

> L12: > **Official implementation** of *"Adaptive Chunking: Optimizing Chunking-Method Selection for RAG"*, accepted at *
> L18: No single chunking method works best for every document in a RAG pipeline. **Adaptive Chunking** solves this by eva
> L72: - **RAG evaluation pipeline** — hybrid retrieval with custom retrieval completeness metric and answer correctness s

## 星数曲线

```mermaid
xychart-beta
    title "ekimetrics/adaptive-chunking 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-24"]
    y-axis "stars" 395 --> 398
    line [396, 397, 397]
```

2026-10-18 396 → 2026-10-24 397（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `af8e46024b5b` · [字段定义](../../DATASET.md)*
