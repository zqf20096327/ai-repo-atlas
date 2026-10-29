# madarco/ragrabbit

⭐ 136 · TypeScript · MIT · 推送 2026-01-05 · [GitHub](https://github.com/madarco/ragrabbit) · [官网](https://ragrabbit.com) · 个人维护

**自托管网站 AI 搜索与 LLMs.txt 生成应用**

基于 Next.js Turborepo 构建的自托管应用：用爬虫抓取并索引网站内容到 PostgreSQL/pgVector，基于 LlamaIndex 提供 AI 问答聊天挂件与即时搜索，生成可定制的 LLMs.txt，并通过 MCP Server（npx @ragrabbit/mcp）让 Claude Desktop、Cursor IDE 等客户端语义检索文档。支持 Vercel 一键部署、用户名密码或邮箱登录、API Key 访问，可与 Fumadocs 集成。运行需 Node.js 20.x、启用 pgVector 的 PostgreSQL 与 OpenAI API Key。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 爬取网站并以 pgVector/PostgreSQL 建立索引
- 可嵌入站点的 AI 聊天挂件与即时搜索
- 生成可定制（ToC 重排）的 LLMs.txt 文件
- MCP Server 供 Claude Desktop / Cursor IDE 语义检索文档

## 适用场景

- 给自己的文档站加 AI 问答和搜索功能
- 为 AI 客户端（Claude/Cursor）提供文档的 MCP 语义检索
- 自动生成并维护网站的 LLMs.txt

## 场景标签

`RAG` `语义搜索` · 领域:知识与检索

## 证据(README 行号)

> L6: Self Hosted Site AI Search, LLMs.txt, MCP Server that crawls your content. 1-Click Deploy on Vercel.
> L14: RagRabbit is a Next.js Turborepo app that uses Llamaindex with pgVector.
> L18: - 💬 Chat Widget: Embeddable AI Chat agent and instant Search

## 星数曲线

```mermaid
xychart-beta
    title "madarco/ragrabbit 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 135 --> 137
    line [136, 136]
```

2026-10-18 136 → 2026-10-29 136（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `f055deb6c003` · [字段定义](../../DATASET.md)*
