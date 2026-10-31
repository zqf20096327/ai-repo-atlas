# kuluruvineeth/chathub

⭐ 57 · TypeScript · 推送 2026-07-30 · [GitHub](https://github.com/kuluruvineeth/chathub) · 个人维护

**自托管多模型聊天界面：OpenAI/Anthropic/Gemini/Ollama 一站对话**

基于 Next.js 与 LangChain 构建的 Web 聊天应用：可在同一对话中切换 GPT-4o、Claude 3 系列、Gemini 1.5 及本地 Ollama 模型，切换时不丢失上下文。API 密钥存储在浏览器 IndexedDB，服务端无密钥库；持久化依赖 Supabase。支持模型可调用的工具（DuckDuckGo/Google 搜索、计算器、DALL·E 生图、跨会话记忆）、自定义助手、Markdown 编辑器、Whisper 语音输入与逐助手参数配置。需本地 git clone 后 npm 安装运行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 同一对话中途切换 OpenAI/Anthropic/Gemini/Ollama 模型且保留上下文
- API 密钥仅存浏览器 IndexedDB，无服务端密钥存储
- 模型可调用工具：网页搜索、计算器、DALL·E 生图、持久记忆
- 自定义助手（独立系统提示词/模型/工具集）与逐助手参数调节

## 适用场景

- 在一个界面里对比使用多家商业模型与本地 Ollama 模型
- 创建带专属提示词与工具集的自定义助手
- 密钥不出浏览器的前提下使用多模型对话

## 场景标签

`聊天机器人` · 领域:对话与助手

## 证据(README 行号)

> L17: **Every model, one thread.** GPT-4o, GPT-4 Turbo, Claude 3 Opus / Sonnet / Haiku, Gemini 1.5 Pro and Flash,
> L20: **Your keys stay yours.** API keys are entered in the app and stored in the browser's own IndexedDB.

## 星数曲线

```mermaid
xychart-beta
    title "kuluruvineeth/chathub 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 56 --> 58
    line [57, 57]
```

2026-10-18 57 → 2026-10-31 57（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `b7649c2f067d` · [字段定义](../../DATASET.md)*
