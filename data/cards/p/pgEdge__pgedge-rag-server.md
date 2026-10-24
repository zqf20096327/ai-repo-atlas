# pgEdge/pgedge-rag-server

⭐ 57 · Go · PostgreSQL · 推送 2026-10-23 · [GitHub](https://github.com/pgEdge/pgedge-rag-server) · [官网](https://docs.pgedge.com/pgedge-rag-server/) · 组织维护

**基于 PostgreSQL+pgvector 的 RAG API 服务器，服务开发者**

pgEdge 公司用 Go 编写的 RAG API 服务器：从安装了 pgvector 的 PostgreSQL 14+ 数据库读取内容，执行检索增强生成。支持多条可配置 embedding 与 LLM 提供商的 RAG 管道、向量相似度与 BM25 混合检索、SSE 流式响应、token 预算管理与 TLS。使用需先用 make build 从源码编译二进制，再编写 YAML 配置文件并启动，通过 REST API 查询管道。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `viral` | PostgreSQL |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 多条 RAG 管道，embedding 与 LLM 提供商可配置
- 向量相似度与 BM25 混合检索
- 支持 OpenAI/Anthropic/Gemini/Voyage/Ollama 及 OpenAI 兼容本地提供商
- SSE 流式响应与 token 预算管理

## 适用场景

- 为已有 PostgreSQL 数据库快速搭建 RAG 问答 API
- 通过可配置管道切换不同 LLM/embedding 提供商
- 在 API 网关或代理后部署 RAG 服务

## 场景标签

`RAG` · 领域:知识与检索

## 证据(README 行号)

> L22: The pgEdge RAG Server is a simple API server for performing Retrieval-Augmented Generation (RAG) of text based on c
> L28: - Multiple RAG pipelines with configurable embedding and LLM providers

## 星数曲线

```mermaid
xychart-beta
    title "pgEdge/pgedge-rag-server 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 56 --> 58
    line [57, 57]
```

2026-10-18 57 → 2026-10-24 57（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `b6ee692ecb7f` · [字段定义](../../DATASET.md)*
