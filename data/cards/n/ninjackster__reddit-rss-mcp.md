# ninjackster/reddit-rss-mcp

⭐ 15 · JavaScript · MIT · 推送 2026-05-31 · [GitHub](https://github.com/ninjackster/reddit-rss-mcp) · 个人维护

**无凭据读取 Reddit 的 MCP 服务器：RSS 通道供 LLM 客户端调用**

零依赖的 MCP 服务器，通过 Reddit 仍开放的 RSS 接口读取内容，规避被封锁的匿名 JSON API 与已停止自助申请的 API key。提供三个工具：搜索帖子、浏览版块（hot/new/top 等）、读取帖子评论（扁平列表），返回包含标题/作者/链接/摘要的 JSON。经 stdio（JSON-RPC 2.0）与 MCP 客户端通信，需 Node.js 18+，可从 GitHub 直接运行无需安装。限制：评论无嵌套结构、无投票分数、单次约 25 条结果。

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

- 零凭据运行，不依赖 API key/OAuth/抓取服务
- 零外部依赖，Node.js 内置 fetch 与 Atom XML 解析
- 提供 search/browse/read comments 三个 MCP 工具
- 支持从 GitHub 直接运行，无需 npm install

## 适用场景

- Reddit 封锁匿名 JSON API 时让 Claude 类客户端读取 Reddit
- 在 MCP 客户端中搜索帖子、浏览版块、读评论
- 不想申请 Reddit OAuth 审批的轻量接入方案

## 场景标签

 · 领域:LLM 基础设施/数据接入

## 证据(README 行号)

> L3: A tiny, **dependency-free** MCP server that reads Reddit through its still-open **RSS feeds**. No API key, no OAuth,
> L73: It parses the Atom XML with no external dependencies and speaks MCP over stdio (JSON-RPC 2.0).

## 星数曲线

```mermaid
xychart-beta
    title "ninjackster/reddit-rss-mcp 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-27", "2026-10-30"]
    y-axis "stars" 13 --> 16
    line [14, 15, 15]
```

2026-10-18 14 → 2026-10-30 15（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 mid · 依据 README sha `db37a3d168a1` · [字段定义](../../DATASET.md)*
