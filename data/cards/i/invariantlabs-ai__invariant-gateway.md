# invariantlabs-ai/invariant-gateway

⭐ 82 · Python · Apache-2.0 · 推送 2025-11-06 · [GitHub](https://github.com/invariantlabs-ai/invariant-gateway) · 组织维护

**观测与调试 AI agent 的 LLM 代理服务**

Invariant Gateway 是一个零配置的 LLM 代理服务，部署在 AI Agent 与 LLM 提供商之间：用户只需将客户端 base URL 指向 Gateway，即可拦截 Chat Completions、Messages、Gemini 请求及 MCP 工具调用（stdio/SSE/Streamable HTTP），自动追踪 agent 交互并把运行时 trace 推送到 Invariant Explorer，供观察、调试与配置 guardrails。面向构建 agent 的开发者及需要在组织内观测 agent 的团队；本地运行依赖 Docker，trace 默认推送到公开 Explorer 实例，也可自建。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 单行接入：仅改 LLM 客户端 base URL 即可启用代理
- 支持 OpenAI/Anthropic/Gemini API 的转发与流式传输
- MCP 工具调用代理（stdio/SSE/Streamable HTTP）并支持 guardrails
- 可从源码或官方 Docker 镜像本地部署，trace 推送至 Invariant Explorer

## 适用场景

- 开发者追踪 agent 的 LLM 交互与工具调用以排查问题
- 组织内无代码接入以观测并加固 AI agent
- 通过代理 MCP 调用并应用阻断或记录型 guardrails

## 场景标签

`LLM 可观测性` · 领域:评测与运维

## 证据(README 行号)

> L3: **LLM proxy to observe and debug what your AI agents are doing.**
> L7: Invariant Gateway is a lightweight _zero-configuration_ service that acts as an intermediary between AI Agents and L
> L9: Gateway automatically traces agent interactions and stores them in the Invariant Explorer, giving you insights into 

## 星数曲线

```mermaid
xychart-beta
    title "invariantlabs-ai/invariant-gateway 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 81 --> 83
    line [82, 82]
```

2026-10-18 82 → 2026-10-25 82（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `4aaa777e3796` · [字段定义](../../DATASET.md)*
