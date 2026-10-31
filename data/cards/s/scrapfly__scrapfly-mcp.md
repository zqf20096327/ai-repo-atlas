# scrapfly/scrapfly-mcp

⭐ 14 · Go · 推送 2026-10-30 · [GitHub](https://github.com/scrapfly/scrapfly-mcp) · [官网](https://scrapfly.io/mcp-cloud) · 组织维护

**面向 MCP 客户端的网页抓取工具服务器，让 AI 实时访问网站数据**

Scrapfly 官方的 MCP 服务器，把网页抓取、云端浏览器会话、AI 结构化抽取、截图、凭据库与告警管理等 62 个工具暴露给任意 MCP 兼容客户端（VS Code、Cursor、Claude Desktop、Codex 等）。提供远程托管端点（免安装）、Go 二进制与 Docker 镜像自托管三种形态，认证支持 OAuth2 或 API Key。抓取经由 Scrapfly 代理池（Basic/Unblocker/Unblocker Ultra/Auto，含 Tor 池）处理反爬与 JS 渲染；自托管 server-key HTTP 模式不做逐请求认证，需置于自有认证代理之后。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 62 个工具分 7 组：网页抓取、云端浏览器会话、页面交互、WebMCP、凭据库、告警等
- 远程端点免安装，或以 Go 二进制/Docker 镜像自托管
- 代理池机制（Basic/Unblocker/Unblocker Ultra/Auto/Tor）处理反爬、代理与 JS 渲染
- 认证支持 OAuth2、API Key 与 Header Auth 三种方式

## 适用场景

- 让 IDE 中的 AI 助手实时抓取网页内容回答问题
- 通过云端浏览器会话执行登录、点击、填表等页面交互
- 用 AI 抽取把网页解析为结构化 JSON
- 在 MCP 工作流中做页面截图与站点监控告警

## 场景标签

`网页抓取` `浏览器自动化` · 领域:效率与自动化

## 证据(README 行号)

> L18: |**Remote server**|`https://mcp.scrapfly.io/mcp` (streamable HTTP, nothing to install)|
> L38: The **Scrapfly MCP Server** connects your AI assistants to live web data through the Model Context Protocol. Transf
> L251: The Scrapfly MCP Server exposes **62 tools** in seven groups. Most tasks need only the first group.

## 星数曲线

```mermaid
xychart-beta
    title "scrapfly/scrapfly-mcp 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 mid · 依据 README sha `1e45f3567d43` · [字段定义](../../DATASET.md)*
