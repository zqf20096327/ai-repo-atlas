# guinacio/langchain-mcp-client

⭐ 49 · Python · MIT · 推送 2026-07-31 · [GitHub](https://github.com/guinacio/langchain-mcp-client) · 个人维护

**连接 MCP 服务器的多模型聊天 Streamlit 应用**

基于 Streamlit 的聊天应用，提供图形界面连接 MCP（Model Context Protocol）服务器并通过工具调用与之交互，支持 OpenAI、Anthropic、Google、Ollama 四类 LLM 提供方。功能包括流式输出、多模态文件附件（图像/PDF/文本）、会话与跨会话持久记忆（SQLite）、多 MCP 服务器同时连接、工具单独测试界面与 Docker 部署。README 声明应用处于活跃开发中，可能存在 bug 或不完整功能；本地优先设计，不含多用户认证。安装经 UV 或 pip 从源码仓库进行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 连接多个 MCP 服务器并通过 LLM 调用工具
- 多提供方支持：OpenAI/Anthropic/Google/Ollama，含自定义模型名
- 会话记忆与 SQLite 跨会话持久记忆及历史检索工具
- 流式输出、文件附件、工具测试界面与 Docker 部署

## 适用场景

- 通过图形界面测试和调试 MCP 服务器的工具
- 在本地与多个 LLM 提供方对话并保留跨会话记忆
- 为聊天消息附加图像、PDF 与文本文档

## 场景标签

`聊天机器人` · 领域:对话与助手

## 证据(README 行号)

> L3: This Streamlit application provides a user interface for connecting to MCP (Model Context Protocol) servers and inte
> L17: - **MCP (Model Context Protocol) Integration**: Connect to MCP servers for tool access

## 星数曲线

```mermaid
xychart-beta
    title "guinacio/langchain-mcp-client 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 48 --> 50
    line [49, 49]
```

2026-10-18 49 → 2026-10-26 49（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 mid · 依据 README sha `2a2da2b15516` · [字段定义](../../DATASET.md)*
