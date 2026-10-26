# hideya/langchain-mcp-tools-py

⭐ 29 · Python · MIT · 推送 2026-10-23 · [GitHub](https://github.com/hideya/langchain-mcp-tools-py) · [官网](https://pypi.org/project/langchain-mcp-tools/) · 个人维护

**把 MCP 服务器工具转换为 LangChain 工具的 Python 库**

提供 convert_mcp_to_langchain_tools() 异步函数：按 Claude for Desktop 相同结构的 mcpServers 配置并行初始化多个 MCP 服务器，将服务器上的工具包装为 LangChain BaseTool 列表并返回 cleanup 回调清理会话。支持 Stdio/Streamable HTTP/SSE/WebSocket 传输、OAuth 2.1 认证、环境变量/工作目录/stderr 重定向等本地服务器配置。限制：仅支持 MCP 2025-03-26 协议与 SDK 1.x、仅文本返回、仅 Tools 功能。项目处于维护/休眠模式，README 建议新项目改用官方 LangChain MCP Adapters。

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

- 并行初始化多 MCP 服务器并包装为 LangChain 工具，附带 cleanup 回调
- 支持 Stdio/Streamable HTTP/SSE/WebSocket 传输选择与自动回退
- Streamable HTTP 连接支持 OAuth 2.1 认证及认证预校验
- 本地服务器支持环境变量、工作目录、stderr 重定向配置

## 适用场景

- 在 LangChain agent 中直接调用现有 MCP 服务器工具
- 通过统一配置接入多个本地与远程 MCP 服务器
- 需要 OAuth 认证的远程 MCP 服务器接入

## 场景标签

`Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L55: `convert_mcp_to_langchain_tools()` utility function accepts MCP server configurations
> L69: and returns LangChain Tools
> L135: This utility's goal is to make these numerous MCP servers easily accessible from LangChain.

## 星数曲线

```mermaid
xychart-beta
    title "hideya/langchain-mcp-tools-py 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 28 --> 30
    line [29, 29]
```

2026-10-18 29 → 2026-10-26 29（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `6315594c8cc7` · [字段定义](../../DATASET.md)*
