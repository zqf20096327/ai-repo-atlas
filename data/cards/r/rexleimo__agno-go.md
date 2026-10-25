# rexleimo/agno-go

⭐ 67 · Go · Apache-2.0 · 推送 2026-09-29 · [GitHub](https://github.com/rexleimo/agno-go) · [官网](http://hno.rexai.top/) · 个人维护

**Go 语言多智能体框架：构建、编排与运行 AI Agent 服务**

用 Go 编写的多智能体框架，延续 Python 项目 Agno 的设计，利用 Go 的并发与静态类型提供 Agents、Teams（4 种协作模式）与 Workflows（5 种原语）组合构建能力，并内置 AgentOS HTTP 服务器（OpenAPI 3.0、会话存储、健康检查）。支持 OpenAI、Anthropic、Gemini、DeepSeek、Ollama 等 17 家模型提供商，附工具箱 SDK、ChromaDB RAG 集成、护栏钩子与 SSE 事件流观测。通过 go get 安装，Docker Compose 运行生产服务器，存储可选 Postgres/MongoDB/SQLite。

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

- Agents/Teams/Workflows 三层架构可自由组合，工作流支持快照恢复
- AgentOS HTTP 服务器：OpenAPI 3.0、会话共享、同步/异步摘要、SSE 流式事件
- 接入 OpenAI、Anthropic、Gemini、Ollama 等 17 家模型提供商
- ChromaDB RAG 集成、提示注入护栏与 OpenTelemetry 观测

## 适用场景

- 在 Go 服务中构建和编排多智能体系统
- 以 HTTP 服务形式部署 Agent 并复用会话与历史
- 接入本地 Ollama 或多家云端模型运行 Agent 示例

## 场景标签

`Agent 框架` `多智能体` · 领域:Agent 开发

## 证据(README 行号)

> L8: **Agno-Go** is a multi-agent framework written in Go. It keeps the KISS philosophy of the Agno project while using G
> L16: - **🔌 Multi-provider models** – OpenAI (incl. o-series reasoning), Anthropic Claude, Google Gemini, DeepSeek, GLM, 

## 星数曲线

```mermaid
xychart-beta
    title "rexleimo/agno-go 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-25"]
    y-axis "stars" 65 --> 68
    line [66, 67, 67]
```

2026-10-18 66 → 2026-10-25 67（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `533eb9926e7e` · [字段定义](../../DATASET.md)*
