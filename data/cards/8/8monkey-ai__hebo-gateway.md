# 8monkey-ai/hebo-gateway

⭐ 27 · TypeScript · NOASSERTION · 推送 2026-10-23 · [GitHub](https://github.com/8monkey-ai/hebo-gateway) · [官网](https://hebo.ai/gateway) · 组织维护

**可嵌入应用的 AI 网关框架，控制模型路由与请求生命周期**

开源、可嵌入的 AI 网关框架（TypeScript/npm 包 @hebo-ai/gateway），设计为内嵌到自有应用中运行，而非开箱即用的托管网关。提供 OpenAI 兼容 /chat/completions、/embeddings、/audio/transcriptions、Open Responses /responses 与 Anthropic 兼容 /messages 端点；内置 18 个厂商适配器（Anthropic/Azure/Bedrock/Groq/DeepSeek/OpenAI 等）与模型预设目录，通过 Canonical IDs 统一跨厂商模型标识，用 Hook 系统定制路由、鉴权、限流与响应；可挂载进 Hono、Elysia、Next.js、TanStack 应用。限制：/conversations 默认内存存储，重启丢数据，官方说明不适用于生产。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- OpenAI 兼容 / Open Responses / Anthropic 兼容三类端点
- 18 个内置厂商适配器 + 模型预设目录（Qwen/Claude/GPT/Kimi/GLM 等）
- Hook 系统定制路由、鉴权、限流与响应
- 可挂载进 Hono / Elysia / Next.js / TanStack，兼容任意 Vercel AI SDK Provider

## 适用场景

- 在自己的 Node 应用内构建可控的 LLM 统一接入层
- 跨多个模型厂商做统一模型 ID 路由与回退策略
- 在网关层注入鉴权、限流、可观测性等自定义逻辑

## 场景标签

`模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L3: Roll your own AI gateway for full control over models, providers, routing logic, guardrails, observability and more 
> L9: Hebo Gateway is an open-source, embeddable AI gateway framework built to live inside your app. It gives you full con
> L22: - 🪝 Hook system to customize routing, auth, rate limits, and shape responses.

## 星数曲线

```mermaid
xychart-beta
    title "8monkey-ai/hebo-gateway 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-27"]
    y-axis "stars" 25 --> 28
    line [26, 27, 27]
```

2026-10-18 26 → 2026-10-27 27（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `5f4afde551c2` · [字段定义](../../DATASET.md)*
