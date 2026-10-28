# JSONbored/mem0-aio

⭐ 21 · Python · 推送 2026-10-28 · [GitHub](https://github.com/JSONbored/mem0-aio) · [官网](https://aethereal.dev) · 个人维护

**Mem0 OpenMemory 一体化自托管 Docker 部署（Unraid 优先）**

面向家庭实验室用户的单容器部署方案：用 s6-overlay 将 Mem0 OpenMemory 的 FastAPI/MCP 服务、Next.js 仪表盘（端口 3000）与预编译 Qdrant 向量库及持久化存储打包进一个镜像，附 Unraid CA 模板。首启路径通过 OPENAI_API_KEY 或外部 Ollama（OLLAMA_BASE_URL）配置模型；高级视图可切换 Anthropic/Groq/DeepSeek 等提供商及 Chroma/Weaviate/pgvector 等外部向量后端（互斥单一选择）。默认 API 绑定 127.0.0.1，直连 MCP 需显式发布端口。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 单容器捆绑 Qdrant、FastAPI/MCP 服务与 Web UI，含持久化存储
- Unraid CA 模板一键安装，外部 Ollama 原生路径自动默认 LLM/Embedder 提供商
- 支持切换外部向量后端（Chroma/Weaviate/Redis/pgvector/Milvus/ES 等，互斥配置）
- 默认 API 绑定容器内部 127.0.0.1，直连 MCP 端口需显式发布

## 适用场景

- 在 Unraid/Homelab 一键自托管 Mem0 OpenMemory 记忆层
- 为本地 agent 通过 MCP 接入持久化长期记忆
- 搭配外部 Ollama 搭建全本地 LLM 记忆服务

## 场景标签

`Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L5: An Unraid-first, single-container deployment of Mem0 OpenMemory for people who want the easiest reliable self-hosted
> L12: - OpenMemory API / MCP server on internal localhost port `8765`
> L13: - Embedded Qdrant vector store

## 星数曲线

```mermaid
xychart-beta
    title "JSONbored/mem0-aio 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 20 --> 22
    line [21, 21]
```

2026-10-18 21 → 2026-10-28 21（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 mid · 依据 README sha `bdbc2da1ae39` · [字段定义](../../DATASET.md)*
