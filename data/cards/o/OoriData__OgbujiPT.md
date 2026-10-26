# OoriData/OgbujiPT

⭐ 115 · Python · Apache-2.0 · 推送 2026-06-24 · [GitHub](https://github.com/OoriData/OgbujiPT) · 组织维护

**面向 LLM 应用的知识库工具包：存储/检索/管理语义知识**

Python 编写的通用知识库（knowledge bank）系统，为 LLM 应用提供统一 API 存取与管理语义知识。支持三种存储后端：内存（零配置，API 与 PostgreSQL 版一致）、PostgreSQL+pgvector、Qdrant；检索策略覆盖稠密向量、BM25 稀疏、RRF 混合与交叉编码器重排；另含对话历史存储与 OpenAI 兼容 API 的 LLM 封装（可用于 Ollama、LM Studio 等）。设计上刻意保持低抽象、可组合、异步优先，声明不做成另一个 LangChain。GraphRAG、MCP 等仍在路线图中。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 内存/PostgreSQL+pgvector/Qdrant 三种存储后端，API 一致可替换
- 稠密/稀疏(BM25)/RRF 混合检索与交叉编码器重排
- 消息与会话历史的语义存储检索
- OpenAI 兼容 API 的 LLM 封装（Ollama/LM Studio/Anthropic 等均可接入）

## 适用场景

- 为 RAG 应用搭建可插拔的知识存储与混合检索层
- 对话记忆与长期语义知识的分型存储
- 从内存后端原型平滑切换到 PostgreSQL/Qdrant 生产部署

## 场景标签

`RAG` `Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L3: **OgbujiPT** is a general-purpose knowledge bank system for LLM-based applications. It provides a unified API for st
> L81: OgbujiPT includes LLM wrapper utilities for integrating knowledge banks with language models.

## 星数曲线

```mermaid
xychart-beta
    title "OoriData/OgbujiPT 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 114 --> 116
    line [115, 115]
```

2026-10-18 115 → 2026-10-26 115（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `2d68c451c275` · [字段定义](../../DATASET.md)*
