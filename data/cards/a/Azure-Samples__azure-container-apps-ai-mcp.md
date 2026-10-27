# Azure-Samples/azure-container-apps-ai-mcp

⭐ 32 · TypeScript · MIT · 推送 2026-02-20 · [GitHub](https://github.com/Azure-Samples/azure-container-apps-ai-mcp) · 组织维护

**开发者示例：在 Azure 容器应用中用 MCP 协议接入 OpenAI 构建 Agent**

Azure-Samples 出品的演示项目，展示如何通过 MCP 协议与 OpenAI、Azure OpenAI、GitHub Models 交互。包含 MCP Host（终端交互界面）、MCP Client（支持 HTTP 与 SSE 两种协议）、MCP Server（连接 DocumentDB Local 存储状态）与 LLM Provider 组件；Agent 可调用工具（如购物清单增删查）完成任务。提供 Docker Compose 与 DevContainer 两种运行方式，Node.js 22+ 环境下可本地源码运行。功能表中 AuthN 与 Resources/Prompts/Sampling 标注为未完成。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- MCP Host/Client/Server 三组件架构，支持 HTTP 与 SSE（legacy）两种协议
- 支持 Azure OpenAI、OpenAI、GitHub Models 三种 LLM Provider
- Docker Compose 一键启动 MCP 服务器与 DocumentDB Local
- Agent 通过 MCP 工具操作购物清单等示例任务

## 适用场景

- 学习 MCP 协议的 Host/Client/Server 实现方式
- 作为在容器环境中部署 MCP 服务的参考模板
- 测试不同 LLM Provider 与 MCP 工具调用的集成

## 场景标签

`Agent 框架` `教程课程` · 领域:Agent 开发

## 证据(README 行号)

> L3: This project showcases how to use the MCP protocol with OpenAI, Azure OpenAI and GitHub Models. It provides a simple
> L10: 1. **MCP Host**: The main application that interacts with the MCP server and the LLM provider. The host instanciate
> L13: 4. **LLM Provider**: The language model provider (e.g., OpenAI, Azure OpenAI, GitHub Models) that generates respons

## 星数曲线

```mermaid
xychart-beta
    title "Azure-Samples/azure-container-apps-ai-mcp 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 31 --> 33
    line [32, 32]
```

2026-10-18 32 → 2026-10-27 32（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `87d4110c38d6` · [字段定义](../../DATASET.md)*
