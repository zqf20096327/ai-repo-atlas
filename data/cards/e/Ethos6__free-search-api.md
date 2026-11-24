# Ethos6/free-search-api

⭐ 4 · Python · MIT · 推送 2026-11-01 · [GitHub](https://github.com/Ethos6/free-search-api) · 个人维护

**自托管免密钥无限网页搜索 API，供 AI agent 与 RAG 使用**

自托管的元搜索引擎：并行查询 DuckDuckGo、Brave、Bing、Yahoo、Wikipedia 及新闻 RSS，用 Reciprocal Rank Fusion 合并去重为统一 JSON API。提供与 Tavily、Serper、Brave Search API、SearXNG 相同请求/响应格式的兼容端点，改 base URL 即可切换；内置 MCP server 为 Claude、Cursor 等 AI 客户端提供 web_search/news_search/read_page 工具。附带 /extract 页面转 Markdown、缓存（内存 LRU 或 Redis）、熔断与代理轮换，支持 Docker、pip、CLI、Python 库四种使用方式。

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

- 免 API key，并行多引擎搜索并以 RRF 合并去重
- Tavily/Serper/Brave/SearXNG 兼容端点，改 base URL 即接入
- 内置 MCP server 与远程 streamable-http 传输
- 熔断降级、Redis 缓存与 HTTP/SOCKS5/Tor 代理轮换

## 适用场景

- 给 AI agent 或 MCP 客户端配置免费网页搜索工具
- 为 RAG 流水线提供自托管搜索与网页抽取接口
- 替换现有按量付费的搜索 API 而不改动代码
- 用 CLI 或 Python 库在脚本中直接做搜索与新闻查询

## 场景标签

`RAG` `网页抓取` · 领域:效率与自动化

## 证据(README 行号)

> L8: It works as a **drop-in replacement for Tavily, Serper, the Brave Search API, and SearXNG**, and ships with an **MCP
> L26: AI agents, RAG pipelines and scripts all need web search, and every search API charges per query:
> L51: - **Several ways to use it:** a REST API, an MCP server, a CLI, or a Python library.

## 星数曲线

```mermaid
xychart-beta
    title "Ethos6/free-search-api 星数(近 3 点)"
    x-axis ["2026-10-23", "2026-11-14", "2026-11-24"]
    y-axis "stars" 2 --> 5
    line [3, 4, 4]
```

2026-10-23 3 → 2026-11-24 4（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-21 · 置信度 high · 依据 README sha `1fa22a56a5f8` · [字段定义](../../DATASET.md)*
