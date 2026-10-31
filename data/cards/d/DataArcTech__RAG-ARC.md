# DataArcTech/RAG-ARC

⭐ 48 · Python · MIT · 推送 2026-03-04 · [GitHub](https://github.com/DataArcTech/RAG-ARC) · 组织维护 · 中文 README

**多路检索与 GraphRAG 的模块化 RAG 框架，供开发者构建知识问答系统**

Python/FastAPI 实现的 RAG 框架：覆盖文档解析（PDF/PPT/Excel，含 OCR 与 VLM 路径）、多种分块策略、HuggingFace 嵌入、BM25/FAISS 密集/Tantivy 全文三路检索与 RRF 融合、基于 Neo4j 的知识图谱构建（子图 PPR、查询感知剪枝、增量更新）、Qwen3 重排序，并提供 REST API、WebSocket 流式对话、JWT 鉴权与用户/会话管理。基于 HippoRAG2 改进。支持 Docker 四容器部署（PostgreSQL/Redis/Neo4j/应用）或本地 uv 运行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- BM25+密集+全文三路检索，RRF/加权和等可配置融合
- 基于 Neo4j 的 GraphRAG：子图 PPR、查询感知剪枝、知识图谱增量更新
- 多格式文档解析，含 OCR 与 VLM-based 识别
- REST API + WebSocket 流式对话，JWT 鉴权与文档级权限

## 适用场景

- 搭建企业或个人知识库问答系统
- 处理非结构化文档（PDF/PPT/Excel）做检索增强问答
- 需要知识图谱推理与增量更新的 GraphRAG 场景

## 场景标签

`RAG` `知识图谱` `文档解析` · 领域:知识与检索

## 证据(README 行号)

> L15: **RAG-ARC** is a modular Retrieval-Augmented Generation (RAG) framework designed to build efficient, scalable archi
> L19: 🧩 **Full RAG Pipeline Support**: Covers the complete pipeline—from document parsing, text chunking, and embedding g

## 星数曲线

```mermaid
xychart-beta
    title "DataArcTech/RAG-ARC 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 47 --> 49
    line [48, 48]
```

2026-10-18 48 → 2026-10-31 48（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `7195f4845f56` · [字段定义](../../DATASET.md)*
