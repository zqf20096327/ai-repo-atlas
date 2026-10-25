# cefege/seo-chat-bot

⭐ 80 · Python · 推送 2026-04-13 · [GitHub](https://github.com/cefege/seo-chat-bot) · 个人维护

**基于 RAG 的语义 SEO 问答聊天机器人，回答带内联引用**

面向 SEO 从业者的检索增强生成（RAG）问答应用：知识库来自 Koray Tugberk Gubur 等语义 SEO 专家文章（6 个 sitemap + 17 篇精选文章），经 Scrapy 抓取、500 token 分块、ada-002 嵌入后存入 Pinecone；回答时检索 top-6 片段、按相关度阈值 0.25 过滤，由 GPT-4o-mini 流式生成并强制以 [N] 格式内联引用来源。前端为 Streamlit，支持 4k token 滑窗多轮对话与点赞/点踩反馈。需自备 OpenAI 与 Pinecone API key，从源码运行，无桌面安装包。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 检索前按相关度阈值（默认 0.25）过滤低分匹配
- 回答强制内联 [N] 引用并可点击跳转原文
- 4k token 滑窗对话记忆支持多轮追问
- scraper-embedder.py 一次性完成抓取、分块、嵌入与入库

## 适用场景

- 向语义 SEO 专家知识库提问并获得带引用的回答
- 核验回答所依据的原始文章
- 作为领域定制 RAG 应用的参考实现

## 场景标签

`聊天机器人` `RAG` · 领域:对话与助手

## 证据(README 行号)

> L3: > A production-grade RAG chatbot that answers SEO questions using retrieval-augmented generation — grounding every a
> L38: |**LLM**|OpenAI GPT-4o-mini|Response generation with streaming|

## 星数曲线

```mermaid
xychart-beta
    title "cefege/seo-chat-bot 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 78 --> 80
    line [79, 79]
```

2026-10-18 79 → 2026-10-25 79（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 mid · 依据 README sha `754968dec664` · [字段定义](../../DATASET.md)*
