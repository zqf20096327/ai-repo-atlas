# brightdata/brightdata-mcp

⭐ 2,733 · JavaScript · MIT · 推送 2026-11-22 · [GitHub](https://github.com/brightdata/brightdata-mcp) · [官网](https://brightdata.com/) · 组织维护

**给 AI agent 提供网页搜索、抓取与浏览器自动化的 MCP 服务器**

Bright Data 的 MCP 服务器，向 AI agent 与 LLM 客户端暴露 30 个工具：网页搜索（Bing/Google）、任意 URL 转 Markdown/HTML/JSON-LD、1,200+ 预构建爬虫的结构化 JSON 输出、远程浏览器自动化（导航/点击/截图），以及向 ChatGPT/Perplexity 发送提示并取回回答文本。提供托管远程服务器（一个 URL）与本地 npx 实例两种部署方式。每账号含每月 5,000 次免费请求，超出后按量计费；工具可按分组加载以减少上下文占用。

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

- 30 个 MCP 工具覆盖搜索、抓取、结构化数据与浏览器自动化
- 1,200+ 预构建爬虫（Amazon、LinkedIn、TikTok、npm、PyPI 等）输出 JSON
- 托管远程服务器与本地 npx 两种部署方式
- 工具分组机制（GROUPS/TOOLS）控制加载范围以减少上下文

## 适用场景

- 让 agent 用实时网页数据回答问题而非依赖训练数据
- 批量采集电商产品的价格、库存与评论数据
- 为编码 agent 按需获取 npm/PyPI 包与 GitHub 仓库信息
- 监控社交媒体平台上账号与内容的互动指标

## 场景标签

`网页抓取` `浏览器自动化` · 领域:效率与自动化

## 证据(README 行号)

> L7:  Web search, page scraping, structured data extraction, and browser automation for AI agents and LLMs over the Model
> L26: The Bright Data MCP server gives AI agents real-time access to public web data. It exposes **30 tools** covering:
> L34: Two deployment options: a hosted remote server (one URL, no installation) or a local instance via `npx @brightdata/

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
*卡片 v1 · prompt 1.4 · 生成 2026-11-23 · 置信度 mid · 依据 README sha `1d16cd930dc5` · [字段定义](../../DATASET.md)*
