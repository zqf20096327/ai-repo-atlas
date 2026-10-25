# ariya/gamal

⭐ 61 · JavaScript · MIT · 推送 2025-11-05 · [GitHub](https://github.com/ariya/gamal) · 个人维护

**零依赖 CLI/Web/Telegram 问答工具：搜索网页并用 LLM 总结作答**

Gamal 是一个用 Node.js 或 Bun 运行的零依赖问答工具：借助 SearXNG 检索相关网页，再由 LLM 总结内容给出带引用的简洁回答。默认接入 OpenRouter，可通过环境变量改配 OpenAI、Groq、DeepInfra、Fireworks、Gemini 等托管服务，或 llama.cpp、Jan、Ollama 等本地推理。支持 CLI、极简 Web 界面和 Telegram bot 三种使用方式，可多语言对话；集成 whisper.cpp 做语音识别、兼容 OpenAI Speech API 的 TTS 做语音回复，并内置基于正则的问答评测工具。Telegram 会话历史仅存内存不落盘。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- SearXNG 搜索 + LLM 总结生成带引用的回答
- CLI、Web 界面、Telegram bot 三种使用方式
- 兼容 OpenRouter/OpenAI/Groq 等托管服务及 llama.cpp/Jan/Ollama 本地推理
- 集成 whisper.cpp 语音输入与兼容 OpenAI Speech API 的 TTS 输出

## 适用场景

- 在终端快速提问并获得带来源引用的回答
- 部署为 Telegram bot 做问答助手
- 本地 LLM 配合自建 SearXNG 实现私有搜索问答
- 用内置评测工具验证回答准确性

## 场景标签

`聊天机器人` · 领域:对话与助手

## 证据(README 行号)

> L3: Gamal is a simple, zero-dependency tool designed to quickly provide answers to questions. It finds relevant web page
> L7: Gamal utilizes SearXNG for web searches and requires an LLM to generate responses based on search results. By defaul

## 星数曲线

```mermaid
xychart-beta
    title "ariya/gamal 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 60 --> 62
    line [61, 61]
```

2026-10-18 61 → 2026-10-25 61（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `c8656c5f361d` · [字段定义](../../DATASET.md)*
