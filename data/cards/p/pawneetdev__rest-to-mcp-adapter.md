# pawneetdev/rest-to-mcp-adapter

⭐ 16 · Python · MIT · 推送 2026-05-28 · [GitHub](https://github.com/pawneetdev/rest-to-mcp-adapter) · [官网](https://pypi.org/project/rest-to-mcp-adapter) · 个人维护

**将 REST API 规范转换为 MCP 工具的 Python 库**

面向 AI agent 开发者的适配层：读取 OpenAPI 3.x / Swagger 2.x / OpenAPI Actions 规范（JSON/YAML，支持 URL/文件/原文），归一化后生成 MCP 工具，内置 API Key/Bearer/Basic/OAuth2 认证处理器并自动过滤认证参数，运行时直接执行 REST 调用（含指数退避重试），通过 JSON-RPC 2.0 over stdio 提供 MCP 服务器，可配置进 Claude Desktop。要求 Python 3.11+，MIT 许可，自述处于 beta（v0.1.0）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- OpenAPI 3.x / Swagger 2.x / OpenAPI Actions 多格式规范读取与 $ref 解引用
- 端点自动转换为 MCP 工具（64 字符命名截断）
- 内置 4 类认证处理器与认证参数自动过滤
- JSON-RPC 2.0 over stdio 的 MCP 服务器，支持 tools/list 与 tools/call

## 适用场景

- 把现有 REST API 快速包装成 MCP 工具供 Claude 等 agent 调用
- 为带签名认证的 API（如 Binance）实现 MCP 服务器
- 统一管理多个 API 的 MCP 工具注册与执行

## 场景标签

`Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L3: **A Python library for converting REST API specifications into MCP (Model Context Protocol) tools for AI agents.**
> L98: ### 🤖 MCP Server
> L100: - **Claude integration**: Ready for Claude Desktop

## 星数曲线

```mermaid
xychart-beta
    title "pawneetdev/rest-to-mcp-adapter 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-30 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `0c07edf80e5d` · [字段定义](../../DATASET.md)*
