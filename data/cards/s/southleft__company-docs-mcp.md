# southleft/company-docs-mcp

⭐ 49 · TypeScript · MIT · 推送 2026-09-10 · [GitHub](https://github.com/southleft/company-docs-mcp) · [官网](https://southleft.com) · 个人维护

**把公司文档变成 AI 可检索知识库的 MCP 服务器**

面向团队内部知识管理的 MCP 服务器：CLI 摄取 markdown/HTML/PDF/URL/整站爬取内容，发布到 Supabase（PostgreSQL 向量库），由 Cloudflare Workers AI 生成向量并托管常驻服务；团队成员在 Claude、Cursor 等 MCP 客户端中用自然语言查询文档。服务器暴露 search_documentation、search_chunks、browse_by_category、get_all_tags 四个工具。嵌入/向量库/聊天后端可通过环境变量插拔替换（如 openai、anthropic）。Cloudflare 与 Supabase 为必需依赖（有免费层），部署需克隆仓库并配置 wrangler。

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

- 摄取 markdown/HTML/PDF/URL/整站爬取并发布为向量检索库
- 以 Cloudflare Worker 形式 24/7 托管 MCP 服务器
- 四个 MCP 搜索工具（语义搜索、分块搜索、分类浏览、标签列表）
- 嵌入/向量库/聊天后端可插拔（workers-ai、openai、anthropic、supabase 等）

## 适用场景

- 把公司政策、价值观、内部文档做成团队可问答的知识库
- 在 Claude/Cursor/Windsurf 中直接检索公司文档并获得带出处的回答
- 批量索引文档站点供 AI 工具语义查询

## 场景标签

`知识库管理` `语义搜索` · 领域:知识与检索

## 证据(README 行号)

> L3: Turn any documentation into an AI-searchable knowledge base. Feed it markdown, HTML, PDFs, web pages, or plain text 
> L262: Once connected, your AI tool will have access to these search tools:
> L266: |`search_documentation`|Finds documentation that matches your question using semantic search|

## 星数曲线

```mermaid
xychart-beta
    title "southleft/company-docs-mcp 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 48 --> 50
    line [49, 49]
```

2026-10-18 49 → 2026-10-31 49（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `e55cfe7739c1` · [字段定义](../../DATASET.md)*
