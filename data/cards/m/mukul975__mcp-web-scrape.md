# mukul975/mcp-web-scrape

⭐ 49 · TypeScript · MIT · 推送 2026-02-16 · [GitHub](https://github.com/mukul975/mcp-web-scrape) · [官网](https://github.com/mukul975/mcp-web-scrape#readme) · 个人维护

**面向 AI agent 的网页内容抓取 MCP 服务器：抓取 URL 输出带引用的 Markdown**

基于 Model Context Protocol 的网页内容抓取服务器：读取任意 URL，提取可读内容并返回带引用的 Markdown/JSON，遵循 robots.txt，使用 ETag/304 缓存与限速。提供 40 余个工具，覆盖正文/表单/表格/结构化数据提取、PDF 转换、关键词与实体分析、SEO 检查、SSL/隐私检测、变更监控与站点地图生成。支持 STDIO 与 HTTP/SSE 传输，可接入 ChatGPT Desktop 与 Claude Desktop，通过 npm 全局安装或 npx 运行，缓存目录、User-Agent、限速可经环境变量配置。

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

- HTML 转带引用 Markdown，确定性输出与 ETag/304 持久化缓存
- 40+ MCP 工具：内容提取、分析、SEO、安全隐私、监控五类
- 默认遵循 robots.txt、限速、不绕过付费墙
- 支持 STDIO 与 HTTP/SSE 两种传输，缓存内容可作为 MCP 资源访问

## 适用场景

- 为 ChatGPT/Claude 等 agent 提供干净的网页读取能力
- 批量提取网页正文、表格、结构化数据用于知识整理
- 监控网页内容变更并生成站点分析报告

## 场景标签

`网页抓取` · 领域:效率与自动化

## 证据(README 行号)

> L3: > Clean, cached web content for agents—Markdown + citations, robots-aware, ETag/304 caching.
> L217: *Built with ❤️ for the Model Context Protocol ecosystem*

## 星数曲线

```mermaid
xychart-beta
    title "mukul975/mcp-web-scrape 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-28"]
    y-axis "stars" 47 --> 50
    line [48, 49, 49]
```

2026-10-18 48 → 2026-10-28 49（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `01c6057d68ab` · [字段定义](../../DATASET.md)*
