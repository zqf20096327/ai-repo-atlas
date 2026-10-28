# genkit-ai/genkit-go

⭐ 29 · 推送 2026-10-10 · [GitHub](https://github.com/genkit-ai/genkit-go) · [官网](https://genkit.dev) · 组织维护

**Google 出品的 Go 语言 AI 应用开发框架**

面向 Go 开发者的 AI SDK：以统一接口提供文本生成、结构化输出、流式响应、工具调用、Prompt 模板与多轮 Agent 工作流。Agent（preview）支持快照恢复、分支、后台运行与子代理委派，会话存储含内存/文件/Firestore。通过插件接入 Gemini、Claude、GPT、Grok、DeepSeek、Qwen、Kimi、GLM、Ollama 及任意 OpenAI 兼容端点。当前仓库为未来新家，源码暂位于 firebase/genkit/go。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 统一 API 覆盖多家模型提供商与 OpenAI 兼容端点
- Agent 支持快照、分支、后台运行与子代理委派
- 类型安全结构化输出与可自定义输出格式
- 工具中断（human-in-the-loop）与重试/降级等中间件

## 适用场景

- 用 Go 构建调用多模型的生成与结构化输出应用
- 搭建带会话快照与后台运行的多轮 Agent
- 为模型接入工具调用并加人工审批环节

## 场景标签

`Agent 框架` `模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L12:  Build production-ready AI-powered applications in Go with a unified interface for text generation, structured outp
> L14:  One interface over Google AI and Vertex AI (Gemini), Anthropic (Claude), OpenAI (GPT), xAI (Grok), DeepSeek, DashS
> L113: Gemini, Claude, GPT, Grok, DeepSeek, Qwen, Kimi, GLM, Llama, Mistral, local models, and anything OpenAI-compatible

## 星数曲线

```mermaid
xychart-beta
    title "genkit-ai/genkit-go 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 28 --> 30
    line [29, 29]
```

2026-10-18 29 → 2026-10-28 29（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 mid · 依据 README sha `7b77b4edcf17` · [字段定义](../../DATASET.md)*
