# vincenzo-afk/vanta

⭐ 24 · TypeScript · Apache-2.0 · 推送 2026-09-03 · [GitHub](https://github.com/vincenzo-afk/vanta) · [官网](https://vanta-exe.vercel.app) · 个人维护

**自托管多供应商 AI 工作台：聊天/搜索/推理/图像视频生成/语音**

基于 Next.js App Router 的私有部署 Web 应用：一个界面聚合 OpenRouter、Google AI、xAI、DeepSeek、Perplexity、Hugging Face 等多家文本模型，支持自动意图路由（对话/编程/分析/搜索/图像/视频）、免费 DuckDuckGo 网页搜索增强、结构化思维分析、Hugging Face/Fal.ai 图像生成、Fal.ai 视频生成、Gemini Live 浏览器语音交互。凭据保存在服务端 API 路由；文件上传限 8MB，文本在浏览器本地分块嵌入做语义检索；聊天记录与记忆存于浏览器 Zustand 存储。需 Node.js 22，配置各供应商 API key 后运行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 多供应商文本生成（OpenRouter/Google AI/xAI/DeepSeek/Perplexity/Hugging Face）
- 免费 DuckDuckGo 网页搜索增强，抓取公开页面并附来源链接
- 图像生成（Hugging Face 推理 + Fal.ai 回退）与 Fal.ai 视频生成队列
- Gemini Live 浏览器语音交互与本地嵌入的记忆/文档语义检索

## 适用场景

- 自托管一个聚合多家模型供应商的 AI 聊天工作台
- 无需付费搜索 API 即可让回答带网页来源
- 在同一界面完成对话、图像与视频生成、语音交互

## 场景标签

`AI 助手` `语音 Agent` `图像生成` `视频生成` · 领域:对话与助手

## 证据(README 行号)

> L3: > A Next.js interface for multi-provider AI chat, search, reasoning, image generation, video generation, and browser
> L21: - Multi-provider text generation through OpenRouter, Google AI, xAI, DeepSeek, Perplexity, and Hugging Face integra

## 星数曲线

```mermaid
xychart-beta
    title "vincenzo-afk/vanta 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 23 --> 25
    line [24, 24]
```

2026-10-18 24 → 2026-10-28 24（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `d06994e72798` · [字段定义](../../DATASET.md)*
