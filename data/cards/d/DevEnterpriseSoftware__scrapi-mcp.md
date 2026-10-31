# DevEnterpriseSoftware/scrapi-mcp

⭐ 18 · TypeScript · MIT · 推送 2026-10-28 · [GitHub](https://github.com/DevEnterpriseSoftware/scrapi-mcp) · [官网](https://scrapi.tech) · 组织维护

**MCP 服务器：让 MCP 客户端通过 ScrAPI 抓取网页**

封装 ScrAPI 网页抓取服务的 MCP server，向 Claude Desktop、Cursor、Windsurf、Codex、VS Code、Claude Code 等 MCP 客户端提供两个工具：scrape_url_html 与 scrape_url_markdown，分别返回 HTML 与 Markdown。支持抓取前执行浏览器命令（点击、输入、滚动、等待），ScrAPI 端处理 CAPTCHA、住宅代理、JS 渲染等。需 ScrAPI API key（无 key 时限免额度），支持 stdio 与 Streamable HTTP 传输，可经 npx、Docker 运行，另有云端托管端点。

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

- scrape_url_html / scrape_url_markdown 两个 MCP 工具
- 抓取前执行浏览器命令（click/input/scroll/wait 等）
- 支持 stdio 与 Streamable HTTP 双传输
- 提供 npx、Docker 与云端托管（api.scrapi.tech/mcp）运行方式

## 适用场景

- 让编码助手在对话中抓取并总结网页内容
- 抓取需要 JS 渲染或 CAPTCHA 处理的页面供模型分析
- 在抓取前自动点掉 cookie 横幅或执行站内搜索

## 场景标签

`网页抓取` · 领域:效率与自动化

## 证据(README 行号)

> L11: ScrAPI MCP Server lets MCP-compatible clients scrape web pages through ScrAPI.
> L22: - Use stdio transport for desktop MCP clients.

## 星数曲线

```mermaid
xychart-beta
    title "DevEnterpriseSoftware/scrapi-mcp 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 17 --> 19
    line [18, 18]
```

2026-10-18 18 → 2026-10-31 18（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `44f41e3aa973` · [字段定义](../../DATASET.md)*
