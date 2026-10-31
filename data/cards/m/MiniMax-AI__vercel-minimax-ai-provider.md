# MiniMax-AI/vercel-minimax-ai-provider

⭐ 14 · TypeScript · Apache-2.0 · 推送 2026-10-19 · [GitHub](https://github.com/MiniMax-AI/vercel-minimax-ai-provider) · [官网](https://platform.minimax.io/docs/guides/models-intro) · 组织维护 · 中文 README

**为 Vercel AI SDK 接入 MiniMax 平台模型的社区 Provider**

MiniMax AI Provider 是 Vercel AI SDK 的社区 provider 包，以 npm 库形式提供，将 MiniMax 平台的语言、图像、语音、视频模型接入 AI SDK。默认实例走 Anthropic 兼容 API，亦可切换 OpenAI 兼容格式；支持流式输出、thinking 作为 reasoning 内容返回、token 用量统计（含缓存与推理 token）。图像/语音/视频调用 MiniMax 自有 /v1 端点，语音返回的 hex 音频会被解码为 bytes，视频生成为异步任务轮询直至返回视频 URL。新版本发布于 @minimax-ai 官方 scope 下，迁移自旧的无 scope 包；API key 按区域区分，中国平台需使用中国 base URL。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 语言、图像、语音、视频四类模型接入 AI SDK
- Anthropic 兼容与 OpenAI 兼容两种 API 模式内置
- thinking 作为 reasoning 内容返回并报告 token 用量（含缓存与推理 token）
- 语音 hex 音频自动解码，视频生成异步任务轮询返回 URL

## 适用场景

- 在基于 Vercel AI SDK 的应用中调用 MiniMax-M3 等语言模型
- 通过 generateImage/generateSpeech/generateVideo 调用 MiniMax 多模态模型
- 中国平台账户通过 createMinimax 指定中国 base URL 接入

## 场景标签

`视频生成` `多模态` `图像生成` · 领域:内容生成

## 证据(README 行号)

> L1: # AI SDK - MiniMax AI Provider
> L3: The **MiniMax AI Provider** for the AI SDK contains language, image, speech, and video model support for the MiniMax

## 星数曲线

```mermaid
xychart-beta
    title "MiniMax-AI/vercel-minimax-ai-provider 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `5f8fdeb1c6e3` · [字段定义](../../DATASET.md)*
