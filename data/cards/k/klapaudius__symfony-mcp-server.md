# klapaudius/symfony-mcp-server

⭐ 32 · PHP · MIT · 推送 2026-07-08 · [GitHub](https://github.com/klapaudius/symfony-mcp-server) · 个人维护

**给 Symfony 开发者的 MCP Server 构建包**

基于 PHP/Symfony（>=8.2/>=6.4）的 Composer 包，用于将 Symfony 应用构建为 Model Context Protocol 服务器：实现 Tools、Prompts、Resources、Sampling 等 MCP 能力，通过 StreamableHTTP 与 SSE 传输（不使用 STDIO），供 Claude Desktop 等 MCP 客户端调用应用业务逻辑。提供配置文件、路由接入、make:mcp-tool 生成命令与 mcp:test-tool 本地测试命令，支持多模态工具结果、进度流式通知与 Redis/Pub/Sub 水平扩展。附带开发用 Docker 环境（Nginx、PHP-FPM、Redis）。当前不支持 Discovery、Roots、Elicitation。MIT 许可。

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

- 实现 MCP 的 Resources/Prompts/Tools/Sampling 能力
- StreamableHTTP 与 SSE 传输，不使用 STDIO
- php bin/console make:mcp-tool 生成工具、mcp:test-tool 本地测试
- Pub/Sub 与 Redis/Cache 适配器支持水平扩展

## 适用场景

- 把 Symfony 应用的业务逻辑封装为 AI agent 可调用的工具
- 构建代码审查、数据分析、客服等 MCP agent 服务端
- 让 Claude Desktop 等 MCP 客户端接入内部系统

## 场景标签

`Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L15: Symfony MCP Server enables you to build **intelligent, context-aware AI agents** that can reason, make decisions, a
> L31: - 🛠️ **Tools**: Create powerful, executable functions that LLM can invoke to interact with your application

## 星数曲线

```mermaid
xychart-beta
    title "klapaudius/symfony-mcp-server 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 31 --> 33
    line [32, 32]
```

2026-10-18 32 → 2026-10-28 32（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 mid · 依据 README sha `9a373edf6105` · [字段定义](../../DATASET.md)*
