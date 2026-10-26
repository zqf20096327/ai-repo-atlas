# Azure-Samples/pizza-mcp-agents

⭐ 33 · TypeScript · MIT · 推送 2026-10-21 · [GitHub](https://github.com/Azure-Samples/pizza-mcp-agents) · 组织维护

**披萨订餐 MCP 服务器示例：教 AI agent 调用真实 API**

微软 Azure Samples 出品的示例项目，演示如何用模型上下文协议（MCP）让 AI agent 与真实 API 交互。系统含披萨订餐 REST API（Azure Functions）、MCP 服务器（Azure Container Apps）、实时订单看板与用户注册系统；提供 9 个 MCP 工具（浏览菜单、下单、取消订单等）。支持 GitHub Codespaces、Dev Containers 或本地 Node.js 环境运行，可经 azd up 部署到 Azure，本地模式用内存存储。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 提供 9 个 MCP 工具（get_pizzas/place_order/delete_order_by_id 等）
- 微服务架构：披萨 API、MCP 服务器、订单看板、注册系统
- 兼容 GitHub Copilot、Claude 等 MCP 客户端，可本地零云成本测试
- azd up 一键部署到 Azure（Cosmos DB 持久化）

## 适用场景

- 学习如何用 MCP 将 AI agent 接入真实 API
- 作为构建 MCP 服务器与 serverless agent 应用的参考模板
- 本地用 MCP Inspector 或 Copilot agent 模式调试 MCP 工具调用

## 场景标签

`Agent 框架` `教程课程` · 领域:Agent 开发

## 证据(README 行号)

> L13: This project demonstrates how to build AI agents that can interact with real-world APIs using the **Model Context P
> L17: - **Pizza MCP server**: MCP server enabling AI agent interactions
> L33: - **Pizza MCP server** (Azure Container Apps): Exposes the pizza API through MCP, enabling AI agents to interact wi

## 星数曲线

```mermaid
xychart-beta
    title "Azure-Samples/pizza-mcp-agents 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 32 --> 34
    line [33, 33]
```

2026-10-18 33 → 2026-10-26 33（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `672e012c98d0` · [字段定义](../../DATASET.md)*
