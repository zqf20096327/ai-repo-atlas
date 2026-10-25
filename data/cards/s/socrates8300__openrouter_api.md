# socrates8300/openrouter_api

⭐ 33 · Rust · MIT · 推送 2026-08-12 · [GitHub](https://github.com/socrates8300/openrouter_api) · 个人维护

**Rust 开发者的 OpenRouter API 客户端库**

用 Rust 编写的 OpenRouter API 客户端库，覆盖 Chat Completions（含流式）、Text Completions、Tool Calling、结构化输出、Web Search、多模态（音频/PDF）、Provider Preferences 路由、Analytics、Guardrails、Providers/Models 查询、Credits 与 Generation 等 OpenRouter 端点，并附带完整的 MCP（Model Context Protocol）JSON-RPC 客户端实现。采用 type-state builder 模式做编译期配置校验，API key 通过 zeroize 在 drop 时清零，错误消息自动脱敏，内置指数退避重试。通过 cargo add 安装，MSRV 1.85。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 覆盖 OpenRouter 主要端点：Chat/Text Completion、Tool Calling、结构化输出、Analytics、Guardrails 等
- 内置 MCP 客户端：JSON-RPC 2.0、资源访问、工具调用、并发信号量控制
- type-state builder 编译期配置校验与 zeroize 密钥内存清零
- 指数退避重试、错误消息脱敏、响应体大小上限（默认 10MB）等安全机制

## 适用场景

- 在 Rust 项目中以类型安全方式调用 OpenRouter 的各类模型端点
- 为应用接入 MCP 服务器获取上下文与调用工具
- 通过 Provider Preferences 配置模型路由、回退与 Zero Data Retention

## 场景标签

`模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L1: # OpenRouter API Client Library
> L29: - **Chat Completions:** Full support for OpenRouter's chat completion API with streaming
> L45: - **MCP Client:** Full JSON-RPC client implementation for the Model Context Protocol

## 星数曲线

```mermaid
xychart-beta
    title "socrates8300/openrouter_api 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 32 --> 34
    line [33, 33]
```

2026-10-18 33 → 2026-10-25 33（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `f897fd123f75` · [字段定义](../../DATASET.md)*
