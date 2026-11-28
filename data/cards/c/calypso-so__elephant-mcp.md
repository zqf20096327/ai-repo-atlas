# calypso-so/elephant-mcp

⭐ 3 · TypeScript · MIT · 推送 2026-11-27 · [GitHub](https://github.com/calypso-so/elephant-mcp) · [官网](https://www.calypso.so/elephant) · 组织维护

**让 AI 客户端问答你的 PDF 与文档并给出页码出处的 MCP 服务器**

Calypso 出品的 MCP 服务器，提供 10 个工具：elephant-ask 从已保存文档跨文件作答并列出来源页码，elephant-search 返回原文匹配段落，另有添加文件/网页、管理 bucket 等工具。支持两种接入方式：托管端点（Streamable HTTP + OAuth 2.1/PKCE）或经 npm 以 stdio 本地运行（需 Node 20+ 和 Calypso API key）。无状态、无数据库设计，scope 控制读写权限，限流 120 请求/分钟。需注册 Elephant 账户，文件存储在 Calypso 侧。

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

- 10 个 MCP 工具：ask/search/添加文件与网页/bucket 管理
- 回答附文件名与页码出处，无来源时明示不作答
- 托管端点支持 OAuth 2.1 + PKCE 与动态注册，一键断开即吊销 key
- npm 包 @calypsohq/elephant-mcp-server 支持本地 stdio 运行与 --preset 只读模式

## 适用场景

- 在 Claude/ChatGPT/Cursor 中问答合同、租约、保单等文档并核对原文页码
- 保存课程资料与研究论文，随时跨文件提问
- 把手册、发票等资料存入 bucket 按团队或项目组织

## 场景标签

`RAG` `文档问答` · 领域:知识与检索

## 证据(README 行号)

> L5: **The MCP server that lets your AI chat with your PDFs, documents and web pages, and show the page each answer came 
> L98: Elephant is a hosted MCP server. You give your client one URL; it opens a sign-in, you pick a team and press Allow.
> L121: The same server ships on npm as `@calypsohq/elephant-mcp-server` for clients that want a local stdio server, or fo


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-28 · 置信度 high · 依据 README sha `c720b471c5dd` · [字段定义](../../DATASET.md)*
