# hasandeveloper/chat-bot

⭐ 20 · Python · MIT · 推送 2026-07-11 · [GitHub](https://github.com/hasandeveloper/chat-bot) · 个人维护 · 中文 README

**带记忆与 RAG 的可部署 AI 聊天机器人后端服务**

基于 FastAPI 的生产式聊天机器人后端：LangGraph 编排对话流程，ChromaDB 做 RAG 检索，Redis 存储短期/长期对话记忆。文档经 API 增量摄取（S3/URL → 分块 → 去重 → 嵌入），检索采用余弦相似度分数门控（默认 0.3）加 MMR 多样性排序，超纲问题在调用 LLM 前被拦截。支持 OpenAI/Anthropic/Groq 多提供商切换、阿英双语自动检测、按 IP 限流，回答附来源引用。面向需要把文档问答能力接入自有系统的开发者，通过 git clone + pip 或 Docker Compose 部署。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Redis 短期+长期对话记忆（含滚动摘要与 TTL）
- 检索分数门控 + MMR 排序，拦截超纲问题后再调用 LLM
- 增量摄取：仅重新嵌入变更分块，含内容哈希去重
- 多 LLM 提供商（OpenAI/Anthropic/Groq）经环境变量切换

## 适用场景

- 把产品文档/政策 PDF 做成带引用的问答 API
- 为 SaaS 集成一个有跨会话记忆的客服后端
- 限制机器人只依据已摄取文档回答，避免编造

## 场景标签

`聊天机器人` `文档问答` · 领域:对话与助手

## 证据(README 行号)

> L17: This project is a **production-style AI chatbot backend** built using:
> L21: * 💬 Multi-LLM support (OpenAI, Anthropic, Groq)
> L28: * Document-based Q&A (RAG)

## 星数曲线

```mermaid
xychart-beta
    title "hasandeveloper/chat-bot 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 19 --> 21
    line [20, 20]
```

2026-10-18 20 → 2026-10-30 20（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `fdcdca5564db` · [字段定义](../../DATASET.md)*
