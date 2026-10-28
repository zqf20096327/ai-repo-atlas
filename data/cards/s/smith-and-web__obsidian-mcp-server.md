# smith-and-web/obsidian-mcp-server

⭐ 19 · TypeScript · MIT · 推送 2026-10-26 · [GitHub](https://github.com/smith-and-web/obsidian-mcp-server) · [官网](https://github.com/smith-and-web/obsidian-mcp-server#readme) · 组织维护

**让 Claude 等 AI 助手读写搜索 Obsidian 笔记库的 MCP 服务器**

基于 Express.js 的 MCP 服务器，通过 HTTP+SSE（无 stdio 模式）向 Claude Desktop、Cursor、Claude Code 等 MCP 客户端暴露 40 余个工具：笔记 CRUD、YAML frontmatter 解析与更新、标签管理与审计、全文搜索、反向链接与断链检测、目录操作及按标题的段落级编辑。可选语义搜索基于 Postgres+pgvector 与 Ollama 本地嵌入，未设置 DATABASE_URL 时该功能关闭。支持 npx、Docker 与源码三种运行方式，可用 API_KEY 或 Tailscale 头做认证。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 笔记 CRUD、frontmatter/标签管理、全文搜索、反向链接与断链检测等 40 余个 MCP 工具
- 可选语义搜索：Postgres+pgvector + Ollama 本地嵌入，嵌入不离开本地网络
- 仅支持 HTTP+SSE 传输，stdio 客户端经 mcp-remote 桥接
- 可选紧凑响应模式（响应体积缩小 40-60%）与 API_KEY 认证

## 适用场景

- 在 Claude Desktop 或 Cursor 中用自然语言管理 Obsidian 笔记库
- 让 AI 助手批量整理标签、frontmatter 和反向链接
- 在本地网络内对笔记库做语义搜索与相似笔记推荐

## 场景标签

`知识库管理` `语义搜索` · 领域:知识与检索

## 证据(README 行号)

> L12: A Model Context Protocol (MCP) server that enables AI assistants like Claude to interact with your Obsidian vault. 
> L53: **How clients connect:** the server speaks MCP over **HTTP + SSE only** (there is no stdio mode). You start it (npx
> L164: **Claude Code** supports SSE servers directly:

## 星数曲线

```mermaid
xychart-beta
    title "smith-and-web/obsidian-mcp-server 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 18 --> 20
    line [19, 19]
```

2026-10-18 19 → 2026-10-28 19（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `7f066c2e8cce` · [字段定义](../../DATASET.md)*
