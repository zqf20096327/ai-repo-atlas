# Minokainduwara/RAG-Chatbot

⭐ 25 · Python · MIT · 推送 2026-03-08 · [GitHub](https://github.com/Minokainduwara/RAG-Chatbot) · 个人维护

**基于自有文档问答的本地/云端 LLM RAG 聊天机器人**

Python 实现的检索增强生成聊天机器人：加载并切分自有文本文档，用 sentence-transformers 本地嵌入模型与 FAISS 构建向量库，检索相关片段后交由 LLM 生成回答。LLM 后端可选本地 Ollama（免 API key）或云端服务（Gemini/Groq/Fireworks/OpenAI），RAG 链路由 LangChain 编排。运行方式为克隆仓库、放置知识库文本、配置 .env 后执行 python chatbot.py 进入交互对话；文档更新需删除 vector_db 缓存重建索引。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 检索（FAISS 向量搜索+本地嵌入）+ 生成的两步 RAG 流程
- 支持本地 Ollama 与 Gemini/Groq/Fireworks/OpenAI 云端后端
- LangChain 编排 RAG 链，pip 一键安装依赖
- 知识库更新后可删除 vector_db 缓存重建向量索引

## 适用场景

- 让聊天机器人回答我自己文档里的内容
- 无 API key、纯本地运行文档问答（Ollama 路线）
- 切换不同云端 LLM 提供商对比文档问答效果

## 场景标签

`聊天机器人` `文档问答` · 领域:对话与助手

## 证据(README 行号)

> L3: A Retrieval-Augmented Generation (RAG) chatbot that answers questions from your own documents using local or cloud-b
> L60: python chatbot.py

## 星数曲线

```mermaid
xychart-beta
    title "Minokainduwara/RAG-Chatbot 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 24 --> 26
    line [25, 25]
```

2026-10-18 25 → 2026-10-28 25（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `660214ba8a4d` · [字段定义](../../DATASET.md)*
