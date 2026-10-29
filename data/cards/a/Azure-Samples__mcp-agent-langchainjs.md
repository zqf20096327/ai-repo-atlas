# Azure-Samples/mcp-agent-langchainjs

⭐ 204 · TypeScript · MIT · 推送 2026-10-28 · [GitHub](https://github.com/Azure-Samples/mcp-agent-langchainjs) · 组织维护

**用 LangChain.js 和 MCP 构建汉堡点餐 AI agent 的 Azure 示例工程**

微软 Azure-Samples 出品的端到端参考工程：演示如何用 LangChain.js 构建 AI agent，通过 MCP（Streamable HTTP 传输）调用工具与汉堡点餐 API 交互，实现浏览菜单、下单、查询订单。系统含多个服务：Agent Web App、Agent API、Burger API、Burger MCP Server、订单可视化 Web App，采用 Azure Static Web Apps、Azure Functions 与 Cosmos DB 的全 serverless 架构，azd 单命令部署。支持本地开发：可用 Ollama 拉取 qwen3:8b 完全本地运行，本地模式使用内存存储。MCP server 也可接入 GitHub Copilot 等 MCP 客户端测试。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- LangChain.js agent 通过 MCP 工具调用（Streamable HTTP）操作点餐 API
- 多服务端到端架构（Web UI、API、MCP Server），Bicep IaC 单命令部署
- 可用 Ollama（qwen3:8b 或 gpt-oss:20b）完全本地运行，无云成本
- Burger MCP Server 提供 9 个工具，兼容 MCP Inspector 与 GitHub Copilot

## 适用场景

- 参考该工程构建自己的 MCP 工具调用型 AI agent
- 在 Azure serverless 架构上部署 AI agent 应用
- 本地用 Ollama 与 npm 运行完整示例进行学习实验

## 场景标签

`Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L24: This project demonstrates how to build AI agents that can interact with real-world APIs using the **Model Context P
> L50: |Agent API|`packages/agent-api`|LangChain.js agent + chat state + MCP client|
> L33: - LangChain.js agent with tool calling via MCP (Streamable HTTP transport)

## 星数曲线

```mermaid
xychart-beta
    title "Azure-Samples/mcp-agent-langchainjs 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 203 --> 205
    line [204, 204]
```

2026-10-18 204 → 2026-10-29 204（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `c389ea587c14` · [字段定义](../../DATASET.md)*
