# VectorInstitute/retrieval-augmented-generation

⭐ 38 · Jupyter Notebook · Apache-2.0 · 推送 2026-10-27 · [GitHub](https://github.com/VectorInstitute/retrieval-augmented-generation) · 组织维护

**RAG 训练营参考实现集合：笔记本演示 RAG 各环节方法**

Vector Institute RAG Bootcamp（2024.11–2025.01）的参考实现合集，以 Jupyter 笔记本演示 RAG 常用方法：数据摄取、分块、嵌入、向量数据库、稀疏/稠密检索、重排序，基于 LangChain 与 LlamaIndex。包含 Web 搜索、文档搜索、SQL 搜索、AWS S3 云数据检索、PubMed QA 全流程（含评测指标）与基于 Ragas 的 RAG 评测等示例。要求 Python 3.10+，支持 uv 环境、Docker 与 Google Colab 运行，需配置 .env 环境变量。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 6 类参考实现：Web/文档/SQL/云数据检索、PubMed QA、RAG 评测
- 覆盖摄取、分块、嵌入、向量库、稀疏/稠密检索、重排序流程
- 基于 LangChain 与 LlamaIndex 库构建
- 提供 Docker 与 Google Colab 两种运行方式

## 适用场景

- 学习 RAG 各环节方法的可运行示例
- 参加 RAG 训练营并本地复现笔记本
- 了解 RAG 评测（Ragas 测试集）的做法

## 场景标签

`RAG` `教程课程` · 领域:知识与检索

## 证据(README 行号)

> L3: This is a collection of reference implementations for Vector Institute's **RAG (Retrieval-Augmented Generation) Boot
> L13: - **PubMed QA**: A full pipeline on the PubMed dataset demonstrating ingestion, embeddings, vector index/storage, r

## 星数曲线

```mermaid
xychart-beta
    title "VectorInstitute/retrieval-augmented-generation 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 37 --> 39
    line [38, 38]
```

2026-10-18 38 → 2026-10-29 38（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `4c6008254d2b` · [字段定义](../../DATASET.md)*
