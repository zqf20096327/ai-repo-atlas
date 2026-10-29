# oxylabs/oxylabs-mcp

⭐ 104 · Python · MIT · 推送 2026-10-28 · [GitHub](https://github.com/oxylabs/oxylabs-mcp) · [官网](https://oxylabs.io) · 组织维护

**为 AI 模型接入网页抓取能力的 Oxylabs MCP 服务器**

Oxylabs 官方维护的 Model Context Protocol 服务器，作为 AI 助手与外部网页数据之间的桥接层。提供 10 个 MCP 工具：Web Scraper API 侧的通用 URL 抓取、Google/Amazon 搜索与商品解析；AI Studio 侧的 AI 抽取、按提示词爬站、浏览器代理与网页搜索。功能包括 JavaScript 渲染、HTML 转 Markdown、CAPTCHA 处理与 195+ 国家代理。使用需持有 Oxylabs API 凭据（Web Scraper API 账户或 AI Studio API key），支持官方托管实例（免安装）或本地 uvx 运行，也支持自托管 streamable-HTTP 传输。

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

- 10 个 MCP 工具：通用抓取、搜索/商品解析、AI 抽取、按提示词爬站与浏览器代理
- JavaScript 无头浏览器渲染与 HTML 自动转 Markdown
- 官方托管实例可免安装接入，或用 uvx 本地运行
- 支持自托管 streamable-HTTP 传输，凭据按请求传递

## 适用场景

- 让 Claude Code/Cursor 等 MCP 客户端直接抓取并总结网页内容
- 为 LLM 提供 Google/Amazon 等结构化数据源
- 构建需要访问 JavaScript 重渲染页面的 AI 数据流水线

## 场景标签

`网页抓取` · 领域:效率与自动化

## 证据(README 行号)

> L19: The Oxylabs MCP server provides a bridge between AI models and the web. It enables them to scrape any URL, render J
> L21: It is built on the Model Context Protocol (MCP), the open standard for connecting AI assistants to external tools a

## 星数曲线

```mermaid
xychart-beta
    title "oxylabs/oxylabs-mcp 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 103 --> 105
    line [104, 104]
```

2026-10-18 104 → 2026-10-29 104（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `39aae1c7c93d` · [字段定义](../../DATASET.md)*
