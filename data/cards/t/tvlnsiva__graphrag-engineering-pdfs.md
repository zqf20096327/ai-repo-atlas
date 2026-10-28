# tvlnsiva/graphrag-engineering-pdfs

⭐ 32 · Python · 推送 2026-01-03 · [GitHub](https://github.com/tvlnsiva/graphrag-engineering-pdfs) · 个人维护

**面向工程 PDF 的 GraphRAG 流水线：本体归纳与知识图谱检索**

针对大型工程技术 PDF 的 GraphRAG 流水线：抽取实体与关系，用 NetworkX 构建物化知识图，从数据归纳本体类型与层级，做社区检测并基于社区边界的检索防止语义漂移，支持 Graph+FAISS 混合检索与多种 RAG 策略评估，LLM 仅用于事实补全的改进循环，并可自动生成 DOCX/PDF 技术文档（PDF 经 LibreOffice 无头转换）。设计取向为先确定性结构后 LLM、可解释性与可复现优先于召回。运维化部分标注为进行中。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 本体归纳与类型层级从数据中学习
- 社区检测驱动的检索，防止语义漂移
- Graph + FAISS 混合检索与多策略评估
- LLM 仅用于事实补全，结构构建为确定性流程

## 适用场景

- 从工程/技术 PDF 构建可检索的知识图谱
- 评估不同 RAG 检索策略的效果
- 自动生成技术文档与事实缺口报告

## 场景标签

`知识图谱` `RAG` · 领域:知识与检索

## 证据(README 行号)

> L3: Production-grade **GraphRAG pipeline** for building, improving, evaluating, and documenting knowledge graphs over la
> L5: This repository implements a **deterministic + LLM-assisted GraphRAG system** with ontology induction, community-awa

## 星数曲线

```mermaid
xychart-beta
    title "tvlnsiva/graphrag-engineering-pdfs 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 31 --> 33
    line [32, 32]
```

2026-10-18 32 → 2026-10-28 32（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 mid · 依据 README sha `caa2aed85cf5` · [字段定义](../../DATASET.md)*
