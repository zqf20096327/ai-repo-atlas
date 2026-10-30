# LarAIgent/larai-kit

⭐ 18 · PHP · MIT · 推送 2026-05-24 · [GitHub](https://github.com/LarAIgent/larai-kit) · 组织维护

**给 Laravel 开发者的 RAG 与 AI Agent 工具包**

基于 Laravel 官方 AI SDK（laravel/ai）构建的 Composer 包，为 Laravel 12/13 应用提供完整 RAG 管线：PDF/DOCX/文本/URL 解析、带重叠的分块、批量嵌入、Pinecone 或 pgvector 向量存储、检索注入与带来源引用的回答。支持 OpenAI/Anthropic/Gemini 供应商切换、SSE 流式聊天、多租户隔离、用量与成本追踪。提供预置 Agent、脚手架命令与健康检查 CLI。要求 PHP 8.3+，PDF/Word 解析器为可选依赖。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 文档摄取管线：解析→分块→批量嵌入→批量 upsert，各步骤为队列任务
- 多供应商 LLM（OpenAI/Anthropic/Gemini）经 .env 切换，代码不变
- Pinecone 与 pgvector 双向量存储，支持多租户范围隔离
- SSE 流式聊天、token 用量事件与健康检查端点/CLI

## 适用场景

- 在 Laravel 应用内搭建带来源引用的客服/知识库问答机器人
- 多租户 SaaS 中按客户隔离摄取、检索与对话数据
- 上传 PDF/Word/URL 做文档问答
- 构建带自定义工具调用的 AI Agent

## 场景标签

`RAG` `文档问答` `Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L11: **Production-ready RAG, AI agents, document ingestion, vector search, and streaming chat for Laravel 12 and 13.** D
> L23: Laravel's AI SDK gives you the low-level building blocks (`Agent`, `Tool`, `prompt()`). But building a production *
> L315: The Laravel AI SDK provides low-level primitives: `Agent`, `Tool`, `prompt()`, embeddings, streaming. **LarAI Kit 

## 星数曲线

```mermaid
xychart-beta
    title "LarAIgent/larai-kit 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-24", "2026-10-30"]
    y-axis "stars" 16 --> 19
    line [17, 18, 18]
```

2026-10-18 17 → 2026-10-30 18（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `d65b1174900f` · [字段定义](../../DATASET.md)*
