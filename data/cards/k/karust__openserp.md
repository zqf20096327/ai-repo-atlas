# karust/openserp

⭐ 1,613 · Go · MIT · 推送 2026-11-19 · [GitHub](https://github.com/karust/openserp) · [官网](https://openserp.org) · 个人维护

**自托管网页搜索 API，为 AI agent 与 SEO 提供搜索结果**

用 Go 编写的自托管网络搜索服务，以真实浏览器渲染 Google、Bing、Yandex、百度、DuckDuckGo、Ecosia 六个引擎的搜索结果页，返回统一 JSON（保留来源引擎与排名），可将结果页读取为干净的 Markdown。提供 REST API、CLI、MCP server 及 Python/JS SDK，无需 API key、按次计费；支持代理、缓存、重试、限流与熔断。Docker 或预编译二进制安装；PDF 抽取依赖 mutool。作者声明存在 CAPTCHA 与限流风险。

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

- 六个搜索引擎统一 JSON schema，保留来源引擎与排名
- extract=N 单次调用返回搜索结果与页面 Markdown，批量最多 20 个 URL
- 提供 MCP server、REST API、CLI 及 Python/JS SDK
- 支持 HTTP/SOCKS5 代理池、缓存、重试、限流与熔断

## 适用场景

- 给 MCP 客户端（Claude Code、Cursor 等）接入联网搜索工具
- 为 RAG 管道获取网页上下文
- SEO 排名监控与多引擎排名对比
- 从终端直接查询搜索引擎并输出 Markdown/JSON

## 场景标签

`网页抓取` · 领域:效率与自动化

## 证据(README 行号)

> L12: OpenSERP is a **free self-hosted web search for AI agents and SEO.** REST API and CLI for Google, Bing, Yandex, Bai
> L14: No API keys, no per-search billing. It loads search results in browser and returns structured JSON with source engi
> L16: Works with Claude Code, Cursor, Codex, Claude Desktop and any MCP client, Open WebUI (built-in provider), n8n, and 

## 星数曲线

```mermaid
xychart-beta
    title "karust/openserp 星数(近 25 点)"
    x-axis ["2026-10-23", "2026-10-25", "2026-10-27", "2026-10-28", "2026-10-29", "2026-10-30", "2026-10-31", "2026-11-01", "2026-11-02", "2026-11-06", "2026-11-08", "2026-11-10", "2026-11-11", "2026-11-12", "2026-11-13", "2026-11-14", "2026-11-15", "2026-11-16", "2026-11-18", "2026-11-19", "2026-11-20", "2026-11-21", "2026-11-22", "2026-11-23", "2026-11-25"]
    y-axis "stars" 1486 --> 1624
    line [1497, 1499, 1501, 1509, 1515, 1519, 1522, 1527, 1537, 1499, 1562, 1566, 1569, 1574, 1578, 1580, 1585, 1590, 1596, 1600, 1604, 1605, 1604, 1610, 1613]
```

2026-10-23 1,497 → 2026-11-25 1,613（+116）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-23 · 置信度 high · 依据 README sha `f605aff55368` · [字段定义](../../DATASET.md)*
