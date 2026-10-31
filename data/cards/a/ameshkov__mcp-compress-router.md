# ameshkov/mcp-compress-router

⭐ 21 · TypeScript · MIT · 推送 2026-10-10 · [GitHub](https://github.com/ameshkov/mcp-compress-router) · [官网](https://github.com/ameshkov/mcp-compress-router) · 个人维护

**将多个 MCP 服务器压缩为单一路由 MCP 以降低 token 开销**

面向为编码代理连接多个 MCP 服务器的开发者的 MCP 路由服务器：把下游各服务器的完整工具定义列表替换为两个工具（get_tool_schema 与 invoke_tool），仅在代理请求时返回具体工具 schema，将约 26K token 的工具清单压缩为约 600 token 的目录。支持从用户级配置统一管理所有下游 MCP 服务器、HTTP 服务器、OAuth、per-server 工具过滤与启用/禁用。通过 npx 运行，需 Node.js 24+；实测节省因代理而异，部分新代理（如开启 Tool Search 的 Claude Code）场景下可能为负。

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

- 以两个工具（get_tool_schema/invoke_tool）替代全部下游工具定义
- 用户级配置统一管理多个下游 MCP 服务器（支持 HTTP/OAuth/工具过滤）
- add/list CLI 命令注册与校验下游服务器
- npx 直接运行，无需单独安装

## 适用场景

- 多个编码代理共用一套 MCP 服务器配置时统一管理
- 代理每轮请求都加载完整工具定义导致 token 开销过高时压缩目录
- 通过环境变量为下游 MCP 服务器集中管理密钥

## 场景标签

 · 领域:AI 工具链/MCP 基础设施

## 证据(README 行号)

> L15: MCP Compress Router is a single MCP server for developers who connect
> L19: replaces those listings with two tools, `get_tool_schema` and
> L63: opencode mcp add mcp-compress-router -- npx -y mcp-compress-router@latest

## 星数曲线

```mermaid
xychart-beta
    title "ameshkov/mcp-compress-router 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 20 --> 22
    line [21, 21]
```

2026-10-18 21 → 2026-10-31 21（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `4f8ececc9602` · [字段定义](../../DATASET.md)*
