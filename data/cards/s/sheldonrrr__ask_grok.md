# sheldonrrr/ask_grok

⭐ 24 · Python · GPL-2.0 · 推送 2026-10-17 · [GitHub](https://github.com/sheldonrrr/ask_grok) · [官网](https://ask-ai-blog.pages.dev/) · 个人维护 · 中文 README

**calibre 书库 AI 问答插件：对选中书直接提问**

calibre 电子书管理器的插件，选中一本书或多本书后直接向 AI 提问，无需复制粘贴元数据；支持 AI 自然语言搜索书库、随机问题、提示模板与按书记录的历史。默认使用 Nvidia AI (Free)（开发者维护的共享通道，无需 API key，可能不稳定），可自配 OpenAI、Claude、Gemini、Grok、DeepSeek、Kimi、Mistral、Perplexity、OpenRouter 及 Ollama/LM Studio/KoboldCpp 等本地推理。要求 calibre 6.0+，无需额外 Python 依赖，API key 存于本地插件设置。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | GPL-2.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 对一本或多本选中书直接提问，无需复制元数据
- 默认 Nvidia AI (Free) 开箱即用，无 API key
- 支持 15 种以上云端与本地 OpenAI 兼容 provider
- 自然语言搜索书库、随机问题、提示模板与按书历史
- UI 覆盖英/德/西/法/日/简繁中文等 17 种语言

## 适用场景

- 读书时对书的内容向 AI 提问而不离开 calibre
- 用自然语言搜索自己的电子书库
- 换不同 AI provider（含本地 Ollama）回答图书问题

## 场景标签

`文档问答` `语义搜索` · 领域:知识与检索

## 证据(README 行号)

> L3: A calibre plugin for asking questions about books in your library. It works immediately after install with **Nvidia 
> L11: - Ask about one book or several selected books, without copy-pasting metadata
> L13: - Search your library in natural language (AI Search)

## 星数曲线

```mermaid
xychart-beta
    title "sheldonrrr/ask_grok 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 23 --> 25
    line [24, 24]
```

2026-10-18 24 → 2026-10-30 24（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `ed5d7374181d` · [字段定义](../../DATASET.md)*
