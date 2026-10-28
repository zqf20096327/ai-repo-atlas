# MpMeetPatel/sniffhunt-scraper

⭐ 28 · JavaScript · NOASSERTION · 推送 2026-06-01 · [GitHub](https://github.com/MpMeetPatel/sniffhunt-scraper) · [官网](https://docs.sniffhunt.com) · 个人维护

**本地运行的 URL 转 LLM 就绪 Markdown 抓取引擎，含 MCP/API/CLI**

基于 Bun 工作区的网页内容抓取工具：将 SPA、动态仪表盘等网页转换为面向 LLM 消费的 Markdown，提供 normal（静态快取）与 beast（交互式界面处理，调用 Gemini AI）两种模式。运行于本地，需自备 Google Gemini API key。交付形态包括 Hono API 服务器（同步与 SSE 流式端点）、React Web 界面、CLI 以及可接入 Claude Desktop/Cursor 等 MCP 客户端的 MCP 服务器。仓库标注为已归档的 MVP，宣称将推出重写版本。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- URL 转 LLM 优化 Markdown，支持 normal/beast 两种抓取模式
- 提供 Hono API 服务器（/scrape 流式与 /scrape-sync 同步端点）
- MCP 服务器可接入 Claude Desktop、Cursor、Windsurf 等 AI 客户端
- 数据在本机处理，AI 抽取需配置 Google Gemini API key

## 适用场景

- 把动态网页和文档站转为 Markdown 供 LLM 使用
- 在 Claude Desktop/Cursor 对话中通过 MCP 直接抓取网页内容
- 通过 API 或 CLI 批量做内容抽取与自动化脚本

## 场景标签

`网页抓取` · 领域:效率与自动化

## 证据(README 行号)

> L8: 🔍 Transform any web interface SPAs, dynamic dashboards, or complex content layers into semantically structured, LLM-
> L214: Model Context Protocol (MCP) is a standardized way for AI applications to access external tools and data sources. 

## 星数曲线

```mermaid
xychart-beta
    title "MpMeetPatel/sniffhunt-scraper 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 27 --> 29
    line [28, 28]
```

2026-10-18 28 → 2026-10-28 28（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `a272862b0ca5` · [字段定义](../../DATASET.md)*
