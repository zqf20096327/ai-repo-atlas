# hoppscotch/hoppscotch-mcp-server

⭐ 14 · TypeScript · MIT · 推送 2026-10-16 · [GitHub](https://github.com/hoppscotch/hoppscotch-mcp-server) · [官网](https://docs.hoppscotch.io/documentation/clients/mcp-server) · 组织维护

**让 AI agent 操作 Hoppscotch API 工作区的 MCP 服务器**

Hoppscotch 官方维护的 Model Context Protocol 服务器，供 Claude Code、Cursor、VS Code Copilot、Gemini CLI 等 AI 编程助手直接读写 Hoppscotch 的集合、环境变量、团队空间并执行 HTTP 请求。提供 53 个 MCP 工具，按 minimal/core/standard/full 四档配置工具面。认证采用浏览器设备登录流程，Cloud 会话自动刷新，Community Edition 会话在本版本不自动刷新需重新登录；无头环境需手动传入 JWT。默认对私有地址做 SSRF 防护，重定向不自动跟随，响应体上限 5MB。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 53 个 MCP 工具，覆盖集合/环境/团队管理与请求执行
- 浏览器设备登录，会话缓存于 ~/.config/hoppscotch-mcp/auth.json
- 四档工具配置（minimal 22 / core 39 / standard 38 / full 53）
- SSRF 防护默认开启，secret 环境变量替换可按 origin 白名单限制

## 适用场景

- 让 Claude Code 等 AI 助手直接管理我的 Hoppscotch API 集合与环境
- 通过对话执行并验证 HTTP 请求，生成代码片段与 Markdown 文档
- 在 CI 等无头环境用 JWT 免浏览器运行

## 场景标签

`Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L3: A Model Context Protocol (MCP) server that enables AI agents like Claude to interact with Hoppscotch: managing colle
> L61: **Claude Code** / **Codex**: register the server once at user scope. For a self-hosted

## 星数曲线

```mermaid
xychart-beta
    title "hoppscotch/hoppscotch-mcp-server 星数(近 4 点)"
    x-axis ["2026-10-19", "2026-10-26", "2026-10-28", "2026-10-31"]
    y-axis "stars" 10 --> 15
    line [11, 12, 14, 14]
```

2026-10-19 11 → 2026-10-31 14（+3）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `968184e0e8ac` · [字段定义](../../DATASET.md)*
