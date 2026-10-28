# alloy-ex/alloy

⭐ 91 · Elixir · MIT · 推送 2026-10-13 · [GitHub](https://github.com/alloy-ex/alloy) · [官网](https://alloylabs.dev) · 个人维护

**Elixir 的模型无关 agent 循环库：完成-工具调用-循环**

面向 Elixir 开发者的最小 agent harness，只提供完成-工具调用循环与提供商线格式翻译：支持 6 个 provider（Anthropic、Gemini、OpenAI、Codex、xAI 及兼容任意 OpenAI 兼容 API 的 OpenAICompat），内置 read/write/edit/bash 四个工具，支持流式输出、中间件钩子、默认开启的上下文压缩（工具结果清理+摘要压缩）、memory 工具、Anthropic 提示缓存、推理块保留与预算限制。会话、持久化、调度、UI 等明确排除在库外，交给应用层的 OTP 机制处理。约 1 万行代码，经 Hex 以 mix 依赖安装。限制：bash 工具的受限模式是护栏而非沙箱。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 6 个 provider 含 OpenAICompat（可接 Ollama/OpenRouter/DeepSeek/Mistral/Groq 等）
- 上下文压缩中间件：批量清理工具结果 + 摘要压缩，超长自动恢复
- 保留 OpenAI 加密推理 / Anthropic 签名思考 / DeepSeek 系 reasoning_content 块
- Anthropic 提示缓存断点，官方称输入 token 节省 60-90%

## 适用场景

- 在 Elixir/OTP 应用中嵌入任意 LLM 的工具调用 agent
- 通过 OpenAICompat 通道接入本地 Ollama 或第三方 API
- 为 agent 运行加预算限制与遥测事件

## 场景标签

`Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L8: **Minimal, OTP-native agent loop for Elixir.**
> L10: Alloy is the completion-tool-call loop and nothing else. Send messages to any LLM, execute tool calls, loop until d
> L62: - **6 providers** — Anthropic, Gemini, OpenAI, Codex, xAI, and OpenAICompat (works with any OpenAI-compatible API: 

## 星数曲线

```mermaid
xychart-beta
    title "alloy-ex/alloy 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 90 --> 92
    line [91, 91]
```

2026-10-18 91 → 2026-10-28 91（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `3847684f0db3` · [字段定义](../../DATASET.md)*
