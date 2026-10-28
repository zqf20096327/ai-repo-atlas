# SecretiveShell/MCP-Bridge

⭐ 923 · Python · MIT · 推送 2025-12-08 · [GitHub](https://github.com/SecretiveShell/MCP-Bridge) · 个人维护

**中间件：为 OpenAI 兼容端点接入 MCP 工具调用**

MCP-Bridge 部署在 OpenAI API 客户端与推理引擎之间：将请求改写以注入 MCP 工具定义，转发给推理引擎并代为管理工具调用，再把结果回传生成最终回复，从而让不支持 MCP 的客户端也能调用 MCP 工具。支持流式/非流式 chat completions、MCP 采样、SSE Bridge 及 REST API 端点，可配置 API Key 认证。推荐 Docker 部署，需搭配支持 tool call 的推理引擎（作者用 vLLM 测试通过）。README 声明因 Open WebUI 原生支持 MCP 而处于软弃用状态，并寻求新维护者。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 将 MCP 工具注入 OpenAI 兼容端点的请求改写与工具调用管理
- SSE Bridge 使具备 MCP 支持的客户端可将其作为 MCP 服务器使用
- 支持流式/非流式 completions、MCP 采样与 API Key 认证
- 提供 REST API 端点操作原生 MCP 原语

## 适用场景

- 让 Open WebUI 等仅支持 OpenAI API 的客户端调用 MCP 工具
- 统一代理多个 MCP 服务器供外部聊天应用使用
- 在推理引擎与客户端之间集中管理 MCP 工具调用

## 场景标签

`模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L7: MCP-Bridge acts as a bridge between the OpenAI API and MCP (MCP) tools, allowing developers to leverage MCP tools th
> L163: The application sits between the OpenAI API and the inference engine. An incoming request is modified to include t

## 星数曲线

```mermaid
xychart-beta
    title "SecretiveShell/MCP-Bridge 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-28"]
    y-axis "stars" 922 --> 925
    line [924, 923, 923]
```

2026-10-18 924 → 2026-10-28 923（-1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 mid · 依据 README sha `49e8290720d8` · [字段定义](../../DATASET.md)*
