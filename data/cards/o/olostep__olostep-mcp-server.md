# olostep/olostep-mcp-server

⭐ 25 · TypeScript · MIT · 推送 2026-10-26 · [GitHub](https://github.com/olostep/olostep-mcp-server) · [官网](https://www.olostep.com/integrations/mcp-server) · 组织维护

**让 MCP 兼容 AI agent 具备网页抓取、爬取与搜索能力的服务器**

Olostep 的官方 MCP 服务器实现，将 Olostep 网页数据基础设施接入 MCP 兼容的 AI 客户端（Gemini CLI、Cursor、Claude Desktop、Claude Code、Windsurf、Cline、VS Code、Metorial 等）。提供 10 个工具：单页抓取（多格式/JS 渲染/国家路由）、解析器式网页搜索、带引用的 AI 问答、最多 1 万 URL 批量抓取、自主爬站、站点 URL 地图及对应的结果轮询接口。需 Olostep API key，可经远程端点、Docker、npx 或全局 npm 安装运行；Docker 镜像支持 linux/amd64 与 linux/arm64。

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

- 10 个 MCP 工具：抓取/搜索/AI 问答/批量抓取/爬取/URL 地图及结果轮询
- 批量抓取支持最多 1 万 URL，爬取为异步两步模式
- 提供远程托管端点、Docker 镜像与 npx 三种运行方式
- 覆盖 8 类 MCP 客户端的配置说明

## 适用场景

- 在 Claude Desktop 或 Cursor 中让 agent 实时抓取网页内容
- 让 agent 对整站进行自主爬取与批量内容提取
- 让 agent 通过带引用的 AI 问答从网络数据获取结构化答案

## 场景标签

`网页抓取` · 领域:效率与自动化

## 证据(README 行号)

> L7: A Model Context Protocol (MCP) server implementation that integrates with Olostep for web scraping, content extracti
> L32: https://mcp.olostep.com/mcp

## 星数曲线

```mermaid
xychart-beta
    title "olostep/olostep-mcp-server 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-26", "2026-10-27"]
    y-axis "stars" 23 --> 26
    line [24, 25, 25]
```

2026-10-18 24 → 2026-10-27 25（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `05d30c3a487e` · [字段定义](../../DATASET.md)*
