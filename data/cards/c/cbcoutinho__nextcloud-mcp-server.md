# cbcoutinho/nextcloud-mcp-server

⭐ 421 · Python · AGPL-3.0 · 推送 2026-11-26 · [GitHub](https://github.com/cbcoutinho/nextcloud-mcp-server) · 个人维护

**将 AI 助手接入 Nextcloud 数据的独立 MCP 服务器**

面向 Claude Code、IDE 等外部 MCP 客户端的独立 MCP 服务器，可部署于 Docker、VM、Kubernetes 或本地，与 Nextcloud 实例解耦运行。提供覆盖 10+ 个 Nextcloud 应用的 110+ 个 MCP 工具，支持笔记、日历、联系人、文件（WebDAV）、Deck、邮件、Talk 等的 CRUD 操作。认证支持应用专用密码（Basic Auth）及 Login Flow v2 多用户模式；可选实验性语义搜索（RAG）依赖 Qdrant 与嵌入服务；支持 PDF/DOCX/图像的 OCR 与文本抽取。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `viral` | AGPL-3.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 110+ MCP 工具覆盖 Notes、Calendar、Contacts、Files 等 10+ 个 Nextcloud 应用
- 多用户认证支持 Basic Auth 与 Login Flow v2（OAuth 接入客户端）
- 实验性语义搜索：向量检索笔记/文件/新闻/Deck 卡片/邮件（需 Qdrant + Ollama）
- PDF、DOCX、图像的 OCR 与文本抽取，支持 streamable-http 与 stdio 传输

## 适用场景

- 让 Claude 等 AI 助手通过自然语言创建笔记、管理日历与联系人
- 通过 MCP 客户端检索和操作 Nextcloud 中的文件与邮件
- 为 Nextcloud 内容搭建语义检索（RAG）管道

## 场景标签

`RAG` `语义搜索` `文档解析` · 领域:知识与检索

## 证据(README 行号)

> L7: **A production-ready MCP server that connects AI assistants to your Nextcloud instance.**
> L11: This is a **dedicated standalone MCP server** designed for external MCP clients like Claude Code and IDEs. It runs 
> L60: - **110+ MCP Tools** - Comprehensive API coverage across 10 Nextcloud apps

## 星数曲线

```mermaid
xychart-beta
    title "cbcoutinho/nextcloud-mcp-server 星数(近 18 点)"
    x-axis ["2026-10-25", "2026-10-28", "2026-10-29", "2026-10-30", "2026-10-31", "2026-11-01", "2026-11-02", "2026-11-06", "2026-11-08", "2026-11-10", "2026-11-13", "2026-11-16", "2026-11-18", "2026-11-19", "2026-11-21", "2026-11-23", "2026-11-26", "2026-11-27"]
    y-axis "stars" 390 --> 423
    line [392, 393, 394, 395, 396, 400, 401, 392, 407, 411, 413, 415, 416, 418, 419, 420, 421, 421]
```

2026-10-25 392 → 2026-11-27 421（+29）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-27 · 置信度 high · 依据 README sha `6f5eaaa365ba` · [字段定义](../../DATASET.md)*
