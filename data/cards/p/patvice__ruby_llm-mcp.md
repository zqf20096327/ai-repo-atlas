# patvice/ruby_llm-mcp

⭐ 269 · Ruby · MIT · 推送 2026-10-08 · [GitHub](https://github.com/patvice/ruby_llm-mcp) · [官网](https://www.rubyllm-mcp.com/) · 个人维护

**Ruby/RubyLLM 的 MCP 客户端库：在 Ruby 应用中接入 MCP 工具**

面向 Ruby 与 RubyLLM 用户的 Model Context Protocol (MCP) 客户端库，以 Ruby-first API 在 RubyLLM 对话工作流中使用 MCP 的工具、资源与提示词。支持 stdio、streamable HTTP 与 SSE 传输；默认遵循稳定版 MCP 规范 2025-06-18，可选用草案规范 2026-01-26。提供 MCP OAuth 2.1 认证（PKCE、动态注册、自动刷新）、Rails per-user OAuth 安装生成器、多 MCP 服务器管理与通知/响应处理器。原生 :ruby_llm 适配器，另有可选 :mcp_sdk 适配器。通过 Gemfile 安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Ruby-first API 在 RubyLLM 对话中使用 MCP 工具/资源/提示词
- stdio / streamable HTTP / SSE 三种传输
- MCP OAuth 2.1 认证（PKCE、动态注册、自动 token 刷新）与 Rails per-user 接入
- 多 MCP 服务器管理与内置通知/响应处理器

## 适用场景

- 在 Rails 或 Ruby 应用中为 LLM 对话接入 MCP 工具服务器
- 为每个用户建立独立的 MCP OAuth 连接
- 在后台任务/服务中以显式连接块调用多 MCP 服务器的工具

## 场景标签

 · 领域:LLM 基础设施/MCP 客户端

## 证据(README 行号)

> L9: RubyLLM::MCP is a Ruby client for the Model Context Protocol (MCP), built to work cleanly with RubyLLM. Aiming to be
> L11: Use MCP tools, resources, and prompts from your RubyLLM chats over `stdio`, streamable HTTP, or SSE.

## 星数曲线

```mermaid
xychart-beta
    title "patvice/ruby_llm-mcp 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 268 --> 270
    line [269, 269]
```

2026-10-18 269 → 2026-10-26 269（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `823c93094ca0` · [字段定义](../../DATASET.md)*
