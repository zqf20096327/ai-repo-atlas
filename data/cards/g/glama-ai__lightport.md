# glama-ai/lightport

⭐ 21 · TypeScript · NOASSERTION · 推送 2026-09-26 · [GitHub](https://github.com/glama-ai/lightport) · [官网](https://lightport.dev) · 组织维护

**轻量 AI 网关：把各 LLM 提供商转为 OpenAI 兼容接口**

Lightport 是从 Portkey AI Gateway 分叉出的轻量网关，仅做一件事：接收 OpenAI 兼容请求，转换后转发给目标提供商并返回响应。支持 77 个提供商（OpenAI、Anthropic、Azure OpenAI、Bedrock、Vertex AI、Ollama 等），覆盖 chat/completions、responses、图像生成等端点，经 x-lightport-provider 头指定提供商。重试、缓存、限流、密钥管理等明确为非目标；带 strategy/targets 的配置会被拒绝。每个响应附 Server-Timing 分阶段耗时头。通过 pnpx 一键运行，源码用 pnpm 构建，直接支撑 Glama 服务。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 支持 77 个 LLM 提供商的 OpenAI 兼容请求转换
- 支持 /v1/chat/completions、/v1/completions、/v1/responses、图像生成端点
- 每个请求的 Server-Timing 分阶段耗时（socket/ttfb 等）与日志
- 为每个提供商提供集成测试（需在 .env 填 API key）

## 适用场景

- 让非 OpenAI 提供商通过统一 OpenAI 兼容接口被调用
- 在服务层自行实现重试/缓存等策略时用作纯转换代理
- 区分网关耗时与上游提供商耗时以定位延迟

## 场景标签

`模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L3: A lightweight AI gateway that makes LLM providers OpenAI-compatible.
> L18: **Supported providers:** OpenAI, Anthropic, Azure OpenAI, Google Gemini, Vertex AI, Bedrock, Cohere, Mistral, Groq,
> L22: Lightport started as a fork of Portkey AI Gateway. Our sole use case for the gateway has always been making AI prov

## 星数曲线

```mermaid
xychart-beta
    title "glama-ai/lightport 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-26", "2026-10-28"]
    y-axis "stars" 19 --> 22
    line [20, 21, 21]
```

2026-10-18 20 → 2026-10-28 21（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `d3c100f583ec` · [字段定义](../../DATASET.md)*
