# PushpenderIndia/browsegenie

⭐ 53 · Python · GPL-3.0 · 推送 2026-09-18 · [GitHub](https://github.com/PushpenderIndia/browsegenie) · [官网](https://pypi.org/project/browsegenie) · 个人维护

**用一句提示词完成浏览器自动化与网页抓取的 AI Agent**

Python 包，提供两种能力：AI 抓取器——分析页面压缩快照后生成自定义 BeautifulSoup4 提取器，按 HTML 结构哈希缓存，仅在页面布局变化时重新调用 LLM 生成；浏览器 Agent——用自然语言描述任务，由 agent 驱动真实 Chromium 浏览器逐步导航、点击、输入并提取数据。支持 Gemini/OpenAI/Anthropic 及 LiteLLM 的 100+ 模型，提供 Web UI（无代码模式）、CLI、Python API 与 MCP 服务器四种使用方式，输出 JSON/CSV。运行需提供 AI 提供商 API key。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 按页面结构哈希缓存生成的 BeautifulSoup4 提取器，每种布局仅调用一次 AI
- 浏览器 Agent 模式：自然语言驱动 Chromium 完成导航/点击/输入/提取
- 提供 Web UI、CLI、Python API 与 MCP 服务器多种使用方式
- 支持 Gemini/OpenAI/Anthropic，回退到 1700+ LiteLLM 模型

## 适用场景

- 不写选择器、用一句话描述就从网页提取结构化数据
- 让 agent 代替我完成登录、搜索、点击等多步浏览器操作
- 把网页抓取能力接入 Claude Code/Cursor 等 MCP 客户端

## 场景标签

`浏览器自动化` `网页抓取` · 领域:效率与自动化

## 证据(README 行号)

> L15: **An AI Agent that can do any kind of browser automation task and web scraping, just using a single prompt.**
> L19: Under the hood the scraping agent writes a custom BeautifulSoup4 extractor for your target page, caches it against 
> L89: **2. Browser Agent** — Describe any browser task in plain English and the agent handles the rest. It opens a real C

## 星数曲线

```mermaid
xychart-beta
    title "PushpenderIndia/browsegenie 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 52 --> 54
    line [53, 53]
```

2026-10-18 53 → 2026-10-29 53（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `1b8ba4a1cbec` · [字段定义](../../DATASET.md)*
