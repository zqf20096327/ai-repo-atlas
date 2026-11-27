# cotletdev/substack-api-mcp-server

⭐ 6 · Python · NOASSERTION · 推送 2026-11-23 · [GitHub](https://github.com/cotletdev/substack-api-mcp-server) · [官网](https://cotlet.dev/integrations/substack-api-mcp-server) · 组织维护

**让 AI agent 通过 MCP/REST 操作 Substack 的本地 API 服务器**

以 Python 提供的 Substack API 与 MCP 服务器：通过 Chrome DevTools Protocol 读取用户自己的 Substack 会话 cookie，配合 curl_cffi 模拟 Chrome TLS 指纹调用 Substack web 端点，提供 50 个工具，覆盖草稿、发布、定时、Notes、评论、订阅者与统计数据，支持 stdio 与 HTTP 两种 MCP 传输方式并附带本地 REST API 与 OpenAPI 文档。面向会用 Python 和终端的开发者自托管使用；同仓库另有面向写作者的托管服务 Cotlet（7 天免费，其后按积分付费），发布类操作需 MCP 客户端确认。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 提供 50 个 Substack 工具，覆盖草稿、定时发布、Notes、评论、订阅者与统计
- 通过 Chrome DevTools Protocol 读取本地 Chrome 会话，不存储 Substack 密码
- 同时提供 MCP server（stdio/HTTP）与本地 REST API（含 OpenAPI 文档）
- 支持 Claude Code、Claude Desktop、Cursor、Codex 等 MCP 客户端的配置示例

## 适用场景

- 让 AI 把 Markdown 笔记转成 Substack 草稿并定时发布
- 用脚本或 n8n/Make/Zapier 自动化查询订阅与收入统计
- 批量查找未回复的评论并生成回复草稿

## 场景标签

 · 领域:内容创作/新闻通讯自动化

## 证据(README 行号)

> L35: Substack has no public API to write posts, publish Notes or manage subscribers, and no official MCP server. This re
> L37: - **MCP server** for Claude Code, Claude Desktop, Cursor, Codex and any MCP client, over stdio or HTTP. Setup
> L100: AI agent (MCP) / script (REST, Python) ──▶ substack-mcp on your computer ──your Substack cookies──▶ substack.com

## 星数曲线

```mermaid
xychart-beta
    title "cotletdev/substack-api-mcp-server 星数(近 2 点)"
    x-axis ["2026-11-08", "2026-11-27"]
    y-axis "stars" 5 --> 7
    line [6, 6]
```

2026-11-08 6 → 2026-11-27 6（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-20 · 置信度 high · 依据 README sha `94bd0539e551` · [字段定义](../../DATASET.md)*
