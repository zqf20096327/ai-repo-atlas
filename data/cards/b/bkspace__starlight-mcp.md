# bkspace/starlight-mcp

⭐ 13 · TypeScript · MIT · 推送 2026-07-14 · [GitHub](https://github.com/bkspace/starlight-mcp) · 个人维护

**为 Astro/Starlight 文档站点生成 MCP server 的集成**

面向 Astro/Starlight 文档站的 Astro 集成：构建期生成收录全部文档页的 JSON 语料与机器可读工具目录，运行期由零依赖的无状态 JSON-RPC handler 通过 streamable HTTP 提供 search_docs、get_doc、list_docs 三个 MCP 工具。无需数据库、嵌入或独立服务；SSR 站点自动注入端点，静态站点可用 Cloudflare Workers 或任意 fetch 环境接线。支持 Claude Code、Cursor、VS Code、Windsurf 等 MCP 客户端。以 TypeScript 源码发布，需经打包器消费。

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

- 构建期生成 docs-index.json 语料，无数据库与嵌入
- 零依赖纯 (Request)=>Promise handler，无状态 streamable HTTP
- SSR 自动注入 /mcp 端点，静态站点提供 Cloudflare Workers 方案
- 提供 search_docs/get_doc/list_docs 三个工具与 mcp-schema.json 工具目录

## 适用场景

- 让 AI 编码代理通过 MCP 结构化搜索我的文档站
- 在 Cloudflare Workers 上为静态文档站托管 MCP 端点
- 通过 llms.txt 让 agent 发现文档站的 MCP server

## 场景标签

 · 领域:开发者工具/文档基础设施

## 证据(README 行号)

> L3: Give your Astro or Starlight docs site an MCP server.
> L5: Agents connect to `https://your-site.com/mcp` and get three tools — `search_docs`, `get_doc`, `list_docs` — answered

## 星数曲线

```mermaid
xychart-beta
    title "bkspace/starlight-mcp 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 12 --> 14
    line [13, 13]
```

2026-10-18 13 → 2026-10-31 13（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `bcbd090d8f06` · [字段定义](../../DATASET.md)*
