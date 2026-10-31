# Kartikayy007/SwiftyAI

⭐ 16 · Swift · 推送 2026-05-24 · [GitHub](https://github.com/Kartikayy007/SwiftyAI) · [官网](https://swifty-ai.vercel.app) · 个人维护

**Swift 统一 AI 工具包：一套 API 接 10 家模型服务商**

面向 Swift/iOS/macOS 开发者的 AI 工具包库，以统一 API 覆盖文本生成、流式输出、类型安全结构化输出、工具调用、Agent 循环、多模态媒体（图像/转录/语音/视频）、MCP 客户端与 SwiftUI 绑定。支持 OpenAI、Anthropic、Gemini、Groq、OpenRouter、Mistral、Cohere、Cloudflare、Ollama、Apple Foundation 共 10 家服务商，通过 provider/model 字符串切换。以 Swift Package Manager 安装，要求 iOS 17+/macOS 14+、Swift 5.9+；Apple Foundation 提供方需 iOS 26+，媒体路由目前仅经 OpenAI 与 Gemini 解析。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 一套 generateText/streamText/generateObject API 适配 10 家服务商
- 类型安全结构化输出：自动 JSON Schema、校验并解码到自定义类型
- MCPClient 连接 Model Context Protocol 服务器并桥接工具到 Agent 循环
- SwiftUI 钩子 AIChat/AICompletion 提供流式与加载状态绑定

## 适用场景

- 在 iOS/macOS 应用中接入多家 LLM 服务商并按需切换
- 用 Swift 构建 tool calling 与多步 Agent 应用
- 通过 SwiftUI 快速搭建聊天与补全界面

## 场景标签

`模型网关` `Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L5: **The AI toolkit for Swift.** One unified API for text, structured output, tools, agents, and media — across every m
> L42: |**10 providers**|OpenAI · Anthropic · Gemini · Groq · OpenRouter · Mistral · Cohere · Cloudflare · Ollama · Apple 

## 星数曲线

```mermaid
xychart-beta
    title "Kartikayy007/SwiftyAI 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-31 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `0b3e5c9c15da` · [字段定义](../../DATASET.md)*
