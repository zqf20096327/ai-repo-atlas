# achetronic/adk-utils-go

⭐ 129 · Go · Apache-2.0 · 推送 2026-08-22 · [GitHub](https://github.com/achetronic/adk-utils-go) · 个人维护

**Google ADK 的 Go 工具库：LLM 客户端、会话/记忆/工件存储与可观测**

面向使用 Google Agent Development Kit (ADK) 的 Go 开发者，提供 OpenAI Chat Completions / OpenAI Responses / Anthropic 客户端（含流式、工具调用、图像输入、扩展思考与 provider 方言机制）、基于 Redis 的会话持久化、PostgreSQL+pgvector 语义搜索的长期记忆、agent 可控的记忆工具集、文件系统带版本工件存储、LLM 摘要的上下文窗口管理，以及经 OTLP/HTTP 追踪全部 LLM 调用的 Langfuse 插件。以 Go 模块安装，另有 Docker 相关内容。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 三种 LLM 客户端实现，Chat Completions 含 provider 方言机制（兼容 Ollama/vLLM/Kimi 等）
- Redis 会话存储与 PostgreSQL+pgvector 语义搜索长期记忆
- 带版本与用户级作用域的文件系统工件存储
- Langfuse 插件追踪所有 LLM 调用含完整载荷与 token 用量

## 适用场景

- 在 Go 中用 ADK 构建多 agent 应用并接入 OpenAI/Anthropic 或本地网关
- 为 agent 应用添加持久化会话与语义长期记忆
- 对 agent 调用链做 Langfuse 可观测追踪

## 场景标签

`Agent 记忆` `LLM 可观测性` `模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L5: Utilities and implementations for Google's Agent Development Kit (ADK) in Go.
> L9: - **LLM Clients**: OpenAI (Chat Completions), OpenAI Responses, and Anthropic clients compatible with ADK
> L15: - **Langfuse**: Observability plugin: traces every LLM call to Langfuse with full prompt/response payloads and toke

## 星数曲线

```mermaid
xychart-beta
    title "achetronic/adk-utils-go 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 128 --> 130
    line [129, 129]
```

2026-10-18 129 → 2026-10-24 129（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `400aeee53bd8` · [字段定义](../../DATASET.md)*
