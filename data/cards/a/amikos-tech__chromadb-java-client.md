# amikos-tech/chromadb-java-client

⭐ 80 · Java · MIT · 推送 2026-09-03 · [GitHub](https://github.com/amikos-tech/chromadb-java-client) · 组织维护

**ChromaDB 的 Java 客户端库，供 Java 应用访问向量数据库**

面向 ChromaDB v2 API 的轻量 Java 客户端，以 Maven/Gradle 依赖形式提供，要求 Java 8+ 与运行中的 ChromaDB >=1.0.0 实例或 Chroma Cloud 账户。功能覆盖集合与记录的增删改查、租户/数据库管理、Basic/Token/Chroma Token 认证、SSL 与自定义 OkHttpClient 传输配置、CMEK（GCP KMS）。内嵌多种嵌入函数：默认本地 ONNX（无需 API key）、OpenAI、Cohere、HuggingFace、Ollama。0.2.0 移除了 v1 API。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 覆盖 ChromaDB v2 API：集合、记录、查询、租户、数据库管理
- 内置嵌入函数：本地 ONNX 默认（无需 API key）、OpenAI、Cohere、HuggingFace、Ollama
- 支持 Chroma Cloud 与自托管实例，提供云/自托管功能对照表
- 客户端 ID 生成器（UUID/ULID/SHA-256）与 SSL/自定义传输配置

## 适用场景

- 在 Java/Spring 技术栈中接入 Chroma 向量数据库构建检索应用
- Java 应用直接生成向量嵌入并写入/查询 Chroma 集合
- 通过 Chroma Cloud 或自托管实例管理租户与数据库

## 场景标签

`向量数据库` · 领域:知识与检索

## 证据(README 行号)

> L3: Production-ready Java client for ChromaDB v2 API.
> L275: - Embedding functions: Default/local (ONNX, no API key), OpenAI, Cohere, HuggingFace Inference API, HuggingFace Te

## 星数曲线

```mermaid
xychart-beta
    title "amikos-tech/chromadb-java-client 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 79 --> 81
    line [80, 80]
```

2026-10-18 80 → 2026-10-29 80（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 mid · 依据 README sha `37ead633d6f1` · [字段定义](../../DATASET.md)*
