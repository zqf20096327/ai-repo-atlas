# chataize/generative-cs

⭐ 44 · C# · GPL-3.0 · 推送 2026-07-10 · [GitHub](https://github.com/chataize/generative-cs) · [官网](https://www.chataize.com) · 组织维护

**.NET 生成式 AI 库：多厂商模型客户端与反射式函数调用**

面向 .NET 10.0 的生成式 AI 库，提供 OpenAI、xAI Grok、Anthropic Claude、Google Gemini 四家的内置客户端，覆盖聊天补全、流式响应、嵌入、语音合成与转写、内容审核与多模态请求等能力。关键机制包括基于反射的 C# 函数调用（支持顶级方法、静态/实例方法、匿名函数）、依赖注入注册、时间感知、消息/字符数限制与消息置顶。Gemini 侧嵌入、审核与流式尚未实现；通过 NuGet 包安装，运行需 .NET 与各家 API key。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- OpenAI/Grok/Claude/Gemini 四家内置 API 客户端
- 基于反射的 C# 函数调用（含匿名函数与默认回调）
- 聊天补全、嵌入、TTS/STT、翻译、内容审核能力
- 消息/字符数限制、消息置顶、时间感知与依赖注入支持

## 适用场景

- 在 .NET 应用中统一接入多家大模型 API
- 通过 C# 方法反射快速实现模型函数调用
- 构建带语音合成、转写与审核的聊天应用

## 场景标签

`模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L2: Generative AI library for .NET 10.0 with built-in OpenAI ChatGPT, xAI Grok, Anthropic Claude, and Google Gemini API 
> L63: var openAIClient = new OpenAIClient("<OPENAI API KEY>");

## 星数曲线

```mermaid
xychart-beta
    title "chataize/generative-cs 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 43 --> 45
    line [44, 44]
```

2026-10-18 44 → 2026-10-29 44（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `88b79b19b697` · [字段定义](../../DATASET.md)*
