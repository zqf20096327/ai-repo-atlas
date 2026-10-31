# bazzi24/RAGEve

⭐ 14 · Python · NOASSERTION · 推送 2026-08-04 · [GitHub](https://github.com/bazzi24/RAGEve) · 个人维护

**本地优先的 RAG 平台：私有文档问答，无需云端**

完全在本地机器运行的 RAG 平台，组合 Ollama（LLM 推理与嵌入）、Qdrant（稠密+稀疏混合检索）、MySQL/SQLite 持久化与 FastAPI + Next.js 前后端，无 API key、数据不出内网。面向非技术用户（一条 run.sh 全自动启动）和开发者（分脚本/手动启动）。支持 PDF 增强解析（栏检测、表格结构化、层级分块）、带引用的答案、交叉编码器重排、HuggingFace 数据集浏览下载与后台摄取、会话持久化与消息反馈。要求 Docker、macOS/Linux/WSL2、≥50 GB 磁盘、≥16 GB 内存，首次运行自动安装依赖并拉取约 8 GB 模型。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 混合检索（稠密+稀疏+可配权重融合）与交叉编码器重排
- 增强 PDF 解析：栏检测、结构化表格提取、层级分块
- 带精确 chunk 引用的答案与会话历史上下文
- UI 内浏览/下载/后台摄取 HuggingFace 数据集

## 适用场景

- 在本地对私有 PDF、Word、Excel 等文档做带引用的问答
- 不依赖云服务和 API key 构建私有知识库聊天
- 从 HuggingFace 拉取数据集到本地做检索问答

## 场景标签

`文档问答` `聊天机器人` `文档解析` · 领域:对话与助手

## 证据(README 行号)

> L23: RAGEve is a **local-first RAG (Retrieval-Augmented Generation) platform** built for developers and teams who want t
> L25: It combines **Ollama** for local LLM inference and embeddings, **Qdrant** as a high-performance vector database, an
> L80: - Exact chunk references from source documents

## 星数曲线

```mermaid
xychart-beta
    title "bazzi24/RAGEve 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `42eecdd51f69` · [字段定义](../../DATASET.md)*
