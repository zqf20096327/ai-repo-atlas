# twilio-labs/mcp

⭐ 113 · TypeScript · MIT · 推送 2026-02-14 · [GitHub](https://github.com/twilio-labs/mcp) · [官网](https://twilioalpha.com/mcp) · 组织维护

**将 Twilio API 与任意 OpenAPI 规范暴露为 MCP 工具的服务器**

Twilio 官方维护的 MCP monorepo，含两个包：mcp 将 Twilio 全部公开 API 以 MCP 工具形式暴露给支持 MCP 协议的 AI 助手；openapi-mcp-server 可读取任意 OpenAPI 规范生成对应的 MCP 服务器。通过 npx 快速启动，需配置 Twilio API Key/Secret；支持 --services/--tags 过滤以应对 LLM 上下文限制，OpenAPI 包用 --apiPath 指定规范文件位置。文档标注为 Alpha 阶段，并建议不要与社区 MCP 服务器混用以防范注入攻击。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 将 Twilio 全部公开 API 暴露为 MCP 工具
- openapi-mcp-server 可从任意 OpenAPI 规范生成 MCP 服务器
- 支持 --services/--tags 过滤暴露的 API 子集
- 通过 npx 启动，无需本地构建

## 适用场景

- 让支持 MCP 的 AI 助手直接调用 Twilio 的短信、语音等 API
- 把已有的 OpenAPI 接口快速转成 MCP 工具供 AI 客户端使用
- 按服务/标签筛选 API 子集以适配 LLM 上下文限制

## 场景标签

 · 领域:开发者工具/AI 接入

## 证据(README 行号)

> L4: This is a monorepo for the Model Context Protocol server that exposes all of Twilio APIs.
> L8: The Model Context Protocol (MCP) is a protocol for exchanging model context information between AI tools and service
> L14: - mcp - MCP Server for all of Twilio's Public API
> L15: - openapi-mcp-server - An MCP server that serves the given OpenAPI spec

## 星数曲线

```mermaid
xychart-beta
    title "twilio-labs/mcp 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 112 --> 114
    line [113, 113]
```

2026-10-18 113 → 2026-10-25 113（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `93a50a1d184f` · [字段定义](../../DATASET.md)*
