# HughesCuit/heventure-search-mcp

⭐ 10 · Python · 推送 2026-05-13 · [GitHub](https://github.com/HughesCuit/heventure-search-mcp) · [官网](https://github.com/HughesCuit/heventure-search-mcp#readme) · 个人维护 · 中文 README

**免 API key 的 MCP 网页搜索服务器，供 MCP 客户端调用**

以 MCP 协议运行的网页搜索服务器，提供 web_search（支持 duckduckgo/bing/google 多引擎，可选搭配 SerpAPI/Tavily）与 get_page_content（网页正文提取）两个工具，内置 LRU 缓存（300 秒 TTL，最多 100 条）与异步运行。默认引擎无需注册 API key，付费引擎通过环境变量可选启用。安装方式包括 pip、命令行运行与 Docker，可接入 Claude Desktop、Cursor 等 MCP 客户端。MIT 许可，要求 Python 3.10+。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | — |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 默认引擎（DuckDuckGo/Bing/Google）无需 API key 即可使用
- 提供 web_search 与 get_page_content 两个 MCP 工具
- 内置 LRU 缓存（300s TTL、上限 100 条）与 asyncio 异步
- 可选通过环境变量启用 SerpAPI/Tavily 付费引擎

## 适用场景

- 为 Claude Desktop 或 Cursor 等客户端接入网页搜索工具
- 在不愿注册搜索 API key 的环境下让 agent 检索网页
- 抓取指定网页的可读文本供对话引用

## 场景标签

`网页抓取` · 领域:效率与自动化

## 证据(README 行号)

> L9: # 🔍 MCP Web Search Server
> L11: > **Free forever. No API key required.** A web search MCP server that works out of the box with Claude Desktop, Cur
> L93: - **Protocol**: MCP (Model Context Protocol)

## 星数曲线

```mermaid
xychart-beta
    title "HughesCuit/heventure-search-mcp 星数(近 2 点)"
    x-axis ["2026-10-19", "2026-11-21"]
    y-axis "stars" 9 --> 11
    line [10, 10]
```

2026-10-19 10 → 2026-11-21 10（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-20 · 置信度 high · 依据 README sha `5527555fb26e` · [字段定义](../../DATASET.md)*
