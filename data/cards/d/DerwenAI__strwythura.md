# DerwenAI/strwythura

⭐ 233 · Python · MIT · 推送 2026-04-15 · [GitHub](https://github.com/DerwenAI/strwythura) · [官网](https://blog.derwen.ai/strwythura-2a8007af3682?source=friends_link&sk=93eb7dcce1f48206162e1f69a0f57661) · 组织维护

**教程与 Python 库：从结构化/非结构化来源构建实体消解知识图谱**

面向数据科学家与 ML/数据/MLOps 工程师的教程，同时打包为 Python 库：用 Senzing 做实体消解合并结构化数据集，结合 SKOS 领域分类构建 RDF 语义层，再以 spaCy/GLiNER 抽取非结构化内容的实体与关系，经人工在环（HITL）策展后生成 NetworkX 属性图与 LanceDB 向量存储，最终产出带 MLOps 观测（Opik）的 Streamlit GraphRAG 问答应用。默认本地运行（Ollama + gemma3:12b），可切换远程 LLM 服务；示例领域为一项饮食与痴呆研究，替换数据源与领域分类即可换域。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Senzing 实体消解合并多数据集生成图骨架
- RDF 语义层 + NetworkX 属性图构成实体消解知识图谱
- GLiNER 零样本 NER 抽取实体与关系，支持 HITL 策展
- 默认本地运行（Ollama/gemma3:12b），可在离线环境运行

## 适用场景

- 为特定领域构建实体消解知识图谱与 GraphRAG 问答应用
- 学习实体消解、本体流水线与上下文工程的技术组合
- 在离线/本地环境运行带 MLOps 观测的知识图谱管线

## 场景标签

`知识图谱` `RAG` `教程课程` · 领域:知识与检索

## 证据(README 行号)

> L9: This tutorial explains how to construct an *entity resolved knowledge graph*
> L16: The material here provides hands-on experience with advanced
> L113: The code is written primarily as a tutorial, although it is also

## 星数曲线

```mermaid
xychart-beta
    title "DerwenAI/strwythura 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 232 --> 234
    line [233, 233]
```

2026-10-18 233 → 2026-10-29 233（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `8483bca4778e` · [字段定义](../../DATASET.md)*
