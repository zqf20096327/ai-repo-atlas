# FlyingFathead/TelegramBot-OpenAI-API

⭐ 40 · Python · 推送 2026-10-21 · [GitHub](https://github.com/FlyingFathead/TelegramBot-OpenAI-API) · [官网](https://github.com/FlyingFathead/TelegramBot-OpenAI-API) · 个人维护

**接入 OpenAI/Perplexity API 的多功能 Telegram 聊天机器人**

基于 Python 的 Telegram 机器人，接入 OpenAI API 与 Perplexity API 提供对话，附带语音转写（gpt-4o-transcribe/whisper-1）、实时天气与地理查询、导航、定时提醒、股价与 RSS 新闻获取、DuckDuckGo/网页浏览的函数调用、计算器、Elasticsearch RAG（自建文档问答）、每日 token 用量追踪与限额、premium/fallback 模型自动切换。面向自行部署的个人/社区用户：需自备 Telegram Bot token 与 OpenAI 项目 key，支持 pip 源码运行或 Docker 部署；语音转写需额外安装 ffmpeg，DuckDuckGo 搜索需 lynx。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- OpenAI 与 Perplexity 双模型接入，含语音转写（多 STT 模型可配）
- Elasticsearch RAG：用自有文档增强回答并生成 Q&A 对
- 每日 token 用量追踪、限额与 premium/fallback 模型自动切换
- 天气/导航/股价/RSS/DuckDuckGo/网页浏览等函数调用模块

## 适用场景

- 在 Telegram 群组或私聊中部署一个接入 GPT 与 Perplexity 的问答机器人
- 用自己的文档建立 RAG 知识库供机器人检索
- 控制 API 成本：限额、用量追踪与自动降级到 mini 模型

## 场景标签

`聊天机器人` `文档问答` `语音识别` · 领域:对话与助手

## 证据(README 行号)

> L7: - **A simple-to-use, quick-to-deploy Python-based Telegram bot for OpenAI API & Perplexity API**
> L8: - **🎙 Transcribed Telegram voice messages via OpenAI speech-to-text models (Whisper and others)**
> L17: - **🔍 Perplexity API models alongside OpenAI models**

## 星数曲线

```mermaid
xychart-beta
    title "FlyingFathead/TelegramBot-OpenAI-API 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 39 --> 41
    line [40, 40]
```

2026-10-18 40 → 2026-10-26 40（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `b90957c1fea0` · [字段定义](../../DATASET.md)*
