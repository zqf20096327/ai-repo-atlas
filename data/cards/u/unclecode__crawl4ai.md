# unclecode/crawl4ai

⭐ 87,638 · Python · Apache-2.0 · 推送 2026-11-20 · [GitHub](https://github.com/unclecode/crawl4ai) · [官网](https://crawl4ai.com/?ref=github-about) · 个人维护

**为 AI agent 与 RAG 生成干净 Markdown/结构化 JSON 的开源爬虫**

开源（Apache-2.0）网络爬虫库，配套托管云 API。核心能力：将网页转为适配 LLM 阅读的 Markdown（含标题、表格、引用列表与去噪过滤器）、通过 CSS/XPath/正则（无 LLM）或任意 LLM 提供商提取结构化 JSON、浏览器控制（会话、代理、隐身模式、Chromium/Firefox/WebKit）、深爬策略与自适应爬取。可通过 pip、CLI（crwl）或 Docker 服务器自托管，亦可用免费 API key 接入云端 /scrape、/extract、/search 等端点及 MCP 服务。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 动量与使用信号

- 维护:`active` — 距上次 push 2.9 天,年发版 15,93 位贡献者
- 涨星:近 1 天 **+65**(自 20261016 起算)
- 安装:pypi 包 `crawl4ai` 月下载 1,275,996
- 平台:— · 协议:MCP / OLLAMA

## 能力要点

- 生成含引用列表的 LLM 友好 Markdown，带 Pruning/BM25/LLM 三种内容过滤器
- 无 LLM 的 CSS/XPath/正则结构化提取，及可接任意 LLM 提供商的 LLMExtractionStrategy
- 浏览器控制：持久会话、代理轮换、隐身模式、多引擎支持
- Docker 自托管带 REST API、MCP、监控面板，支持 AMD64/ARM64

## 适用场景

- 为 RAG 管道批量抓取网页并转成 Markdown 语料
- 从网页抽取结构化 JSON 供数据管道使用
- 给 Claude Code/Cursor 等 agent 接入抓取与网页搜索工具
- 自托管爬虫服务并控制代理与会话

## 场景标签

`网页抓取` `文档解析` · 领域:效率与自动化

## 证据(README 行号)

> L3: **Crawl4AI Cloud is a hosted web scraping, extraction, and search API for AI agents and data pipelines.** Turn pages
> L111: - **LLM-ready output**: smart Markdown with headings, tables, code and citation hints
> L132: - 🤖 **LLM extraction**: any LLM provider, open-source or hosted, into a typed JSON schema (`LLMExtractionStrategy`

## 星数曲线

```mermaid
xychart-beta
    title "unclecode/crawl4ai 星数(近 27 点)"
    x-axis ["2026-10-20", "2026-10-22", "2026-10-23", "2026-10-24", "2026-10-25", "2026-10-26", "2026-10-27", "2026-10-28", "2026-10-29", "2026-10-30", "2026-10-31", "2026-11-01", "2026-11-02", "2026-11-06", "2026-11-08", "2026-11-10", "2026-11-11", "2026-11-12", "2026-11-13", "2026-11-14", "2026-11-15", "2026-11-16", "2026-11-18", "2026-11-19", "2026-11-20", "2026-11-21", "2026-11-22"]
    y-axis "stars" 85675 --> 87816
    line [85853, 85978, 86038, 86113, 86171, 86251, 86319, 86404, 86462, 86535, 86602, 86648, 86712, 86171, 87095, 87190, 87232, 87278, 87317, 87353, 87399, 87449, 87483, 87529, 87571, 87599, 87638]
```

2026-10-20 85,853 → 2026-11-22 87,638（+1,785）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-22 · 置信度 high · 依据 README sha `aca4d1854255` · [字段定义](../../DATASET.md)*
