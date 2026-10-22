# jetify-com/ai

⭐ 261 · Go · Apache-2.0 · 推送 2026-01-22 · [GitHub](https://github.com/jetify-com/ai) · [官网](https://www.jetify.com) · 组织维护

**Go 语言的统一 AI SDK：一套接口接入多家 LLM 提供商**

Jetify 维护的开源 Go 库，为 OpenAI、Anthropic 等多家 AI 提供商提供统一接口，覆盖语言模型文本生成（流式与非流式）、多模态输入、工具调用等能力；Embedding、图像生成与结构化输出为待完成项。设计上强调 Go 惯用模式与强类型，含自动重试、限流与提供商故障转移。目前处于 Public Alpha，API 可能有破坏性变更。通过 go get 安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 统一接口抽象多家提供商（OpenAI、Anthropic）
- 文本生成（流式/非流式）、多模态输入、工具/函数调用
- 自动重试、限流、提供商故障转移
- Go 惯用设计，强类型接口

## 适用场景

- Go 项目中用同一套代码切换不同 LLM 提供商
- 构建带工具调用与流式输出的 AI agent
- 避免各提供商 SDK 接口差异带来的改写成本

## 场景标签

 · 领域:LLM 基础设施/开发库

## 证据(README 行号)

> L14: Jetify's **AI SDK for Go** is a unified interface for interacting with multiple AI providers including OpenAI, Anth
> L32: 1. **Provider abstraction** - Common interfaces for language models, embeddings, and image generation

## 星数曲线

```mermaid
xychart-beta
    title "jetify-com/ai 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-22"]
    y-axis "stars" 260 --> 262
    line [261, 261]
```

2026-10-18 261 → 2026-10-22 261（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `acc9d706a3fb` · [字段定义](../../DATASET.md)*
