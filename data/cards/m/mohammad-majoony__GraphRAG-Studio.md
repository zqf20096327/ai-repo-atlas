# mohammad-majoony/GraphRAG-Studio

⭐ 16 · Python · MIT · 推送 2026-08-17 · [GitHub](https://github.com/mohammad-majoony/GraphRAG-Studio) · 个人维护

**全栈 GraphRAG 文档问答应用：建知识图谱并对话式检索**

Django 后端加 React 前端的知识图谱增强 RAG 应用：用户导入文本文档后，系统用 spaCy 做命名实体识别、NetworkX 构建共现图谱，按贪心模块度算法聚类社区并由 LLM 生成摘要；问答走多步流水线——实体抽取与图谱邻域扩展、BM25+向量混合检索（局部/全局）、RRF 融合与 Cross-Encoder 重排（ms-marco-MiniLM-L-6-v2），最终由 LLM 基于给定上下文合成带引用的回答。前端提供聊天、力导向图可视化和社区面板，后端内置评测套件与可配置 worker 池。源码运行，需 Python 3.10+ 与 Node.js 18+。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- spaCy NER + NetworkX 构建实体共现知识图谱与社区检测
- 局部（BM25+向量）与全局（社区摘要）混合检索，RRF 融合加 Cross-Encoder 重排
- 2D 力导向图可视化与社区摘要面板
- 内置数据集准备、检索精度与生成质量的评测套件

## 适用场景

- 上传文档后以对话方式提问并获得带引用的回答
- 对文档做全局性主题提问（如主要主题）与多跳推理
- 可视化浏览文档中的实体关系与主题社区

## 场景标签

`文档问答` `知识图谱` · 领域:知识与检索

## 证据(README 行号)

> L3: **GraphRAG Studio** is a full-stack, intelligent Knowledge Graph-enhanced Retrieval-Augmented Generation (RAG) appli
> L15: 1. **Entity Extraction & Graph Expansion:** The system identifies key entities in your question. It then traverses 
> L117: 5. **Chat:** Return to the **Conversation** tab and ask questions. The system will use hybrid retrieval and graph 

## 星数曲线

```mermaid
xychart-beta
    title "mohammad-majoony/GraphRAG-Studio 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-30 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `76cfad1ddd87` · [字段定义](../../DATASET.md)*
