# datalayer/langchain-mcp-client

⭐ 10 · Jupyter Notebook · NOASSERTION · 推送 2026-11-24 · [GitHub](https://github.com/datalayer/langchain-mcp-client) · [官网](https://datalayer.ai) · 组织维护

**让 LangChain ReAct Agent 调用 MCP 服务器工具的客户端**

一个 Model Context Protocol 客户端，演示 LangChain ReAct Agent 如何使用 MCP 服务器工具。核心是 convert_mcp_to_langchain_tools() 工具函数，并行初始化多个 MCP 服务器并将其工具转换为 LangChain BaseTool 列表；支持任何 LangChain 兼容 LLM，通过 JSON5 文件配置 LLM、MCP 服务器与示例查询，经 CLI 交互。要求 Python 3.11+，需在 .env 中配置 LLM API key。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- convert_mcp_to_langchain_tools() 将多个 MCP 服务器的工具并行转换为 LangChain BaseTool
- 支持任何 LangChain 兼容的 LLM
- CLI 交互方式，配置经 llm_mcp_config.json5 管理

## 适用场景

- 让 LangChain Agent 接入已有的 MCP 服务器工具
- 通过 CLI 与连接多个 MCP 服务器的 Agent 对话
- 在 Jupyter 环境中让 Agent 调用 Jupyter MCP Server 执行任务

## 场景标签

`Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L10: This simple Model Context Protocol (MCP) client demonstrates the use of MCP server tools by LangChain ReAct Agent.
> L18: It leverages a utility function `convert_mcp_to_langchain_tools()`. This function handles parallel initialization o


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 high · 依据 README sha `10ed050bf8f8` · [字段定义](../../DATASET.md)*
