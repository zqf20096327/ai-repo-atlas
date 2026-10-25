# G12789/mcp-quickstart

⭐ 80 · JavaScript · MIT · 推送 2026-06-14 · [GitHub](https://github.com/G12789/mcp-quickstart) · 个人维护

**MCP 服务器脚手架 CLI：30 秒生成可运行、可测试、可发布的服务器**

面向开发者的命令行脚手架工具：一条命令生成 TypeScript 或 Python 的 MCP server，自带示例 tool/resource/prompt、单元测试与 Inspector 命令，可连接 Claude Desktop / Cursor。核心机制包括：从 OpenAPI 3.x 规格或单条 curl 命令生成 MCP 工具（每个 API 操作一个工具，请求体展开为逐字段 zod 类型），生成可自行编辑的普通源码而非运行时解析；支持部署到 Cloudflare Workers 免费计划作为远程 MCP 服务器（stdio / Streamable HTTP 两种传输）。License 为 MIT。

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

- 一条命令生成含示例工具、测试与 Inspector 的 MCP 服务器（TS/Python）
- 从 OpenAPI 规格或 curl 命令自动生成 MCP 工具，每个 API 操作一个
- 生成普通可编辑源码，无运行时 spec 解析
- 一键部署为 Cloudflare Workers 上的远程 MCP 服务器（免费计划）

## 适用场景

- 快速搭建可连接 Claude Desktop / Cursor 的 MCP 服务器
- 把现有 REST API 转成 MCP 工具供 AI agent 调用
- 将 MCP 服务器部署到边缘作为远程服务

## 场景标签

`代码生成` · 领域:编码与开发

## 证据(README 行号)

> L11: > **Forge a working, testable, publishable MCP server in 30 seconds.**
> L21: Most "create an MCP server" guides leave you with an empty skeleton and a 20-step setup. `mcp-quickstart` hands you
> L35: Point it at any OpenAPI 3.x document (a URL or a local `.json` / `.yaml`) and it generates a real, typed MCP server

## 星数曲线

```mermaid
xychart-beta
    title "G12789/mcp-quickstart 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 79 --> 81
    line [80, 80]
```

2026-10-18 80 → 2026-10-25 80（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `77a9fa2917bc` · [字段定义](../../DATASET.md)*
