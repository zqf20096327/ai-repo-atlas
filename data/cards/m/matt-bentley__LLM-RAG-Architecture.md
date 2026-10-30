# matt-bentley/LLM-RAG-Architecture

⭐ 81 · C# · MIT · 推送 2026-01-12 · [GitHub](https://github.com/matt-bentley/LLM-RAG-Architecture) · 个人维护

**给开发者的 .NET 生产级 RAG 文档问答参考架构**

基于 .NET 10 控制台应用与 Semantic Kernel 编排的完整 RAG 方案：PDF 多策略抽取与分块、BAAI/bge-small-en-v1.5 稠密向量与 BM25 稀疏向量混合检索（RRF 融合）、bge-reranker-base 交叉编码器重排、相邻块补全上下文，最终由 LLM 生成带引用的回答。向量库使用 Qdrant，LLM 支持 Azure OpenAI、OpenAI 或本地 Ollama。通过 Docker Compose 一键拉起 Qdrant、嵌入、重排与 Ollama 服务，内置 Kubernetes 文档作为示例语料，面向构建企业文档搜索问答系统的开发者。

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

- 稠密向量 + BM25 稀疏向量混合检索并用 RRF 融合
- 交叉编码器重排与相邻块上下文补全
- Docker Compose 一键拉起 Qdrant/嵌入/重排/Ollama 全套服务
- LLM 可切换 Azure OpenAI、OpenAI 或本地 Ollama（默认 llama3.2:3b）

## 适用场景

- 搭建企业内部文档的检索问答系统
- 学习生产级混合检索 RAG 管线的完整实现
- 对比云端（Azure OpenAI）与本地（Ollama）LLM 的 RAG 部署方式

## 场景标签

`RAG` `文档问答` · 领域:知识与检索

## 证据(README 行号)

> L3: Production-grade Retrieval-Augmented Generation (RAG) architecture demonstrating best practices for building AI-powe
> L16: - **Interactive Chat**: Console-based assistant with Semantic Kernel function calling
> L59: Performs hybrid retrieval by combining dense vector semantic search with BM25 sparse vector keyword search, fusing 

## 星数曲线

```mermaid
xychart-beta
    title "matt-bentley/LLM-RAG-Architecture 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 80 --> 82
    line [81, 81]
```

2026-10-18 81 → 2026-10-30 81（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `c9946fca635e` · [字段定义](../../DATASET.md)*
