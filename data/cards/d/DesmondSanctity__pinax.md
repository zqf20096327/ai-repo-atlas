# DesmondSanctity/pinax

⭐ 14 · Go · MIT · 推送 2026-07-10 · [GitHub](https://github.com/DesmondSanctity/pinax) · [官网](https://pinax.dev) · 个人维护

**把任意公开文档站点变成本地 MCP 服务的 Go CLI**

单二进制 Go 命令行工具：抓取公开文档站点，经 llms.txt、sitemap 或有界 BFS 爬取发现页面并索引结构，以 stdio MCP 服务形式向 Claude Desktop、Cursor、Windsurf、Copilot 等客户端暴露 list_sections、search_pages（BM25）、get_section_pages、get_page 四个工具；get_page 按需实时抓取并返回 Markdown，配合 SQLite 持久缓存。内置 Stripe、React 等编目，支持多个 manifest 统一服务。JS 渲染站点需自备 Jina Reader API key 或关闭渲染器；不支持私有文档认证，无定时重爬。

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

- llms.txt → sitemap → BFS 的页面发现链路
- 四工具 MCP 接口：list_sections / search_pages（BM25）/ get_section_pages / get_page
- get_page 实时抓取返回 Markdown，附 SQLite 页面缓存
- JS SPA 站点可选 Jina Reader 渲染（自备 key，可 --renderer=off 关闭）

## 适用场景

- 给编码 agent 接入目标框架的最新文档，避免训练截止导致的过期 API
- 在一个 MCP 服务里跨多个已索引文档站统一搜索
- 查看 agent 正在调用哪些文档工具的日志 UI

## 场景标签

`网页抓取` · 领域:效率与自动化

## 证据(README 行号)

> L17: Pinax is a small Go CLI that crawls a public documentation site, indexes its
> L18: structure, and exposes it to any Model Context Protocol
> L19: client (Claude Desktop, Cursor, Windsurf, Copilot, custom agents) as four

## 星数曲线

```mermaid
xychart-beta
    title "DesmondSanctity/pinax 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `53a01ed879ed` · [字段定义](../../DATASET.md)*
