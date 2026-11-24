# brightdata/brightdata-mcp

⭐ 2,734 · JavaScript · MIT · 推送 2026-11-23 · [GitHub](https://github.com/brightdata/brightdata-mcp) · [官网](https://brightdata.com/) · 组织维护

**为 AI agent 和 MCP 客户端提供网页搜索、抓取与浏览器自动化**

Bright Data 出品的 MCP 服务器，通过 Model Context Protocol 向 AI agent 暴露 31 个工具，覆盖网页搜索（Bing/Google）、URL 抓取为 Markdown/HTML/JSON-LD、1200+ 预构建爬虫的结构化数据提取、远程浏览器自动化，以及向 ChatGPT/Perplexity 发送 prompt 收集回答。支持托管远程服务器（一个 URL 即用）与本地 npx 实例两种部署方式，提供 Claude Desktop、Claude Code、Cursor、VS Code、Windsurf、Gem CLI、Zed、Warp 等客户端的接入配置。账户含每月 5,000 次免费请求额度，超出后按量计费，可设消费上限。

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

- 31 个 MCP 工具：搜索、抓取、结构化提取、远程浏览器自动化
- 1200+ 预构建爬虫返回干净 JSON（Amazon、LinkedIn、TikTok、npm、PyPI 等）
- 托管远程服务器（无需安装）与本地 npx 两种部署方式
- 工具分组机制（GROUPS/TOOLS）按需加载以减少上下文占用

## 适用场景

- 让 AI agent 用实时网页数据替代训练数据回答问题
- 为编程 agent 按需读取 npm/PyPI 包与 GitHub 仓库信息
- 监控社交平台上竞品的帖子、评论与互动数据
- 替换 agent 内置的 fetch/search 工具以处理需 JS 渲染的页面

## 场景标签

`浏览器自动化` `网页抓取` · 领域:效率与自动化

## 证据(README 行号)

> L7:  Web search, page scraping, structured data extraction, and browser automation for AI agents and LLMs over the Model
> L26: The Bright Data MCP server gives AI agents real-time access to public web data. It exposes **31 tools** covering:
> L35: Two deployment options: a hosted remote server (one URL, no installation) or a local instance via `npx @brightdata/

## 星数曲线

```mermaid
xychart-beta
    title "brightdata/brightdata-mcp 星数(近 24 点)"
    x-axis ["2026-10-21", "2026-10-23", "2026-10-24", "2026-10-27", "2026-10-28", "2026-10-29", "2026-10-30", "2026-10-31", "2026-11-01", "2026-11-02", "2026-11-06", "2026-11-08", "2026-11-10", "2026-11-11", "2026-11-12", "2026-11-13", "2026-11-14", "2026-11-15", "2026-11-16", "2026-11-18", "2026-11-19", "2026-11-21", "2026-11-22", "2026-11-24"]
    y-axis "stars" 2680 --> 2737
    line [2684, 2685, 2686, 2687, 2691, 2693, 2695, 2696, 2698, 2703, 2686, 2715, 2718, 2722, 2724, 2726, 2727, 2729, 2728, 2730, 2733, 2732, 2733, 2733]
```

2026-10-21 2,684 → 2026-11-24 2,733（+49）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-24 · 置信度 mid · 依据 README sha `0e40193d09ee` · [字段定义](../../DATASET.md)*
