# iammm0/context-engine

⭐ 36 · Python · MIT · 推送 2026-07-12 · [GitHub](https://github.com/iammm0/context-engine) · 个人维护

**构建检索、记忆与上下文感知 AI 系统的工程基础设施**

面向开发者的检索增强 AI 应用基础设施：FastAPI 后端提供文档摄取（PDF/Word/Markdown/TXT 解析、分块、嵌入、进度跟踪）、向量+关键词+图谱混合检索、流式聊天、多 agent 深度研究、知识空间与运行时配置 API。依赖 MongoDB、Qdrant、Neo4j、Redis，本地模型调用通过 Ollama 完成；前端为 TanStack React 应用，另有仅作兼容保留的旧版 Next.js 前端。需自行搭建环境并拉取模型。

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

- 文档摄取管线：解析、分块、嵌入、存储与进度跟踪（SSE 流式进度）
- 混合检索：向量搜索、关键词搜索与图关联结合
- 多 agent 协作的深度研究模式与预评估端点
- 通过 Ollama 调用本地 LLM 与嵌入模型

## 适用场景

- 搭建本地私有化部署的知识库问答系统
- 构建带文档摄取与混合检索的 RAG 应用
- 对复杂问题执行多 agent 深度研究

## 场景标签

`RAG` `文档问答` `多智能体` · 领域:Agent 开发

## 证据(README 行号)

> L8: `context-engine` is engineering infrastructure for building retrieval, memory, and context-aware AI systems. The bac
> L15: - Context-augmented Q&A: chat requests can select knowledge spaces and enhance retrieval through vector search, key

## 星数曲线

```mermaid
xychart-beta
    title "iammm0/context-engine 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 35 --> 37
    line [36, 36]
```

2026-10-18 36 → 2026-10-27 36（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `2f893857e805` · [字段定义](../../DATASET.md)*
