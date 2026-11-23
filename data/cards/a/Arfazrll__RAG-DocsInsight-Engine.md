# Arfazrll/RAG-DocsInsight-Engine

⭐ 10 · CSS · MIT · 推送 2026-04-30 · [GitHub](https://github.com/Arfazrll/RAG-DocsInsight-Engine) · [官网](https://docsinsight-ten.vercel.app) · 个人维护

**本地 RAG 平台：上传文档并用本地 LLM 问答**

基于 Flask + LangChain 的私有化 RAG 平台，支持上传 PDF/DOCX/XLSX/CSV/TXT 文档，经 ChromaDB 向量化存储后通过本地 LLM（Ollama 运行 Llama 3 8B）进行检索问答，每个回答附带文档引用以标注出处。数据全程本地执行，不上传外部服务。通过 Docker Compose 一键部署，前端为深色主题 Web 界面，分块参数为 1000 字符/200 重叠。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 多格式文档处理：PDF、DOCX、XLSX、CSV、TXT
- 基于 ChromaDB 的向量相似度检索
- 全本地执行（Ollama + Llama 3 8B），数据不出本地基础设施
- 回答附带来源引用；按文件哈希过滤支持多文档并存

## 适用场景

- 本地私有环境下对业务文档做问答与摘要
- 上传多格式文档并检索其中的关键信息
- 需要回答可溯源到原始文档的场景

## 场景标签

`RAG` `文档问答` · 领域:知识与检索

## 证据(README 行号)

> L9: **DocsInsight Engine** is a high-performance, private Retrieval-Augmented Generation (RAG) platform. It allows users
> L26: - **LLM/Embeddings**: Llama 3 (8B) via Ollama.

## 星数曲线

```mermaid
xychart-beta
    title "Arfazrll/RAG-DocsInsight-Engine 星数(近 2 点)"
    x-axis ["2026-10-21", "2026-11-23"]
    y-axis "stars" 9 --> 11
    line [10, 10]
```

2026-10-21 10 → 2026-11-23 10（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-20 · 置信度 high · 依据 README sha `25362276839c` · [字段定义](../../DATASET.md)*
