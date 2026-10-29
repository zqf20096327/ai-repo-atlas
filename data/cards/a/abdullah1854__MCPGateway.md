# abdullah1854/MCPGateway

⭐ 17 · TypeScript · MIT · 推送 2026-06-25 · [GitHub](https://github.com/abdullah1854/MCPGateway) · 个人维护

**MCP 聚合网关：把多个 MCP 服务器的工具经单端点路由并压缩 token**

TypeScript 实现的通用 MCP 聚合服务器：将多个 MCP 后端（STDIO/HTTP/SSE）聚合为一个网关端点，供 Claude Desktop、Claude Code、Cursor、OpenAI Codex、VS Code Copilot 等客户端连接。提供 15 层 token 优化（渐进式披露、结果过滤、聚合、代码批处理、增量响应、自动摘要等，README 称典型会话 token 降 95%）、Node.js VM 沙箱内执行 TS/JS、Web 仪表盘热重载管理后端、API Key/OAuth 认证、速率限制与 Prometheus 指标。安装需 git clone 后 npm install，要求 Node.js ≥20；支持 Docker 部署。与 Anthropic 原生 Tool Search 定位不同，README 说明两者可并用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 聚合多个 MCP 服务器（STDIO/HTTP/SSE）为单一网关端点
- 15 层 token 优化：渐进披露、结果过滤、聚合、增量响应、自动摘要等
- Node.js VM 沙箱执行 TypeScript/JavaScript 与 Skills 复用模式
- Web 仪表盘热重载管理服务器与工具，含认证与 Prometheus 指标

## 适用场景

- 把上百个 MCP 工具收敛到一个端点供 AI 客户端调用
- 降低多工具场景下的上下文 token 消耗
- 团队通过浏览器仪表盘统一管理后端 MCP 服务器

## 场景标签

`模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L9: > Universal MCP aggregation server that routes 300+ tools from multiple MCP servers through a single endpoint with 1
> L13: - **Multi-Server Aggregation** — Connect multiple MCP servers (STDIO, HTTP, SSE) through one gateway endpoint

## 星数曲线

```mermaid
xychart-beta
    title "abdullah1854/MCPGateway 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 16 --> 18
    line [17, 17]
```

2026-10-18 17 → 2026-10-29 17（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `3e09174a2df2` · [字段定义](../../DATASET.md)*
