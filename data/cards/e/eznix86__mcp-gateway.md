# eznix86/mcp-gateway

⭐ 22 · TypeScript · MIT · 推送 2026-03-08 · [GitHub](https://github.com/eznix86/mcp-gateway) · 个人维护

**聚合多个 MCP 服务器为单一网关，用搜索替代全量工具注入**

面向同时接入多个 MCP 服务器的 AI 客户端（Claude Code、OpenCode 等）的网关工具：作为 MCP 客户端连接上游服务器，作为 MCP 服务器向下游客户端仅暴露 5 个工具（search/describe/invoke/invoke_async/invoke_status），将全部工具索引为可搜索目录，按需检索与调用，以缓解多服务器场景下的上下文溢出问题。支持本地 stdio 与远程 HTTP/WebSocket 上游，搜索采用 MiniSearch 的 BM25 与模糊匹配，README 提及初始 token 约减少 40%。以 npm 包形式配置接入，另提供 Docker 运行方式。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 仅暴露 5 个统一工具（search/describe/invoke/invoke_async/invoke_status）
- 统一工具目录与 BM25+模糊匹配搜索，工具 ID 格式为 serverKey::toolName
- 支持本地 stdio 与远程 Streamable HTTP/WebSocket 上游，传输自动检测
- 异步任务队列支持优先级与并发限制（默认最多 3 并发）

## 适用场景

- 接入 10+ MCP 服务器导致系统提示词中工具描述过多时收拢为搜索入口
- 统一管理本地与远程 MCP 服务器的工具调用
- 对长耗时工具做异步执行与状态轮询

## 场景标签

 · 领域:LLM 基础设施/MCP 工具生态

## 证据(README 行号)

> L8: MCP Gateway is a server aggregation tool that connects multiple Model Context Protocol (MCP) servers into a single g
> L37: MCP Gateway operates as both an MCP client (connecting to upstream servers) and an MCP server (exposing tools to do

## 星数曲线

```mermaid
xychart-beta
    title "eznix86/mcp-gateway 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 21 --> 23
    line [22, 22]
```

2026-10-18 22 → 2026-10-27 22（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `e00deb924537` · [字段定义](../../DATASET.md)*
