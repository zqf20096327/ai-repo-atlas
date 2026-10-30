# AuraFriday/mcp-link-server

⭐ 16 · Python · NOASSERTION · 推送 2026-08-07 · [GitHub](https://github.com/AuraFriday/mcp-link-server) · [官网](https://aurafriday.com/) · 个人维护

**本地 MCP SSE 服务器：让 AI agent 在本机执行受控工具**

面向 MCP（Model Context Protocol）的服务端实现，通过 SSE 端点向 ChatGPT、Claude、Gemini 等 MCP 兼容客户端提供工具发现与执行能力。内置文件操作、终端、浏览器自动化、SQLite 语义检索、系统自动化、Python 执行等工具，另含统一 LLM 聊天工具（支持 Ollama/llama.cpp 本地模型及 OpenRouter 等云 API）。提供工具级权限控制、执行审批与 Docker 沙箱。采用专有许可的'可见源码'模式，禁止再分发。提供三平台安装包，无需 Python。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 实现 MCP 服务端：工具发现、SSE 实时通信、插件扩展
- 内置 fs/terminal/chrome_browser/sqlite/system/python 等本地工具
- 工具级权限控制：可见性开关、三种执行审批策略、Docker 沙箱
- 统一 LLM 工具支持 Ollama、llama.cpp、transformers 本地模型及 OpenRouter

## 适用场景

- 让 ChatGPT/Claude 等网页 AI 通过浏览器扩展操作本机工具
- 在 Cursor、Claude Code 等 IDE 中接入本地 MCP 工具执行环境
- 以审批与沙箱机制控制 AI agent 的本机操作权限

## 场景标签

`浏览器自动化` `Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L6: **MCP Link Server** is the core engine that powers real-world AI agent capabilities through a secure, feature-rich *
> L99: **MCP Link Server** implements the server side of this protocol, providing:
> L101: * **Tool Discovery**: Advertises available tools and their capabilities to AI clients

## 星数曲线

```mermaid
xychart-beta
    title "AuraFriday/mcp-link-server 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-30"]
    y-axis "stars" 14 --> 17
    line [15, 16, 16]
```

2026-10-18 15 → 2026-10-30 16（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `d1206cac9820` · [字段定义](../../DATASET.md)*
