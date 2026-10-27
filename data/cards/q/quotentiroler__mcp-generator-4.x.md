# quotentiroler/mcp-generator-4.x

⭐ 24 · Python · Apache-2.0 · 推送 2026-09-03 · [GitHub](https://github.com/quotentiroler/mcp-generator-4.x) · [官网](https://quotentiroler.github.io/mcp-generator-4.x/) · 个人维护

**从 OpenAPI 规范生成 FastMCP 4 MCP 服务器的代码生成器**

面向开发者的 CLI 代码生成器：读取 OpenAPI 3.0.x/3.1.x/Swagger 2.0 规范（JSON/YAML），用纯 Python 客户端生成器产出模块化的 FastMCP 4 MCP 服务器，包含 JWT/JWKS 验证、OAuth2 流程、中间件栈（timing/logging/cache/auth）、自动测试与本地服务器注册表。AI 客户端（如 Claude Desktop）通过 STDIO/HTTP 连接生成的服务器以调用 REST API。需 Python 3.11+，可选特性（存储/缓存/资源/A2A 等）默认关闭，可加参数启用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 从 OpenAPI 3.0/3.1/Swagger 2.0 生成模块化 FastMCP 4 MCP 服务器
- JWT/JWKS 验证、OAuth2 流程与多认证组合支持
- 可选启用缓存、MCP 资源模板、MCP Apps UI、A2A agent 等特性
- generate-mcp/register-mcp/run-mcp CLI 命令链与本地服务器注册表

## 适用场景

- 把现有 REST API 封装成 MCP 服务器供 Claude 等 AI 客户端调用
- 为生产环境 API 生成带认证中间件的 MCP 工具
- 用 MCP Inspector 调试与测试生成的服务器

## 场景标签

`代码生成` · 领域:编码与开发

## 证据(README 行号)

> L12: Transform any OpenAPI specification into a production-ready Model Context Protocol (MCP) server with enterprise-gra
> L16: MCP Generator 4.x is an advanced code generator that automatically creates FastMCP 4 servers from OpenAPI 3.0.x/3.1

## 星数曲线

```mermaid
xychart-beta
    title "quotentiroler/mcp-generator-4.x 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 23 --> 25
    line [24, 24]
```

2026-10-18 24 → 2026-10-27 24（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 mid · 依据 README sha `3006628a8afc` · [字段定义](../../DATASET.md)*
