# drmikecrypto/WebSearchFree

⭐ 10 · C++ · MIT · 推送 2026-09-08 · [GitHub](https://github.com/drmikecrypto/WebSearchFree) · 个人维护

**自托管无密钥网页搜索+提取 API，供 AI 代理与 RAG 接入**

C++ 实现的本地元搜索服务：聚合 DuckDuckGo HTML、Brave Search HTML、Wikipedia、可选 SearXNG 与 DDG 新闻五个引擎，输出 Tavily 风格 JSON，提供 /search、/search/batch、/extract、/health、/openapi.json 端点及嵌入式 UI。面向 AI 代理、RAG 与 LLM 工具链用户，通过 HTTP、MCP、LangChain 工具包装或 C++/Python 绑定接入。限制：answer 为抽取式而非 LLM 生成；提取仅支持静态 HTML；查询仍会发往公共搜索引擎。MIT 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 无 API key、无配额的本地元搜索 API，输出 Tavily 形状 JSON
- 内置 MCP 服务器（web_search / web_search_multi / web_extract），适配 Cursor 与 Claude Desktop
- 支持 include/exclude_domains、search_depth、time_range、max_tokens 等代理/RAG 参数
- Docker、GHCR、安装脚本与 GitHub Release 二进制多种部署路径

## 适用场景

- 为 RAG 管线提供实时网页检索与页面文本提取
- 给 AI 代理接入免密钥的网页搜索工具
- 作为 MCP 工具接入 Cursor 或 Claude Desktop

## 场景标签

`网页抓取` · 领域:效率与自动化

## 证据(README 行号)

> L3: **Free open-source Tavily alternative** — keyless web search + content extraction for AI agents, RAG, LangChain, MCP
> L5: Self-host a local **web search API for AI** with **no API key**, **no quota**, and **no per-query bill**. Drop-in st
> L32: - **In-process MCP**: `wsf mcp` — tools `web_search`, `web_search_multi`, `web_extract`

## 星数曲线

```mermaid
xychart-beta
    title "drmikecrypto/WebSearchFree 星数(近 2 点)"
    x-axis ["2026-10-21", "2026-11-26"]
    y-axis "stars" 9 --> 11
    line [10, 10]
```

2026-10-21 10 → 2026-11-26 10（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-19 · 置信度 mid · 依据 README sha `ace04787c3e7` · [字段定义](../../DATASET.md)*
