# arnobt78/Website-URL-RAG-Chatbot-NextJS

⭐ 23 · TypeScript · NOASSERTION · 推送 2026-08-30 · [GitHub](https://github.com/arnobt78/Website-URL-RAG-Chatbot-NextJS) · [官网](https://scraper-rag-chatbot.vercel.app/www.wikipedia.org) · 个人维护

**粘贴网站 URL 即可与该站内容对话的 Next.js RAG 聊天应用**

全栈教育型 Web 应用：用户粘贴任意公开网站 URL，应用通过 Firecrawl（或 Crawl4AI/Jina 单页回退）抓取全站内容，展开 FAQ/标签页等隐藏 UI 后，用 Upstash 内置嵌入模型（bge-large-en-v1.5）索引到 Upstash Vector；提问时检索相关片段，经 Gemini→Groq→OpenRouter 免费模型→Hugging Face 的多供应商自动回退链生成回答，逐字符流式输出，Redis 存储会话历史并做限流与 SSRF 防护。需配置 Upstash Redis/Vector 密钥，全站抓取需 Firecrawl 与 QStash。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | NOASSERTION |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Firecrawl 全站抓取 + 隐藏内容（FAQ/对话框/标签页）采集
- 多供应商 LLM 自动回退链（Gemini→Groq→OpenRouter→HF→可选 OpenAI）
- Upstash Vector 内置 bge-large-en-v1.5 嵌入，无需单独嵌入 API key
- Jina Reader 单页回退：未配置抓取服务时仍可对话

## 适用场景

- 我想针对某个网站的内容直接提问获得有依据的回答
- 学习 Next.js 全栈 RAG 架构（抓取、嵌入、检索、流式生成）
- 部署一个轻量的网站问答机器人用于演示或教学

## 场景标签

`聊天机器人` `文档问答` · 领域:对话与助手

## 证据(README 行号)

> L32: 6. **Generate answers** via an LLM with **multi-provider automatic fallback**
> L77: A **Large Language Model** generates human-like text. This project supports several providers (Gemini, Groq, OpenRo
> L85: - **Multi-provider LLM fallback** — Gemini → Groq → OpenRouter (`:free`) → Hugging Face → OpenAI (optional)

## 星数曲线

```mermaid
xychart-beta
    title "arnobt78/Website-URL-RAG-Chatbot-NextJS 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 22 --> 24
    line [23, 23]
```

2026-10-18 23 → 2026-10-30 23（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `d90dd57b1df3` · [字段定义](../../DATASET.md)*
