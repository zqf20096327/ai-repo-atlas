# shenald-dev/one-api

⭐ 28 · JavaScript · 推送 2026-10-27 · [GitHub](https://github.com/shenald-dev/one-api) · 个人维护

**统一 20+ LLM 提供商的 OpenAI 兼容边缘 API 网关**

Node.js/TypeScript（Hono）实现的单一部署单元 LLM 网关：将 OpenAI、Anthropic、Google Gemini、Azure OpenAI、DeepSeek、Groq、Together AI、Mistral 及 Ollama/LM Studio 本地推理等 20+ 提供商统一到单个 OpenAI 兼容端点，客户端仅需替换 baseURL 即可复用现有 SDK。支持 SSE 流式转发、响应压缩、环境变量配置路由，无需数据库。面向不想为各模型差异重写集成代码的开发者，可通过 npm 源码运行或 Docker 部署。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | — |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 20+ LLM 提供商统一为 OpenAI 兼容的 /v1/chat/completions 端点
- 单一部署单元，无数据库、配置即全部状态
- 原生 SSE 流式转发与自动响应压缩
- 提供 Docker 镜像与 npm 两种运行方式

## 适用场景

- 开发中切换模型时避免重写 SDK 集成代码
- 在现有 openai-node/LangChain 代码中只改 baseURL 接入多家模型
- 将 OpenAI/Anthropic/本地推理统一到一个生产端点

## 场景标签

`模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L16: A dead-simple, single-binary gateway that turns **dozens of LLM providers** into one clean, standard OpenAI-compati
> L26: - **100% OpenAI-Compatible**: Your existing code, libraries, and SDKs (like `openai-node` or `langchain`) work comp

## 星数曲线

```mermaid
xychart-beta
    title "shenald-dev/one-api 星数(近 2 点)"
    x-axis ["2026-10-26", "2026-10-28"]
    y-axis "stars" 27 --> 29
    line [28, 28]
```

2026-10-26 28 → 2026-10-28 28（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `1860993f850c` · [字段定义](../../DATASET.md)*
