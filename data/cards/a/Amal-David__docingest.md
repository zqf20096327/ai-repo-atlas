# Amal-David/docingest

⭐ 20 · TypeScript · MIT · 推送 2026-09-26 · [GitHub](https://github.com/Amal-David/docingest) · [官网](https://docingest.com) · 个人维护

**将文档站点转为可搜索、MCP 可访问上下文的开源引擎**

DocIngest 爬取文档站点，以 markdown 形式版本化存储，用 Redis 建立自动补全与全文搜索索引，并通过 Web UI、CLI 和 MCP server 三种方式暴露同一语料。MCP 工具含 find-docs、read-docs、query-docs，可接入 Claude Code 等 MCP 兼容编码工具，为编码 agent 提供文档上下文。爬取依赖 Firecrawl（托管或自托管），需 Node.js 18+ 或 Bun，Redis 推荐但小规模本地测试可选。README 自述搜索排序待调优、版本 UX 尚早期，未达企业级文档平台成熟度。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 同一语料通过 Web UI、CLI、MCP server 三种方式访问
- 按域存储版本化快照，上游文档变更后可重建索引
- MCP 工具：find-docs / read-docs / query-docs，npx 即装即用
- 托管部署在 docingest.com 提供 1,635 个文档站点语料

## 适用场景

- 给 Claude Code 等编码 agent 接入新鲜的文档检索上下文
- 自托管内部文档语料并做全文搜索
- 在命令行快速查找与阅读库的文档

## 场景标签

`网页抓取` `RAG` · 领域:效率与自动化

## 证据(README 行号)

> L3: DocIngest is the open-source engine for turning documentation sites into searchable, MCP-accessible context for huma
> L17: - Query docs from MCP-compatible coding tools
> L147: claude mcp add docingest -- npx -y @docingest/mcp-server

## 星数曲线

```mermaid
xychart-beta
    title "Amal-David/docingest 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 19 --> 21
    line [20, 20]
```

2026-10-18 20 → 2026-10-28 20（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `e1c9f3a57cdc` · [字段定义](../../DATASET.md)*
