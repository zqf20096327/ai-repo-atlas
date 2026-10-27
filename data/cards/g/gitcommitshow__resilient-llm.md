# gitcommitshow/resilient-llm

⭐ 51 · TypeScript · MIT · 推送 2026-10-11 · [GitHub](https://github.com/gitcommitshow/resilient-llm) · [官网](https://www.npmjs.com/package/resilient-llm) · 个人维护

**多 LLM 接入层：统一 chat API 加内置重试/限流/熔断**

面向构建生产级 AI Agent 与 LLM 应用的 Node.js/TypeScript 库：用一个统一的 llm.chat() 接口封装 OpenAI、Anthropic、Google/Gemini、OpenRouter、Ollama 及自定义兼容 API，内置自动重试与指数退避、熔断器、令牌桶限流、token 自动估算、多提供商故障回退，并响应 retry-after 等信号；支持 JSON/JSON Schema 结构化输出与 AbortController 取消。明确不做链式编排、多模态、流式、工具调用与 RAG（建议复杂场景用 LangChain）。npm 安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 统一 .chat() 覆盖 OpenAI/Anthropic/Google/OpenRouter/Ollama 及自定义提供商
- 自动重试、指数退避、熔断器与令牌桶限流
- 多提供商故障回退与 retry-after 信号响应
- JSON/JSON Schema 结构化输出与 token 自动估算

## 适用场景

- 我的 AI Agent 上线后频遇限流和网络故障，需要可靠的 LLM 调用层
- 想在多个 LLM 提供商之间统一接口并自动切换
- 需要机器可读 JSON 输出的 LLM 集成

## 场景标签

`模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L18: - **Unified API**: One `.chat()` works seamlessly across OpenAI, Anthropic, Google, OpenRouter, Ollama, and custom 
> L93: ResilientLLM comes with built-in support for all text chat completion models provided by **OpenAI**, **Anthropic**,
> L95: **Adding custom providers:** You can add support for other LLM providers (e.g., Together AI, Groq, self-hosted vLLM

## 星数曲线

```mermaid
xychart-beta
    title "gitcommitshow/resilient-llm 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 50 --> 52
    line [51, 51]
```

2026-10-18 51 → 2026-10-27 51（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `67029343a4e3` · [字段定义](../../DATASET.md)*
