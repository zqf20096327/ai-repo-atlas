# dirmacs/daedra

⭐ 17 · Rust · MIT · 推送 2026-10-29 · [GitHub](https://github.com/dirmacs/daedra) · [官网](https://dirmacs.github.io/daedra/) · 个人维护

**给 AI agent 用的 Rust 网页搜索 MCP 服务器，14 个免钥后端**

用 Rust 编写的单二进制网页搜索 MCP 服务器，向 Claude、Cursor 等 AI agent 提供 web_search、visit_page、crawl_site 三个 MCP 工具。通过 14 个无需付费 API key 的后端（Mwmbl、Marginalia、Bing RSS、Wikipedia、Hacker News、GitHub 等）并发扇出查询并按相关性合并结果，带熔断器与按后端限流，可在数据中心/VPS IP 上运行。页面抓取支持 HTML Readability 提取、PDF 与 Office 文档转 Markdown，站点爬取遵守 robots.txt。也可作为 CLI 和 Rust 库使用。

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

- 14 个免钥搜索后端自动回退，相关性排序合并结果
- MCP 工具 web_search / visit_page / crawl_site，单二进制零配置
- 熔断器 + 按后端独立限流，仅重试瞬时错误
- HTML/PDF/Office 文档提取为 Markdown，爬取遵守 robots.txt

## 适用场景

- 给 Claude/Cursor 等 MCP 客户端挂上无需 API key 的网页搜索能力
- 在数据中心/VPS IP 环境下为 agent 提供检索与页面抓取
- 作为 CLI 或 Rust 库在脚本中做多后端搜索

## 场景标签

`网页抓取` · 领域:效率与自动化

## 证据(README 行号)

> L12: Daedra is a self-contained web search MCP server in Rust. It gives search and page-fetch tools to AI agents. It wor
> L38: - MCP tools: `web_search`, `visit_page`, `crawl_site`, and the `search_duckduckgo` alias

## 星数曲线

```mermaid
xychart-beta
    title "dirmacs/daedra 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-30"]
    y-axis "stars" 15 --> 18
    line [16, 17, 17]
```

2026-10-18 16 → 2026-10-30 17（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `8f7b68603f39` · [字段定义](../../DATASET.md)*
