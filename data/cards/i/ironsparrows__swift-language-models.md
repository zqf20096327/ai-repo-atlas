# ironsparrows/swift-language-models

⭐ 24 · Swift · Apache-2.0 · 推送 2026-11-20 · [GitHub](https://github.com/ironsparrows/swift-language-models) · [官网](https://swiftpackageindex.com/ironsparrows/swift-language-models) · 个人维护

**统一 Swift API：把多家 LLM 接入 Apple Foundation Models 会话**

面向 Apple 平台开发者的 Swift Package，提供三个 provider 模块（OpenRouter、OpenAI、OpenAI-compatible），将 Claude、GPT、Gemini、DeepSeek、Ollama 等模型接入 Apple 的 LanguageModelSession 接口，保留工具调用、@Generable 引导生成、流式输出、推理等级与附件等原生能力。提供类型化模型目录（含上下文长度与能力）、按价格/数据策略路由、回退、缓存与服务器端工具。要求 iOS/macOS/visionOS/watchOS 27.0、Xcode 27.0 与 Swift 6.4，不支持 tvOS/Linux；通过 SwiftPM 安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 三个 provider 模块统一映射到 LanguageModelSession 接口
- 类型化模型目录与编译期检查的推理等级
- 路由、回退、提示缓存与响应缓存
- 服务器端工具：web search、web fetch、advisors、subagents

## 适用场景

- 在 iOS/macOS 应用中用 Apple 原生 API 调用云端或本地 LLM
- 按价格或数据策略在多个模型间路由与回退
- 用 Apple Evaluations 框架对任意模型做测试与评测

## 场景标签

`模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L30: Apps keep Apple's `LanguageModelSession`, with its transcripts, tools, `@Generable` guided generation, Dynamic Prof
> L31: and reasoning levels. Provider modules plug other providers' models into it. Claude, GPT, Gemini, DeepSeek, Qwen, L
> L39:  on your own machines through Ollama, LM Studio and vLLM; any other provider by its URL.

## 星数曲线

```mermaid
xychart-beta
    title "ironsparrows/swift-language-models 星数(近 2 点)"
    x-axis ["2026-11-08", "2026-11-21"]
    y-axis "stars" 23 --> 25
    line [24, 24]
```

2026-11-08 24 → 2026-11-21 24（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-18 · 置信度 high · 依据 README sha `05073d3bfeeb` · [字段定义](../../DATASET.md)*
