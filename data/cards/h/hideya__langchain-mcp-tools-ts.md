# hideya/langchain-mcp-tools-ts

⭐ 24 · TypeScript · MIT · 推送 2026-08-22 · [GitHub](https://github.com/hideya/langchain-mcp-tools-ts) · [官网](https://www.npmjs.com/package/@h1deya/langchain-mcp-tools) · 个人维护

**将 MCP 服务器工具转换为 LangChain 工具的 TypeScript 库**

提供 convertMcpToLangchainTools() 函数：接收与 Claude for Desktop 同构的 mcpServers 配置，并行初始化多个 MCP 服务器，把服务器可用工具包装为 LangChain StructuredTool 数组，并返回清理回调关闭会话。支持 Stdio/Streamable HTTP/SSE/WebSocket 传输选择、OAuth 2.1、按 LLM 提供商做 schema 变换、stderr 重定向与工作目录配置。限制：仅支持工具调用文本结果，不支持 Resources/Prompts/Sampling；项目处于维护/休眠状态，仅支持 MCP 2025-03-26 及向后兼容 2024-11-05，README 推荐新项目改用 LangChain 官方 MCP Adapters。给 TypeScript/LangChain 开发者使用，npm 安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 并行初始化多个 MCP 服务器并包装为 LangChain StructuredTool
- 按 LLM 提供商（OpenAI/Gemini/Claude/Grok）做工具 schema 兼容变换
- Stdio/Streamable HTTP/SSE/WebSocket 传输自动检测与显式选择
- Streamable HTTP 连接支持 OAuth 2.1 认证

## 适用场景

- 在 LangChain/TypeScript 项目中调用现成 MCP 服务器的工具
- 通过 mcpServers 配置同时接入多个本地与远程 MCP 服务器
- 解决不同 LLM 提供商 function calling 的 schema 兼容问题

## 场景标签

`Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L3: A simple, lightweight library to use
> L4: Model Context Protocol (MCP)
> L5: server tools from LangChain.
> L141: This utility's goal is to make these numerous MCP servers easily accessible from LangChain.

## 星数曲线

```mermaid
xychart-beta
    title "hideya/langchain-mcp-tools-ts 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 23 --> 25
    line [24, 24]
```

2026-10-18 24 → 2026-10-28 24（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `c659d1393310` · [字段定义](../../DATASET.md)*
